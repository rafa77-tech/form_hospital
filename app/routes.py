from flask import render_template, request, flash, redirect, url_for
from app import app, hospitals_data
from app.utils import get_pending_hospitals, save_hospital_data
import pandas as pd


@app.route('/')
def index():
    pending_hospitals = get_pending_hospitals(hospitals_data)
    return render_template('index.html', hospitals=pending_hospitals)

@app.route('/formulario/<hospital_id>', methods=['GET', 'POST'])
def formulario(hospital_id):
    if request.method == 'POST':
        required_fields = [
            'EMPRESA_RESP_PSA', 'EMPRESA_RESP_PSI',
            'EMPRESA_RESP_UTIA', 'EMPRESA_RESP_UTIPED',
            'EMPRESA_RESP_ANESTESIA',
            'EMPRESA_RESP_UIA', 'EMPRESA_RESP_UIP'
        ]
        
        form_data = request.form.to_dict()
        missing_fields = [field for field in required_fields 
                         if not form_data.get(field)]
        
        if missing_fields:
            flash('Por favor, preencha todos os campos obrigatórios!', 'danger')
            return render_template('formulario.html', 
                                hospital=hospitals_data[hospital_id],
                                missing_fields=missing_fields)
        
        try:
            hospitals_data[hospital_id].update(form_data)
            save_hospital_data(hospitals_data)
            flash('Dados do hospital atualizados com sucesso!', 'success')
            return redirect(url_for('index'))
            
        except Exception as e:
            flash(f'Erro ao salvar os dados: {str(e)}', 'danger')
            return render_template('formulario.html', 
                                hospital=hospitals_data[hospital_id])
    
    hospital = hospitals_data.get(hospital_id)
    if not hospital:
        flash('Hospital não encontrado!', 'danger')
        return redirect(url_for('index'))
    
    return render_template('formulario.html', hospital=hospital)