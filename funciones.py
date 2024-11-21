from flask import Flask, render_template, request

def agregar():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        fecha_inicio = request.form.get('fecha_inicio')
        fecha_fin = request.form.get('fecha_fin')
        recordar_cada = request.form.get('recordar_cada')
        descirpcion = request.form.get('descripcion')
    return render_template('agregar.html')