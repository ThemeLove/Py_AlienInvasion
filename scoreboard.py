# -*- coding: utf-8 -*-
import pygame
from pygame.sprite import Group
from ship import Ship
class Scoreboard():
	'''显示得分信息类'''
	def __init__(self,ai_settings,screen,stats):
		'''初始化显示得分设计的属性'''
		self.screen=screen
		self.screen_rect=screen.get_rect()
		self.ai_settings=ai_settings
		self.stats=stats

		# 显示得分信息时使用的字体设置
		self.text_color=(30,30,30)
		self.font=pygame.font.SysFont(None,48)

		# 准备初始得分图像
		self.prep_score()
		# 准备最高得分图像
		self.prep_high_score()

		# 准备当前等级图像
		self.prep_level()

		# 准备剩余可用飞船编组
		self.prep_left_ships()
		
	def prep_left_ships(self):
		self.left_ships=Group()
		for ship_number in range(self.stats.ships_left):
			ship=Ship(self.ai_settings,self.screen)
			ship.rect.x=10+ship_number*ship.rect.width
			ship.rect.y=10
			self.left_ships.add(ship)

	def prep_score(self):
		# 格式化分数
		rounded_score=int(round(self.stats.score,-1))
		score_str="current score:"+"{:,}".format(rounded_score)

		self.score_image=self.font.render(score_str,True,self.text_color,self.ai_settings.bg_color)

		# 将得分板放置到屏幕右上角上
		self.rect=self.score_image.get_rect()
		self.rect.right=self.screen_rect.right-20
		self.rect.top=20
	def prep_high_score(self):
		# 格式化最高得分
		high_score=int(round(self.stats.high_score,-1))
		high_score_str="highest score:"+"{:,}".format(high_score)

		self.high_score_image=self.font.render(high_score_str,True,self.text_color,self.ai_settings.bg_color)

		# 将最高得分放置在屏幕顶部中央
		self.high_score_rect=self.high_score_image.get_rect()
		self.high_score_rect.centerx=self.screen_rect.centerx
		self.high_score_rect.top=self.rect.top

	def prep_level(self):
		# 格式化当前等级
		self.level_image=self.font.render("current level:"+str(self.stats.level),True,self.text_color,self.ai_settings.bg_color)
		# 将等级放在得分下方
		self.level_image_rect=self.level_image.get_rect()
		self.level_image_rect.right=self.screen_rect.right-20
		self.level_image_rect.top=self.rect.bottom+20

	def show_score(self):
		'''在屏幕上显示得分'''
		self.screen.blit(self.score_image,self.rect)
		# 在屏幕上显示最高得分
		self.screen.blit(self.high_score_image,self.high_score_rect)

		# 在屏幕上显示
		self.screen.blit(self.level_image,self.level_image_rect)
		
		# 绘制飞船,对编组调用draw(),pygame将绘制每艘飞船
		self.left_ships.draw(self.screen)