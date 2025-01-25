# src/use_cases/person_usecase.py

from repositories.person_repository import PersonRepository
from werkzeug.security import generate_password_hash, check_password_hash

class PersonUseCase:
    @staticmethod
    def create_person(data):
        data['password'] = generate_password_hash(data['password'])
        return PersonRepository.create(data)

    @staticmethod
    def login(email, password):
        person = PersonRepository.get_by_email(email)
        if person and check_password_hash(person.password, password):
            return person
        return None