class Catalogo:
    productos = [] # atriburto de clase
    
    def agregar_producto(self, codigo, descripcion, cantidad, precio, imagen, proveedor):
        if self.consultar_producto(codigo):
            return False
        
        nuevo_producto = { #diccionario de datos
            'codigo': codigo,
            'descripcion': descripcion,
            'cantidad': cantidad,
            'precio': precio,
            'imagen': imagen,
            'proveedor': proveedor,
        }
        self.productos.append(nuevo_producto)
        return True  
    
    def consultar_producto(self, codigo):
        for producto in self.productos:
            if producto['codigo'] == codigo: # si es igual lo encontro
                return producto
        return False 
    
    def listar_productos(self):
        print("_"*50)
        for producto in self.productos:
            print(f"codigo.......: {producto['codigo']}")
            print(f"descripcion..: {producto['descripcion']}")
            print(f"cantidad.....: {producto['cantidad']}")
            print(f"precio.......: {producto['precio']}")
            print(f"imagen.......: {producto['imagen']}")
            print(f"proveedor....: {producto['proveedor']}")
            print("_"*50)

    def modificar_producto(self, codigo, nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_imagen, nuevo_proveedor):
        for producto in self.productos:
            if producto['codigo'] == codigo:
                producto['descripcion'] = nueva_descripcion
                producto['cantidad'] = nueva_cantidad
                producto['precio'] = nuevo_precio
                producto['imagen'] = nueva_imagen
                producto['proveedor'] = nuevo_proveedor
                return True
            return False    
    def eliminar_producto(self, codigo):
        for producto in self.productos:
            if producto['codigo'] == codigo:
                self.productos.remove(producto)
                return True
        return False 

    def mostrar_producto(self, codigo):
        producto = self.consultar_producto(codigo) 
        if producto:
            print("_"*50)
            print(f"codigo.......: {producto['codigo']}")
            print(f"descripcion..: {producto['descripcion']}")
            print(f"cantidad.....: {producto['cantidad']}")
            print(f"precio.......: {producto['precio']}")
            print(f"imagen.......: {producto['imagen']}")
            print(f"proveedor....: {producto['proveedor']}")
            print("_"*50)


#programa principal

# Agregamos productos a la lista:
catalogo = Catalogo()
catalogo.agregar_producto(1, 'Teclado USB 101 teclas', 10, 4500, 'teclado.jpg',
101)
catalogo.agregar_producto(2, 'Mouse USB 3 botones', 5, 2500, 'mouse.jpg', 102)  

catalogo.mostrar_producto(2)

'''
print("lista de productos")
catalogo.listar_productos()

print("modoficando producto...")
catalogo.modificar_producto(1, 'Teclado USB 1114 teclas', 15, 3500000, 'tecladovvv.jpg',
101)

print("lista de productos")
catalogo.listar_productos()

catalogo.eliminar_producto(2)

print("lista de productos")
catalogo.listar_productos()


def agregar_producto(codigo, descripcion, cantidad, precio, imagen, proveedor):

    if consultar_producto(codigo):
        return False
    

    nuevo_producto = { #diccionario de datos
        'codigo': codigo,
        'descripcion': descripcion,
        'cantidad': cantidad,
        'precio': precio,
        'imagen': imagen,
        'proveedor': proveedor,
    }
    productos.append(nuevo_producto)
    return True

def consultar_producto(codigo):
    for producto in productos:
        if producto['codigo'] == codigo: # si es igual lo encontro
            return producto
    return False    

def listar_productos():
    print("_"*50)
    for producto in productos:
        print(f"codigo.......: {producto['codigo']}")
        print(f"descripcion..: {producto['descripcion']}")
        print(f"cantidad.....: {producto['cantidad']}")
        print(f"precio.......: {producto['precio']}")
        print(f"imagen.......: {producto['imagen']}")
        print(f"proveedor....: {producto['proveedor']}")
        print("_"*50)
        print()

def modificar_producto(codigo, nueva_descripcion,  nueva_cantidad,  nueva_precio,  nueva_imagen,  nueva_proveedor):
    for producto in productos:
        if producto['codigo'] == codigo:
            producto['descripcion'] = nueva_descripcion
            producto['cantidad'] = nueva_cantidad
            producto['precio'] = nueva_precio
            producto['imagen'] = nueva_imagen
            producto['proveedor'] = nueva_proveedor
            return True
    return False    


def eliminar_producto(codigo):
    for producto in productos:
        if producto['codigo'] == codigo:
             productos.remove(producto)
             return True
    return False    



#programa principal

#definimos una lista de productos (es una lista de diccionarios)

productos= []

# Agregamos productos a la lista:
agregar_producto(1, 'Teclado USB 101 teclas', 10, 4500, 'teclado.jpg',
101)
agregar_producto(2, 'Mouse USB 3 botones', 5, 2500, 'mouse.jpg', 102)
agregar_producto(3, 'Monitor LCD 22 pulgadas', 15, 52500,
'monitor22.jpg', 103)
agregar_producto(4, 'Monitor LCD 27 pulgadas', 25, 78500,
'monitor27.jpg', 104)
agregar_producto(5, 'Pad mouse', 5, 500, 'padmouse.jpg', 105)
#print(productos)
listar_productos()

#consultamos producto...
#cod_prod = int(input("ingrese el codigo del producto: "))
#producto = consultar_producto (cod_prod)
#if producto:
#    print(f"producto encontrado {producto['codigo']} - {producto['descripcion']}")
#else:
#    print (f'producto {cod_prod} no encontrado.')

# modificando un producto...

#modificar_producto(1, 'Teclado mecanico 62 teclas', 20, 36500, 'tecladomecanico.jpg',
#106)

# eliminar producto...

eliminar_producto(2)
eliminar_producto(55)

listar_productos()

'''