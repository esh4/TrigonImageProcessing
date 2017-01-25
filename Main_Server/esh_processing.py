import cv2
import numpy as np


class Processing:
	def threshold(self, frame, lThresh, hThresh):
		threshed_image = cv2.inRange(cv2.medianBlur(frame, 15), np.array(lThresh), np.array(hThresh))
		_, cnts, _ = cv2.findContours(threshed_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		contour_image = cv2.drawContours(threshed_image, cnts, -1, (0, 255, 0), 3)
		return contour_image, cnts

