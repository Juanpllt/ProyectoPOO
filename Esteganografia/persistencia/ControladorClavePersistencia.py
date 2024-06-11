import psycopg2
import sys
sys.path.append("../")
from persistencia.Conexion import Conexion
import datetime


class ControladorClavePersistencia():
    
    conexion = Conexion("localhost", 5432, "postgres", "Jpllt123", "Esteganografia")
    conexionExitosa = conexion.conectar()
    
    def verClave(self):
        try:
            with self.conexionExitosa.cursor() as cursor:
                cursor.execute("SELECT * FROM "+'"claveEsteganografia"'+";")
                clave = cursor.fetchone()
                if clave:
                    print(clave)
                else:
                    print("No hay clave")
            return clave
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)
    
    def cambiarClave(self, clave, id=1):
        try:
            with self.conexionExitosa.cursor() as cursor:
                consulta = ("UPDATE "+'"claveEsteganografia"'+" set clave=%s WHERE id =%s ;")
                cursor.execute(consulta, (clave, id))
            self.conexionExitosa.commit()
            print("Se ha hecho el update")
        except psycopg2.Error as e:
            print("Ocurrió un error al hacer el update", e)
    
    def ingresarClave(self, clave, id=1):
        try:
            with self.conexionExitosa.cursor() as cursor:
                consulta = ("INSERT INTO "+'"claveEsteganografia"'+"(id, clave) VALUES (%s, %s);")
                cursor.execute(consulta, (id, str(clave)))
                
            self.conexionExitosa.commit()
        except psycopg2.Error as e:
            print("Ocurrió un error al hacer el update", e)
            
    def eliminarClave(self, id=1):
        try:
            with self.conexionExitosa.cursor() as cursor:
                consulta = ("DELETE FROM "+'"claveEsteganografia"'+" WHERE id = %s;")
                cursor.execute(consulta, (id,))
            self.conexionExitosa.commit()
            print("Se ha borrado la clave")
        except psycopg2.Error as e:
            print("Ocurrió un error al hacer el update", e)
    
    def crearUsoSoftware(self, idUsuario):
        try:
            with self.conexionExitosa.cursor() as cursor:
                consulta = ("INSERT INTO public."+'"usoSoftware"'+" ( "+'"idUsuario"'+", fecha) VALUES (%s, %s);")
                fecha = datetime.datetime.now().strftime("%Y/%m/%d")
                
                cursor.execute(consulta, (idUsuario, fecha))
            self.conexionExitosa.commit()
        except psycopg2.Error as e:
            print("Ocurrió un error al hacer la consulta", e)
            
    def consultarUsoSoftware(self):
        try:
            with self.conexionExitosa.cursor() as cursor:
                consulta = ("SELECT * FROM public."+'"usoSoftware"'+";")
                cursor.execute(consulta)
                
                usos = cursor.fetchall()
                return usos
                
        except psycopg2.Error as e:
            print("Ocurrió un error al hacer la consulta", e)
            
            
    def hacerEsteganografia(self, idUsuario, rutaImagen1, rutaImagen2, rutaTexto):
        try:
            with self.conexionExitosa.cursor() as cursor:
                consulta = ("INSERT INTO public.esteganografia ("+'"rutaImagen1"'+", rutaimagen2,"+' "rutaTexto"'+", "+'"idUsuario"'+") VALUES (%s, %s, %s, %s);")
                cursor.execute(consulta, (rutaImagen1,rutaImagen2, rutaTexto, idUsuario))
            self.conexionExitosa.commit()
        except psycopg2.Error as e:
            print("Ocurrió un error al hacer el update", e)
            
    def consultarEsteganografia(self):
        try:
            with self.conexionExitosa.cursor() as cursor:
                consulta = ("SELECT * FROM public."+'"esteganografia"'+";")
                cursor.execute(consulta)
                
                esteganografia = cursor.fetchall()
                return esteganografia
        except psycopg2.Error as e:
            print("Ocurrió un error al hacer el update", e)
    
    


