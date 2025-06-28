from flask import Flask, render_template, request, redirect, url_for
import os
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__, template_folder='html', static_folder='css')
app.secret_key = 'secret-key'

login_manager = LoginManager()
login_manager.init_app(app)

# Dummy user database
users = {
    'admin': {'password': '123'},
    'user': {'password': '123'}
}

class User(UserMixin):
    def __init__(self, id):
        self.id = id
        self.name = id

@login_manager.user_loader
def load_user(user_id):
    if user_id in users:
        return User(user_id)
    return None

@app.route('/login', methods=['GET', 'POST'])
def login():
    pesan = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            user = User(username)
            login_user(user)
            # Redirect sesuai role
            if username == 'admin':
                return redirect(url_for('admin_dashboard'))
            else:
                return redirect(url_for('user_dashboard'))
        pesan = "Login gagal, username atau password salah."
    return render_template('login.html', pesan=pesan)

@app.route('/admin')
@login_required
def admin_dashboard():
    if current_user.id != 'admin':
        return redirect(url_for('user_dashboard'))
    return render_template('admin.html')

@app.route('/user')
@login_required
def user_dashboard():
    if current_user.id == 'admin':
        return redirect(url_for('admin_dashboard'))
    return render_template('user.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/')
def home():
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)