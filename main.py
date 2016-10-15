#Course name: CST205. Multimedia Programming
#Program Title: FaceSwapp
#Abstract: This code inherits from a QtDesign generated .py file
# and displays a GUI interface. This interface is linked to faceswap.py
# which is a code used by the team to implement facial feature swapping.
# The interface is used to read images, read facial feature choices
# via checkboxes, and display an image that has the selected features
# from the second image swapped onto the first image.
#Authors: Adrian Figueroa, Darya Yanouskaya, Sebastian Magana-Garcia, Ian Devito
#Date: Friday, October 14th, 2016

#Adrian: Found the faceswapping code, set up main.py so other members
# only had to fill out blank functions linked to buttons, made actual functions from faceswap.py work
# with button presses
#Darya: Figured out how to make faceswap.py swap individual features,
# set up QPixmap to display final output image, and designed GUI. Also assisted
# Adrian in fixing a bug which made only fragments of faces be swappped.
#Sebastian: Set up checkboxes so that when a user clicks on a feature it adds those facial points
# to an initially empty list of facial points
#Ian: Set up checkbox functionality

from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtGui import *
import os
import sys
import design
import faceswap
import cv2
import dlib
import numpy


class SwapApp(QtGui.QMainWindow, design.Ui_FaceSwap):
    #Empty CV2 images and empty numpy data structures for use in multiple class member functions
    im1 = cv2.imread('')
    im2 = cv2.imread('')
    landmarks1 = numpy.empty([])
    landmarks2 = numpy.empty([])
   
    #This block links the buttons to their functions and sets text inside of text editing boxes
    def __init__(self, parent=None):
        super(SwapApp, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.swap)
        self.pushButton_2.clicked.connect(self.upload)
        self.textEdit.setText("Image name+format")
	self.textEdit_2.setText("Image 2 name+format")
    def upload(self):
	#Opens images and checks whether they exist in the program directory
	SwapApp.im1 = cv2.imread(str(self.textEdit.text()))
    	SwapApp.im2 = cv2.imread(str(self.textEdit_2.text()))
 	#If they do exist, it runs them through a function that returns landmarks for later use
	if (SwapApp.im1 != None and SwapApp.im2 != None):
		print("Images can be read")
		SwapApp.im1, SwapApp.landmarks1 = faceswap.read_im_and_landmarks(str(self.textEdit.text()))
		SwapApp.im2, SwapApp.landmarks2 = faceswap.read_im_and_landmarks(str(self.textEdit_2.text()))
		print("Images read")
		self.label.setText("Image 1 found")
		self.label_2.setText("Image 2 found")
		self.textEdit.setText(" ")
		self.textEdit_2.setText(" ")
	if (SwapApp.im1 == None):
		self.label.setText("Image 1 not found")
	if (SwapApp.im2 == None):
		self.label_2.setText("Image 2 not found")
    #This function checks if certain checkboxes are checked. If so it adds the corresponding face
    #points to the OVERLAY_POINTS list. OVERLAY_POINTS holds numbers which are points on the face.
    #This list will then be read by a function which will swap the corresponding points
    #NOTE: OVERLAY_POINTS is a global function from faceswap.py
    def swap(self):
	del faceswap.OVERLAY_POINTS[:]
	HOLDPOINTS = []
        print("You clicked swap")
        if (self.checkBox.isChecked() == True):
            print("Jaw is checked")
            HOLDPOINTS += faceswap.JAW_POINTS
        if (self.checkBox_2.isChecked() == True):
            print("Face is checked")
	    HOLDPOINTS += faceswap.FACE_POINTS
        if (self.checkBox_3.isChecked() == True):
            print("Brow is checked")
	    HOLDPOINTS += faceswap.RIGHT_BROW_POINTS
	    HOLDPOINTS += faceswap.LEFT_BROW_POINTS
        if (self.checkBox_4.isChecked() == True):
            print("Mouth is checked")
	    HOLDPOINTS += faceswap.MOUTH_POINTS
        if (self.checkBox_5.isChecked() == True):
            print("Eyes is checked")
	    HOLDPOINTS += faceswap.RIGHT_EYE_POINTS
            HOLDPOINTS += faceswap.LEFT_EYE_POINTS
        if (self.checkBox_6.isChecked() == True):
            print("Nose is checked")
	    HOLDPOINTS += faceswap.NOSE_POINTS
	faceswap.OVERLAY_POINTS.append(HOLDPOINTS)

	
	#The following code will only run if images exist. It aligns facepoints and then makes a warped
        # image of the second image that will be overlayed on to the first one. It also corrects colors
        # of skintones and blurs edges.
	if (SwapApp.im1 != None and SwapApp.im2 != None):
		M = faceswap.transformation_from_points(SwapApp.landmarks1[faceswap.ALIGN_POINTS],SwapApp.landmarks2[faceswap.ALIGN_POINTS])
		mask = faceswap.get_face_mask(SwapApp.im2, SwapApp.landmarks2)
		warped_mask = faceswap.warp_im(mask, M, SwapApp.im1.shape)
		combined_mask = numpy.max([faceswap.get_face_mask(SwapApp.im1, SwapApp.landmarks1), warped_mask], axis=0)
		
		warped_im2 = faceswap.warp_im(SwapApp.im2, M, SwapApp.im1.shape)
		warped_corrected_im2 = faceswap.correct_colours(SwapApp.im1, warped_im2, SwapApp.landmarks1)
		
		output_im = SwapApp.im1 * (1.0 - combined_mask) + warped_corrected_im2 * combined_mask
                #Outputs final imag and displays it using a QPixmap
		cv2.imwrite('output.jpg', output_im)
		outputdir = QPixmap(os.getcwd() + '/output.jpg')
		self.graphicsView.setPixmap(outputdir.scaled(self.graphicsView.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
	else:
		self.label.setText("Cannot swap")
		self.label_2.setText("empty files")
	
	
	

def main():
    app = QtGui.QApplication(sys.argv)
    form = SwapApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
