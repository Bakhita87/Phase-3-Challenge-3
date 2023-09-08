from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.restaurant import Restaurant
from models.review import Review
from .base import Base
class Customer(Base):
    __tablename__ = 'Customers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    review = relationship('Review', back_populates='customer')
    

    def _init_(self, first_name,last_name):
     self.first_name = first_name
     self.last_name = last_name
 

    def reviews(self):
        return self.reviews

    def restaurants(self):
        return self.restaurants

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    
    def add_review(self, restaurant, rating):
      review1 = Review(customer=self,restaurant=restaurant,rating=rating)
      self.review.append(review1)
     
    def favorite_restaurant(self):
        favs=[review.rating for review in self.review]
        return [review.restaurant for review in self.review if review.rating== max(favs)]
    

    def delete_reviews(self, restaurant, session):
        for review in self.reviews:
            if review.restaurant == restaurant:
                self.reviews.remove(review)
                session.delete(review)

        session.commit()           
 


    
    def _str_(self):
        return f"Customer(id={self.id}, name={self.name})"