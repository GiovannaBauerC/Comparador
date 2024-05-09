from flask import Flask, render_template, request  # Importa as classes do Flask

app = Flask(__name__)  # Cria uma instância da aplicação Flask

def comparar_textos(texto1, texto2):
    # Esta função recebe os dois textos como e retorna as diferenças
    palavras_texto1 = texto1.split()  # Divide o primeiro texto em palavras
    palavras_texto2 = texto2.split()  # Divide o segundo texto em palavras
    diferencas = []  # lista para armazenar as diferenças entre os textos

    for palavra1, palavra2 in zip(palavras_texto1, palavras_texto2):
        if palavra1 != palavra2:
            # Se uma palavra de um texto for diferente da palavra correspondente no outro texto
            # Adiciona a diferença formatada à lista de diferenças
            diferenca_formatada = f'<{palavra1}> ({palavra2})'  # mostra a diferença com "<>" e parênteses
            diferencas.append(diferenca_formatada)

    # Retorna as diferenças como uma string formatada
    return ' '.join(diferencas)

@app.route('/')  # Define a rota da aplicação
def index():
    # Esta função é chamada quando alguém acessa a rota
    # Renderiza o template index.html
    return render_template('index.html')

@app.route('/compare', methods=['POST'])  # Define a rota para comparar os textos
def compare():
    # Esta função é chamada quando o formulário é enviado via método POST
    if request.method == 'POST':
        # Obtém os textos enviados pelo formulário
        text1 = request.form['text1']
        text2 = request.form['text2']
        # Chama a função comparar_textos para encontrar as diferenças entre os textos
        diferencas = comparar_textos(text1, text2)
        # Renderiza o template result.html com os textos e as diferenças encontradas
        return render_template('resultado.html', text1=text1, text2=text2, diferencas=diferencas)

if __name__ == '__main__':
    # Executa a aplicação Flask
    app.run(debug=True)
