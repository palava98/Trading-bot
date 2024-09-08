from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class TradeLog(Base):
    __tablename__ = 'trades'
    id = Column(Integer, primary_key=True)
    symbol = Column(String)
    action = Column(String)
    volume = Column(Float)
    price = Column(Float)
    datetime = Column(DateTime, default=datetime.utcnow)

DATABASE_URL = "sqlite:///trading_bot.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def log_trade(symbol, action, volume, price):
    trade = TradeLog(symbol=symbol, action=action, volume=volume, price=price)
    session.add(trade)
    session.commit()

Base.metadata.create_all(engine)