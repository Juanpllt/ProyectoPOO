import psycopg2
import sys
sys.path.append("../")

from persistencia.Conexion import Conexion

class ControladorGeneralPersistencia:
    
    conexion = Conexion("localhost", 5432, "postgres", "Jpllt123", "Esteganografia")
    conexionExitosa = conexion.conectar()
    
    def recuperarContrasena(self):
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
        
    
    def consultarUsuarios(self):
        try:
            with self.conexionExitosa.cursor() as cursor:
                cursor.execute("SELECT * FROM usuario;")
                usuarios = cursor.fetchall()
                return usuarios
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)
