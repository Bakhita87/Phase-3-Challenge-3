
from os import name
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.customer import Customer
from models.restaurant import Restaurant
from models.review import Review
from models.base import Base

import sys
DATABASE_URI='sqlite:///restaurant.db'
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(bind=engine)


customer1 = session.query(Customer).filter_by(first_name="Mary").first()
if not customer1:
    customer1 = Customer(first_name="Mary", last_name="Wendy")


restaurant1=session.query(Restaurant).filter_by(name="Botanica").first()
if not restaurant1 :
    restaurant1 = Restaurant(name="Botanica", price=8)

review1=Review(rating=8,restaurant=restaurant1,customer=customer1)
session.add(review1)


customer1.review.append(review1)


if customer1 not in session:
 session.add(customer1)

if restaurant1 not in session:
 session.add(restaurant1)      

session.commit()


session.close()