import sys
import pygame
from bullet import Bullet
from alien  import Alien
from time   import sleep

def check_events(ai_settings,screen,stats,ship,bullets,aliens,play_button,scoreboard):
	'''响应按键和鼠标事件'''
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type==pygame.KEYDOWN:
			check_keydown_events(ai_settings,screen,event,ship,bullets)  
		elif event.type==pygame.KEYUP:
			check_keyup_events(event,ship)
			# 鼠标按下事件
		elif event.type==pygame.MOUSEBUTTONDOWN:
			mouse_x,mouse_y=pygame.mouse.get_pos()
			check_play_button(ai_settings,screen,stats,ship,bullets,aliens,play_button,scoreboard,mouse_x,mouse_y)

def check_play_button(ai_settings,screen,stats,ship,bullets,aliens,play_button,scoreboard,mouse_x,mouse_y):
	# 检查鼠标点击的位置是否在矩形区域内
	click_in_button=play_button.rect.collidepoint(mouse_x,mouse_y)
	# 只有在游戏没有开始并且点击在'play'按钮上时，才重置游戏
	if not stats.game_active and click_in_button:

		# 游戏正常进行时，光标可能影响用户体验，正常进行时隐藏用户体验
		pygame.mouse.set_visible(False)
		
		stats.game_active=True

		# 重置游戏时，初始化游戏难度
		ai_settings.init_dynamic_settings()
		stats.reset_stats()

		# 初始化等级提升，因为等级提升时在清空一组外星人之后，所以不是每次都刷新，这里手动初始化
		scoreboard.prep_level()
		# 每次点击都初始化剩余飞船数
		scoreboard.prep_left_ships()

		# 清空子弹和外星人
		bullets.empty()
		aliens.empty()

		# 创建新外星人、重置飞船数量，并让飞船居中
		create_alien_fleet(ai_settings,screen,ship,aliens)
		ship.center_ship()


def check_keydown_events(ai_settings,screen,event,ship,bullets):
	'''响应按键'''
	if event.key==pygame.K_q:
		sys.exit()
	elif event.key==pygame.K_RIGHT:
		ship.moving_right=True
		ship.moving_left=False
	elif event.key==pygame.K_LEFT:
		ship.moving_left=True
		ship.moving_right=False
	elif event.key==pygame.K_SPACE:
		fire_bullet(ai_settings,screen,ship,bullets)

def check_keyup_events(event,ship):
	'''响应松开'''
	if event.key==pygame.K_RIGHT or event.key==pygame.K_LEFT:
		ship.moving_right=False
		ship.moving_left=False

def fire_bullet(ai_settings,screen,ship,bullets):
	if len(bullets)<ai_settings.bullets_count_max:
			# 空格键的时候开火，创建一个子弹,并添加到子弹编组中
			new_bullet=Bullet(ai_settings,screen,ship)
			bullets.add(new_bullet)

def create_alien_fleet(ai_settings,screen,ship,aliens):
	'''创建外星人舰队'''
	number_alien_x=get_number_aliens_x(ai_settings,screen)
	number_alien_y=get_number_aliens_y(ai_settings,screen,ship)
	for index_y in range(number_alien_y):
		for index_x in range(number_alien_x):
			create_aliens(ai_settings,screen,aliens,index_y,index_x)

def get_number_aliens_y(ai_settings,screen,ship):
	'''y轴方向上可以容纳的飞船行数'''
	alien=Alien(ai_settings,screen)
	alien_height=alien.rect.height
	# y轴方向最多可用的高度（减去飞船的高度，和3倍外星人的高度）
	available_height=ai_settings.screen_height-3*(alien_height)-ship.rect.height
	# 最多外星人的行数
	number_alien_y=int(available_height/(2*alien_height))
	return number_alien_y

def get_number_aliens_x(ai_settings,screen):
	'''x轴方向上最多容纳的外星人数量'''
	alien=Alien(ai_settings,screen)
	# 一个外星人的宽度
	alien_width=alien.rect.width;
	# x轴方向可利用的最大游戏宽度
	available_width=ai_settings.screen_width-2*(alien_width)
	# x轴一行最多容纳的外星人数量
	number_alien_x=int(available_width/(2*alien_width))
	return number_alien_x

