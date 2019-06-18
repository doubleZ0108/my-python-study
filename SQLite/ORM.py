# Object-Relational Mapping
from sqlalchemy import Column, String, Integer, DateTime, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    course = Column(String(20))
    create_time = Column(DateTime)

def write(session):
    new_user = User(name='double Z', course='Python', create_time=datetime.now())
    session.add(new_user)
    session.commit()

def read(session):
    users = session.query(User).all()
    return users

def another_read(session):
    users = session.query(User).filter(User.name=="double Z").all()
    return users


def display(users):
    for user in users:
        print('Name: ', user.name)
        print('Course: ', user.course)
        print('Create Time: ', user.create_time)



if __name__ == '__main__':
    engine = create_engine(('mysql+mysqlconnector://root:pengcheng00@localhost:3306/test')) # 这里是搭的mysql的地址
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    write(session)

    users = read(session)
    display(users)
    users = another_read(session)
    display(users)
        
    session.close()
