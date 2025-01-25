# src/routes/person_routes.py

from flask import Blueprint, request, jsonify
from use_cases.person_usecase import PersonUseCase
from repositories.person_repository import PersonRepository
from auth.jwt_handler import decode_token

person_bp = Blueprint('person', __name__)

# Rota para criar uma pessoa
@person_bp.route('/', methods=['POST'])
def create_person():
    data = request.get_json()
    person = PersonUseCase.create_person(data)
    return jsonify({'message': 'Person created successfully', 'id': person.idperson}), 201

# Rota para obter uma pessoa por ID
@person_bp.route('/<int:person_id>', methods=['GET'])
def get_person(person_id):
    person = PersonRepository.get_by_id(person_id)
    if not person:
        return jsonify({'message': 'Person not found'}), 404
    return jsonify({
        'id': person.idperson,
        'name': person.name,
        'email': person.email,
        'address': person.address,
        'birthday': person.birthday,
        'typeuser': person.typeuser,
        'rg': person.rg,
        'cpf': person.cpf
    })

# Rota para atualizar uma pessoa
@person_bp.route('/<int:person_id>', methods=['PUT'])
def update_person(person_id):
    data = request.get_json()
    person = PersonRepository.update(person_id, data)
    if not person:
        return jsonify({'message': 'Person not found'}), 404
    return jsonify({'message': 'Person updated successfully'})

# Rota para deletar uma pessoa
@person_bp.route('/<int:person_id>', methods=['DELETE'])
def delete_person(person_id):
    person = PersonRepository.delete(person_id)
    if not person:
        return jsonify({'message': 'Person not found'}), 404
    return jsonify({'message': 'Person deleted successfully'})