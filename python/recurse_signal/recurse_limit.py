from sys import setrecursionlimit
from sys import exit

import signal


def signal_handler(sig, frame):
	exit(0)
	pass


def recurse(n):	
	print(n)
	recurse(n+1)


if __name__ == '__main__':	
	signal.signal(signal.SIGSEGV, signal_handler)
	setrecursionlimit(1000000000)
	recurse(1)	
