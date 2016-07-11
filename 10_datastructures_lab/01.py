import sys
ip= {'work':'10.0.0.2', 'router':'10.0.0.1', 'mycard': '10.0.0.5', 'router':'10.0.60.6'}
for arg in sys.argv:
	if arg in ip:
		print ip[arg]