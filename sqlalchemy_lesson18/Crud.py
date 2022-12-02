

from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from Data_for_model import region, skills, vacancy, number_offer, full_offer_list
from model_relations import full_offer, Skill, Region, Vacancy, Number_offer

engine = create_engine('sqlite:///orm.sqlite', echo=True)

Base = declarative_base()


Session = sessionmaker(bind=engine)

session = Session()

for name in region:
    region_name = Region(name[0])
    session.add(region_name)


for name in skills:
    skills_name = Skill(name[0])
    session.add(skills_name)


for name in vacancy:
    vacancy_name = Vacancy(name[0])
    session.add(vacancy_name)


for name in number_offer:
    number_offer_name = Number_offer(name[0])
    session.add(number_offer_name)


for line in full_offer_list:
    full_offer_line = full_offer(line[0], line[1], line[2], line[3])
    session.add(full_offer_line)


session.commit()


offer_11 = session.query(full_offer).filter(full_offer.number_offer == '22').all()

print(offer_11)

session.close()