#выполняем простой запрос в базу.
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from Data_for_model import region, skills, vacancy, number_offer, full_offer_list
from model_relations import full_offer, Skill, Region, Vacancy, Number_offer

engine = create_engine('sqlite:///orm.sqlite', echo=True)

Session = sessionmaker(bind=engine)

session = Session()

for line in session.query(full_offer).filter(full_offer.number_offer == '1'):
    print(line)
    print(type(line))




session.commit()

session.close()
