import mysql.connector
from mysql.connector import errorcode

print("conectando ...")

try:
      banco = mysql.connector.connect(
            host='127.0.0.1',
            database='cadastro',
            port='3306',
            user='root',
            password='Efds11091999.'
      )
except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Existe algo errado no nome de usuário ou senha')
      else:
            print(err)
else:
      if banco.is_connected():
            print('conexão estabelecida')
            cursor=banco.cursor()

      banco.close()
      cursor.close()


