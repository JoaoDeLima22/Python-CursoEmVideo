import os
import openai
from pytrends.request import TrendReq
from google.cloud import texttospeech
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Configurar chaves de API
OPENAI_API_KEY = 'YOUR_OPENAI_API_KEY'
YOUTUBE_API_KEY = 'YOUR_YOUTUBE_API_KEY'

# Configurar credenciais do Google Cloud
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/google-credentials.json"


def get_trending_topic():
    pytrends = TrendReq(hl='pt-BR', tz=360)
    pytrends.build_payload(kw_list=['tecnologia'], timeframe='now 7-d', geo='BR')
    trends = pytrends.interest_over_time()
    trending_topic = trends.idxmax().values[0]
    return trending_topic


def generate_script(topic):
    openai.api_key = OPENAI_API_KEY
    prompt = f"Escreva um roteiro de vídeo sobre {topic}."
    response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=500)
    script = response.choices[0].text.strip()
    return script


def generate_audio(script):
    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.SynthesisInput(text=script)
    voice = texttospeech.VoiceSelectionParams(language_code="pt-BR", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL)
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

    response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

    with open("output.mp3", "wb") as out:
        out.write(response.audio_content)


def create_video():
    # Supondo que você tenha um vídeo base 'input_video.mp4'
    input_video = "input_video.mp4"
    output_audio = "output.mp3"
    final_video = "final_video.mp4"

    os.system(f"ffmpeg -i {input_video} -i {output_audio} -c:v copy -c:a aac {final_video}")


def upload_to_youtube(title, description, file_path):
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "categoryId": "22",
                "description": description,
                "title": title
            },
            "status": {
                "privacyStatus": "public"
            }
        },
        media_body=MediaFileUpload(file_path)
    )
    response = request.execute()
    return response


def main():
    trending_topic = get_trending_topic()
    print(f"Tópico em tendência: {trending_topic}")

    script = generate_script(trending_topic)
    print(f"Roteiro gerado: {script}")

    generate_audio(script)
    print("Áudio gerado: output.mp3")

    create_video()
    print("Vídeo final criado: final_video.mp4")

    title = f"Vídeo sobre {trending_topic}"
    description = f"Este vídeo fala sobre {trending_topic}. Aproveite e inscreva-se no canal!"
    response = upload_to_youtube(title, description, "final_video.mp4")
    print(f"Vídeo enviado: {response['id']}")


if __name__ == "__main__":
    main()
