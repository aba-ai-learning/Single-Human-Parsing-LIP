# -*- coding: utf-8 -*-

import os
import cv2
import numpy as np
import tqdm
    

index2label = {
    0 : 'Background',
    1 : 'Hair',
    4 : 'Upclothes',
    5 : 'Left-shoe',
    6 : 'Right-shoe',
    8 : 'Pants',
    9 : 'Left_leg',
    10 : 'Right_leg',
    11 : 'Left_arm',
    12 : 'Face',
    13 : 'Right_arm',
}

cmap = np.array([(0, 0,  0), (81,  0, 81),
                 (128, 64, 128), (244, 35, 232), (250, 170, 160), (230,
                                                                   150, 140), (70, 70, 70), (255, 255, 255), (190, 153, 153),
                 (180, 165, 180), (150, 100, 100), (150, 120, 90), (153,
                                                                    153, 153), (153, 153, 153), (250, 170, 30), (220, 220,  0),
                 (107, 142, 35), (152, 251, 152), (70, 130, 180), (220,
                                                                   20, 60), (255,  0,  0), (0,  0, 142), (0,  0, 70),
                 (0, 60, 100), (0,  0, 90), (0,  0, 110), (0, 80, 100), (0,  0, 230), (119, 11, 32), (0,  0, 142)],
                dtype=np.uint8)



if __name__ == "__main__":
    cwd = os.getcwd()

    trainidfile = os.path.join(cwd, 'myLIP/train/id.txt')
    trainlabelfolder = os.path.join(cwd, 'myLIP/train/gt/')
    trainimgfolder = os.path.join(cwd, 'myLIP/train/img/')
    idlines = open(trainidfile, 'r').readlines()

    for item in tqdm.tqdm(idlines):
        item = item.strip() + '.jpg'
        itemlabel = item.strip().replace('.jpg', '.png')
        labelfile = os.path.join(trainlabelfolder, itemlabel)
        imgfile = os.path.join(trainimgfolder, item)
        print(labelfile)

        labelimg = cv2.imread(labelfile)
        img = cv2.imread(imgfile)

        for i in range(labelimg.shape[0]):
            for j in range(labelimg.shape[1]):
                label = labelimg[i][j][0]
                color = cmap[label]
                labelimg[i][j] = color
                # print(color)

        # #wash label 7 noise
        # mask = np.array(labelimg == 7)
        # labelimg[mask] = 255

        # cv2.imwrite(labelfile,  labelimg)

        # maskclothes = np.array(labelimg == 7)
        # labelimg[maskclothes] = 255
        
        # labelimg = labelimg * (1-mask) + 
        # print(mask.shape)
        # print(mask)

        cv2.imshow('labelimg', labelimg)
        cv2.imshow('origimg', img)
        cv2.waitKey(0)
        
        
                

