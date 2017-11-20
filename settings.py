class Settings():
	def __init__(self):
		# 游戏名
		self.game_name = "Alien Invasion"
		# 屏幕设置
		self.screen_width = 1200
		self.screen_height = 800
		# 背景色
		self.bg_color = (230,230,230)

		# 飞船相关设置
		# 玩家拥有飞船的数量限制
		self.ship_limit=3

		# 添加子弹设置
		# 最多子弹数量
		self.bullets_count_max=6
		# 子弹速度

		self.bullet_width=5
		self.bullet_height=15
		self.bullet_color=(60,60,60)

		# 等级提升时速度提升增量因素
		self.speedup_scale=1.1

		# 等级提高时每击落一个外星人分数提升增量
		self.alien_scoreup_scale=1.5

		# 初始化飞船、子弹、外星人速度
		self.init_dynamic_settings()


	def init_dynamic_settings(self):
		'''初始化随游戏进行而变化的设置'''
		# 飞船的初始化速度
		self.ship_speed=1.5
		# 子弹的初始化速度
		self.bullet_speed=1
		# 外星人初始化速度
		self.alien_speed=1

		# 每击落一个外星人获得的得分
		self.alien_points=50

	def increase_speed(self):
		'''递增速度'''
		self.ship_speed*=self.speedup_scale
		self.bullet_speed*=self.speedup_scale
		self.alien_speed*=self.speedup_scale

		# 递增得分,为整数
		self.alien_points=int(self.alien_points*self.alien_scoreup_scale)
		print(self.alien_points)