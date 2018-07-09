# client.py to be run in python

import socket
import json

host = "127.0.0.1"
port = 1234
buffer_size = 1024

my_socket = socket.socket()
my_socket.connect( (host, port) )

# sample data
a = [d/10 for d in range(1, 51, 5)]
b = [d/10 for d in range(3, 53, 5)]
humans = list(zip(a,b))
# [(0.1, 0.3), (0.6, 0.8), (1.1, 1.3), (1.6, 1.8), (2.1, 2.3), (2.6, 2.8), (3.1, 3.3), (3.6, 3.8), (4.1, 4.3), (4.6, 4.8)]
p1_id = 1
p2_id = 2

for x, y in humans:
	x1_coord = x
	y1_coord = y
	x2_coord = x+5
	y2_coord = y+5
	data = {'p1_id':p1_id,'x1_coord':x1_coord, 'y1_coord':y1_coord,'p2_id':p2_id,'x2_coord':x2_coord, 'y2_coord':y2_coord}
	data = json.dumps(data)
	p1_id += 2;	p2_id += 2
	
	print("Sending {} to server\n".format(data))
	my_socket.send(data.encode())

	ret = my_socket.recv(buffer_size).decode()		# for synchronization

my_socket.close()
