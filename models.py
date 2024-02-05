from flask_sqlalchemy import SQLAlchemy

# Inicializar la extension SQLALCHEMY

db = SQLAlchemy()

# Definimos una clase que representa una tabla en la base de datos

class Ingresos(db.Model): # Heredando de la clase 
    id = db.Column(db.Integer, primary_key=True)
    monto = db.Column(db.Integer, nullable=False)
    concepto = db.Column(db.String(20), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    descripcion = db.Column(db.String, nullable=False)

    # Constructor de clase

    def __init__(self, monto, concepto,fecha, descripcion):
        self.monto = monto
        self.concepto = concepto
        self.fecha = fecha 
        self.descripcion = descripcion
        
class Egresos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    monto = db.Column(db.Integer, nullable=False)
    concepto = db.Column(db.String(20), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    descripcion = db.Column(db.String, nullable=False)

    # Constructor de clase

    def __init__(self, monto, concepto,fecha, descripcion):
        self.monto = monto
        self.concepto = concepto
        self.fecha = fecha 
        self.descripcion = descripcion


