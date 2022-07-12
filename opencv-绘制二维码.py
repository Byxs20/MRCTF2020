import cv2
import numpy as np


file = open("./flag/qr.txt", "r").read()
arr = [eval(i) for i in file.splitlines()]
img = np.array(arr, dtype=np.uint8).reshape((200, 200, 3))

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()