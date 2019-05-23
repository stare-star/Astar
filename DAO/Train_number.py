# coding: utf-8

import random
from faker import Factory

from sqlalchemy import create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy import Column, String, Integer, Text
from sqlalchemy.orm import sessionmaker, relationship


engine = create_engine('mysql+mysqldb://root:mysql666@118.25.176.99:3306/traffic?charset=utf8')
Base = declarative_base()


class Train(Base):

    __tablename__ = 'trains'

    id = Column(Integer, primary_key=True)
    number = Column(String(255), nullable=False, index=True)
    start_time = Column(String(255), nullable=False)
    time = Column(String(255), nullable=False)
    arrive_time = Column(String(255), nullable=False)
    start_where = Column(String(255), nullable=False)
    arrive_where = Column(String(255), nullable=False)
    price = Column(Integer, nullable=False)
    date= Column(String(255), nullable=False)


    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.number)




if __name__ == '__main__':
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = (session
             .query(Train)
             .filter(Train.id< 100)
             .limit(100)
             .offset(0).all()
             )
    print(query)
    # session.commit()
