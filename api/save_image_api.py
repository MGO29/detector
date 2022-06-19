import cv2
import numpy as np


def save_pattern_image(img,imgName):
    img =  np.array(img)

    # Save Original Image
    original_location = 'db_image/original/'
    cv2.imwrite(original_location+imgName,img)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 

    # Save Canny Edge Detection
    canny_Location = 'db_image/canny/'
    edges = cv2.Canny(image=img_blur, threshold1=200, threshold2=10)
    cv2.imwrite(canny_Location+'edge_'+imgName,edges)

    # Save Sobel Image
    sobel_location = 'db_image/sobel/'
    sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=1)
    cv2.imwrite(sobel_location+'sobelxy_'+imgName,sobelxy)

    return True
