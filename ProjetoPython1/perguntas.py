# Banco de perguntas e respostas por categorias
banco_perguntas_facil = [
    {
        "pergunta": "Qual é a capital do Brasil?",
        "opcoes": ["A) São Paulo","B) Rio de Janeiro","C) Brasília","D) Belo Horizonte"],
        "resposta_correta": "C",
    },
    {
        "pergunta": "Qual é a cor do céu em um dia claro?",
        "opcoes": ["A) Azul", "B) Verde", "C) Vermelho", "D) Amarelo"],
        "resposta_correta": "A",
    },
    {
        'pergunta': 'Quantos lados tem um triângulo?',
        'opcoes': ['A) 3', 'B) 4', 'C) 5', 'D) 6'],
        'resposta_correta': 'A'
    },
    {
        'pergunta': 'Quem pintou a Mona Lisa?',
        'opcoes': ['A) Leonardo da Vinci', 'B) Michelangelo', 'C) Pablo Picasso', 'D) Vincent van Gogh'],
        'resposta_correta': 'A'
    },
    {
        'pergunta': 'Quem foi o primeiro presidente do Brasil?',
        'opcoes': ['A) Getúlio Vargas', 'B) Juscelino Kubitschek', 'C) Marechal Deodoro da Fonseca', 'D) Tancredo Neves'],
        'resposta_correta': 'C'
    },
    {
        'pergunta': 'Qual é o maior oceano do mundo?',
        'opcoes': ['A) Atlântico', 'B) Índico', 'C) Ártico', 'D) Pacífico'],
        'resposta_correta': 'D'
    },
     {
        'pergunta': 'Qual é a capital da França?',
        'opcoes': ['A) Madri', 'B) Roma', 'C) Paris', 'D) Berlim'],
        'resposta_correta': 'C'
    },
    {
        'pergunta': 'Quem é conhecido como "Rei do Pop"?',
        'opcoes': ['A) Elvis Presley', 'B) Michael Jackson', 'C) Madonna', 'D) Prince'],
        'resposta_correta': 'B'
    },
    # Adicione mais perguntas fáceis conforme necessário
]

banco_perguntas_media = [
    {
        "pergunta": "Quem foi o primeiro presidente dos Estados Unidos?",
        "opcoes": ["A) Abraham Lincoln","B) George Washington","C) Thomas Jefferson","D) John Adams",],
        "resposta_correta": "B",
    },
    {
        "pergunta": "Qual é o símbolo químico para o ouro?",
        "opcoes": ["A) Au", "B) Ag", "C) Fe", "D) Hg"],
        "resposta_correta": "A",
    },
    {
        'pergunta': 'Em que ano ocorreu a Revolução Industrial?',
        'opcoes': ['A) 1750', 'B) 1800', 'C) 1850', 'D) 1900'],
        'resposta_correta': 'C'
    },
    {
        'pergunta': 'Quem foi o primeiro astronauta a caminhar na Lua?',
        'opcoes': ['A) Neil Armstrong', 'B) Buzz Aldrin', 'C) Yuri Gagarin', 'D) John Glenn'],
        'resposta_correta': 'A'
    },
    {
        'pergunta': 'Quem foi o autor de "Cem Anos de Solidão"?',
        'opcoes': ['A) Gabriel García Márquez', 'B) Julio Cortázar', 'C) Isabel Allende', 'D) Mario Vargas Llosa'],
        'resposta_correta': 'A'
    },
    {
        'pergunta': 'Qual é a fórmula química da água?',
        'opcoes': ['A) CO2', 'B) H2O', 'C) NaCl', 'D) O2'],
        'resposta_correta': 'B'
    },
    {
        'pergunta': 'Quem é considerado o "pai da computação"?',
        'opcoes': ['A) Alan Turing', 'B) Bill Gates', 'C) Steve Jobs', 'D) Mark Zuckerberg'],
        'resposta_correta': 'A'
    },
    {
        'pergunta': 'Qual é a unidade de medida de temperatura no sistema internacional?',
        'opcoes': ['A) Kelvin', 'B) Celsius', 'C) Fahrenheit', 'D) Rankine'],
        'resposta_correta': 'B'
    },
    
    # Adicione mais perguntas médias conforme necessário
]

banco_perguntas_dificil = [
    {
        "pergunta": "Qual é a velocidade da luz?",
        "opcoes": [
            "A) 300.000 km/s",
            "B) 150.000 km/s",
            "C) 450.000 km/s",
            "D) 600.000 km/s",
        ],
        "resposta_correta": "A",
    },
    {
        "pergunta": "Quem descobriu a penicilina?",
        "opcoes": [
            "A) Alexander Fleming",
            "B) Marie Curie",
            "C) Louis Pasteur",
            "D) Jonas Salk",
        ],
        "resposta_correta": "A",
    },
    # Adicione mais perguntas difíceis conforme necessário
]

def getOpcoesFacil(index):
    opcoes = banco_perguntas_facil[int(index)]['opcoes']
    for opcao in opcoes:
        print(opcao)

def getPerguntaFacil(index):
    pergunta = banco_perguntas_facil[int(index)]['pergunta']
    return pergunta

def getRespostaFacil(index):
    resposta = banco_perguntas_facil[int(index)]['resposta_correta']
    return resposta

def getOpcoesMedia(index):
    opcoes = banco_perguntas_media[int(index)]['opcoes']
    for opcao in opcoes:
        print(opcao)

def getPerguntaMedia(index):
    pergunta = banco_perguntas_media[int(index)]['pergunta']
    return pergunta

def getRespostaMedia(index):
    resposta = banco_perguntas_media[int(index)]['resposta_correta']
    return resposta

# def gerarNumerosAleatorios():

    
    
