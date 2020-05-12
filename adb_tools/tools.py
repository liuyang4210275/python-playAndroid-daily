# Author liuyang
# coding=utf-8
# @Time    : 2020/5/9 21:53
# @Site    : 
# @File    : tools.py
# @Software: PyCharm

# ---功能描述
"""
adb工具集合,
adb在开启多个的情况下会反应很慢
"""
import subprocess

# 正文

st = subprocess.STARTUPINFO
st.dwFlags = subprocess.STARTF_USESHOWWINDOW
st.wShowWindow = subprocess.SW_HIDE


def list_devices():
    """
    查找全部可连接的设备
    adb devices
    List of devices attached
    41cecaa9	device
    emulator-5554	device
    :return: 可连接的设备序号字符数组
    """
    devices = []
    cmd1 = ['adb', 'devices']
    print(' '.join(cmd1))
    p = subprocess.Popen(args=cmd1, stdout=subprocess.PIPE, encoding='utf-8', shell=True, startupinfo=st)
    for line in p.stdout.readlines():
        line = line.strip()
        if line.endswith('device'):
            arr = line.split('\t')
            # print(arr)
            devices.append(arr[0])
    return devices


def screen_cap_normal(device_id):
    """
    截图，下载，删除
    :param device_id: 
    :return: 
    """
    # adb -s emulator-5554 shell screencap -p /sdcard/screen.png
    cmd1 = ['adb', '-s', device_id, 'shell', 'screencap', '-p', '/sdcard/screen.png']
    # adb -s emulator-5554 pull /sdcard/screen.png
    cmd2 = ['adb', '-s', device_id, 'pull', '/sdcard/screen.png', './out']
    # adb -s emulator-5554 shell rm /sdcard/screen.png
    cmd3 = ['adb', '-s', device_id, 'shell', 'rm', '-rf', '/sdcard/screen.png']
    cmd1.append("&&")
    cmd1.extend(cmd2)
    cmd1.append("&&")
    cmd1.extend(cmd3)
    print(' '.join(cmd1))
    p = subprocess.Popen(args=cmd1, stdout=subprocess.PIPE, encoding='utf-8', shell=True, startupinfo=st)
    for line in p.stdout.readlines():
        line = line.strip()
        print(line)
    pass


def screen_cap_exec(device_id):
    """
    截图到本地
    :param device_id: 
    :return: 
    """
    cmd1 = ['adb', '-s', device_id, 'exec-out', 'screencap', '-p', '>', './out/sc.png']
    print(' '.join(cmd1))
    p = subprocess.Popen(args=cmd1, stdout=subprocess.PIPE, encoding='utf-8', shell=True, startupinfo=st)
    for line in p.stdout.readlines():
        line = line.strip()
        print(line)
    pass


def input_tap(device_id, x, y):
    cmd1 = ['adb', '-s', device_id, 'shell', 'input', 'tap', str(x), str(y)]
    print(' '.join(cmd1))
    p = subprocess.Popen(args=cmd1, stdout=subprocess.PIPE, encoding='utf-8', shell=True, startupinfo=st)
    for line in p.stdout.readlines():
        line = line.strip()
        print(line)
    pass


if __name__ == '__main__':
    devices = list_devices()
    print(devices)
    screen_cap_exec(devices[0])
