from flask import Flask
from flask import render_template
app = Flask(__name__)
makekat()
@app.route("/")
def index():
    list = getKategori('abc')
    return render_template('template.html', templatelist=list)


@app.route('/<kategori>')
def say_hi(kategori):
    return 'Hello, %s!' % (kategori)

def getKategori(hei):
    list = ['as','ss','bb']
    list.append(hei)
    return list


def makekat():
    mat = ['kake','ost','brød']
    drikke =['cola','vann','saft']
