##Overview: This project demonstrates how to detect fire from images using YOLOv8 in Google Colab and from a webcam using PyCharm.

##Requirements: 
-Python 3.x
-OpenCV
-Google Colab 
-PyCharm 

##Setup
1.Clone this repository:git clone https://github.com/Hamida-majumder/mdmynoddin.git
2.Install dependencies:pip install -r requirements.txt
3.Download YOLOv8 weights

##Fire Detection from Images in Google Colab
1.Open the fire_detection_colab.ipynb notebook in Google Colab.

2.Follow the instructions in the notebook to upload your image(s) and run the detection process.

3.The detected images will be saved in the output/ directory.

##Fire Detection from Webcam in PyCharm
1.Open the fire_detection_pycharm.py script in PyCharm.

2.Make sure your webcam is connected and accessible by your system.

3.Run the script.

4.The webcam feed will open, and the script will detect fire in real-time.

#Custom Data
from roboflow import Roboflow

rf = Roboflow(api_key="ZxxNYh8DK5KRIhp90MPb")
project = rf.workspace("rehman-2vlay").project("fire-detection-vdtmc")
version = project.version(1)
dataset = version.download("yolov5")

##Evaluation: The below chart show the loss, mAP(mean,Average precision)score for the train,test,validation set.

![photo_2024-05-13_01-45-42](https://github.com/Hamida-majumder/mdmynoddin/assets/160351711/397165be-1267-4356-8bd4-c37b8ce69e8a)

##Confusion Matrix:

![photo_2024-05-13_01-50-05](https://github.com/Hamida-majumder/mdmynoddin/assets/160351711/96524d61-b0ac-4348-9f4c-824bf801d9ff)

##Result: fire detect from image

![photo_2024-05-13_01-51-18](https://github.com/Hamida-majumder/mdmynoddin/assets/160351711/50fe28b4-a7cc-4731-9245-494bb6903f3e)
and detect fire with alarm system from webcam 

![Screenshot (129)](https://github.com/Hamida-majumder/mdmynoddin/assets/160351711/48ff9945-f216-4c0f-84d6-cd5b0d6bae56)

