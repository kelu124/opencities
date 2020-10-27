
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
