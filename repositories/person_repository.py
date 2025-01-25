# src/repositories/person_repository.py

from models.person import Person
from database import db

class PersonRepository:
    @staticmethod
    def create(data):
        person = Person(**data)
        db.session.add(person)
        db.session.commit()
        return person

    @staticmethod
    def get_by_email(email):
        return Person.query.filter_by(email=email).first()

    @staticmethod
    def get_by_id(person_id):
        return Person.query.get(person_id)

    @staticmethod
    def update(person_id, data):
        person = Person.query.get(person_id)
        if person:
            for key, value in data.items():
                setattr(person, key, value)
            db.session.commit()
        return person

    @staticmethod
    def delete(person_id):
        person = Person.query.get(person_id)
        if person:
            db.session.delete(person)
            db.session.commit()
        return person
