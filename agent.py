#agent
#think of it more as, rules are actions that an agent tries to perform, then there are constraints that the environment imposes that may conflict with those rules
class Agent:
	def __init__(self, coordinates,state,rules):
		self.coordinates = coordinates
		self.state = state

	def step(self):
		pass