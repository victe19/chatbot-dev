from dataclasses import dataclass
from this import d
import pymysql

class DataBase:
    def __init__(self) -> None:
        self.connection = pymysql.connect(
            host='localhost', #ip
            user='root',
            password='',
            db='demo',
        )

        self.cursor = self.connection.cursor()
        print('Conexxió establerta')
        
database=DataBase()
