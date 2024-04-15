from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Route pour traiter la requête de recherche
@app.route('/rechercher-utilisateur')
def rechercher_utilisateur():
    numero_matricule = request.args.get('numeroMatricule')
    # Ici, vous devriez remplacer cette partie avec votre propre logique pour récupérer les données de l'utilisateur en fonction du numéro de matricule
    # C'est juste un exemple de réponse
    if numero_matricule == '12345':
        data = {
            'nom': 'Doe',
            'prenoms': 'John',
            'adresse': '123 Rue de la Paix'
        }
    else:
        data = {
            'nom': '',
            'prenoms': '',
            'adresse': ''
        }
    return jsonify(data)

if __name__ == '__main__':
    app.run()