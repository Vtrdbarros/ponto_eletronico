from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Empregado(Base):
    __tablename__ = 'empregados'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    pis = Column(String, unique=True, nullable=False)

class RegistroPonto(Base):
    __tablename__ = 'registros_ponto'
    id = Column(Integer, primary_key=True)
    empregado_id = Column(Integer, nullable=False)
    data_hora = Column(DateTime, nullable=False)
    tipo = Column(String, nullable=False)

DATABASE_URL = "sqlite:///ponto_eletronico.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)
