# ADB工具命令

## 基本语法
`adb [-d|-e|-s]`

|参数|描述|
| --- | --- |
|-d|指定当前唯一通过 USB 连接的 Android 设备为命令目标|
|-e|指定当前唯一运行的模拟器为命令目标|
|-s `serialNumber`|指定相应 serialNumber 号的设备/模拟器为命令目标|

- 查看adb版本
```shell script
$ adb version
Android Debug Bridge version 1.0.41
Version 29.0.6-6198805
Installed as \usr\local\android_sdk\platform-tools\adb.exe
```

- 查看设备
```shell script
$ adb devices
List of devices attached
emulator-5554   device
```

- 获取屏幕分辨率
```shell script
$ adb -s emulator-5554 shell wm size
Physical size: 960x540
```

- 安装APK
```shell script
$ adb -s emulator-5554 install \home\pi\test.apk
Performing Streamed Install
Success
```

- 卸载APK
`adb shell pm list packages [-f] [-d] [-e] [-s] [-3] [-i] [-u] [--user USER_ID] [FILTER]`

|参数|描述|
| --- | --- |
|无|所有应用|
|-f|显示应用关联的 apk 文件|
|-d|只显示 disabled 的应用|
|-e|只显示 enabled 的应用|
|-s|只显示系统应用|
|-3|只显示第三方应用|
|-i|显示应用的 installer|
|-u|包含已卸载应用|
|`<FILTER>`|包名包含 <FILTER> 字符串|

查找apk
卸载指定apk
```shell script
$ adb -s emulator-5554 shell pm list packages
package:com.android.cts.priv.ctsshim
package:com.android.providers.telephony
package:com.android.providers.calendar
package:com.android.providers.media
package:com.android.documentsui
package:com.android.externalstorage
package:com.android.htmlviewer
package:com.android.mms.service
package:com.android.providers.downloads
package:com.android.browser
package:com.android.inputmethod.pinyin
package:com.android.defcontainer
package:com.android.providers.downloads.ui
package:com.android.pacprocessor
package:com.android.certinstaller
package:com.android.carrierconfig
package:android
package:com.android.contacts
package:com.android.mtp
package:com.android.launcher3
package:com.android.provision
package:com.android.statementservice
package:com.android.providers.settings
package:com.android.sharedstoragebackup
package:com.android.printspooler
package:com.android.webview
package:android.ext.shared
package:com.android.server.telecom
package:com.android.keychain
package:com.android.gallery3d
package:com.android.flysilkworm
package:android.ext.services
package:com.android.packageinstaller
package:com.android.basicsmsreceiver
package:com.android.proxyhandler
package:com.cyanogenmod.filemanager
package:com.android.googleinstaller
package:com.android.storagemanager
package:com.android.bookmarkprovider
package:com.android.settings
package:com.android.cts.ctsshim
package:com.android.vpndialogs
package:com.android.phone
package:com.android.shell
package:com.android.wallpaperbackup
package:com.android.providers.blockednumber
package:com.android.providers.userdictionary
package:com.android.location.fused
package:com.android.systemui
package:com.android.providers.contacts
package:com.android.captiveportallogin
package:com.android.coreservice

$ adb -s emulator-5554 uninstall com.test.info
Success
```

- root运行
```shell script
C:\Users\android>adb root
adbd is already running as root
```

- 模拟按键/输入
```text
Usage: input [<source>] <command> [<arg>...]

The sources are:
      mouse
      keyboard
      joystick
      touchnavigation
      touchpad
      trackball
      stylus
      dpad
      gesture
      touchscreen
      gamepad

The commands and default sources are:
      text <string> (Default: touchscreen)
      keyevent [--longpress] <key code number or name> ... (Default: keyboard)
      tap <x> <y> (Default: touchscreen)
      swipe <x1> <y1> <x2> <y2> [duration(ms)] (Default: touchscreen)
      press (Default: trackball)
      roll <dx> <dy> (Default: trackball)
```

|keycode|含义|
| --- | --- |
|3 	|HOME 键|
|4 	|返回键|
|5 	|打开拨号应用|
|6 	|挂断电话|
|24 |	增加音量|
|25 |	降低音量|
|26 |	电源键|
|27 |	拍照（需要在相机应用里）|
|64 |	打开浏览器|
|82 |	菜单键|
|85 |	播放/暂停|
|86 |	停止播放|
|87 |	播放下一首|
|88 |	播放上一首|
|122 |	移动光标到行首或列表顶部|
|123 |	移动光标到行末或列表底部|
|126 |	恢复播放|
|127 |	暂停播放|
|164 |	静音|
|176 |	打开系统设置|
|187 |	切换应用|
|207 |	打开联系人|
|208 |	打开日历|
|209 |	打开音乐|
|210 |	打开计算器|
|220 |	降低屏幕亮度|
|221 |	提高屏幕亮度|
|223 |	系统休眠|
|224 |	点亮屏幕|
|231 |	打开语音助手|
|276 |	如果没有 wakelock 则让系统休眠|

1. 模拟点击
```shell script
$ adb -s emulator-5554 shell input tap 270 110
```
2. HOME键
```shell script
$ adb -s emulator-5554 shell input keyevent 3
```
3. 输入文本
在焦点处于某文本框时，可以通过 input 命令来输入文本
```shell script
$ adb -s emulator-5554 shell input text hello
```


- 打开Activity
```shell script
C:\Users\android>adb -s emulator-5554 shell am start -n com.tencent.mobileqq/.activity.LoginActivity
Starting: Intent { cmp=com.tencent.mobileqq/.activity.LoginActivity }
adb -s emulator-5554 shell am start -n com.tencent.tmgp.xxsy/net.pixelgame.unity3dwrapper.Unity3DWrapper
```

- 查看Activity
```shell script
C:\Users\android>adb -s emulator-5554 shell dumpsys activity activities | findstr mFocusedActivity
  mFocusedActivity: ActivityRecord{aabd750 u0 com.tencent.mobileqq/.activity.LoginActivity t8}
D:\android\RabbitMQ Server\rabbitmq_server-3.6.5\sbin>adb -s emulator-5554 shell dumpsys activity activities | findstr mFocusedActivity
  mFocusedActivity: ActivityRecord{bdd6655 u0 com.tencent.tmgp.xxsy/net.pixelgame.unity3dwrapper.Unity3DWrapper t14}
```

- 屏幕截图
```shell script
adb -s emulator-5554 exec-out  screencap -p > sc.png

adb -s emulator-5554 shell screencap -p /sdcard/screen.png
adb -s emulator-5554 pull /sdcard/screen.png
adb -s emulator-5554 shell rm -rf /sdcard/screen.png
```
