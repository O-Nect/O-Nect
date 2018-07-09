from flask import Flask
from flask import request
from flask import jsonify
app = Flask(__name__)

g_coordinates = []		# stores all the received coordinates
						# Also acts as a buffer until it receives the request from C#
g_coord_index = 0		# Acts as a pointer, maintaining the position of the unset coordinates

@app.route("/")
def hello():
    return "Hello!<br>To store coordinates on the server type the foll. url in the browser:<br> \
    		localhost:5000/store?x_coord=0.61&y_coord=0.87 <br> OR <br>To retreive the \
    		coordinates in json format: <br> localhost:5000/retrieve "

@app.route("/store", methods=['GET'])
def store_coord():
    global g_coordinates, g_coord_index

    x_coord = float(request.args.get('x_coord'))
    y_coord = float(request.args.get('y_coord'))

    g_coordinates.append((x_coord, y_coord))

    #return ""
    return str(g_coordinates[-1:]) + " was successfully stored on the server! <br> g_coordinates = " + str(g_coordinates) + "<br> g_coord_index = " + str(g_coord_index)

@app.route("/retrieve")
def retrieve_coord():
	global g_coordinates, g_coord_index

	x_coords = []
	y_coords = []
	for i in range(g_coord_index, len(g_coordinates)):
		x_coords.append(g_coordinates[i][0])
		y_coords.append(g_coordinates[i][1])
	g_coord_index = len(g_coordinates)

	return jsonify({'x_coord':x_coords, 'y_coord':y_coords})

if __name__ == "__main__":
	app.run(host="0.0.0.0",debug=True)