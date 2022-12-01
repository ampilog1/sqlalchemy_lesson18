

from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from Data_for_model import region, skills, vacancy, number_offer
from model_relations import full_offer, Skill, Region, Vacancy, Number_offer

engine = create_engine('sqlite:///orm.sqlite', echo=True)

Base = declarative_base()


Session = sessionmaker(bind=engine)

session = Session()

for name in region:
    name = str(name)
    region_name = Region(name)
    session.add(region_name)


for name in skills:
    name = str(name)
    skills_name = Skill(name)
    session.add(skills_name)


for name in vacancy:
    name = str(name)
    vacancy_name = Vacancy(name)
    session.add(vacancy_name)


for name in number_offer:
    name = str(name)
    number_offer_name = Number_offer(name)
    session.add(number_offer_name)
    print(Number_offer(name))

session.commit()
session.close()

offer_11 = session.query(full_offer).filter(full_offer.number_offer == '22').all()

print(offer_11)

