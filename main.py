from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/')

#Página de inicio 
def home():
    return render_template('inicio.html')  # Renderiza el archivo HTML desde la carpeta templates

@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        # Datos del formulario
        nombre = request.form.get('nombre')
        fecha_inicio = request.form.get('fecha_inicio')
        fecha_fin = request.form.get('fecha_fin')
        recordar_cada = request.form.get('recordar_cada')
        descripcion = request.form.get('descripcion')

        # Agregar la nueva fila
        nueva_fila = [nombre, fecha_inicio, fecha_fin, recordar_cada, descripcion]

        with open('db.csv', mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(nueva_fila)

        # Mostrar la página de éxito
        return render_template('llenado.html')

    return render_template('agregar.html')


@app.route('/ver')
def ver():
    return render_template("ver.html")

@app.route('/editar')
def editar():
    #Lista con los nombres de pendientes
    tareas = []
    try:
        with open('db.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            tareas = list(reader)
    except FileNotFoundError:
        tareas = [] 

    return render_template('editar.html', tareas=tareas, enumerate=enumerate)


@app.route('/editar/modificar', methods=['GET', 'POST'])
def modificar():
    tareas = []
    try:
        with open('db.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            tareas = list(reader)
    except FileNotFoundError:
        return "No se encontraron datos para editar.", 404

    id = request.args.get('id', type=int)  # Obtener el índice seleccionado del formulario.

    if request.method == 'POST':
        # Actualizar los datos con los valores enviados por el formulario.
        tareas[id] = [
            request.form.get('nombre'),
            request.form.get('fecha_inicio'),
            request.form.get('fecha_fin'),
            request.form.get('recordar_cada'),
            request.form.get('descripcion')
        ]

        with open('db.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(tareas)

        return render_template('llenado.html')
    # Renderizar la página para modificar la tarea seleccionada.
    return render_template('modificar.html', tarea=tareas[id])



if __name__ == '__main__':
    app.run(debug=True)
