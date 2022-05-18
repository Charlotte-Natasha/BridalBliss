from flask_login import UserMixin
from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class User(db.Model, UserMixin):
    __tablename__="users"
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(255), unique=True, nullable=False)
    email=db.Column(db.String(255), unique=True, index = True, nullable=False)

    password_secure=db.Column(db.String(255), nullable=False)
    bio=db.Column(db.String(255))
    profile_pic_path=db.Column(db.String())

    services=db.relationship("Service",backref="user",lazy="dynamic")
    orders= db.relationship('Order',backref = 'user',lazy = "dynamic")
    reviews= db.relationship('Review',backref = 'user',lazy = "dynamic")

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    @property
    def set_password(self):
        raise AttributeError("You cannot read the password attribute")

    @set_password.setter
    def password(self,password):
        self.password_secure=generate_password_hash(password)
    
    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)
    
    def save_u(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f"User:{self.username}"

class Service(db.Model):
    __tablename__="services"
    id=db.Column(db.Integer, primary_key=True)
    category=db.Column(db.String(255), nullable=False)
    cost=db.Column(db.String(255), nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey('users.id'))
    order_id=db.Column(db.Integer, db.ForeignKey('orders.id'))

    reviews= db.relationship('Review',backref = 'service',lazy = "dynamic")

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f"Service:{self.category}" 

class Order(db.Model):
    __tablename__="orders"
    id=db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer, db.ForeignKey('users.id'))
    order_date=db.Column(db.DateTime, default=datetime.utcnow)
    details=db.Column(db.Text())
    services=db.relationship("Service",backref="order",lazy="dynamic")
    

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f"Order:{self.post}" 

class Review(db.Model):
    __tablename__="reviews"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'))
    time=db.Column(db.DateTime, default=datetime.utcnow)

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_reviews(cls,id):
        reviews=Review.query.filter_by(service_id=id).all()

        return reviews

    def __repr__(self):
        return f"Review{self.id}"