from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from Data_for_model import region, skills, vacancy, number_offer
from model_relations import full_offer, Skill, Region, Vacancy, Number_offer

engine = create_engine('sqlite:///orm.sqlite', echo=True)

Base = declarative_base()


Session = sessionmaker(bind=engine)

session = Session()



offer_11 = session.query(full_offer).filter(full_offer.number_offer == '(22,)').all()

print(offer_11)