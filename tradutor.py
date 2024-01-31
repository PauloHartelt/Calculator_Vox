def traduzir(fonte):
    from deep_translator import GoogleTranslator
    
    from numerizador import numerizar

    # Valida se foi traduzido

    try:
        tradutor = GoogleTranslator(source="pt", target="en") # Cria um tradutor

        texto_traduzido = tradutor.translate(fonte) # Utiliza o Google tradutor pra transformar para inglês
        
        return texto_traduzido
    except:
        print("Não traduzi áudio algum")