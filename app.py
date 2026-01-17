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
                tags = "Python | Pandas | Data Engineering",
                estado = "🚧 En Desarrollo", #🚀
                link = "#"
            )

            p2 = Proyecto( 
                titulo = "Smart Task Planner",
                descripcion = "Planificador de escritorio con alertas recurrentes y base de datos local",
                tags = "Python | Tkinter | SQLite",
                estado = "📦 Finalizado",
                link = "https://github.com/CorradiGonzalo/SmartTaskPlanner"
            )

            p3 = Proyecto(
                titulo = "Web Mi Pequeña Gran Estrella",
                descripcion = "Web de local de venta de ropa" \
                "Incluye catalogo (stock incluido), carrito de compras, gestion de usuarios y gestion de cobros",
                tags = "Pythom | Django | HTML | SCSS",
                estado = "🚧 En Desarrollo", #🚀
                link = "https://github.com/CorradiGonzalo/Web-MiPequenaGranEstrella"
            )

            p4 = Proyecto (
                titulo = "Gmail-Inbox-Cleaner (n8n Automation)",
                descripcion = "Este workflow convierte una bandeja de entrada caótica en un pipeline organizado de oportunidades. Diseñado para automatizar la gestión de correos electrónicos, el sistema actúa como un filtro inteligente que separa el 'ruido' (Spam/Promociones) de la información crítica (Propuestas laborales de LinkedIn, Workana, Freelancer). "
                "El bot lee los correos no leídos, extrae metadatos clave (Remitente, Asunto, Fecha), y aplica lógica condicional para decidir su destino: una base de datos de seguimiento o la papelera. ",
                tags = "n8n Workflow | Gmail API | Google Sheets API | Telegram Bot API | JSON Logic",
                estado = "🤖 Finalizado",
                link = "https://github.com/CorradiGonzalo/n8n-automation-portfolio/tree/main/02_Gmail_Inbox_Cleaner"
            )

            p5 = Proyecto(
                titulo = "E-commerce Price Tracker & Alert Bot Stack (n8n Automation)",
                descripcion = "Diseñé un bot de monitoreo de precios automatizado para detectar oportunidades de mercado en tiempo real en plataformas de e-commerce (MercadoLibre). " \
                "El sistema se ejecuta periódicamente, realiza scraping del sitio web objetivo para extraer el precio actual y lo cruza con una base de datos histórica en Google Sheets. Mediante lógica condicional, evalúa si el precio ha bajado respecto al último registro o si cumple con un objetivo de compra definido. " \
                "Si se detecta una oportunidad, el bot dispara una alerta instantánea a un canal privado de Discord, permitiendo tomar decisiones de compra inmediatas sin necesidad de monitoreo manual. " \
                "Puntos Clave:" \
                "Web Scraping: Extracción de datos no estructurados (HTML Parsing) de sitios dinámicos; " \
                "Lógica de Negocio: Algoritmo de comparación de precios y cálculo de variación porcentual; " \
                "Alertas en Tiempo Real: Integración con Discord API para notificaciones push; " \
                "Persistencia de Datos: Registro histórico de fluctuaciones en Google Sheets; ",
                tags = "n8n Workflow | Web Scraping | Discord Webhooks | Google Sheets API",
                estado = "🤖 Finalizado",
                link = "https://github.com/CorradiGonzalo/n8n-automation-portfolio/tree/main/03_Price_Tracker_Discord"
            )

            p6 = Proyecto (
                titulo = "AI-Job-Hunter (n8n Automation)",
                descripcion = "Este workflow automatiza la búsqueda y análisis de ofertas laborales. Utiliza un modelo LLM (Groq) para leer feeds RSS, interpretar las descripciones y filtrar solo aquellas relevantes para mi perfil.",
                tags = "n8n Workflow | Groq LLM | RSS Feeds | Google Sheets",
                estado = "🤖 Finalizado",
                link = "https://github.com/CorradiGonzalo/n8n-automation-portfolio/tree/main/01_AI_Job_Hunter"
            )

            p7 = Proyecto(
                titulo = "Dashboard de Precios e Inflación",
                descripcion = "Herramienta de BI que analiza volatilidad de precios desde Excel o datos simulados.",
                tags = "Python, Streamlit, Pandas, Data Viz",
                estado = "🚀 Finalizado", 
                link = "https://dashboard-de-precios-interactivo.streamlit.app/"
            )

            db.session.add(p1)
            db.session.add(p2)
            db.session.add(p3)
            db.session.add(p4)
            db.session.add(p5)
            db.session.add(p6)
            db.session.add(p7)
            db.session.commit()
            print("Base de datos creada y cargada existosamente.")



@app.route('/')
def home():
    mis_proyectos = Proyecto.query.all()
    return render_template('index.html', proyectos=mis_proyectos)

crear_datos_iniciales()
if __name__=='__main__':
    app.run(debug=True)
