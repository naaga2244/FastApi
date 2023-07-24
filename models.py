from database import Base
from sqlalchemy import String,Integer,Column

class Employee(Base):
    __tablename__='employees'
    id=Column(Integer,primary_key=True)
    name=Column(String(255),nullable=False,unique=True)
    age=Column(Integer)

    def __repr__(self):
        return f"<Employee name={self.name} age={self.age}"