import python_weather
import asyncio

async def getweather():
  async with python_weather.Client(unit=python_weather.METRIC) as client:
    weather = await client.get('ramat gan')
    print(weather.temperature)

if __name__ == '__main__':
  asyncio.run(getweather())