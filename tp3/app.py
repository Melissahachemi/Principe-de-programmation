from flask import flask, jsonfy, request 
import repository 

#creer l'aplication 
app = Flask(_name_)

#Definir les routes 
@app.route('/')
def home(): 
    return "C'est cool REST !"


@app.route('/students' , methods=['GET'])
def get_students(): 
    students=repositoory.get_all_students()
    return jsonify(students), 200

#Lancer le server 
#force Flask à écouter sur toutes les interfaces(IPV4 + IPV6 ):
if _name_ = '_main_' :
    app.run(host="0.0.0.0", port=5001, debug=true)

