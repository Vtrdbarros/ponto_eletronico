from datetime import datetime
from .models import SessionLocal, Empregado, RegistroPonto

def registrar_ponto(pis, tipo):
    session = SessionLocal()
    empregado = session.query(Empregado).filter(Empregado.pis == pis).first()
    if empregado:
        registro = RegistroPonto(empregado_id=empregado.id, data_hora=datetime.now(), tipo=tipo)
        session.add(registro)
        session.commit()
        session.close()
        return f"Ponto registrado para {empregado.nome} às {registro.data_hora}"
    session.close()
    return "Empregado não encontrado"

def listar_pontos():
    session = SessionLocal()
    registros = session.query(RegistroPonto).all()
    result = []
    for registro in registros:
        empregado = session.query(Empregado).filter(Empregado.id == registro.empregado_id).first()
        result.append({
            'nome': empregado.nome,
            'data_hora': registro.data_hora,
            'tipo': registro.tipo
        })
    session.close()
    return result
