import pygame
import settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
def run_game():
	# 初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_settings=settings.Settings()
	screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	# 创建一个用于存储游戏统计信息的实例
	stats=GameStats(ai_settings)
	# 创建飞船
	ship=Ship(ai_settings,screen)
	# 创建子弹编组
	bullets=Group()
	# 创建外星人编组，并生产外星人
	aliens=Group()
	gf.create_alien_fleet(ai_settings,screen,ship,aliens)

	# 创建按钮
	play_button=Button(ai_settings,screen,'play')

	# 创建一个计分板
	scoreboard=Scoreboard(ai_settings,screen,stats)

	pygame.display.set_caption(ai_settings.game_name)

	# 开始游戏的主循环
	while True:
		# 监视键盘和鼠标事件
		gf.check_events(ai_settings,screen,stats,ship,bullets,aliens,play_button,scoreboard)

		# 根据游戏的可用状态来更新游戏的位置
		if stats.game_active:
			# 更新飞船的位置
			gf.update_ship(ship)
			
			# 更新所有子弹的位置，移除每次抵达屏幕边缘的子弹
			gf.update_bullets(ai_settings,screen,stats,ship,bullets,aliens,scoreboard)

			# 更新所有外星人的位置
			gf.update_aliens(ai_settings,screen,stats,ship,bullets,aliens,scoreboard)

		# 每次循环时都重新绘制屏幕
		gf.update_screen(ai_settings,screen,stats,ship,bullets,aliens,play_button,scoreboard)

run_game()
