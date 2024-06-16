import sys
import os
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app.models import SessionLocal, Empregado, RegistroPonto, init_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base

# Configuração do banco de dados de teste
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope='module')
def test_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope='function')
def session(test_db):
    connection = engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)
    yield session
    session.close()
    transaction.rollback()
    connection.close()

def test_create_empregado(session):
    empregado = Empregado(nome="João", pis="123456789")
    session.add(empregado)
    session.commit()
    result = session.query(Empregado).filter_by(pis="123456789").first()
    assert result.nome == "João"

def test_registrar_ponto(session):
    empregado = Empregado(nome="Maria", pis="987654321")
    session.add(empregado)
    session.commit()
    data_hora = datetime.strptime("2024-06-16 08:00:00", "%Y-%m-%d %H:%M:%S")
    registro = RegistroPonto(empregado_id=empregado.id, data_hora=data_hora, tipo="entrada")
    session.add(registro)
    session.commit()
    result = session.query(RegistroPonto).filter_by(empregado_id=empregado.id).first()
    assert result.tipo == "entrada"
