from ctypes import Structure, windll, c_uint, sizeof, byref
import time
class LASTINPUTINFO(Structure):
    _fields_ = [
        ('cbSize', c_uint),
        ('dwTime', c_uint),
    ]

def get_idle_duration():
    lastInputInfo = LASTINPUTINFO()
    lastInputInfo.cbSize = sizeof(lastInputInfo)
    windll.user32.GetLastInputInfo(byref(lastInputInfo))
    millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
    return millis / 1000.0

def main(sec):
    while True:
        print("Waiting", sec, "Seconds...")
        time.sleep(sec)
        idle_time = get_idle_duration()
        print(f"You Are AFK: {idle_time} Seconds...")

main(3)