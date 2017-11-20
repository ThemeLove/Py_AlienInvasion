import pygame
from pygame.sprite import Sprite
from ship import Ship

class Bullet(Sprite):
	'''子弹管理类'''
	def __init__(self,ai_settings,screen,ship):
		super(Bullet,self).__init__( )
		self.screen=screen
		self.rect=pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
		self.rect.centerx=ship.rect.centerx
		self.rect.top=ship.rect.top

		# 存储用小数标示子弹位置
		self.y=float(self.rect.y)

		self.color=ai_settings.bullet_color
		self.speed=ai_settings.bullet_speed

	def update(self):
		'''更新子弹的位置，自下往上移动'''

		# 更新子弹位置的小数值
		self.y-=self.speed
		self.rect.y=self.y

	def draw_bullet(self):
		'''绘制子弹'''
		pygame.draw.rect(self.screen,self.color,self.rect)
