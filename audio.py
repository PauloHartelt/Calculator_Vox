def captar_audio():
    import speech_recognition as sr

    rec = sr.Recognizer() # Cria um reconhecedor

    # Cria um microfone, utilizando o padrão do computador, a partir do reconhecedor e capta o que fora falado

    with sr.Microphone() as microfone:

        rec.adjust_for_ambient_noise(microfone)

        print("Fale, pausadamente, o calculo que queira realizar:")

        audio = rec.listen(microfone)
    
    # Valida se foi falado algo no microfone

    try:
        audio = rec.recognize_google(audio, language="pt-BR") # Utiliza o reconhecedor de voz do Google pra traduzir o falado

        return audio
    except:
        print("Não captei áudio nenhum")

