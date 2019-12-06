# -*- conding:utf-8 -*-
'''
模块管理的相关接口
'''
__author__ = "Jin"
from flask import jsonify, request,redirect,url_for,render_template
from app import bp
from app.utils import dbfucs
from app.core import collect
from app.utils.log import Logger
from app.utils.jsonfuc import dict_to_dbjson
Logger = Logger()

@bp.route("/queryreport",methods=["POST"])
def getreport():
    '''
    获取用例列表
    编号	名称	所属模块	描述	执行状态	责任人	备注	创建时间
    '''
    dictdata = request.get_json()
    pageNo=int(dictdata["pageNo"])
    pageSize=int(dictdata["pageSize"])
    start=(pageNo-1)*pageSize
    sql = "select  \
           t_reports.cassid,\
           case status when 0 then 'Pass' when 1 then 'Fail' else 'Error' end as status,\
           t_reports.runtime,\
           t_reports.result,\
           t_reports.validate,\
           t_reports.createtime,\
           t_testcass.testname,\
           (SELECT COUNT(*) FROM t_reports) as reportnum\
           from t_testcass INNER JOIN t_reports\
           on t_testcass.id=t_reports.cassid \
           order by createtime desc\
            limit %d, %d" % (start,pageSize)
    res = dbfucs.query(sql)
    print(res)
    response = {}
    response["code"] = 200
    response["data"] = res
    response["msg"] = "查询成功！！！"
    return jsonify(response)

@bp.route("/queryreportcount",methods=["GET"])
def queryreportcount():
    '''
    获取用例列表
    编号	名称	所属模块	描述	执行状态	责任人	备注	创建时间
    '''
    sql = "SELECT COUNT(*)reportnum FROM t_reports"
    res = dbfucs.query(sql)
    response = {}
    response["code"] = 200
    response["data"] = res
    response["msg"] = "查询成功！！！"
    return jsonify(response)


@bp.route("/queryresultCount",methods=["GET"])
def queryresultCount():
    '''
    获取用例列表
    编号	名称	所属模块	描述	执行状态	责任人	备注	创建时间
    '''
    sql = "select \
         case status when 0 then 'Pass' when 1 then 'Fail' else 'Error' end as status,\
         count(status) as nums \
         from t_reports \
         GROUP BY status"

    res = dbfucs.query(sql)
    response = {}
    response["code"] = 200
    response["data"] = res
    response["msg"] = "查询成功！！！"
    return jsonify(response)