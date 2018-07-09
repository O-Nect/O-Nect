import requests
import time

while 1:
	URL = "http://localhost:5000/retrieve"
	r = requests.get(url=URL)
	print("Get request sent: ")
	data = r.json()
	
	p1_id = [p for p in data['p1_id']]
	x1_coords = [x for x in data['x1_coord']]
	y1_coords = [y for y in data['y1_coord']]
	p2_id = [p for p in data['p2_id']]
	x2_coords = [x for x in data['x2_coord']]
	y2_coords = [y for y in data['y2_coord']]

	coordinates = list(zip(p1_id, x1_coords, y1_coords, p2_id, x2_coords, y2_coords))
	for c in coordinates:
		print("Received coordinate "+str(c)+" in response")
	print()

	time.sleep(1)
