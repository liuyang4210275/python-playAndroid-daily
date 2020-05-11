# bilibili comic
## 1. 签到操作
步骤：
- 打开app
`adb -s emulator-5554 shell am start -n com.bilibili.comic/.home.view.FlutterMainActivity`

```shell script
C:\Users\android>adb -s emulator-5554 shell am start -n com.bilibili.comic/.home.view.FlutterMainActivity
Starting: Intent { cmp=com.bilibili.comic/.home.view.FlutterMainActivity }
Security exception: Permission Denial: starting Intent { flg=0x10000000 cmp=com.bilibili.comic/.home.view.FlutterMainActivity } from null (pid=19515, uid=2000) not exported from uid 10268

java.lang.SecurityException: Permission Denial: starting Intent { flg=0x10000000 cmp=com.bilibili.comic/.home.view.FlutterMainActivity } from null (pid=19515, uid=2000) not exported from uid 10268
        at com.android.server.wm.ActivityStackSupervisor.checkStartAnyActivityPermission(ActivityStackSupervisor.java:1089)
        at com.android.server.wm.ActivityStarter.startActivity(ActivityStarter.java:788)
        at com.android.server.wm.ActivityStarter.startActivity(ActivityStarter.java:587)
        at com.android.server.wm.ActivityStarter.startActivityMayWait(ActivityStarter.java:1397)
        at com.android.server.wm.ActivityStarter.execute(ActivityStarter.java:518)
        at com.android.server.wm.ActivityTaskManagerService.startActivityAsUser(ActivityTaskManagerService.java:1089)
        at com.android.server.wm.ActivityTaskManagerService.startActivityAsUser(ActivityTaskManagerService.java:1063)
        at com.android.server.am.ActivityManagerService.startActivityAsUser(ActivityManagerService.java:3560)
        at com.android.server.am.ActivityManagerShellCommand.runStartActivity(ActivityManagerShellCommand.java:518)
        at com.android.server.am.ActivityManagerShellCommand.onCommand(ActivityManagerShellCommand.java:172)
        at android.os.ShellCommand.exec(ShellCommand.java:104)
        at com.android.server.am.ActivityManagerService.onShellCommand(ActivityManagerService.java:10061)
        at android.os.Binder.shellCommand(Binder.java:881)
        at android.os.Binder.onTransact(Binder.java:765)
        at android.app.IActivityManager$Stub.onTransact(IActivityManager.java:4663)
        at com.android.server.am.ActivityManagerService.onTransact(ActivityManagerService.java:2790)
        at android.os.Binder.execTransactInternal(Binder.java:1021)
        at android.os.Binder.execTransact(Binder.java:994)
```
- 找到目标'我的view'
- 点击目标'我的view'
- 找到‘签到’
- 点击‘签到’
- HOME键,退出