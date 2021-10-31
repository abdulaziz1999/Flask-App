from flask import request, render_template, redirect, url_for, jsonify
from app import app, response
from app.controller import DosenController
from app.controller import UserController
from app.controller import ProdiController
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required


# routes root
@app.route('/')
def index():
    return render_template('home.html')

# routes protected
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return response.success(current_user, 'Sukses')
    
# routes dosen
@app.route('/dosen',methods=['GET', 'POST'])
@jwt_required()
def dosens():
    if request.method == 'GET':
        return DosenController.index()
    elif request.method == 'POST':
        return DosenController.save()

# routes dosen detail 
@app.route('/dosen/<id>',methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def dosensDetail(id):
    if request.method == 'GET':
        return DosenController.detail(id)
    elif request.method == 'PUT':
        return DosenController.ubah(id)
    elif request.method == 'DELETE':
        return DosenController.hapus(id)
    
#route prodi
@app.route('/prodi', methods=['GET'])
@jwt_required()
def prodi():
    return ProdiController.index()

# routes login
@app.route('/login', methods=['POST'])
def logins():
    return UserController.login()

# routes create admin
@app.route('/createadmin',methods=['POST'])
@jwt_required()
def admins():
        return UserController.buatAdmin()