from gps import *
import time
from pyowm import OWM
from pyowm.utils.config import get_default_config

# pyowm 3 버전 기준으로 작성되었음.
config_dict = get_default_config()
config_dict['language'] = 'kr'
apiKey = '9af17afaa6adcac0ef8e83a1f9289626' # 본인의 apiKey
owm = OWM(apiKey, config_dict)
mgr = owm.weather_manager() # manager

# 현재 위치 가져오기
gpsd = gps(mode=WATCH_ENABLE)
while True:
	report = gpsd.next()
	if report['class'] == 'TPV':
		lat = getattr(report, 'lat', 0.0)
		lon = getattr(report, 'lon', 0.0)
		time = getattr(report, 'time', '')
		print("현재 좌표 및 시간 :", lat, lon, time); break
		
obs = mgr.weather_at_coords(lat, lon) # observer
w = obs.weather
temp = w.temperature('celsius').get('temp')
print("현재 날씨 :", w.detailed_status, ", 습도 : ", w.humidity, ", 기온 : ", int(temp), "도")
