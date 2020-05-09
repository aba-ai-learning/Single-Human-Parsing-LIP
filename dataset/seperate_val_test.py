import os
import random

if __name__ == "__main__":

    cwd = os.getcwd()
    ## create train id.txt
    trainimgfolder = os.path.join(cwd, 'myLIP/train/train_img')
    trainimglist = os.listdir(trainimgfolder)
    trainimglistfilter = [item for item in trainimglist if item.endswith('.jpg')]

    trainid = os.path.join(cwd, 'myLIP/train/id.txt')
    filetrainid = open(trainid, 'w+')

    for item in trainimglistfilter:
        filetrainid.write(item + '\n')



    ## create test val id.txt
    testimgfolder = os.path.join(cwd, 'myLIP/test_img')
    testimglist = os.listdir(testimgfolder)
    testimglistfilter = [item for item in testimglist if item.endswith('.jpg')]

    valid = os.path.join(cwd, 'myLIP/val/id.txt')
    testid = os.path.join(cwd, 'myLIP/test/id.txt')

    filevalid = open(valid, 'w+')
    filetestid = open(testid, 'w+')


    for  item in testimglistfilter:
        if random.random() > 0.5:
            filevalid.write(item+'\n')
        else:
            filetestid.write(item+'\n')
