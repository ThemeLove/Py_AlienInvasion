import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
	# 飞船类
	def __init__(self,ai_settings,screen):
		"""初始化飞船并设置其初始位置"""
		super(Ship,self).__init__()

		self.screen=screen
		# 加载飞船图像并获取其外接矩形
		self.image=pygame.image.load('images/ship.bmp')
		self.rect=self.image.get_rect()
		self.screen_rect=screen.get_rect()
		# 将每艘新飞船放在屏幕底部中央
		self.center_ship()

		# 定义飞船的中心点x值
		self.ai_settings=ai_settings
		self.centerx=float(self.rect.centerx)

		# 标志是否向右移动的flag
		self.moving_right=False
		# 标志是否向左移动的flag
		self.moving_left=False

	def blitme(self):
		'''在指定位置绘制飞船'''
		self.screen.blit(self.image,self.rect)

	def center_ship(self):
		'''初始化飞船的位置为屏幕底端中央'''
		self.rect.centerx=self.screen_rect.centerx
		self.rect.bottom=self.screen_rect.bottom

	def update(self):
		'''根据移动标志调整飞船的位置,并控制飞船不能超出屏幕边缘'''
		if self.moving_right and self.rect.right<self.screen_rect.right :
			# 向右移动x坐标+1
			self.centerx+=self.ai_settings.ship_speed

		if self.moving_left and self.rect.left>0 :
			# 向左移动-1
			self.centerx-=self.ai_settings.ship_speed

		# 根据self.centerx更新rect对象，因为最终显示还是rect对象属性确定的
		self.rect.centerx=self.centerx

	
	  

