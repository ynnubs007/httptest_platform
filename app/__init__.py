# -*- coding:utf-8 -*-
__author__ = 'Jin'
from flask import Flask, Blueprint
from config import config

bp = Blueprint("bp", __name__)


def create_app(config_name="DevelopmentConfig"):
    app = Flask(__name__, static_url_path='',template_folder='./templates')
    app.config.from_object(config[config_name])
    # 注册蓝本
    app.register_blueprint(bp)
    return app


from flask_cors import CORS
from flask import render_template
from app.response import products, projects, modules, testcass,reports

app = create_app("ProductionConfig")
CORS(app)

@app.route('/')
def index():
    """访问首页"""
    return render_template('index.html')


@app.route('/dashboard')
def dash():
    """访问仪表展示页面"""
    return app.send_static_file('./page/dashboard.html')

@app.route('/product')
def product():
    """访问产品页面"""
    return app.send_static_file('./page/product.html')


@app.route('/project')
def project():
    """访问项目页面"""
    return app.send_static_file('./page/project.html')

@app.route('/modules')
def modules():
    """访问模块页面"""
    return app.send_static_file('./page/modules.html')

@app.route('/testcass')
def testcass():
    """访问用例页面"""
    return app.send_static_file('./page/testcass.html')

@app.route('/report')
def report():
    """访问配置报告页面"""
    return app.send_static_file('./page/report.html')


@app.route('/config')
def config():
    """访问配置报告页面"""
    return app.send_static_file('./page/config.html')
