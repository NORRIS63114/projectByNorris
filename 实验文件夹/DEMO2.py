import wave
import json
from vosk import Model, KaldiRecognizer


model_path = "/Users/Bradley/PycharmProjects/MOSS2/vosk-model-small-en-us-0.15"

model = Model(model_path)

audio_file = "/Users/Bradley/PycharmProjects/MOSS2/实验文件夹/test.wav"

wf = wave.open(audio_file, "rb")

recognizer = KaldiRecognizer(model, wf.getframerate())

result = " "

while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if recognizer.AcceptWaveform(data):
        res = recognizer.Result()
        result += json.loads(res)['text'] + " "


final_res = recognizer.FinalResult()
result += json.loads(final_res)['text']
print('the final result is...')
print(result)

wf.close()