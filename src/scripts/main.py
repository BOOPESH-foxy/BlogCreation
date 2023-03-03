import sqlalchemy as Al
from sqlalchemy.orm import sessionmaker
import pymysql
from BlogInstance.models import User, Post, Comment

engine = Al.create_engine('mysql+pymysql://BlogInstance:BlogInstance@localhost:3306/BlogInstance')
Session = sessionmaker(bind=engine)

NewSession = Session.query(User).all()
new_user = User(name='boo', email='boopesh.mc@gmail.com', password='HEYboo@013')

NewSession.add(new_user)
NewSession.commit()
NewSession.close()