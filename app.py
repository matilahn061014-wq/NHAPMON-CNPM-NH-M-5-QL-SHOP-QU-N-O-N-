from flask import Flask, render_template

# Chạy server tìm file ngay tại thư mục gốc
app = Flask(__name__, template_folder='.')

@app.route('/')
def home():
    # Khi mở web lên là thấy cái index.html (menu hồng) ngay
    return render_template('index.html')

@app.route('/interface/<filename>')
def load_interface(filename):
    # Khi nhấn menu, cái iframe sẽ gọi link này để lấy file trong folder interface
    return render_template(f'interface/{filename}')

if __name__ == '__main__':
    app.run(debug=True)
