import speech_recognition
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser

audio = speech_recognition.Recognizer()
assistente = pyttsx3.init()
voz = assistente.getProperty('voices')
assistente.setProperty('voice', voz[1].id)

def FalarDiana(text):
  assistente.say(text)
  assistente.runAndWait()

def RealizarComando():
  global comando
  try:
    with speech_recognition.Microphone() as microfone:
      print('Aguardando comando...')
      voz = audio.listen(microfone)
      comando = audio.recognize_google(voz, language="pt-BR")
      comando = comando.lower()
      if 'Diana' in comando:
        comando = comando.replace('Diana', '')
        print(comando)
  except speech_recognition.UnknownValueError:
    print('Não foi possível captar o áudio do microfone.')
  except speech_recognition.RequestError:
    print('Serviço fora do ar.')  
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
  elif 'abrir google' in comando:
    url = 'https://google.com.br/'
    webbrowser.get().open(url) 
  elif 'você é comprometida' in comando:
    FalarDiana('Estou em um relacionamento sério com Wi-fi da casa de sua avó.')
  elif 'eu sou o batman' in comando:
    FalarDiana('Se você é o Batman então eu sou a Joana D\'Arc.')
  elif 'diga seu nome' in comando:
    FalarDiana('Meu nome é Diana, e fui criada na linguagem Python.')
  elif 'desligar' in comando:
    FalarDiana('Até outro momento.')
    exit()
  else:
    FalarDiana('Não entendi o comando, por favor repita novamente.')
    
while True:
  ExecutarDiana()
