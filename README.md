Faceswap readme.md file


INTRODUCTION
------------
This program detects facial features on the photos and allows to transfer selected facial features from one face to another. 
Uploaded first, the Image 1 receives facial features from the Image 2.

You can find the files at: https://github.com/Insucha/CST205.git

Files included in this project:

Main.py						Mail file with combined codes
FaceSwap.py					Code for the Faceswap
Design.py					Code for the GUI Interface
shape_predictor_68_face_landmarks.dat.bz2	Trained model for analyzing poins of the face
Test1.jpg					Image 1.
Test2.jpg					Image 2.


REQUIREMENTS
------------
To run this program you need to have dlib, Python binding, QT, and Open CV installed.


RUNNING
-------
How To Run the "Faceswap":

	1. Make sure pictures you want to swap are in the same directory as main.py
	2. Run the "main.py" file.
	3. In the opened window upload your picture 1 and picture 2 (e.g. Test2.jpg, Test1.jpg in the text edit fields) 
       Pictures must have .png or .jpg formats and not exceed 340*640 pixels. You can use the ones provided by the authors.
	4. If you have done everything correctly, labels for picture 1 and 2 must change.
	5. Check the check-boxes with the features that you would like to transfer from the Picture 1 to the Picture 2.	
	6. Click "Swap" button. If successful, the result of the faceswap shoul appear in the window.


FUTURE WORK
-----------

Future plans for this project include additional filters and atributes to the swapped faces (like glasses, hat or makeup)
Moreover, we are planing to fix design bags and improve the interface in order to make it more user-friendly.
We will additionally work on the bug that prevents uploading second set of photos without closing the window.

SOURCES 
--------

Source for the Faceswap feature:

    http://matthewearl.github.io/2015/07/28/switching-eds-with-python/

