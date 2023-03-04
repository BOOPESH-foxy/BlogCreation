from sqlalchemy import Table, Column, Integer, String, MetaData
meta = MetaData()

userData = Table(
   'userData', meta, 
   Column('id', Integer, primary_key = True), 
   Column('name', String), 
   Column('password', String), 
)
postData = Table(
   'postData', meta, 
   Column('title', String, primary_key = True), 
   Column('content', String), 
   Column('author', String), 
   Column('email', String), 
   Column('category', String), 

)