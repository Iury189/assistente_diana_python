import speech_recognition
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

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
      global comando
      print('Aguardando comando...')
      voz = audio.listen(microfone)
      comando = audio.recognize_google(voz, language="pt-BR")
      comando = comando.lower()
      if 'Diana' in comando:
        comando = comando.replace('Diana', '')
        print(comando)
  except:
    print("Algo de errado aconteceu")
  return comando

def ExecutarDiana():
  comando = RealizarComando()
  print(comando)
  if 'tocar' in comando:
    musica = comando.replace('tocar', '')
    FalarDiana(f'Tocando: {musica}')
    pywhatkit.playonyt(musica)
  elif 'horário atual' in comando:
    tempo = datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')
    FalarDiana(f'Horário atual: {tempo}')
  elif 'procurar por' in comando:
    wikipedia.set_lang('pt')
    procurar = comando.replace('procurar por', '')
    informacao = wikipedia.summary(procurar, 1)
    FalarDiana(informacao)
  elif 'piada' in comando:
    FalarDiana(pyjokes.get_joke())
  elif 'você está comprometida?' in comando:
    FalarDiana('Estou em um relacionamento sério com Wi-fi da casa de sua avó.')
  else:
    FalarDiana('Não entendi o comando, por favor repita novamente.')
    
while True:
  ExecutarDiana()
