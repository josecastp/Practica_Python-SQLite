import sqlite3

def crea_bd_personal():

    conexion = sqlite3.connect('practica.db')
    
    # Creamos el cursor
    cursor = conexion.cursor()
    
    # Ahora crearemos una tabla de usuarios con nombres, edades y emails
    sql = "CREATE TABLE IF NOT EXISTS personal (dni CHAR(10), nom VARCHAR(50), " 
    sql += "cognom1 VARCHAR(50),cognom2 VARCHAR(50), correu VARCHAR(100), telefon VARCHAR(30),  "
    sql += "codipostal CHAR(5))"
    cursor.execute(sql)
    
    # Guardamos los cambios haciendo un commit
    conexion.commit()
    print("commit de crea_bd:personal")
    
    conexion.close()
    
def crea_personal(lista_personas):

    conexion = sqlite3.connect('practica.db')
    cursor = conexion.cursor()
    
    # Creamos una lista con varios usuarios (dni, nom, cognom1,congom2, correu, telf, codipostal)
# =============================================================================
#    personal = [('1946-2006','Mario', 'Benedetti', 'Farugia', 'mario@ejemplo.com', '+55 677 890', '08021'), \
#                 ('46227542-A', 'Marta', 'Artigas', 'Font', '5589@telefonica.es', '678553312', '08005'),\
#                 ('37128934-J','Joan', 'Artigas', 'Piqué', 'joan@dosnoms.cat', '933192211', '08003')]
#     
# =============================================================================
    # Ahora utilizamos el método executemany() para insertar varios
    cursor.executemany("INSERT INTO personal VALUES (?,?,?,?,?,?,?,?,?)", lista_personas)
    
    # Guardamos los cambios haciendo un commit
    conexion.commit()

    conexion.close()
    
def consulta_personal() :
    
    conexion = sqlite3.connect('practica.db')
    cursor = conexion.cursor()
    
    # Recuperamos los registros de la tabla de usuarios
    cursor.execute("SELECT * FROM personal")
    
    # Recorremos todos los registros con fetchall
    # y los volcamos en una lista de usuarios
    personal = cursor.fetchall()
    conexion.close()
    return (personal)

def añadir_campos():
    print("abrimos añadir_campos")
    conexion = sqlite3.connect('practica.db')
    # Creamos el cursor
    cursor = conexion.cursor()

    # Ahora añadimos en la tabla personal los campos direccion y poblacion
    #♠alter= "ALTER TABLE personal ADD direccion VARCHAR(80), ADD poblacion VARCHAR(60)"
    cursor.execute("ALTER TABLE personal ADD direccion VARCHAR(90)")
    cursor.execute("ALTER TABLE personal ADD poblacion VARCHAR(60)")
    #cursor.execute(alter)

    # Guardamos los cambios haciendo un commit
    conexion.commit()

    conexion.close()
  
    #si ejecuto este mismo fichero "bdatos.py" la variable __name__ es igual a __main__ 
    #si ejecuto "form_personal" el atributo __name__ pasa a contener el nombre del archivo en si: "form_personal"         
if __name__ == '__main__':
    crea_bd_personal()
    print("Ejecutado crea_bd_personal")
    añadir_campos()
    print("Ejecutado añadir_campos")
   