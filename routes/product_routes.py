# src/routes/product_routes.py

from flask import Blueprint, request, jsonify
from repositories.product_repository import ProductRepository

product_bp = Blueprint('product', __name__)

# Rota para criar um produto
@product_bp.route('/', methods=['POST'])
def create_product():
    data = request.get_json()
    product = ProductRepository.create(data)
    return jsonify({'message': 'Product created successfully', 'id': product.idproduct}), 201

# Rota para listar todos os produtos
@product_bp.route('/', methods=['GET'])
def list_products():
    products = ProductRepository.get_all()
    return jsonify([
        {
            'id': p.idproduct,
            'name': p.name,
            'price': p.price,
            'description': p.description,
            'weight': p.weight,
            'brand': p.brand,
            'expiration': p.expiration
        }
        for p in products
    ])

# Rota para obter um produto por ID
@product_bp.route('/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = ProductRepository.get_by_id(product_id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    return jsonify({
        'id': product.idproduct,
        'name': product.name,
        'price': product.price,
        'description': product.description,
        'weight': product.weight,
        'brand': product.brand,
        'expiration': product.expiration
    })

# Rota para atualizar um produto
@product_bp.route('/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    product = ProductRepository.update(product_id, data)
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    return jsonify({'message': 'Product updated successfully'})

# Rota para deletar um produto
@product_bp.route('/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = ProductRepository.delete(product_id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    return jsonify({'message': 'Product deleted successfully'})
