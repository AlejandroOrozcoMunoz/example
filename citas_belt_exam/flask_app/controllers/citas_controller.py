from flask import render_template, redirect, session, request
from flask_app import app

from flask_app.models.users import User
from flask_app.models.citas import Cita


@app.route('/nueva/cita')
def nueva_cita():
    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesión
        return redirect('/')

    formulario = {
        'id': session['user_id']
    }

    user = User.get_by_id(formulario) #Instancia del usuario que inicio sesión

    return render_template('nueva_cita.html', user=user)

@app.route('/crear/cita', methods=['POST'])
def crear_cita():
    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesión
        return redirect('/')

    if not Cita.valida_tarea(request.form): 
        return redirect('/nueva/cita')

    Cita.save(request.form)

    return redirect('/dashboard')

@app.route('/editar/cita/<int:id>')
def editar_cita(id):
    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesiónh
        return redirect('/')

    formulario = {
        'id': session['user_id']
    }

    user = User.get_by_id(formulario) 
    
    formulario_cita = {"id": id}
    cita = Cita.get_by_id(formulario_cita)
    
    return render_template('editar_cita.html', user=user, cita=cita)

@app.route('/update/cita', methods=['POST'])
def update_cita():
    if 'user_id' not in session:
        return redirect('/')
    if not Cita.valida_tarea(request.form):
        return redirect('/editar/cita/' + request.form['id'])
    
    Cita.update(request.form)
    return redirect('/dashboard')

@app.route('/delete/cita/<int:id>')
def delete_cita(id):
    if 'user_id' not in session:  
        return redirect('/')
    
    formulario = {"id": id}
    Cita.delete(formulario)

    return redirect('/dashboard')

