from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///orm.sqlite', echo=True)

Base = declarative_base()


class Region(Base):
    __tablename__ = 'region'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    number = Column(Integer, nullable=True)


    def __init__(self, name, number):
        self.name = name
        self.number = number




Base.metadata.create_all(engine)

