#objective
#read ExportSessionProto and dump as numpy data
#copy the whole structure inside d0ExportSessionProto

import FeatureExport_pb2 as pb
import numpy as np
import math
import glob
import os
import pickle

f=open(r'02Kinect+IMU\comb\mixAbnormal\AL_COMB_ab1_2018-09-27_10-03-34.ExportSessionProto','rb')
reader=pb.ExportSessionProto()
reader.ParseFromString(f.read())
f.close()

targetFrame=123
frame=reader.frames[targetFrame]

print('record length:',len(reader.frames),'frames')

print('extracted data from frame',targetFrame)
#unit vector
print(frame.rightSide.upperArmPointingDirectionX)
print(frame.rightSide.upperArmPointingDirectionY)
print(frame.rightSide.upperArmPointingDirectionZ)
#unit vector
print(frame.rightSide.forearmPointingDirectionX)
print(frame.rightSide.forearmPointingDirectionY)
print(frame.rightSide.forearmPointingDirectionZ)

print(frame.trunkFrontalTilt)	#[-90,90] degree
print(frame.trunkLateralTilt) 	#[-90,90] degree

print(frame.trunkOrientationX)	#[-90,90] degree
print(frame.trunkOrientationY)	#[-90,90] degree
print(frame.trunkOrientationZ)	#[-90,90] degree

print(frame.rightSide.preShoulderFront)	#[-90,90] degree
print(frame.rightSide.preShoulderUp)	#[-90,90] degree

print(frame.rightSide.forearmPronation)	#[-100,100] degree

print(frame.rightSide.shoulderInternalRotation)		#degree
print(frame.rightSide.elbowAngle)					#degree

#3D wrist position (meter)
print(frame.rightSide.wristX)		
print(frame.rightSide.wristY)
print(frame.rightSide.wristZ)
