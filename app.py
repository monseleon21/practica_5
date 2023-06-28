from flask import Flask,render_template,request,redirect,url_for
from flask_mysqldb import MySQL


#inicializacion del APP
app= Flask(__name__)

#Configuracion de la conexion
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='dbflask'
mysql= MySQL(app)

#declaracion de ruta http://localhost:5000
@app.route('/')
def index():
    CC= mysql.connection.cursor();
    CC.execute('select*from albums')
    conAlbums= CC.fetchall()
    print(conAlbums) #es para mostrar una tabla en vista con los registros
    return render_template('index.html', listAlbums = conAlbums)

#ruta http:localhost:5000/guardar tipo POST para Insert
@app.route('/guardar',methods=['POST'])
def guardar():
    if request.method == 'POST':

        # pasamos a variables el contenido de los input
        Vtitulo=request.form['txtTitulo']
        Vartista=request.form['txtArtista']
        Vanio=request.form['txtAnio']
        # print(titulo,artista,anio)

# conectar y ejecutar el insert

CS=mysql.connection.cursor()
CS.execute('insert into tbalbums(titulo,artista,anio) values(%s,%s,%s)',(Vtitulo,Vartista,Vanio))
mysql.connection.commit()

return redirect(url_for'index')

@app.route('/eliminar')
def eliminar():
    return "Se elimino en la base de datos"


#ejecucion del servidor en el puerto 5000
if __name__ == '__main__':
    app.run(port=5000,debug=True)