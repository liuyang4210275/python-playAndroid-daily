# Author liuyang
# coding=utf-8
# @Time    : 2020/4/15 20:36
# @Site    :
# @File    : app_posenet_cv_hikvision.py
# @Software: PyCharm

# ---功能描述
"""
使用openCV显示图像，并处理图像的内容
"""

# 正文
import cv2
import time

import queue
from concurrent.futures import ThreadPoolExecutor
import os
import traceback
import imageio
import numpy as np
import skimage

# 帧图像队列,将frame 放入队列中
q = queue.Queue()
executor = ThreadPoolExecutor(max_workers=10)
camera = None
client = None
host = '192.168.0.60'


def imageio_capture():
    iv = imageio.get_reader('700', 'ffmpeg')
    for img in enumerate(iv):
        image2 = skimage.img_as_float(img).astype(np.float32)
        cv2.imshow('abc', image2)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


def app_video_capture():
    global camera
    camera = cv2.VideoCapture()
    camera.open('/dev/video0', apiPreference=cv2.CAP_V4L2)

    camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
    # camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('H', '2', '6', '4'))
    # camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('I', '4', '2', '2'))
    camera.set(cv2.CAP_PROP_FPS, 20)
    if camera.isOpened():
        ref, frame = camera.read()
        print('视频流打开')
    else:
        ref = False
        print('视频流失败')
    while ref:
        ref, frame = camera.read()
        q.put(frame)
        q.get() if q.qsize() > 1 else time.sleep(0.01)


def image_get():
    cv2.namedWindow('faces', flags=cv2.WINDOW_FREERATIO)
    cv2.resizeWindow('faces', 640, 480)
    while True:
        frame = q.get()
        if frame is None:
            continue
        try:
            cv2.imshow("faces", frame)
        except Exception as e:
            traceback.print_exc()
            print('报错')
            pass
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    if camera is not None:
        camera.release()
    if client is not None:
        client.close()
    print('关闭窗口')
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # 编号 0 硬件

    # task1 = executor.submit(app_video_capture)
    # task_show = executor.submit(image_get)
    # while task_show.running():
    #     time.sleep(0.02)
    #     continue
    # print('结束')
    # os._exit(0)
    imageio_capture()
