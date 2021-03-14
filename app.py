from flask import Flask, render_template, request, url_for
from flask_migrate import Migrate
from werkzeug.utils import redirect

from database import db
from forms import PersonaForm
from models import Persona

app = Flask(__name__)
db.init_app(app)

USER_DB = 'postgres'
PASS_DB = '1234'
URL_DB = 'localhost'
NAME_DB = 'my_db'
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'asdfghjkl'



migrate = Migrate()
migrate.init_app(app, db)

@app.route('/')
def index():
    personas = Persona.query.all()
    total_personas = Persona.query.count()
    return render_template('index.html',personas=personas, total_personas=total_personas)

@app.route('/create-person',methods=['GET','POST'])
def create():
    personas = Persona()
    personaForm = PersonaForm(obj=personas)
    if request.method == 'POST':
        if personaForm.validate_on_submit():
            personaForm.populate_obj(personas)
            db.session.add(personas)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('create.html', forma=personaForm)

@app.route('/edit-person/<int:id>',methods=['GET','POST'])
def edit(id):
    persona = Persona.query.get_or_404(id)
    personaForma = PersonaForm(obj=persona)
    if request.method == 'POST':
        if personaForma.validate_on_submit():
            personaForma.populate_obj(persona)
            db.session.commit()
            return redirect(url_for('index'))

    return render_template('edit.html', forma=personaForma)

@app.route('/delete/<int:id>')
def delete(id):
    persona = Persona.query.get_or_404(id)
    db.session.delete(persona)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/read/<int:id>')
def read_person(id):
    persona = Persona.query.get_or_404(id)
    return render_template('read.html', persona=persona)

