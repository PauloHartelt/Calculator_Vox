def main():
    from audio import captar_audio

    from tradutor import traduzir

    from numerizador import numerizar

    from calculadora import calcular

    from texto_fala import texto_para_fala

    fonte = captar_audio()

    texto_traduzido = traduzir(fonte)

    calculo = numerizar(texto_traduzido)

    texto_final = calcular(calculo)

    texto_para_fala(texto_final)