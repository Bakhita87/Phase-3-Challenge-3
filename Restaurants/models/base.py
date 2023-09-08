# parent class of the object relational mapping
# purpose is to provide a common set of functionality and attributes amongst the ORM model classes
# They inherit
  # Mapping of db columns to class attributes,creation of database tables and handling sessions.
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()