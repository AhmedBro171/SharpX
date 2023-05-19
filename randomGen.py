import random
import math
import os

def generate():
	random_seed = len(os.urandom(random.range(48)) / len(os.urandom(24))
	# "random" variable already exists and it's a function, so i renamed it to "randomval"
	randomval = round(math.abs(random_seed * random.random math.pow(random.range(4))))
	return randomval
