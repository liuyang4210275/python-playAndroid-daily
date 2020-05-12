# Author liuyang
# coding=utf-8
# @Time    : 2020/5/11 23:41
# @Site    : 
# @File    : cam_pyv4l2.py
# @Software: PyCharm

# ---功能描述
"""
https://github.com/duanhongyi/pyv4l2
sudo apt-get install libv4l-dev
pip3 install pyv4l2
"""

# 正文

from pyv4l2.frame import Frame
from pyv4l2.control import Control

frame = Frame('/dev/video0')
frame_data = frame.get_frame()
control = Control("/dev/video0")
control.get_controls()
control.get_control_value(9963776)
control.set_control_value(9963776, 8)
