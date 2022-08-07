import datetime
from flask import Flask, render_template, jsonify, make_response, session
from flask import request
from pymongo import MongoClient
from bson.objectid import ObjectId
import jwt

app = Flask(__name__)

app.config['SECRET_KEY'] = "itisatopsecret"



client = MongoClient("mongodb+srv://abhi:abhi@cluster0.h7jb6cg.mongodb.net/?retryWrites=true&w=majority")
#client = MongoClient("mongodb://localhost:27017/")
db = client["Prescriptiondatabasee"] 
collection = db["prescriptionss"]  



@app.route('/login', methods =['POST','GET'])
def homes():
    id=request.form.get("id")
    passed=request.form.get("pass")
    return render_template('index.html',text1="{}".format(id),text="{}".format(passed))

@app.route("/", methods=["POST","GET"])
def create():
    data={};mssg="";i=0
    data["id"] = request.form.get("idee")
    data["passed"] = request.form.get("ideee")
    if ( data["id"])  and (data["passed"]):
        if not collection.find_one({"id":data["id"]}):
            collection.insert_one(data)
            mssg="Sign Up Successful"
        else:
            mssg="Id already Exists" 
    return render_template("index1.html",mssg=mssg)

# @app.route("/check", methods=["POST","GET"])
# def creates():
#     id=request.form.get("id")
#     passed=request.form.get("passed")
#     authorize=collection.find_one({"id":id,"passed":passed})
#     print(authorize)
#     if authorize:
#         token = jwt.encode({
#             'public_id': id,    
#             'exp' : "1234345",       
#         }, "secretkeyAbhishek")
#         print(id, passed)
#         return make_response(jsonify({"data":{'token' : token.decode('UTF-8')}}), 201)
        
#     return  make_response(jsonify({'data': "Not Verified"}),403)


@app.route("/check", methods=["POST","GET"])
def creates():
    id=request.form.get("id")
    passed=request.form.get("passed")
    print("forgotttttttt.......")
    authorize=collection.find_one({"id":id,"passed":passed})
    print("abhishek is printing here.......",authorize)
    if authorize:
        token = jwt.encode({
            'public_id': id,
            'exp' : "1234345",       
        }, app.config['SECRET_KEY'])
        return make_response(jsonify({"data":{'token' : token.decode()}}), 201)
    return  make_response(jsonify({'data': "Not Verified"}),403)


if __name__=="__main__":
    app.run(debug=True,use_reloader=True)