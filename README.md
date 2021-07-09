# Overview
System to determine whether an individual is following the rule of social distancing or not. 

# Algorithm
The system detects human beings in the video stream using YOLO model. It then computes the pairwise distance between the people with respect to their centroids. System checks whether the distance matrix of people less than N pixels apart, if Yes then People maintaining Social Distancing or else violating the rule. The dataset used for training is COCO dataset. 

![](Modules/Images/Dataflow.JPG)