def create_aliens(ai_settings,screen,aliens,index_y,index_x):
	'''创建所有外星人'''
	alien=Alien(ai_settings,screen)
	alien_width=alien.rect.width
	alien_height=alien.rect.height
	# 初始化每个外星人的位置
	alien.x=alien_width+alien_width*2*index_x
	alien.y=alien_height+alien_height*2*index_y
	alien.rect.x=alien.x
	alien.rect.y=alien.y
	aliens.add(alien)

def update_ship(ship):
	'''更新飞船的位置'''
	ship.update()

def update_bullets(ai_settings,screen,stats,ship,bullets,aliens,scoreboard):
	'''更新子弹的位置，并删除已消失的子弹'''
	# 更新子弹的位置
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom<=0:
			bullets.remove(bullet)
	check_bullet_alien_collisions(ai_settings,screen,stats,ship,bullets,aliens,scoreboard)

def check_bullet_alien_collisions(ai_settings,screen,stats,ship,bullets,aliens,scoreboard):
	'''检测子弹和外星人之前的碰撞'''
		# 检测碰撞，并删除响应的子弹和外星人
	collisions=pygame.sprite.groupcollide(bullets,aliens,False,True)

	for aliens in collisions.values():
		stats.score+=ai_settings.alien_points*len(aliens)

	# 更新分数
	scoreboard.prep_score()
	# 更新最高分数
	check_high_score(stats,scoreboard)

	# 当飞船数量为0时，提升等级，增加游戏难度，并重新创建外星人
	if len(aliens)==0:
		#等级提升
		stats.level+=1
		scoreboard.prep_level()

		bullets.empty()
		ai_settings.increase_speed()
		create_alien_fleet(ai_settings,screen,ship,aliens)

def check_high_score(stats,scoreboard):
	'''检查当前得分是否超过最高得分'''
	if stats.score>stats.high_score:
		stats.high_score=stats.score
		scoreboard.prep_high_score()


def update_aliens(ai_settings,screen,stats,ship,bullets,aliens,scoreboard):
	'''更新所有外星人的位置'''
	aliens.update()
	# 检测外星人和飞船的碰撞
	if pygame.sprite.spritecollideany(ship,aliens):
		ship_hit(ai_settings,screen,stats,ship,bullets,aliens,scoreboard)

	# 检查外星人是否到达屏幕底端
	check_aliens_bottom(ai_settings,screen,stats,ship,bullets,aliens,scoreboard)
		
def check_aliens_bottom(ai_settings,screen,stats,ship,bullets,aliens,scoreboard):
	'''检查是否有外星人到达屏幕底端'''
	for alien in aliens:
		if alien.rect.bottom>=ai_settings.screen_height:
			ship_hit(ai_settings,screen,stats,ship,bullets,aliens,scoreboard)
			break

def ship_hit(ai_settings,screen,stats,ship,bullets,aliens,scoreboard):
	'''处理外星人和飞船碰撞之后的逻辑'''
	if stats.ships_left>0:
		# 玩家可用飞船数量减少1
		stats.ships_left-=1
		# 清空当前剩余所有外星人，并重新创建一批外星人
		aliens.empty()
		create_alien_fleet(ai_settings,screen,ship,aliens)
		# 清空子弹
		bullets.empty()
		# 并将飞船重新放置在屏幕底端中央
		ship.center_ship()

		# 更新剩余可用飞船
		scoreboard.prep_left_ships()

		# 暂停游戏0.5秒
		sleep(0.5)
	else :
		stats.game_active=False
		# 游戏结束，让光标重新先显示
		pygame.mouse.set_visible(True)
		
def update_screen(ai_settings,screen,stats,ship,bullets,aliens,play_button,scoreboard):
	'''更新屏幕上的图像，并切换到新屏幕'''
	screen.fill(ai_settings.bg_color)
	# 重新绘制飞船，更新飞船位置
	ship.blitme()

	# 重新绘制所有子弹，更新所有子弹位置
	for bullet in bullets.sprites():
		bullet.draw_bullet()

	# 重新绘制所有外星人，直接调用编队的draw()
	aliens.draw(screen)

	# 显示计分板
	scoreboard.show_score()

	# 如果游戏处于非活跃状态，将play按钮放到最上面
	if not stats.game_active:
		play_button.draw_button()

	# 让最近绘制的屏幕可见
	pygame.display.flip()

