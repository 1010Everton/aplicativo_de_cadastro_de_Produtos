import os

SQLALCHEMY_DATABASE_URI ='mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database_name}'.format(
        username='root',
        password='Efds11091999.',
        host='localhost',
        port='3306',
        database_name='cadastro'
    )
UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'