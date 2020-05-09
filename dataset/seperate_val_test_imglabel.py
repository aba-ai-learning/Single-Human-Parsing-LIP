import os
import random
from shutil import copyfile

if __name__ == "__main__":

    cwd = os.getcwd()

    ## mv test val img and label according to id.txt
    imgfolder = os.path.join(cwd, 'myLIP/test_img')
    labelfolder = os.path.join(cwd, 'myLIP/test_label')

    testimgfolder = os.path.join(cwd, 'myLIP/test/img')
    testlabelfolder = os.path.join(cwd, 'myLIP/test/label')
    valimgfolder = os.path.join(cwd, 'myLIP/val/img')
    vallabelfolder = os.path.join(cwd, 'myLIP/val/label')

    if not os.path.exists(testimgfolder):
        os.mkdir(testimgfolder)
    if not os.path.exists(testlabelfolder):
        os.mkdir(testlabelfolder)
    if not os.path.exists(valimgfolder):
        os.mkdir(valimgfolder)
    if not os.path.exists(vallabelfolder):
        os.mkdir(vallabelfolder)

    valid = os.path.join(cwd, 'myLIP/val/id.txt')
    testid = os.path.join(cwd, 'myLIP/test/id.txt')

    validlist = open(valid, 'r').readlines()
    testidlist = open(testid, 'r').readlines()

    for validitem in validlist:
        validitem = validitem.strip()
        srcimg = os.path.join(imgfolder, validitem)
        dstimg = os.path.join(valimgfolder, validitem)
        srclabel = os.path.join(labelfolder, validitem.replace('.jpg', '.png'))
        dstlabel = os.path.join(vallabelfolder, validitem.replace('.jpg', '.png'))
        copyfile(srcimg, dstimg)
        copyfile(srclabel, dstlabel)

    for testitem in testidlist:
        testitem = testitem.strip()
        srcimg = os.path.join(imgfolder, testitem)
        dstimg = os.path.join(testimgfolder, testitem)
        srclabel = os.path.join(labelfolder, testitem.replace('.jpg', '.png'))
        dstlabel = os.path.join(testlabelfolder, testitem.replace('.jpg', '.png'))
        copyfile(srcimg, dstimg)
        copyfile(srclabel, dstlabel)
