from flask import Flask, render_template, redirect, url_for
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm, EditPetForm
from models import db, connect_db, Pet
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.config['SECRET_KEY'] = 'shhitsasecret!'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


@app.route('/')
def homepage():
    '''Show pet listings'''

    pets = Pet.query.all()

    return render_template('pet_listings.html', pets=pets)


@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    '''Add a new pet'''

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        age = form.age.data
        notes = form.notes.data
        photo_url = form.photo_url.data

        pet = Pet(name=name, species=species, age=age, notes=notes, photo_url=photo_url)

        db.session.add(pet)
        db.session.commit()

        return redirect(url_for('homepage'))

    else:
        return render_template('pet_add_form.html', form=form)


@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def edit_pet(pet_id):
    '''Edit Pet'''

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.photo_url = form.photo_url.data
        pet.available = form.available.data

        db.session.commit()

        return redirect(url_for('homepage'))

    else:
        return render_template('pet_edit_form.html', form=form, pet=pet)
