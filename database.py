# database.py

from flask_sqlalchemy import SQLAlchemy
from data import PRODUCTS_DATA

db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama_produk = db.Column(db.String(100), nullable=False)
    petunjuk_penggunaan = db.Column(db.Text, nullable=False)
    harga = db.Column(db.Float, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    total_penjualan = db.Column(db.Integer, nullable=False)
    gambar = db.Column(db.String(255), nullable=True) # URL gambar

    def __repr__(self):
        return f"<Product {self.nama_produk}>"

    def to_dict(self):
        return {
            "id": self.id,
            "nama_produk": self.nama_produk,
            "petunjuk_penggunaan": self.petunjuk_penggunaan,
            "harga": self.harga,
            "rating": self.rating,
            "total_penjualan": self.total_penjualan,
            "gambar": self.gambar
        }

def init_db(app):
    with app.app_context():
        db.create_all()
        # Masukkan data awal jika database kosong
        if not Product.query.first():
            print("Mengisi database dengan data awal...")
            for product_data in PRODUCTS_DATA:
                product = Product(
                    id=product_data["id"],
                    nama_produk=product_data["nama_produk"],
                    petunjuk_penggunaan=product_data["petunjuk_penggunaan"],
                    harga=product_data["harga"],
                    rating=product_data["rating"],
                    total_penjualan=product_data["total_penjualan"],
                    gambar=product_data["gambar"]
                )
                db.session.add(product)
            db.session.commit()
            print("Data awal berhasil dimasukkan.")
        else:
            print("Database sudah berisi data.")