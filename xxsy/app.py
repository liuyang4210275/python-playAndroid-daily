# Author liuyang
# coding=utf-8
# @Time    : 2020/5/10 0:59
# @Site    : 
# @File    : app.py
# @Software: PyCharm

# ---功能描述
"""
获取屏幕的截图，分析出需要的view
"""
import cv2
import time
import adb_tools
from PIL import ImageGrab


# 正文


def app_main():
    device_ids = adb_tools.list_devices()
    adb_tools.screen_cap_exec(device_ids[0])
    image = cv2.imread('./out/sc.png')
    # 灰度图
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    height_ = image_gray.shape[0]
    width_ = image_gray.shape[1]
    # print("width:{},height:{}".format(width_, height_))
    # 展示画框
    p, pt1, pt2 = find_into_game(width_, height_)
    cropImg = image_gray[pt1[1]: pt2[1], pt1[0]: pt2[0]]
    # cv2.imwrite('./data/login/1.into_game.png', cropImg)

    # image = cv2.rectangle(img=image, pt1=(10, 10), pt2=(30, 30), color=(33, 33, 255), thickness=1)
    image = cv2.rectangle(img=image, pt1=pt1, pt2=pt2, color=(33, 33, 255), thickness=2)
    cv2.imshow('xxsy', image)
    adb_tools.input_tap(device_ids[0], p[0], p[1])
    cv2.waitKey(0)


def find_into_game(w, h):
    # 找出按钮
    # 进入游戏
    wc = w // 2
    hc = (h // 50) * 42
    return (wc, hc), (wc - 70, hc - 30), (wc + 70, hc + 30)


if __name__ == '__main__':
    app_main()
