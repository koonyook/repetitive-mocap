# Extracted kinematic features from repetitive upper-limb movements
This dataset contains extracted kinematic features from 2 groups of people, normal healthy subjects and stroke survivors. The healthy subject group includes 12 subjects (5 males and 7 females) between 25-59 years old. The stroke survivor group includes 14 subjects (6 males and 8 females) between 44-86 years old with the right arm affected. All of the subjects are in the chronic stage (more than six months post-stroke) at the moment of the data collection except one subject (NAH). Their Fugl-Meyer upper extremity motor sub-scores for shoulder-elbow-coordination portion range from 19 to 41 with the highest total score of 42 (without wrist and hand portions).

The movements include 4 repetitive actions (COMB, RECT, POUR, and TAP).

Healthy subject records include normal movement at a normal pace, normal movement at various pace, and normal movement with anomalous insertions. Those segments with simulated anomaly are labeled to the frame level. All those labels are also given.

Stroke survivor records include their own movements trying to follow the instructions that may include their natural anomaly.

Each session from healthy subjects is recorded by 3 different motion capture systems (with different levels of noise). Those systems are KinectV2, KinectV2+wrist-worn IMU, and a marker-based motion capture system.

All the sessions from stroke survivors may or may not have the record from a marker-based motion capture system.

The data collection protocol is approved by Nanyang Technological University Institutional Review Board (IRB-2018-03-036).

## Data and how to read it

As the raw records (sequences of depth images, and raw sensor data) from all the subjects combined are about 1TB, we are not able to share those data. To keep the data in a manageable size, we decide to extract and share important features from the upper body motion capture systems instead (~350MB). 

Each file with .ExportSessionProto extension contains those extracted information in time-series. You can follow the provided python example (fileReader.py) to read the information you want.

You need protobuf to read the *.ExportSessionProto files.

## protobuf installation
pip install protobuf