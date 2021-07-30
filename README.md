# AI_volume-controller
  This is an project which help to control our volume with help of our hand fingers.
  
# Requirements

Install a following requirements

     * pip install opencv-python

     * pip install mediapipe
 
 # About my project
 
 In this project i learn how to use opencv library and mediapipe library
 
 # OpenCv
 
* OpenCV (Open Source Computer Vision Library) is a library of programming functions mainly aimed at real-time computer vision.
* Originally developed by Intel, it was later supported by Willow Garage then Itseez. The library is cross-platform and free of cost. 
* Use under the open-source Apache 2 License.Starting with 2011, OpenCV features GPU acceleration for real-time operations.
 
 # OpenCv Applications

* 2D and 3D feature toolkits
* Egomotion estimation
* Facial recognition system
* Gesture recognition
* Human–computer interaction (HCI)
* Mobile robotics
* Motion understanding
* Object detection
* Segmentation and recognition
* Stereopsis stereo vision: depth perception from 2 cameras
* Structure from motion (SFM)
* Motion tracking
* Augmented reality

# Mediapipe

* MediaPipe is a cross-platform framework for building multimodal applied machine learning pipelines.
* MediaPipe is a framework for building multimodal (eg. video, audio, any time series data), cross platform (i.e Android, iOS, web, edge devices) applied ML pipelines. With MediaPipe, a perception pipeline can be built as a graph of modular components, including, for instance, inference models (e.g., TensorFlow, TFLite) and media processing functions.

# Cutting edge ML models:

* Face Detection
* Multi-hand Tracking
* Hair Segmentation
* Object Detection and Tracking
* Objectron: 3D Object Detection and Tracking
* AutoFlip: Automatic video cropping pipeline
* Cross Platform ML solutions
* Build once, deploy anywhere. Works optimally across mobile (iOS, Android), desktop server and the Web

# How its works

* First with help of mediapipe library detect a hand and track on it.

* With help of hand landmarks : https://www.google.com/url?sa=i&url=https%3A%2F%2Fgoogle.github.io%2Fmediapipe%2Fsolutions%2Fhands.html&psig=AOvVaw3Qjh0md8AbzSjVMLBoICwj&ust=1627732292635000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi0gb3divICFQAAAAAdAAAAABAD

* Put which two number will adjusted [I use [8] Index finger tip and [4] Thumb Tip]

* With a help of pycaw [Python Core Audio Windows library] Connect with Local audio controls Here link : https://github.com/AndreMiras/pycaw.

* And put your range depends on your display config and connect it with pycaw parameters.
 
