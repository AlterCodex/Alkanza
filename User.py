from . import Subject

class User(Subject):
	
	def __init__ (self):
		super()
	
	def Save(self):
		super().sync_notify("User Updated")
		