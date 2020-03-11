# import the necessary packages
import numpy as np
import argparse
import cv2
 
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
 
# load the image and show it
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
 
# images are NumPy arrays, stored as unsigned 8 bit integers -- this
# implies that the values of our pixels will be in the range [0, 255]; when
# using functions like cv2.add and cv2.subtract, values will be clipped
# to this range, even if the added or subtracted values fall outside the
# range of [0, 255]. Check out an example:
print("max of 255: {}".format(str(cv2.add(np.uint8([200]), np.uint8([100])))))
print("min of 0: {}".format(str(cv2.subtract(np.uint8([50]), np.uint8([100])))))
 
# NOTE: if you use NumPy arithmetic operations on these arrays, the value
# will be modulo (wrap around) instead of being  clipped to the [0, 255]
# range. This is important to keep in mind when working with images.
print("wrap around: {}".format(str(np.uint8([200]) + np.uint8([100]))))
print("wrap around: {}".format(str(np.uint8([50]) - np.uint8([100]))))

# let's increase the intensity of all pixels in our image by 100 -- we
# accomplish this by constructing a NumPy array that is the same size of
# our matrix (filled with ones) and the multiplying it by 100 to create an
# array filled with 100's, then we simply add the images together; notice
# how the image is "brighter"
M = np.ones(image.shape, dtype = "uint8") * 100
added = cv2.add(image, M)
cv2.imshow("Added", added)
 
# similarly, we can subtract 50 from all pixels in our image and make it
# darker
M = np.ones(image.shape, dtype = "uint8") * 50
subtracted = cv2.subtract(image, M)
cv2.imshow("Subtracted", subtracted)

# 1. Question
# Assuming 8-bit, unsigned integers, what is the output of 200 + 68 using OpenCV?
print("1. Question: {}".format(str(cv2.add(np.uint8([200]), np.uint8([68])))))

# 2. Question
# Assuming 8-bit, unsigned integers, what is the output of 200 + 68 using NumPy?
print("2. Question: {}".format(str(np.uint8([200]) + np.uint8([68]))))

# 3. Question
# Again, assuming 8-bit unsigned integers, what is the output of 1 – 251 using OpenCV?
print("3. Question: {}".format(str(cv2.subtract(np.uint8([1]), np.uint8([251])))))

# 4. Question
# What about the output of 1 – 251 using NumPy?
print("4. Question: {}".format(str(np.uint8([1]) - np.uint8([251]))))

# 5. Question
# Download the source code from this lesson. Add value of 75 to all pixels to the grand_canyon.png image using the cv2.add function. What is the value of the pixel located at x=61, y=152?
M = np.ones(image.shape, dtype = "uint8") * 75
added = cv2.add(image, M)
(b, g, r) = added[152, 61]

print("r={r}, g={g} b={b}".format(b=b,r=r,g=g))

cv2.waitKey(0)