import python_weather
import asyncio
from desktop_notifier import DesktopNotifier
import time
from ctypes import Structure, windll, c_uint, sizeof, byref
import time

already_notified = False
MAX_TEMP = 28
CITY_NAME = 'New York'

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

async def main():
  global already_notified, MAX_TEMP
  while True:
    idle_time = get_idle_duration()
    if idle_time > 10:
      print(f"You Are AFK: {idle_time} Seconds...")
      print("Waiting 3 seconds...")
      time.sleep(3)
    else:
      # Check Weather pythonWeatherAPI -> Notify if above MAX_TEMP ONCE! -> And notify when it's cold again ONCE!
      async with python_weather.Client(unit=python_weather.METRIC) as client:
        weather = await client.get(CITY_NAME)
        if weather.temperature >= MAX_TEMP:
          if already_notified:
            print(f"Already Notified! Temperature is still warm!\nCurrent Temperature: {weather.temperature}℃")
          else:
            already_notified = True
            msg = f"Temperature is higher than {MAX_TEMP}℃,\nCurrent Temperature: {weather.temperature}℃"
            title =  "Warning: It's too hot outside!"
            print(title, msg)
            await notifier.send(title=title, message=msg)
        else:
          print(f"Its cold right now outside!\nCurrent Temperature: {weather.temperature}℃ / {MAX_TEMP}℃")
          if already_notified:
            already_notified = False
            msg = f"The hot weather has disappeared,\nCurrent Temperature: {weather.temperature}℃"
            title =  "You can go outside now: It's cold now!"
            print(title, msg)
            await notifier.send(title=title, message=msg)
      print("Waiting 30 seconds...")
      time.sleep(30)

if __name__ == '__main__':
  notifier = DesktopNotifier()
  asyncio.run(main())