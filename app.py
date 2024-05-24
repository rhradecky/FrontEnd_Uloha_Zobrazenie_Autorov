from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://upkjsca8ynbl11b0ikgz:f1nKXzsR6eivAWjmQDT6i6W0E7b2vG@bdipmw29ejuoeccxynb1-postgresql.services.clever-cloud.com:50013/bdipmw29ejuoeccxynb1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from author import Author
from book import Book
#from members_X import Members
from genres import Genre

@app.route('/')
def command_list():
    return ('<big>Zoznam dostupnych prikazov<small><BR>/authors <BR>/author/ID <BR>/authors/add <BR>/books<BR>/books/ID<BR>/books/add<BR>/books/update<BR>/books/delete/ID')


@app.route('/authors', methods=['GET'])
def ge_Authors():
    authors = Author.query.all()
    authors_list = [author.to_dict() for author in authors]
    #return jsonify(authors_list)
    return render_template('authors.html', authors = authors_list)



















if __name__ == '__main__':
    app.run(debug=True)
