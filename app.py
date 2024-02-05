from flask import render_template, request,session, redirect, url_for, flash
from conexion import app, db
from models import Ingresos, Egresos
from datetime import datetime

@app.route('/')
def index():
    # Obtén todas las cajas de ahorro
    return render_template('index.html')

# CRUD (Crear, Leer, Actualizar, Eliminar)

@app.route('/cargar_datos', methods = ['POST', 'GET'])
def cargar_datos():

    if request.method == 'POST':
        tipo = request.form['tipo']
        monto = request.form['monto']
        concepto = request.form['concepto']
        fecha_str = request.form['fecha']  # Recibes la cadena de texto de la fecha
        fecha = datetime.strptime(fecha_str, '%Y-%m-%d').date()  # Conviertes a objeto date
        descripcion = request.form['descripcion']
        

        if tipo == 'ingreso':

            ingresos = Ingresos(monto, concepto,fecha, descripcion)

            db.session.add(ingresos)
        else:

            egresos = Egresos(monto, concepto, fecha, descripcion)
            db.session.add(egresos)
        
        db.session.commit()
        
    
        return render_template('cargar_datos.html')

    return render_template('cargar_datos.html')



@app.route('/mostrar_datos', methods = ['GET', 'POST'])

def mostrar_datos():  
    lista_ingresos = Ingresos.query.all()
    lista_egresos = Egresos.query.all()
    return render_template('mostrar_datos.html', lista_ingresos=lista_ingresos, lista_egresos=lista_egresos)
    

            
@app.route('/actualizar-ingreso/<int:id>', methods=['GET','POST'])
def actualizar_ingreso(id):
    dato_a_actualizar = Ingresos.query.get_or_404(id)

    if request.method == 'POST':
        monto = request.form['monto']
        concepto = request.form['concepto']
        if len(concepto) > 20:
            flash('El concepto no puede exceder los 20 caracteres', 'error')
            return render_template("actualizar_ingreso.html", dato_a_actualizar=dato_a_actualizar)
        fecha_str = request.form['fecha']  # Recibes la cadena de texto de la fecha
        fecha = datetime.strptime(fecha_str, '%Y-%m-%d').date()  # Conviertes a objeto date
        descripcion = request.form['descripcion']



        dato_a_actualizar.monto = monto
        dato_a_actualizar.concepto = concepto
        dato_a_actualizar.fecha = fecha
        dato_a_actualizar.descripcion = descripcion

        db.session.commit()

        return redirect(url_for('mostrar_datos'))
    
    return render_template("actualizar_ingreso.html", dato_a_actualizar=dato_a_actualizar)


@app.route('/actualizar-egreso/<int:id>', methods=['GET','POST'])
def actualizar_egreso(id):
    dato_a_actualizar = Egresos.query.get_or_404(id)

    if request.method == 'POST':
        monto = request.form['monto']
        concepto = request.form['concepto']
        if len(concepto) > 20:
            flash('El concepto no puede exceder los 20 caracteres', 'error')
            return render_template("actualizar_ingreso.html", dato_a_actualizar=dato_a_actualizar)
        fecha_str = request.form['fecha']  # Recibes la cadena de texto de la fecha
        fecha = datetime.strptime(fecha_str, '%Y-%m-%d').date()  # Conviertes a objeto date
        descripcion = request.form['descripcion']



        dato_a_actualizar.monto = monto
        dato_a_actualizar.concepto = concepto
        dato_a_actualizar.fecha = fecha
        dato_a_actualizar.descripcion = descripcion

        db.session.commit()

        return redirect(url_for('mostrar_datos'))
    
    return render_template("actualizar_egreso.html", dato_a_actualizar=dato_a_actualizar)


@app.route('/eliminar_ingreso', methods = ['GET','POST'])
def eliminar_ingreso():
    if request.method == 'POST':
        id = request.form['ingreso_id']
        ingreso_a_eliminar = Ingresos.query.filter_by(id=id).first()

        db.session.delete(ingreso_a_eliminar)
        db.session.commit()

        return redirect(url_for('mostrar_datos'))
    
@app.route('/eliminar_egreso', methods = ['GET','POST'])
def eliminar_egreso():
    if request.method == 'POST':
        id = request.form['egreso_id']
        egreso_a_eliminar = Egresos.query.filter_by(id=id).first()

        db.session.delete(egreso_a_eliminar)
        db.session.commit()

        return redirect(url_for('mostrar_datos'))


@app.route('/balance')
def mostrar_balance():
    total_ingresos = db.session.query(db.func.sum(Ingresos.monto)).scalar() or 0
    total_egresos = db.session.query(db.func.sum(Egresos.monto)).scalar() or 0
    balance = total_ingresos - total_egresos
    return render_template('balance.html', total_ingresos=total_ingresos, total_egresos=total_egresos, balance=balance)




if __name__ == ("__main__"):
    app.run(debug = True, port=5000)
    