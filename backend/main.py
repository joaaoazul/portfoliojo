from flask import Flask, jsonify, render_template  # Importamos Flask para criar a app e jsonify para os dados
from flask_cors import CORS  # Importamos o CORS para o React conseguir falar com o Flask

app = Flask(__name__)
CORS(app)

projects_list = [
    {
        "title": "Portefólio Flask + HTMX",
        "desc": "Desenvolvimento de uma SPA focada em performance.",
        "tech": ["Python", "Flask", "HTMX", "Tailwind"],
        "link": "https://github.com/joaaoazul/portfoliojo"
    },
]

@app.route("/")
def index():
    # O Flask usa isto para servir o HTML inicial
    return render_template("index.html")

# 2. Rota para o React consumir (O teu fetch no App.jsx vai bater aqui)
@app.route("/api/projects")
def get_projects():
    return jsonify(projects_list)  # Converte a lista Python para JSON

if __name__ == "__main__":
    app.run(debug=True, port=8000)