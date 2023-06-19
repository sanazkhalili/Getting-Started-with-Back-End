from database import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text, DECIMAL
import datetime


class User(Base):
    __tablename__="user"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(20), nullable=False, unique=True)
    email = Column(String(200), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    is_verified = Column(Boolean, default=False)
    join_data = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)

class Business(Base):
    __tablename__="business"
    id = Column(Integer, primary_key=True, index=True)
    business_name = Column(String(20), nullable=False, unique=True)
    city = Column(String(100), nullable=False, default="unspecified")
    region = Column(String(100), nullable=False, default="unspecified")
    business_description = Column(Text, nullable=True )
    logo = Column(String(200), nullable=False, default='default.jpg')
    owner = Column(Integer, ForeignKey('user.id'))


class Product(Base):
    __tablename__="product"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, index=True)
    category = Column(String(30), index=True)
    original_price = Column(DECIMAL)
    percentag_discount = Column(Integer)
    offer_expiration_data = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    product_image = Column(String(200), nullable=False, default="product.jpg")
    business = Column(Integer, ForeignKey('business.id'))