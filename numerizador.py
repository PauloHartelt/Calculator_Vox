def numerizar(texto):
    from numerizer import numerize
    
    # Valida se foi numerizado

    try:
        texto_numerizado = numerize(texto) # Numerifica o calculo traduzido, ainda em string.

        return texto_numerizado
    except:
        print("Não consegui numerificar")