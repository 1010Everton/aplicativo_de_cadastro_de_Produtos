from errno import errorcode

import mysql.connector

try:
    conn=mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='Efds11091999.'
        )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Existe algo errado no nome de usuário ou senha')
    else:
        print(err)

cursor = conn.cursor()

