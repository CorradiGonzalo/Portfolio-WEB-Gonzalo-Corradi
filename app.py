import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

#config basica.
app = Flask(__name__)

#config de base de datos
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'portfolio.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#inicio DB
db = SQLAlchemy(app)
#estructura de la tabla
class Proyecto(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    titulo = db.Column(db.String(100), nullable = False)
    descripcion = db.Column(db.String(255), nullable = False)
    tags = db.Column(db.String(100), nullable = False)
    estado = db.Column(db.String(50), nullable = False)
    link = db.Column(db.String(200), nullable = True)

    def get_tags_list(self):
        #comvertimos SQL en una lista
        ['Python', 'SQL']
        return self.tags.split(',')
    
#cargar datos iniciales
def crear_datos_iniciales():
    with app.app_context():
        db.create_all() #crea las tablas si no existen

        #si esta vacia, cargamos los proyectos.
        if Proyecto.query.count() == 0:
            p1 = Proyecto(
                titulo = "Sistema de Gestion Industrial",
                descripcion = "Sistema para optimizar costos y parametrizar tiempos de produccion.",
                tags = "Python, Pandas, Data Engineering",
                estado = "En Desarrollo",
                link = "#"
            )

            p2 = Proyecto( 
                titulo = "Smart Task Planner",
                descripcion = "Planificador de escritorio con alertas recurrentes y base de datos local",
                tags = "Python, Tkinter, SQLite",
                estado = "En Desarrollo",
                link = "#"
            )

            db.session.add(p1)
            db.session.add(p2)
            db.session.commit()
            print("Base de datos creada y cargada existosamente.")



@app.route('/')
def home():
    mis_proyectos = Proyecto.query.all()
    return render_template('index.html', proyectos=mis_proyectos)

crear_datos_iniciales()
if __name__=='__main__':
    app.run(debug=True)
