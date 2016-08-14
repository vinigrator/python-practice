"""
    
"""
import random

def generate_some_names():
    names = ['Tetardis', 'Estinira', 'Deilanla', 'Deirisell', 'Mirdaren', 'Yarmiel']
	#random.seed()
    with open('names.txt', 'w') as f:
		for cnt in range(0,200):
			f.write(names[random.randrange(0,6,1)]+"\n")
    f.close()
	
generate_some_names()