from flask import Flask, escape, request, json, abort

app = Flask(__name__)

DB = {"students":[],
      "classes":[]
}

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'
    
@app.route('/students', methods = ['POST'])
def create_student():
    req = request.json
    print(req["name"])
    temp = {"id":1234456,"name":req["name"]}
    DB["students"].append(temp)
    return DB["students"][-1],201
    
    
    
@app.route('/students/<int:id>',methods = ['GET'])
def get_student(id):
    for i in range(len(DB["students"])):
        temp = DB["students"][i]
        if temp["id"] == id:
            return DB["students"][i]
    return abort(404)
    
    
@app.route('/classes',methods = ['POST'])
def create_class():
    req = request.json
    print(req["name"])
    temp = {"id":1122334, "name":req["name"],"students":[]}
    DB["classes"].append(temp)
    return DB["classes"][-1]
    
@app.route('/classes/<int:id>',methods = ['GET'])
def get_class(id):
    for i in range(len(DB["classes"])):
        temp = DB["classes"][i]
        if temp["id"] == id:
            return DB["classes"][i]
    return abort(404)


@app.route('/classes/<int:id>',methods = ['PUT'])
def patch_class(id):
    req = request.json
    sid = req["student_id"]
    for i in range(len(DB["students"])):
        temps = DB["students"][i]
        if temps["id"] == sid:
            student = DB["students"][i]
            for j in range(len(DB["classes"])):
                tempc = DB["classes"][j]
                if tempc["id"] == id:
                    result = DB["classes"][j]
                    result["students"].append(student)
                    return result
    return abort(404)
        

@app.route('/students/printall', methods = ['GET'])
def getAll():
    return DB
