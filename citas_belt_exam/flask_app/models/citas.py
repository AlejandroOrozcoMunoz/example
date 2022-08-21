from flask_app.config.mysqlconnection import  connectToMySQL

from flask import flash

class Cita:

    def __init__(self, data):
        self.id = data['id']
        self.tasks = data['tasks']
        self.date_made = data['date_made']
        self.status = data['status']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.first_name = data['first_name']

    @staticmethod
    def valida_tarea(formulario):
        es_valido = True

        if len(formulario['tasks']) < 3:
            flash('La tarea debe de tener mas de 3 caracteres', 'appointment')
            es_valido = False

        if formulario['date_made'] == "":
            flash('Ingrese una fecha', 'appointment')
            es_valido = False
    
        return es_valido

    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO appointments (tasks,date_made, status, user_id) VALUES (%(tasks)s, %(date_made)s, %(status)s, %(user_id)s)"
        result = connectToMySQL('citas').query_db(query, formulario)
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT appointments.*, first_name  FROM citas.appointments LEFT JOIN users ON users.id = appointments.user_id;"
        results = connectToMySQL('citas').query_db(query) #Lista de diccionarios 
        cita = []
        for Cita in results:
            #recipe = diccionario
            cita.append(cls(Cita)) #1.- cls(recipe) me crea una instancia en base al diccionario, 2.- Agrego la instancia a mi lista de recetas
    
        return cita
    
    @classmethod
    def get_by_id(cls,formulario):
        query = "SELECT appointments.*, first_name  FROM citas.appointments LEFT JOIN users ON users.id = appointments.user_id WHERE appointments.id = %(id)s;"
        result = connectToMySQL('citas').query_db(query, formulario)
        cita = cls(result[0])
        return cita
    
    @classmethod
    def update(cls, formulario):
        query = "UPDATE citas.appointments SET tasks=%(tasks)s, date_made=%(date_made)s, status=%(status)s, user_id=%(user_id)s WHERE appointments.id = %(id)s"
        result = connectToMySQL('citas').query_db(query, formulario)
        return result
    
    @classmethod
    def delete(cls, formulario): #borrar
        query = "DELETE FROM citas.appointments WHERE id = %(id)s"
        result = connectToMySQL('citas').query_db(query, formulario)
        return result