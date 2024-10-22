from app import db, app
from app.models import User, Product

def init_db():
    with app.app_context():
        db.create_all()

        db.session.query(User).delete()

        user1 = User(name='John Doe', email='john@example.com')
        user2 = User(name='Mary Smith', email='mary@example.com')

        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()

        db.session.query(Product).delete()

        product1 = Product(name='Manzana', price=50)
        product2 = Product(name='Banana', price=30)
        product3 = Product(name='Naranja', price=40)
        product4 = Product(name='Fresa', price=60)
        product5 = Product(name='Kiwi', price=80)

        db.session.add_all([product1, product2, product3, product4, product5])
        db.session.commit()

        print("Base de datos inicializada")


if __name__ == '__main__':
    init_db()

