import collections
def swapchars (st) :
	com = collections.Counter(st).most_common()
	com = filter ((lambda (c,n): c != " "), com)
	if len(com) > 1:
		(most, n) = com[0]
		(least, m) = com[len(com) - 1]
		new_st = ""
		for ch in st:
			if ch == most:
				new_st += least
			elif ch == least:
				new_st += most
			else:
				new_st += ch
		return new_st
	return st

print swapchars('I\'m just a chi-town coder with a nice flow.')

def sortcat (*arg):
	n = arg[0]
	strs = list(arg[1:])
	catstr = ""
	if n == -1:
		n = len(strs)
	for i in range (0,n):
		m = max(strs, key=len)
		catstr += m
		strs.remove(m)
	return catstr

print sortcat(-1, 'bc', 'c', 'abc')

def load_states (d):
	with open("states.txt") as f:
		for line in f:
			(val, key) = line.split(',')
			d[key.rstrip()] = val

abbrev = {}
load_states (abbrev)

def abbrev_to_name (ab, abbrev): 
	return abbrev[ab]

print abbrev_to_name ("PA", abbrev)

def name_to_abbrev (name, abbrev):
	for key in abbrev:
		if abbrev[key] == name:
			return key

print name_to_abbrev ("Nebraska", abbrev)
