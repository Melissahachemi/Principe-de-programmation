from flask import Flask, jsonify, request
app=Flask(__name__)
students=[
    {"id":1,"name":"Youcef","age":21},
    {"id":2,"name":"Samir","age":41},
]

@app.route('/')
def home():
    return "Bienvenue dans l'API de gestion des étudiants !"

#Endpoint pour lister tous les étudiants
@app.route('/students', methods=['GET'])
#Méthode HTTP GET qui permet de retourner la liste des étudiants
def get_students():
    "jsonif transforme la liste students en json"
    return jsonify(students)

#Ajouter un étudiant (POST)
@app.route('/students', methods=['POST'])
def add_student():
    new_student=request.get_json()
    new_student['id']=len(students)+1
    #Pour récupérer les données envoyé par le client
    students.append(new_student)
    return jsonify(students),201
    #Le code 201 pour dire création réussie

#Afficher un étudiant sachant son identifiant
@app.route('/students/<int:id>', methods=['GET'])
def get_students_by_id(id):
    student=next((s for s in students if s['id']==id),None)
    if student:
        return jsonify(student)
    return jsonify({"erreur":"l'étudiant n'existe pas !"}),404

#Mettre a jour un étudiant PUT
@app.route('/students/<int:id>', methods=['PUT'])
def update_students(id):
    student=next((s for s in students if s['id']==id),None)
    if not student:
        return jsonify({"message":"Etudiant non trouvé !"}),404
    data=request.get_json()
    student.update(data) # Mise a jour des données
    return jsonify(student)

if __name__=='__main__':
    print("Checkpoint")
    app.run(debug=True)

#Postman : GET http://127.0.0.1:5000/students retourne la liste des étudiant
#POST http://127.0.0.1:5000/students avec {"name":"Mathurin","age": 22} dans Body sous forme raw ajoute un élève nommé Mathurin et agé de 22 ans
#GET http://127.0.0.1:5000/students/2 retourne uniquement l'étudiant avec l'id 2
#PUT http://127.0.0.1:5000/students/1 avec {"name":"Mathurin","age": 22} dans Body sous forme raw change le nom et l'age de l'étudiant qui possède l'id 1. Le nom devient Mathurin
#et l'age 22 ans.
