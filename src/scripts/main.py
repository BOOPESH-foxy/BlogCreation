import sqlalchemy as Al
from sqlalchemy.orm import sessionmaker
import pymysql
import mysql.connector


Engine = Al.create_engine("mysql://root:BlogInstance@localhost/BlogInstance")
print(Engine)