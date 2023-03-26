import time
from flask import Flask,request, jsonify, make_response
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URL'] = 'mysql+pymysql://<mysql_username>:<mysql_password>@<mysql_host>:<mysql_port>/<mysql_db_name>'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app,db)
CORS(app)

# 建立作者模型
class Author(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))
    specialisation = db.Column(db.String(50))

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __init__(self,name,specialisation):
        self.name = name
        self.specialisation = specialisation

    def __repr__(self):
        return '<Product %d>' % self.id

class AuthorSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Author
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    name = fields.String(required=True)
    specialisation = fields.String(required=True)


@app.route('/authors',methods=['GET'])
def get_authors():
    get_authors = Author.query.all()
    author_schema = AuthorSchema(many=True)
    authors = author_schema.dump(get_authors)
    return make_response(jsonify({"authors":authors}))

@app.route('/authors/<id>',methods=['GET'])
def get_author_by_id(id):
    get_author = Author.query.get(id)
    author_schema = AuthorSchema()
    author = author_schema.dump(get_author)
    return make_response(jsonify({"author":author}))

@app.route('/authors',methods=['POST'])
def create_author():
    data = request.get_json()
    author_schema = AuthorSchema()
    authors = author_schema.load(data)
    result = author_schema.dump(authors.create())
    return make_response(jsonify({"author":result}),201)

@app.route('/authors/<id>',methods=['PUT'])
def update_author_by_id(id):
    data = request.get_json()
    get_author = Author.query.get(id)
    if data.get('specialisation'):
        get_author.specialisation = data['specialisation']

    if data.get('name'):
        get_author.name = data['name']

    db.session.add(get_author)
    db.session.commit()
    author_schema = AuthorSchema(only=['id','name','specialisation'])
    author = author_schema.dump(get_author)
    return make_response(jsonify({"author":author}))

@app.route('/authors/<id>',methods=['DELETE'])
def delete_author_by_id(id):
    get_author = Author.query.get(id)
    db.session.delete(get_author)
    db.session.commit()
    return make_response({"msg":"ok"},204)

@app.route('/time')
def get_current_time():
    return {'time': time.time()}