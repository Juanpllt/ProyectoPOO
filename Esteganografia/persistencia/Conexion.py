import psycopg2

class Conexion:
    def __init__(self, url, port, user, password, database):
        self._url = url
        self._port = port
        self._user = user
        self._password = password
        self._database = database
        
    @property
    def url(self):
        return self._url
    @url.setter
    def url(self, url):
        self._url = url
    
    @property
    def port(self):
        return self._port
    @port.setter
    def port(self, port):
        self._port= port
        
    @property
    def user(self):
        return self._user
    @user.setter
    def user(self, user):
        self._user = user
        
    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, password):
        self._password = password
    
    @property
    def database(self):
        return self._database
    @database.setter
    def database(self, database):
        self._database = database
    
    
    def conectar(self):
        try:
            credenciales = {
                'dbname': self._database,
                'user' : self._user,
                'password' : self._password,
                'host' : self._url,  # Solo el nombre del host o la dirección IP
                'port' : self._port          
            }
            conexion = psycopg2.connect(**credenciales)
            if conexion:
                print("Conexión exitosa:", conexion)
            return conexion
        except Exception as e:
            print("Ha ocurrido un error en la conexión:", e)

# Corrige la URL del host aquí:
conexion = Conexion("bubble.db.elephantsql.com", 5432, "kjvgttho", "ltm-xd9v1tZRvF2CwG_1zFX93xnfij6H", "kjvgttho")
conexion.conectar()
