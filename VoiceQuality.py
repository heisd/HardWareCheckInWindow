import sounddevice as sd
import soundfile as sf
import numpy as np

device_id = 39  # 换成你上面找到的编号
duration = 5   # 秒
sample_rate = 16000

print("开始录音，说点什么...")
audio = sd.rec(int(duration * sample_rate),
               samplerate=sample_rate,
               channels=1,
               dtype='int16',
               device=device_id)
sd.wait()
print("录音结束")

sf.write('test.wav', audio, sample_rate)
print("已保存到 test.wav，播放检查音质")

# 直接播放回来听
sd.play(audio, sample_rate)
sd.wait()