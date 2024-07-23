from utils.database import Base
from sqlalchemy import Column, String, DATE, Integer


class Tokens(Base):
    __tablename__ = 'tokens'

    id = Column(Integer, primary_key=True, autoincrement=True)
    token = Column(String(500), nullable=False)
    date = Column(DATE, name='issueDate', nullable=False)

    def __init__(self, date, token, user):
        self.token = token
        self.date = date

    def __repr__(self):
        return f'<tokens {self.id!r}>'
