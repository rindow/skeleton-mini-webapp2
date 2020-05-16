import sys,os
for path in [
	'rindow/framework/lib',
]:
	sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), path)))
