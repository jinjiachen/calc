#coding=utf-8
import MySQLdb
def calc(s1,s2):
    db=MySQLdb.connect('JJC-PC','root','123456','flange_SO',use_unicode=0,charset='gbk')
    cursor=db.cursor()
    sql1='select * from SO'+s2+' where DN='+s1
    cursor.execute(sql1)
    results=cursor.fetchall()
    db.close()
    return(results)

def catch_DN():
    db=MySQLdb.connect('localhost','root','123456','flange_SO',use_unicode=0,charset='gbk')
    cursor=db.cursor()
    sql2='select DN from SO6'
    cursor.execute(sql2)
    results=cursor.fetchall()
    return(results)

db=MySQLdb.connect('localhost','root','123456','flange_SO',use_unicode=0,charset='gbk')
cursor=db.cursor()
sql2='select DN from SO6'
cursor.execute(sql2)
results=cursor.fetchall()
print(results)
