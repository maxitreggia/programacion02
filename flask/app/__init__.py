from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Filtro personalizado para formatear fechas
@app.template_filter('format_date')
def format_date(date):
    if isinstance(date, datetime):
        return date.strftime('%d/%m/%Y')
    return date


from app import routes, models
