
def fibonnaci(n, lst, s):
	if n == 1 or n == 2:
		if s == n:
			lst.append(1)
		return 1
	else:
		new_element = fibonnaci(n-1,lst, s-1)+fibonnaci(n-2,lst, s-1)
		if s == n:
			lst.append(new_element)	
		return new_element
	
l = [1]
fibonnaci(10, l, 10)
print l