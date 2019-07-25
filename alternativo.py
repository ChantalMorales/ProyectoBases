import pymysql

db= pymysql.connect(host= 'localhost', port=3306, user='root', passwd='', db='proyecto_bases')#conexion con la base de datos

cursor=db.cursor()

sql = "INSERT INTO notas (id,PROGRAMACION,SISTEMAS,ALGORITMOS) \
VALUES (null, 6, 5, 8)"




try:

    cursor.execute(sql)
    db.commit()

except:
	db.rollback()


db.close()
