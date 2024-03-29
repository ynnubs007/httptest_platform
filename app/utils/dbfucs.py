# -*- coding:utf-8 -*-
__author__ = 'Jin'
'''
说明：操作数据库的相关方法封装
'''
import pymysql
from config import db_config
from app.utils.log import Logger

def query(sql=""):
    """
        ex: 根据sql查询结果
        args: sql
        return: results
    """
    results = []
    db = pymysql.connect(**db_config)
    cur = db.cursor()
    try:
        cur.execute(sql)  # 执行sql语句
        # 获得列名
        descs = []

        for desc in cur.description:
            descs.append(desc[0])
        print(descs)
        # 构造键值对{"列名":数据}
        results = []
        for res in cur.fetchall():
            row = {}
            for i in range(len(descs)):
                row[descs[i]] = res[i]
            results.append(row)
    except Exception as e:
        Logger().error("sql语句[%s]执行失败,错误信息为 --> %s" % (sql, e))
        raise e
    finally:
        cur.close()
        db.close()  # 关闭连接
        return results


def excute(sql=""):
    '''
        ex: 根据sql插入或更新数据
        args: sql
        return: is_success，true:成功 false:失败
    '''
    is_success = True
    db = pymysql.connect(**db_config)
    cur = db.cursor()
    try:
        cur.execute(sql)
        db.commit()
    except Exception as e:
        db.rollback()
        Logger().error("sql语句[%s]执行失败,错误信息为 --> %s" % (sql, e))
        is_success = "%s" % e
    finally:
        cur.close()
        db.close()
        return is_success