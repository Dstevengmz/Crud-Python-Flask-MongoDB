class Producto:
    def __init__(self,codigo,nombre,precio,categoria,foto):
        self.codigo=codigo
        self.nombre=nombre
        self.precio=precio
        self.categoria=categoria
        self.foto=foto

    def ConexionDB(self):
        return {
            'codigo':self.codigo,
            'nombre':self.nombre,
            'precio':self.precio,
            'categoria':self.categoria,
            'foto':self.foto
        }
    
    
    
    