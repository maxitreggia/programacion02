from datetime import datetime

from flask import render_template, request, jsonify, redirect, url_for
from app import app, db
from app.models import User, Product


@app.route("/")
def hello_world():
    return "Hello world"


@app.route("/saludo/<name>")
def hello_user(name):
    return f"Hola, {name}"


@app.route('/saludo_personalizado', methods=['GET', 'POST'])
def greeting_post_method():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hola, {name}"
    return render_template('seccion1_3.html')


@app.route('/formulario', methods=['GET', 'POST'])
def handleFormRequest():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        return f"Hola, {name}. Tu mensaje es: {message}"
    return render_template('seccion1_4.html')


@app.route('/par_impar/<int:num>')
def even_odd(num):
    try:
        num = int(num)
    except ValueError:
        return jsonify({"error": "Por favor, ingresa un número entero válido."}), 400
    if num % 2 == 0:
        return f"El número {num} es par."
    else:
        return f"El número {num} es impar."


@app.route('/frutas')
def mostrar_frutas():
    fruits = ['Manzana', 'Banana', 'Naranja', 'Fresa', 'Kiwi']
    # fruits = [] # descomentar para probar el mensaje de lista vacia
    return render_template('seccion2_6.html', frutas=fruits)


@app.route('/mostrar_productos')
def show_products():
    products = [
        {'name': 'Apple', 'price': 80},
        {'name': 'Banana', 'price': 50},
        {'name': 'Television', 'price': 1500},
        {'name': 'Headphones', 'price': 120},
        {'name': 'Shoes', 'price': 90},
    ]
    return render_template('seccion2_8.html', products=products)


@app.route('/bienvenida', methods=['GET', 'POST'])
def welcome():
    name = ""
    if request.method == 'POST':
        name = request.form.get('name')
        return render_template('seccion2_9.html', name=name)

    return render_template('seccion2_9.html', name=name)


CREDENTIALS = {
    'usuario': '123'
}


@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ""
    if request.method == 'POST':
        user = request.form.get('user')
        password = request.form.get('password')

        if (user in CREDENTIALS) and (CREDENTIALS[user] == password):
            message = f"¡Bienvenido, {user}!"
        else:
            message = "Usuario o contraseña incorrectos."

    return render_template('seccion2_10.html', message=message)


@app.route('/numeros')
def numbers():
    list_numbers = list(range(1, 11))
    return render_template('seccion3_11.html', numbers=list_numbers)


@app.route('/productos')
def products():
    list_products = [
        {'name': 'Manzana', 'price': 50, 'category': 'Frutas'},
        {'name': 'Leche', 'price': 30, 'category': 'Lácteos'},
        {'name': 'Pan', 'price': 25, 'category': 'Panadería'},
        {'name': 'Carne', 'price': 150, 'category': 'Carnes'},
        {'name': 'Zanahoria', 'price': 20, 'category': 'Vegetales'}
    ]

    return render_template('seccion3_12.html', products=list_products)


@app.route('/tabla_multiplicar', methods=['GET', 'POST'])
def multiplication_table():
    result = []
    if request.method == 'POST':
        number = request.form.get('number')

        if number:
            try:
                number = int(number)
                result = [number * i for i in range(1, 11)]
            except ValueError:
                result = "Por favor, ingresa un número válido."

    return render_template('seccion3_13.html', result=result)


@app.route('/usuarios')
def list_users():
    users = User.query.all()
    return render_template('seccion3_14.html', users=users)


@app.route('/producto')
def show_product():
    product = {
        'name': 'Manzana',
        'price': 1.2345
    }
    return render_template('seccion4_15.html', product=product)


@app.route('/products')
def list_products():
    product = [
        {'name': 'Manzana', 'price': 1.23},
        {'name': 'Banana', 'price': 0.99},
        {'name': 'Naranja', 'price': 1.50},
        {'name': 'Frutilla', 'price': 2.00}
    ]
    return render_template('seccion4_16.html', product=product)

@app.route('/date')
def show_date():
    current_date = datetime.now()
    return render_template('seccion4_17.html', date=current_date)


@app.route('/form', methods=['GET', 'POST'])
def form():
    name = ""
    email = ""

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

    return render_template('seccion5_18.html', name=name, email=email)


@app.route('/buscar', methods=['GET', 'POST'])
def search():
    results = []
    keyword = ""

    if request.method == 'POST':
        keyword = request.form.get('keyword', '').lower()
        results = Product.query.filter(Product.name.ilike(f'%{keyword}%')).all()

    return render_template('seccion5_19.html', results=results, keyword=keyword)


@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        try:
            new_user = User(name=name, email=email)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('list_user'))
        except Exception as e:
            error = str(e)
            return render_template('seccion5_20.html', error=error)

    return render_template('seccion5_20.html')


@app.route('/users')
def list_user():
    users = User.query.all()
    return render_template('seccion5_20_2.html', users=users)
