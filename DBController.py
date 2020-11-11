import pymysql

connection = pymysql.connect(host="159.203.59.83",user="gamestop",
                          password='Sn123456', database='gamestop')

try:
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Game"
        cursor.execute(sql)

        result = cursor.fetchall()

        for item in result:
            print(item,type(item))

except pymysql.err.ProgrammingError:
    print('A DB error caught')
finally:
    connection.close()

