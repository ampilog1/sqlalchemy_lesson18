from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///orm.sqlite', echo=False)

Base = declarative_base()

class full_offer(Base):
    __tablename__ = 'full_offer'
    id = Column(Integer, primary_key=True)
    number_offer = Column(Integer, ForeignKey('Number_offer.id'))
    vacancy = Column(Integer, ForeignKey('vacancy.id'))
    region = Column(Integer, ForeignKey('region.id'))
    skill = Column(Integer, ForeignKey('skill.id'))

    def __init__(self, number_offer, vacancy, region, skill):
        self.number_offer = number_offer
        self.vacancy = vacancy
        self.region = region
        self.skill = skill

    def __str__(self):
        return f'{self.id}: {self.number_offer}, {self.vacancy}, {self.region}, {self.skill}'

class Skill(Base):
    __tablename__ = 'skill'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Region(Base):
    __tablename__ = 'region'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.id}: {self.name}'


class Vacancy(Base):
    __tablename__ = 'vacancy'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f'{self.id}: {self.name}'

class Number_offer(Base):
    __tablename__ = 'Number_offer'
    id = Column(Integer, primary_key=True)
    number = Column(String)

    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f'{self.id}: {self.number}'


Base.metadata.create_all(engine)
