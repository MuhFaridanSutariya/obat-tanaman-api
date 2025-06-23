# app.py

import os
from flask import Flask, jsonify
from dotenv import load_dotenv
from database import db, init_db, Product

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///products.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
init_db(app) # Inisialisasi database dan masukkan data awal

@app.route('/')
def home():
    return jsonify({
        "message": "Selamat datang di API Produk Obat Tanaman!",
        "endpoints": {
            "/products": "Mengambil semua produk",
            "/products/<int:product_id>": "Mengambil produk berdasarkan ID"
        }
    })

@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products])

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get_or_404(product_id)
    return jsonify(product.to_dict())

if __name__ == '__main__':
    # Untuk development, Railway akan menggunakan gunicorn atau sejenisnya
    app.run(debug=True, host='0.0.0.0', port=os.getenv('PORT', 5000))