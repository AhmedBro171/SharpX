import random
import math
import os

def generate():
	prekey = random.range(32786) * 70
	random_seed = random.range(math.pow(2, 31) - 1)
	gena = random_seed / random.range(math.pow(2, 15) - 1) + math.pow(2, 4)
	genb = gena / random_seed
	genc = gena - genb * 3 + prekey
	gend = random_seed * gena / genc
	gen = gend - genc / prekey
	return gen
