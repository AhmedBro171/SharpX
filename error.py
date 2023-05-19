class Error:
	def __init__(self, name, details):
		self.name = name
		self.details = details
	def asString():
		result = self.name + ": " + self.details
		return result

class UndefinedCharError(Error):
	def __init__(self, details):
		super("Undefined Character", details)