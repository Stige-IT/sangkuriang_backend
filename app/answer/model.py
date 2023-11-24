from sqlalchemy import Column, String, Boolean, ForeignKey

from core.database import Base


class Answer(Base):
    __tablename__ = "answer"
    id = Column(String(100), primary_key=True, autoincrement=False)
    id_voter = Column(String(100),ForeignKey('voter.id'), nullable=False)
    q1 = Column(Boolean)
    q2 = Column(Boolean)
    q3 = Column(Boolean)
    q4 = Column(Boolean)
    q5 = Column(Boolean)
    q6 = Column(Boolean)