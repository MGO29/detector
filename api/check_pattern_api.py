from service.match_pattern import pattern_rec
import cv2
import numpy as np
import os
def check_pattern(img,chackOnlyPrint = True):
    img = np.array(img)
    if(chackOnlyPrint):
         #Check with original
        # original_Location = 'db_image/original/'
        # original_acc = []
        # original_image_location= []
        # for i in os.listdir(original_Location):
        #     orig_img = cv2.imread(original_Location+i)
        #     original_image_location.append(original_Location+i)
        #     original_acc.append(pattern_rec(orig_img,img))

        canny_Location = 'db_image/canny/'
        canny_acc = []
        canny_image_location= []
        for i in os.listdir(canny_Location):
            orig_img = cv2.imread(canny_Location+i)
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 
            edges = cv2.Canny(image=img_blur, threshold1=200, threshold2=10)
            canny_image_location.append(canny_Location+i)
            canny_acc.append(pattern_rec(edges,orig_img))
        return min(canny_acc),canny_image_location[canny_acc.index(min(canny_acc))]
    #Check with canny
    
    canny_Location = 'db_image/canny/'
    canny_acc = []
    for i in os.listdir(canny_Location):
        orig_img = cv2.imread(canny_Location+i)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 
        edges = cv2.Canny(image=img_blur, threshold1=200, threshold2=10)
        canny_acc.append(pattern_rec(edges,orig_img))


    #sobel with sobel
    sobel_Location = 'db_image/sobel/'
    sobel_acc = []
    for i in os.listdir(sobel_Location):
        orig_img = cv2.imread(sobel_Location+i)
        sobel_acc.append(pattern_rec(orig_img,img))


    #Check with original
    original_Location = 'db_image/original/'
    original_acc = []
    for i in os.listdir(original_Location):
        orig_img = cv2.imread(original_Location+i)
        original_acc.append(pattern_rec(orig_img,img))
    
    max_acc=0
    img_loc=''
    for x,y,z,i in canny_acc,original_acc,sobel_acc,os.listdir(original_Location):
        if sum(x,y,z) >= max_acc:
            max_acc = sum(x,y,z)
            img_loc = i
    return i 
