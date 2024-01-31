def calcular(calculo):
    import ast

    texto_numerizado_formatado = calculo.strip().replace("x", "*") # Corrige espaços a mais e operadores indesejados 

    arvore_sintatica = ast.parse(texto_numerizado_formatado, mode='eval') # Particiona uma árvore para o calculo

    resultado = eval(compile(arvore_sintatica, filename='<string>', mode='eval')) # Calcula o informado em uma árvore de calculo

    return resultado