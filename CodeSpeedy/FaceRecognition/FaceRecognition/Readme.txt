Face Recognition Tool using Python:

This is a Face Recognition Tool built using Python. It can compare two photos and check if both images have the same face.


Detailed Description:

This is a Face Recognition Tool built using Python. It can compare two photos and check if both images have the same face. I have used
python libraries OpenCV, Dlib and face_recognition which can efficiently give the output whether both the images have same face.


Technologies:

Language: Python
Libraries: OpenCV, Dlib, face_recognition
Platform: Jupyter Notebook (Python Anaconda distribution)


Installation of Python Libraries:

Open Terminal

To install the modules (OpenCV) type the following commands:-

pip install opencv-python.





we need to install two additional libraries:

dlib & face_recognition


Now we can install dlib. First of all, we need to install CMake library to install dlib library.

pip install cmake


Then, you can install dlib library using pip install.

pip install dlib


Alternatively, Dlib can be installed using the wheel file also.

I have attatched the Dlib Wheel file with the Project File.

Go to that folder where the Dlib Wheel File is stored (Lib/Dlib_Python3.10) > Then Open with Terminal >

Enter the following Command:

pip install dlib-19.22.99-cp310-cp310-win_amd64.whl

**** This Dlib Wheel File is compatible with Python 3.10 Version. The Dlib Wheel File Compatible with
a corresponding Python Version is easily available on Internet.



Now, Enter the following command to install face_recognition Library.

pip install face-recognition


How to Use:

Install Anaconda and Jupyter Notebook

1. Go to the Project Folder where the corresponding python file is saved.

2. Right Click > Open in Terminal > Enter in Terminal : jupyter notebook

The Jupyter Notebook will be opened

Go to the Jupyter Source File (FaceRecognize.ipynb)

3. Check any two images through the Python Project if both images have same face.

4. If both images have same face, it will return True and will display the message "Face Matched!!!",
otherwise it will return False and will display the message "Face Not Matched!!!"



 