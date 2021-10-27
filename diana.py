import speech_recognition
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import pytz

audio = speech_recognition.Recognizer()
assistente = pyttsx3.init()
voz = assistente.getProperty('voices')
assistente.setProperty('voice', voz[1].id)

def FalarDiana(text):
  assistente.say(text)
  assistente.runAndWait()

def RealizarComando():
  try:
    with speech_recognition.Microphone() as microfone:
      print('Aguardando comando...')
      voz = audio.listen(microfone)
      comando = audio.recognize_google(voz, language="pt-BR")
      comando = comando.lower()
      if 'Diana' in comando:
        comando = comando.replace('Diana', '')
        print(comando)
  except:
    print("Algo de errado no microfone, verifique se está funcionando corretamente.")
  return comando

def ExecutarDiana():
  comando = RealizarComando()
  print(comando)
  if 'tocar' in comando:
    musica = comando.replace('tocar', '')
    FalarDiana(f'Tocando: {musica}')
    pywhatkit.playonyt(musica)
  elif 'horário atual' in comando:
    tempo = datetime.now(pytz.timezone('America/Sao_Paulo')).strftime('%d/%m/%Y %H:%M:%S')
    FalarDiana(f'Horário atual: {tempo}')
  elif 'quem é' in comando:
    pessoa = comando.replace('quem é', '')
    informacao = wikipedia.summary(pessoa, 1)
    FalarDiana(informacao)
  elif 'piada' in comando:
    FalarDiana(pyjokes.get_joke())
  elif 'você está comprometida' in comando:
    FalarDiana('Estou em um relacionamento sério com Wi-fi da casa de sua avó.')
  else:
    FalarDiana('Por favor, repita novamente o comando.')

while True:
  ExecutarDiana()