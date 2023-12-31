import sqlite3

class BaseDeDatos:
    def __init__(self):
        self.conn = sqlite3.connect('ventas.db')
        self.cursor = self.conn.cursor()
    
    def inicializar_base_de_datos(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS ventas (
            id TEXT PRIMARY KEY,
            producto TEXT NOT NULL,
            cantidad INTEGER NOT NULL,
            unidad TEXT NOT NULL,
            precio_unitario REAL NOT NULL,
            fecha TIMESTAMP NOT NULL
        )
        ''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS compras (
            id TEXT PRIMARY KEY ,
            proveedor TEXT NOT NULL,
            producto TEXT NOT NULL,
            cantidad INTEGER NOT NULL,
            unidad TEXT NOT NULL,
            precio_unitario REAL NOT NULL,
            fecha TIMESTAMP NOT NULL
        )
        ''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS almacen (
            id_producto TEXT PRIMARY KEY,
            producto TEXT NOT NULL,
            cantidad INTEGER NOT NULL,
            unidad TEXT NOT NULL,
            precio_unitario REAL NOT NULL,
            proveedor TEXT NOT NULL
        )
        ''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        
        self.conn.commit()        

    def registrar_usuario(self, username, password):
        self.cursor.execute("INSERT INTO usuarios (username, password) VALUES (?, ?)", (username, password))
        self.conn.commit()

    def autenticar_usuario(self, username, password):
        self.cursor.execute("SELECT * FROM usuarios WHERE username = ? AND password = ?", (username, password))
        usuario = self.cursor.fetchone()
        return usuario
    
    def generar_id_unico(self):
        self.cursor.execute('SELECT COUNT(*) FROM almacen')
        ultimo_registro = self.cursor.fetchone()[0]
        nuevo_id = f'DJ001P00{ultimo_registro + 1:03d}'
        return nuevo_id

    def generar_id_unico_ventas(self):
        self.cursor.execute('SELECT COUNT(*) FROM ventas')
        ultimo_registro_ventas = self.cursor.fetchone()[0]
        nuevo_id_venta = f'VDJ001P00{ultimo_registro_ventas + 1:03d}'
        return nuevo_id_venta

    def __del__(self):
        self.conn.close()
