import unittest

class E:
	@classmethod
	def keys(cls):
		return [ x for x in cls.__dict__.keys() 
					if x[0] != '_' or x not in dir(dict)]
	
	@classmethod
	def items(cls):
		return { k: v for (k,v) in cls.__dict__.items()
					if k[0] != '_' 
					or k not in dir(dict) 
					or k not in cls.__methods__}

def debug(message):
	pass                           # disables debugging output
	print(f"DEBUG: {message}")	

