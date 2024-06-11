import psycopg2
import sys
sys.path.append("../")

from persistencia.Conexion import Conexion

class ControladorAdminPersistencia:
    
    conexion = Conexion("localhost", 5432, "postgres", "Jpllt123", "Esteganografia")
    conexionExitosa = conexion.conectar()
    
    def __init__(self) -> None:
        pass
    
    
    
    def crearUsuario(self, nombre, correo, nombreUsuario, rol, documento, contrasena):
        try:
            with self.conexionExitosa.cursor() as cursor:
                consulta = f'INSERT INTO usuario(nombre, correo, '+'"nombreUsuario"'+', rol, documento, contrasena) VALUES (%s, %s, %s, %s, %s, %s);'
                cursor.execute(consulta, (nombre, correo, nombreUsuario, rol, documento, contrasena))
            self.conexionExitosa.commit()
            print("Usuario Exitoso")
            return True 
        except psycopg2.Error as e:
            print("Ocurrió un error al crear el usuario: ", e)
            return False
        
    def consultarUsuario(self, nombreUsuario, contrasena):
        try:
            with self.conexionExitosa.cursor() as cursor:
                cursor.execute(f"SELECT * FROM usuario WHERE "+'"nombreUsuario"'+" = '"+nombreUsuario+"' and contrasena = '"+contrasena+"';")
                usuario = cursor.fetchone()
                if usuario:
                    print(usuario)
                    return usuario
                else:
                    print("El usuario no existe")
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)

    def consultarIdUsuario(self, id):
        try:
            with self.conexionExitosa.cursor() as cursor:
                cursor.execute("SELECT * FROM usuario WHERE id='"+str(id)+"';")
                usuario = cursor.fetchone()
                if usuario:
                    print(usuario)
                else:
                    print("El usuario no existe")
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)
    
    def consultarNombreUsuario(self, nombreUsuario):
        try:
            with self.conexionExitosa.cursor() as cursor:
                cursor.execute("SELECT * FROM usuario WHERE nombreUsuario='"+str(nombreUsuario)+"';")
                usuario = cursor.fetchall()
                if usuario:
                    print(usuario)
                else:
                    print("El usuario no existe")
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)

    def consultarUsuarios(self):
        try:
            with self.conexionExitosa.cursor() as cursor:
                cursor.execute("SELECT * FROM usuario;")
                usuarios = cursor.fetchall()
                return usuarios
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)

    def actualizarNombre(self, nombre, nombreUsuario):
        try:
            with self.conexionExitosa.cursor() as cursor:
                consulta = "UPDATE usuarios SET nombre = '" + str(nombre) + "' WHERE nombreUsuario = '"+str(nombreUsuario)+"';"
                cursor.execute(consulta)
            self.conexionExitosa.commit()
            print("El registro se actualizo con exito")
        except psycopg2.Error as e:
            print("Ocurrió un error al editar: ", e)
            
    def actualizarContrasena(self, contrasena, nombreUsuario):
        try:
            with self.conexionExitosa.cursor() as cursor:
                consulta = "UPDATE usuarios SET contrasena = '" + str(contrasena) + "' WHERE nombreUsuario = '"+str(nombreUsuario)+"';"
                cursor.execute(consulta)
            self.conexionExitosa.commit()
            print("El registro se actualizo con exito")
        except psycopg2.Error as e:
            print("Ocurrió un error al editar: ", e)

    def eliminarUsuario(self, id):
        try:
            with self.conexionExitosa.cursor() as cursor:
                consulta = "DELETE FROM usuario WHERE id =" + str(id)
                cursor.execute(consulta)
                print("Usuario eliminado con exito")
            self.conexionExitosa.commit()
        except psycopg2.Error as e:
            print("Error eliminando: ", e)
            