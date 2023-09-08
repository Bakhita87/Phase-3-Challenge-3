from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.review import Review
from .base import Base

class Restaurant(Base):
    __tablename__ ='Restaurants'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    review = relationship('Review', back_populates='restaurant')
   
def _init_(self, name, price):
        self.name = name
        self.price = price
def reviews(self):
        return self.reviews

def customer(self):
        return self.customer