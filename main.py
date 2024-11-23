from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('inicio.html')  # Renderiza el archivo HTML desde la carpeta templates

@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        fecha_inicio = request.form.get('fecha_inicio')
        fecha_fin = request.form.get('fecha_fin')
        recordar_cada = request.form.get('recordar_cada')
        descirpcion = request.form.get('descripcion')
        return render_template('llenado.html')
    return render_template('agregar.html')

@app.route('/ver')
def ver():
    return render_template("ver.html")

@app.route('/editar')
def editar():
    return render_template('editar.html')

@app.route('/editar/modificar')
def nuevo_elemento():
    return render_template('modificar.html')


if __name__ == '__main__':
    app.run(debug=True)