import requests
import json
import os
from gtts import gTTS
from playsound import playsound

# 获取天气数据
response = requests.get('http://t.weather.sojson.com/api/weather/city/101010100')
weather_json = json.loads(response.text)

# 解析天气数据
city = weather_json['cityInfo']['city']
today = weather_json['data']['forecast'][0]
temperature = today['high'] + '到' + today['low']
type = today['type']
notice = today['notice']

# 生成语音播报内容
text = f'{city}今天天气{type}，温度{temperature}，{notice}'

# 生成并播放语音
tts = gTTS(text=text, lang='zh')
tts.save('weather.mp3')
playsound('weather.mp3')

# 删除生成的语音文件
os.remove('weather.mp3')
