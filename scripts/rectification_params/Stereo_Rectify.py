#!/usr/bin/env python3

import cv2 as cv
import os
import numpy as np
import matplotlib.pyplot as plt

camera_matrix_left = np.array( [[923.127713710528, 0, 687.4228471324863],
                       [0, 925.2110354167382, 546.3225816092311],
                       [0, 0, 1]] )
camera_matrix_right = np.array( [[923.0960152412666, 0, 675.9074027774546],
                       [0, 925.7985594359268, 543.1698626136331],
                       [0, 0, 1]] )

distortionCoefficients_left = np.array( [-0.1705266572420859, 0.09052954356608053, 0.0008524091088442974, 0.00014363914590400428, 0.0] )
distortionCoefficients_right = np.array( [-0.16407642566321382, 0.0969413015313159, 0.0002351104695664023, 0.00033062719152664123, 0.0] )

frame_resolution = (1376, 1100)

rotation_lc_to_rc = np.array( [[ 0.9998011594343311, 0.019937510930602562, -0.0003704749129950495],
                     [ -0.019936812872882174, 0.9997996198762341, 0.0018009963384764628],
                     [ 0.00040630806137048066, -0.001793252138331271, 0.9999983095788358]] ) 

translation_lc_to_rc = np.array( [0.14940543637139198, -0.000351444945639901, -0.0036748354043960475] ) 

R1 = np.zeros(shape=(3,3))
R2 = np.zeros(shape=(3,3))
P1 = np.zeros(shape=(3,4))
P2 = np.zeros(shape=(3,4))

cv.stereoRectify(camera_matrix_left, distortionCoefficients_left, camera_matrix_right, distortionCoefficients_right, 
                frame_resolution, rotation_lc_to_rc, translation_lc_to_rc, R1, R2, P1, P2, Q=None, alpha=-1, newImageSize=(0,0))

print(P1)
print("=====================")
print(P2)
print("=====================")
print(R1)
print("=====================")
print(R2)