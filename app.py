from flask import Flask
app = Flask(__name__)

@app.route("/piadaruim", methods=['GET'])
def hello():
    import random
    piadas = [
        "Um caipira chega á casa de um amigo que está vendo TV e pergunta: E aí, firme? E o outro responde: Não, futebor",
        "Quando os americanos comeram carne? \n\nQuanjdo chewgou cristóvão com lombo.",
        "Por que o pinheiro não se perde na floresta? \n\nPor que ele tem uma pinha",
        "Por que a formiga tem quatro patas? \n\nPor que se ela tivesse cinco era fivemigas.",
        "O que o pato falou pra pata? \n\nVem quá",
        "Qual é o rei dos queijos? \n\nÉ o requeijão",
        "Você conhece a piada do pônei? \n\nPô nei eu",
        "Qual é a fórmula da água benta? \n\nH Deus Ó",
        "O Que o pagodeiro foi fazer na igreja? \n\nFoi cantar pa god (pagode)"
    ]
    index = random.randint(0, len(piadas) - 1)
    return piadas[index]

if __name__ == '__main__':
    app.run()