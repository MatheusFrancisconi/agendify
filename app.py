from flask import Flask, render_template, request, redirect, url_for
import time

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nome_aluno = request.form.get("nome")
        tempo = int(request.form.get("tempo"))
        materia = int(request.form.get("materia"))

        conteudos = []
        if materia == 1:
            conteudos = ["Tipologia textual e gêneros textuais", "Figuras de linguagem", "Artes literárias", "Gramática", "Classes de palavras"]
        elif materia == 2:
            conteudos = ["Matemática básica", "Estatística", "Geometria espacial", "Razões e proporções", "Análise combinatória", "Probabilidade", "Funções"]
        elif materia == 3:
            conteudos = ["Movimentos sociais", "Cidadania e Direitos Humanos", "Diversidade cultural", "Gênero e sexualidade", "Trabalho e sociedade"]
        elif materia == 4:
            conteudos = ["Meio ambiente", "Átomos e água", "Eletroquímica", "Separação de misturas", "Cinética química"]

        return render_template("index.html", nome=nome_aluno, tempo=tempo, conteudos=conteudos)

    return render_template("index.html")

@app.route("/cronometro")
def pomodoro():
    return render_template("cronometro.html")

if __name__ == "__main__":
    app.run(debug=True)