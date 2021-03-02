import sqlalchemy as alc
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Operation(Base):
	__tablename__ = 'operations'

	id = alc.Column(alc.Integer, primary_key=True)
	date = alc.Column(alc.Date)
	kind = alc.Column(alc.String)
	amount = alc.Column(alc.Numeric(10, 2))
	description = alc.Column(alc.String, nullable=True)