#!/usr/bin/env python3
from app import app
from models import db, User

def ensure_admin():
    with app.app_context():
        db.create_all()
        if User.query.filter_by(email='admin@vvce.ac.in').first() is None:
            admin = User(email='admin@vvce.ac.in', full_name='Admin User', role='admin')
            admin.set_password('admin123')
            db.session.add(admin)
            db.session.commit()
            print('Admin user created: admin@vvce.ac.in / admin123')
        else:
            print('Admin already exists')

if __name__ == '__main__':
    ensure_admin()
