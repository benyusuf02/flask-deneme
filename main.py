from flask import Flask,render_template,flash,redirect,url_for,session,logging,request
from flask import request
from flask_mysqldb import MySQL,MySQLdb
from wtforms import Form,StringField,TextAreaField,PasswordField,validators
from passlib.hash import sha256_crypt
app =Flask(__name__)

app.secret_key="üzeyir"
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "test1"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL

@app.route("/")

def index():
    return render_template("index.html")
    
@app.route("/layout")

def layout():
    return render_template("layout.html")
    
@app.route("/about")

def about():
    return render_template("about.html")
    
@app.route("/contact")

def contact():
    return render_template("contact.html")
@app.route("/more")

def more():
    return render_template("more.html")
#gönderi kaydı
class registerform(Form):
    title = StringField("Gönderi Başlığı Giriniz :")
    body = StringField("Konu içeriği")
    images = StringField("Resim url giriniz ")

@app.route("/panel", methods=["GET","POST"])


def panel():
    form = registerform(request.form)

    if request.method == "POST" and form.validate():
        title = form.title.data
        body = form.body.data
        images = form.images.data

        #değişkenler tanıldı sql giriş yapıyoruz
        cursor = mysql.connection.cursor()
        sorgu = "Insert into yazi(baslik,metin,resim) Values (%s,%s,%s,)"
        cursor.execute(sorgu,(title,body,images))
        mysql.connection.commit
        cursor.close()
        return redirect(url_for("panel"))
    else:
        return render_template("panel.html",form = form)
    



if __name__ == "__main__":
    app.run(debug=True)