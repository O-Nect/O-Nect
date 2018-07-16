
O-Nect is an Open Source Interface for Unity Game developers which uses deep learning (human pose estimation) along with socket connectivity which provides kinect similar performance with just a regular RGB camera.

Yes,No sensors required.


![alt text](https://github.com/O-Nect/O-Nect/O-nect.gif)
Inspired by the work of OpenPose Developers(Caffe) : https://github.com/CMU-Perceptual-Computing-Lab/openpose
We believe that this holds alot of potential and the users can manipulate the code as per their convenience.

You need dependencies below.
- python3
- tensorflow 1.4.1+
- opencv3, protobuf, python3-tk
- socket,json,threading

use : $pip install -r requirements.txt
and Blender

Once you've got everything ready
Run this command for RealTime Webcam 

$ python run_webcam.py --camera=0
You can now use socket based connectivity in Unity to access the keyPoints in real-time to use it as per your game design.

We have tested the performance to be around 15fps on a gtx 1050Ti 4gb GPU on blender game engine using socket in python.
The user can use unity or any other game engine with socket support and implement the desired module.

We send cordinates using json + sockets .The basic layout of the json file is given below

json data format
{
data['p1_id'], data['x1_coord'], data['y1_coord']
data['p2_id'], data['x2_coord'], data['y2_coord']
}

We welcome contributers to test the product.
We've now added a blend file to our repo.
Run the blender script and run_webcam.py from src 
(Unity Support To be added soon)

We currently only support blender and are looking for contributers to port this to unity3D.
