# Author liuyang
# coding=utf-8
# @Time    : 2020/5/15 21:51
# @Site    : 
# @File    : app_cv_combination.py
# @Software: PyCharm

# ---功能描述
"""
图片按照上下左右排列
"""
import numpy as np
import cv2


# 正文

def app_main():
    img_left = np.zeros((320, 320, 3), np.uint8)
    img_left.fill(64)

    img_right = np.zeros((320, 320, 3), np.uint8)
    img_right.fill(128)

    img_front = np.zeros((320, 320, 3), np.uint8)
    img_front.fill(192)

    img_back = np.zeros((320, 320, 3), np.uint8)
    img_back.fill(222)

    img_center = np.zeros((320, 320, 3), np.uint8)
    img_center.fill(255)

    cv2.imshow("360 VR", img_center)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    app_main()
