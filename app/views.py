from flask import Blueprint, render_template, request, redirect, url_for, flash
from .controllers import registrar_ponto, listar_pontos

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/registrar', methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        pis = request.form['pis']
        tipo = request.form['tipo']
        resultado = registrar_ponto(pis, tipo)
        flash(resultado)
        return redirect(url_for('main.registrar'))
    return render_template('registrar.html')

@bp.route('/pontos')
def pontos():
    registros = listar_pontos()
    return render_template('pontos.html', registros=registros)
