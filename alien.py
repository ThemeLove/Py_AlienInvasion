import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
	'''外星人类'''
	def __init__(self,ai_settings,screen):
		super(Alien,self).__init__()
		self.screen=screen
		self.ai_settings=ai_settings
		self.alien_speed=ai_settings.alien_speed

		# 加载外星人图像，并设置其rect属性
		self.image=pygame.image.load('images/alien.bmp')
		self.rect=self.image.get_rect()
		# 初始化每个外星人的位置为屏幕左上角附近
		self.rect.x=self.rect.width
		self.rect.y=self.rect.height


		# 存储外星人的准确位置
		self.x=float(self.rect.x)
		self.y=float(self.rect.y)

		# 标示外星人移动方向的flag
		self.ismoving_right=True

	def update(self):
		'''外星人移动更新位置的函数'''
		'''外星人默认开始向右移动，
		当外星人触碰屏幕边缘的时候，以相同速度向相反方向移动，
		同时，y坐标向下移动自身高度的距离'''
		if self.x >=self.ai_settings.screen_width-self.rect.width:
			self.x-=self.alien_speed
			self.y+=self.rect.height
			self.ismoving_right=False
		elif self.x<=0:
			# 当x坐标小于0的时候
			self.x+=self.alien_speed
			self.y+=self.rect.height
			self.ismoving_right=True
		else :
			# 在屏幕之间移动，最正常的移动,根据移动方向改变x坐标的值
			if self.ismoving_right:
				self.x+=self.alien_speed
			else :
				self.x-=self.alien_speed

		# 更新外星人矩形实际位置
		self.rect.x=self.x
		self.rect.y=self.y

	def blitme(self):
		'''绘制外星人'''
		self.screen.blit(self.image,self.rect)

