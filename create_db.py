from database import Base,engine
from models import Employee

print("Creating database.........")

Base.metadata.create_all(engine)