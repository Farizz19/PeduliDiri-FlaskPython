from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'

mysql = MySQL(app)


@app.route("/")
def home():
    return render_template('login.html', nama='fariz')


@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html', nama='fariz')


@app.route("/cp")
def catatanperjalanan():
    return render_template('catatanperjalanan.html', nama='fariz')


@app.route("/id")
def isidata():
    return render_template('isidata.html', nama='fariz')


@app.route("/register", methods=['POST', 'GET'])
def register():
    nik = request.form['nik']
    nama = request.form['nama']
    cursor = mysql.connection.cursor()
    cursor.execute(
        ''' INSERT INTO users(nik,nama) VALUES(%s,%s)''', (nik, nama))
    mysql.connection.commit()
    cursor.close()
    return render_template('dashboard.html')


@app.route("/simpandata", methods=['POST', 'GET'])
def simpandata():
    tanggal = request.form['tanggal']
    jam = request.form['jam']
    lokasi = request.form['lokasi']
    suhu = request.form['suhu']
    cursor = mysql.connection.cursor()
    cursor.execute(''' INSERT INTO catatan_perjalanan(tanggal,jam,lokasi,suhu) VALUES(%s,%s,%s,%s)''',
                   (tanggal, jam, lokasi, suhu))
    mysql.connection.commit()
    cursor.close()
    return render_template('dashboard.html')


# @app.route("/simpanregister", methods=['POST', 'GET'])
# def simpan_register():
#     nik = request.form['nik']
#     nama = request.form['nama']
#     cursor = mysql.connection.cursor()
#     cursor.execute(
#         ''' INSERT INTO users(nik,nama) VALUES(%s,%s)''', (nik, nama))
#     mysql.connection.commit()
#     cursor.close()
#     return f"Done!!"


# @app.route("/register")
# def register():
#     return render_template('register.html')


if __name__ == '__main__':
    app.run()
