import os



def Listion_Devices():
    '''获得已连接的手机设备随机数'''
    os.system('adb devices')
    return os.system('adb devices')

def GetAppLog(tag,logclass='E'):
    '''根据过滤基本查看app日志'''
    os.system('adb logcat ' + tag + ':'+ logclass)

def ClearDeicesLog():
    '''清除手机app级别的缓存'''
    os.system("adb logcat -c")

def ConnectDeviceByUSB():
    '''指定当前唯一通过 USB 连接的 Android 设备为命令目标'''
    os.system("adb -d" )

def ConnectTureDevices(number:str):
   '''可以通过adb devices 获得的值，连接多个手机/模拟器设备'''
    os.system("adb -s" + number)

def ConnectMultipleDevices(number:str):
    '''指定相应 serialNumber 号的设备/模拟器为命令目标'''
    os.system("adb -e" + number)
