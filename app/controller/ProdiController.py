from app.model.prodi import Prodi
from app import response,app, db
from flask import request

def index():
    try:
        prodi = Prodi.query.all()
        data = formatarray(prodi)
        return response.success(data,"success")
    except Exception as e:
        print(e)
        
        
def formatarray(datap):
    array = []
    for i in datap:
         array.append(singleObjt(i))
    return array


def singleObjt(data):
    data = {
        'id' : data.id,
        'nama_prodi' : data.nama_prodi
    }
    
    return data
