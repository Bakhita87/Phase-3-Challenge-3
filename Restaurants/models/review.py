from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
class Review(Base):
    __tablename__ ='Reviews'
    id = Column(Integer, primary_key=True)
    rating = Column(Integer)
    customer_id = Column(Integer, ForeignKey('Customers.id'))
    restaurant_id = Column(Integer, ForeignKey('Restaurants.id'))
    restaurant = relationship('Restaurant', back_populates='review')
    customer = relationship('Customer', back_populates='review')

    def _init_(self, rating, customer, restaurant):
        self.rating = rating
        self.customer= customer
        self.restaurant = restaurant

    def restaurant_instance(self):
        return self.restaurant
    
    def customer_instance(self):
        return self.customer

    