import os

def show_info_and_delete_file(f):
	print f + " - " + str(os.path.getsize(f))
	os.remove(f)

show_info_and_delete_file("names.txt")