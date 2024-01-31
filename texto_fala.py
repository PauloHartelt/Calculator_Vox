def texto_para_fala(text):
    import pyttsx3

    # Inicializa o objeto da engine TTS
    engine = pyttsx3.init()

    # Configura a voz para português brasileiro
    engine.setProperty('voice', 'brazil')

    # Configura a taxa de fala (opcional)
    engine.setProperty('rate', 150)  # Velocidade da fala, ajuste conforme necessário

    # Faz a engine falar o texto fornecido
    engine.say(text)

    # Aguarda até que a fala seja concluída
    engine.runAndWait()
