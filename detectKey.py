import tty, sys

def checking():
	tty.setraw(sys.stdin.fileno())
	while True:
		ch = sys.stdin.read(1)
		if ch == 'a':
			print "Wohoo"
			break
checking()