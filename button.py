import pygame
class Button():
	'''button类用以显示记录'''
	def __init__(self,ai_settings,screen,msg):
		self.ai_settings=ai_settings
		self.screen=screen
		self.msg=msg;
		self.screen_rect=screen.get_rect()

		# 设置按钮的属性和其他属性
		# 按钮宽高
		self.width=200
		self.height=50
		# 按钮颜色
		self.button_color=(0,255,255)
		self.text_color=(255,255,255)
		# 按钮字体
		self.font=pygame.font.SysFont(None,48)

		# 创建按钮的Rect对象，并使其居中
		self.rect=pygame.Rect(0,0,self.width,self.height)
		self.rect.center=self.screen_rect.center

		# 初始化字体
		self.prep_msg(msg)

	def prep_msg(self,msg):
		'''将msg渲染为图像，并使其在按钮上居中'''
		self.msg_image=self.font.render(msg,True,self.text_color,self.button_color)
		self.msg_image_rect=self.msg_image.get_rect()
		self.msg_image_rect.center=self.rect.center

	def draw_button(self):
		# 绘制一个用颜色填充的按钮，在绘制文本
		self.screen.fill(self.button_color,self.rect)
		self.screen.blit(self.msg_image,self.msg_image_rect)