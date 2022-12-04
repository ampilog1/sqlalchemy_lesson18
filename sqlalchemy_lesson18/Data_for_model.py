#в этом файле готовим данные для заливки в базу. База из прошлого урока
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('TestDB.db')

# Создаем курсор
cursor = conn.cursor()

cursor.execute('SELECT name from Region')

region = cursor.fetchall()

cursor.execute('SELECT name from Skills')

skills = cursor.fetchall()

cursor.execute('SELECT name from vacancy')

vacancy = cursor.fetchall()

cursor.execute('SELECT number from Number_offer')

number_offer = cursor.fetchall()

full_offer_list = []
for row in cursor.execute('SELECT number_offer, vacancy, region, skill FROM full_offer ORDER BY number_offer'):
    full_offer_list.append(row)

print(full_offer_list)
print(type(full_offer_list[1][3]))

#
# print(skills)
# #
# print(vacancy)
# #
# print(number_offer)


# print(region)
# print(type(region))

# engine = create_engine('sqlite:///orm.sqlite', echo=True)
#
# Base = declarative_base()
#
#
# class Region(Base):
#     __tablename__ = 'region'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     number = Column(Integer, nullable=True)
#
#
#     def __init__(self, name, number):
#         self.name = name
#         self.number = number
#
#     def __str__(self):
#         return f'{self.id}) {self.name}: {self.number}'
#
#
#
#
# Base.metadata.create_all(engine)
#
# Session = sessionmaker(bind=engine)
#
# session = Session()
#
# region = Region('Москва', 1)
#
# session.add(region)
#
# region = Region('Петербург', 2)
#
# session.add(region)
#
# session.commit()
#
# region.name = 'Тула'
#
# session.commit()
#
# session.delete(region)
#
# session.commit()
#
# for i in range(10):
#     region = Region(f'region{i}', i)
#     session.add(region)
#
# session.commit()
#
# region_query = session.query(Region)
#
# print(type(region_query))
#
# for region in region_query:
#     print(region.name)
#
# regions = session.query(Region).all()
#
# print(type(regions))
#
# regions = session.query(Region).filter(Region.name == 'Москва' and Region.id > 14).all()
