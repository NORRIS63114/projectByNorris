import  wave

import pyaudio

def record_audio(filename):
    mic = pyaudio.PyAudio()
    stream = mic.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=44100,
        input=True,
        frames_per_buffer=8192)

    print('recording...')
    frame = []
    for _ in range(0, int(44100 / 8192 * 5)):
        data = stream.read(8192)
        frame.append(data)
    stream.stop_stream()
    stream.close()
    mic.terminate()

    wf = wave.open(filename, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(mic.get_sample_size(pyaudio.paInt16))
    wf.setframerate(44100)
    wf.writeframes(b''.join(frame))
    wf.close()

record_audio('test.wav')