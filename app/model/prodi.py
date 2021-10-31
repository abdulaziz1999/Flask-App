from app import db

class Prodi(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    nama_prodi =db.Column(db.String(20), nullable=False)
    
    def __repr__(self):
        return '<Prodi {}>'.format(self.name)