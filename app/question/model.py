from sqlalchemy import Column, String

from core.database import Base


class Question(Base):
    __tablename__ = "question"
    id = Column(String(100), primary_key=True, autoincrement=False)
    id_volunteer = Column(String(100), nullable=False)
    question1 = Column(String(100), nullable=False)
    question2 = Column(String(100), nullable=False)
    question3 = Column(String(100), nullable=False)
    question4 = Column(String(100), nullable=False)
    question5 = Column(String(100), nullable=False)
    question6 = Column(String(100), nullable=False)
