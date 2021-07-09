# -*- coding: utf-8 -*-
"""Object detection testing.ipynb

## Mounting Google Drive and GPU
"""

#from google.colab import drive
#drive.mount('/content/gdrive')

# make sure you use Tesla K80 GPU (12GB), by changing 'runtime type' 
!nvidia-smi

"""## Cloning Darknet GitHub repository"""

import os
os.environ['PATH'] += ':/usr/local/cuda/bin'
!rm -fr darknet
!git clone https://github.com/AlexeyAB/darknet/

!apt install gcc-5 g++-5 -y
!ln -s /usr/bin/gcc-5 /usr/local/cuda/bin/gcc 
!ln -s /usr/bin/g++-5 /usr/local/cuda/bin/g++

"""##Enable GPU"""

# Commented out IPython magic to ensure Python compatibility.
# %cd darknet
!sed -i 's/GPU=0/GPU=1/g' Makefile
!sed -i 's/OPENCV=0/OPENCV=1/g' Makefile
!make

"""##Import YOLO Weights file"""

!wget https://pjreddie.com/media/files/yolov3.weights
!chmod a+x ./darknet

!pwd

!apt install ffmpeg libopencv-dev libgtk-3-dev python-numpy python3-numpy libdc1394-22 libdc1394-22-dev libjpeg-dev libtiff5-dev libavcodec-dev libavformat-dev libswscale-dev libxine2-dev libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libv4l-dev libtbb-dev qtbase5-dev libfaac-dev libmp3lame-dev libopencore-amrnb-dev libopencore-amrwb-dev libtheora-dev libvorbis-dev libxvidcore-dev x264 v4l-utils unzip

"""## It's time to upload the video"""

from google.colab import files

uploaded = files.upload()

!wget http://pjreddie.com/media/files/darknet53.conv.74

!cp cfg/yolov3.cfg yolov3-obj.cfg

!./darknet partial cfg/yolov3-tiny.cfg cfg/yolov3-tiny.weights fire/model/yolov3-tiny.conv.15 15

!./darknet detector train cfg/coco.data cfg/yolov3.cfg darknet53.conv.74

!./darknet detector demo cfg/coco.data cfg/yolov3.cfg yolov3.weights -dont_show test_video.mp4 -i 0 -out_filename outputtv1.avi -thresh 0.7

from google.colab import files
files.download('outputdt.avi')

