#coding=utf-8
import MySQLdb
def calc(PN,DN):
#    db=MySQLdb.connect('JJC-PC','root','123456','seal',use_unicode=0,charset='gbk')
    db=MySQLdb.connect('PC-JJC','root','123456','seal',use_unicode=0,charset='gbk')
    cursor=db.cursor()
    sql1='select PN'+PN+' from mifengmian where DN='+DN
    cursor.execute(sql1)
    result1=cursor.fetchall()
    sql2='select * from mifengmian where DN='+DN
    cursor.execute(sql2)
    result2=cursor.fetchall()
    results=result1+result2
    db.close()
    return(results)
