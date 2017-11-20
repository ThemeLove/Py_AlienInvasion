class GameStats():
	'''跟踪游戏的统计信息'''
	def __init__(self,ai_settings):
		self.ai_settings=ai_settings
		# 标示游戏的活动状态
		self.game_active=False

		# 在任何情况下都不应该重置最高得分
		self.high_score=0

		self.reset_stats()

	def reset_stats(self):
		'''初始化统计信息,开始游戏或者重玩时可调用'''
		self.ships_left=self.ai_settings.ship_limit

		# 得分记录
		self.score=0

		# 当前等级
		self.level=0
