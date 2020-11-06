
from app import db


class Population(db.Model):
    __tablename__ = 'db_res'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String())
    nom = db.Column(db.String())
    population = db.Column(db.Integer())

    def __init__(self, code, nom, population):
        self.code = code
        self.nom = nom
        self.population = population

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'code': self.code,
            'nom': self.nom,
            'population':self.population
        }

class PopCSV(db.Model):
    __tablename__ = 'table_cps'

    depcom = db.Column(db.String())
    com = db.Column(db.String())
    pop = db.Column(db.Integer())

    def __init__(self, code, nom, population):
        self.depcom = code
        self.com = nom
        self.pop = population

    def __repr__(self):
        return '<id {}>'.format(self.depcom)
    
    def serialize(self):
        return { 
            'depcom': self.depcom,
            'com': self.com,
            'pop':self.pop
        }
