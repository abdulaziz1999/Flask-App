from app.model.mahasiswa import Mahasiswa
from app import response,app, db
from flask import request

def index():
    try:
        mhs = Mahasiswa.query.all()
        data = formatarray(mhs)
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
        'nim' : data.nim,
        'nama' : data.nama,
        'prodi' : data.prodi,
        'phone' : data.phone,
        'alamat' : data.alamat,
    }
    
    return data
