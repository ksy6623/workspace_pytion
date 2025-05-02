# pip install openai-whisper
# pip install openai
import whisper
import os
from openai import OpenAI
api_key = os.getenv('GROK_API_KEY')
#tiny/base/small/medium/large
model = whisper.load_model("base")
client = OpenAI(api_key=api_key, base_url='https://api.x.ai/v1')
def trans_audio(audio_path):
    result = model.transcribe(audio_path, language='ko')
    return result['text']

text = trans_audio('audio.wav')
print(text)
resource = client.chat.completions.create(
    model='grok-3-mini-bate',
    messages=[{"role":"system","content":"""넌 한국어 요약을 정말 잘하는 모델 요청 텍스트를 컴팩트하게 요약해줘"""},
              {"role":"user","content":text}])
print("요약:")
print(resource.choices[0].message.content)