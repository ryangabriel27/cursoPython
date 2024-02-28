# Banco de perguntas e respostas por categorias
banco_perguntas_facil = [
    {
        "pergunta": "Qual é a capital do Brasil?",
        "opcoes": [
            "A) São Paulo",
            "B) Rio de Janeiro",
            "C) Brasília",
            "D) Belo Horizonte",
        ],
        "resposta_correta": "C) Brasília",
    },
    {
        "pergunta": "Qual é a cor do céu em um dia claro?",
        "opcoes": ["A) Azul", "B) Verde", "C) Vermelho", "D) Amarelo"],
        "resposta_correta": "A) Azul",
    },
    # Adicione mais perguntas fáceis conforme necessário
]

banco_perguntas_media = [
    {
        "pergunta": "Quem foi o primeiro presidente dos Estados Unidos?",
        "opcoes": [
            "A) Abraham Lincoln",
            "B) George Washington",
            "C) Thomas Jefferson",
            "D) John Adams",
        ],
        "resposta_correta": "B) George Washington",
    },
    {
        "pergunta": "Qual é o símbolo químico para o ouro?",
        "opcoes": ["A) Au", "B) Ag", "C) Fe", "D) Hg"],
        "resposta_correta": "A) Au",
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
        "resposta_correta": "A) 300.000 km/s",
    },
    {
        "pergunta": "Quem descobriu a penicilina?",
        "opcoes": [
            "A) Alexander Fleming",
            "B) Marie Curie",
            "C) Louis Pasteur",
            "D) Jonas Salk",
        ],
        "resposta_correta": "A) Alexander Fleming",
    },
    # Adicione mais perguntas difíceis conforme necessário
]

def getOpcoesFacil(index):
    opcoes = banco_perguntas_facil[index]['opcoes']
    for opcao in opcoes:
        print(opcao)
    
