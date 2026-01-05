from flask import Flask, render_template, request, redirect, flash
from models import db, Product, Customer, Invoice

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop_nhom5.db'
app.secret_key = "secret_key_nhom5"
db.init_app(app)

@app.route('/')
def index():
    # US17: Báo cáo doanh thu thuần
    total = db.session.query(db.func.sum(Invoice.total_amount)).scalar() or 0
    return render_template('dashboard.html', total=total)

@app.route('/ban-hang', methods=['GET', 'POST'])
def sell():
    # US1: Quét mã/Thanh toán & US10: Trừ tồn kho
    prods = Product.query.all()
    if request.method == 'POST':
        p_id = request.form.get('p_id')
        p = Product.query.get(p_id)
        if p and p.stock > 0:
            p.stock -= 1 # Tự động trừ kho
            inv = Invoice(total_amount=p.price)
            db.session.add(inv)
            db.session.commit()
            flash("Thanh toán thành công!")
        return redirect('/ban-hang')
    return render_template('sell.html', prods=prods)

if __name__ == '__main__':
    with app.app_context():
        db.create_all() # Tự tạo file DB
        if not Product.query.first(): # Tạo mẫu
            db.session.add(Product(id="SP01", name="Váy Xòe", price=200000, stock=10))
            db.session.commit()
    app.run(debug=True)
