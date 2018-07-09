# Server.py to be run in unity or blender
#set  blender on game engine and create keypoints using spheres
#access these in real time to get body pose based movement
#import bpy
import socket
import json

host = "127.0.0.1"
port = 1234
buffer_size = 1024

my_socket = socket.socket()
my_socket.bind( (host, port) )

my_socket.listen(1);		# listen indefinately
conn, addr = my_socket.accept()
print("Connected to client at :"+str(addr))

# since we read buffer_size bytes every time, we need the client to send just 1 json string each time, else we may read many buffered strings and json.loads() gives adn error, hence synchronization is needed.
while True:
	data = conn.recv(buffer_size).decode()
	if not data:
		break
	data = json.loads(data)

	conn.send("ACK".encode())		# for synchronization
	print("{0}: ({1},{2})\n".format(data['p1_id'], data['x1_coord'], data['y1_coord']))
	print("{0}: ({1},{2})\n".format(data['p2_id'], data['x2_coord'], data['y2_coord']))
	
conn.close()
