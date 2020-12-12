class Clock:   
	def __init__(self, hours, minutes, seconds):
			self.hours = hours
			self.minutes = minutes
			self.seconds = seconds

	def getHours(self):
			return self.hours

	def getMinutes(self):
			return self.minutes

	def getSeconds(self):
			return self.seconds

	def show(self):
			print(f'{self.hours}:{self.minutes}:{self.seconds}')

clk = Clock(10,2,1)
print(clk.getHours())
clk.show()
