import time
from flask_cors import CORS
from flask import Flask,request, jsonify, make_response
# import sys
# print (sys.path)
from flask_migrate import Migrate  
from flask_sqlalchemy import SQLAlchemy #这里使用pip install -U flask-sqlalchemy安装的，不是pip install flask-sqlalchemy
from marshmallow_sqlalchemy import SQLAlchemySchema 
from marshmallow import fields


app = Flask(__name__)
class Config(object):
    """配置参数"""
    # 设置连接数据库的URL
    user = 'root'
    password = '076538'
    database = 'book'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%s:%s@127.0.0.1:3306/%s' % (user,password,database)

    # 设置sqlalchemy自动更跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # 查询时会显示原始SQL语句
    app.config['SQLALCHEMY_ECHO'] = True

    # 禁止自动提交数据处理
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = False

# 读取配置
app.config.from_object(Config)

db = SQLAlchemy(app)

migrate = Migrate(app,db)  # 添加到db = SQLAlchemy(app)后面

class Role(db.Model):
    # 定义表名
    __tablename__ = 'roles'
    # 定义字段
    id = db.Column(db.Integer, primary_key=True,autoincrement=True) # 自增长的
    name = db.Column(db.String(64), unique=True)
    def __init__(self, name):
            self.name = name  
   


# 作者信息模型
class Author(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))
    specialisation = db.Column(db.String(50))

    def __init__(self,name,specialisation):
        self.name = name
        self.specialisation = specialisation

    def __repr__(self):
        return '<Product %d>' % self.id

# 序列接口数据为JSON格式
class RoleSchema(SQLAlchemySchema):
    class Meta(SQLAlchemySchema.Meta):
        model = Role
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    name = fields.String(required=True)



@app.route('/',methods=['GET'])
def get_started():
    return 'hello world'

@app.route('/add',methods=['POST'])
def add():
    data = request.get_json()
    role = Role(data)
    db.session.add(role)
    db.session.commit()
    return 'add success'

@app.route('/show',methods=['GET'])
def show():
    roles = Role.query.all()
    role_schema = RoleSchema(many=True)
   
    roles_json = role_schema.dump(roles)
    return make_response(jsonify({"roles": roles_json}))
   

@app.route('/roles',methods=['GET'])
def get_roles():
    db.drop_all()
    db.create_all()
    roles = Role.query.all()
    role_schema = RoleSchema(many=True)
    roles_json = role_schema.dump(roles)
    return make_response(jsonify({"roles": roles_json}))
