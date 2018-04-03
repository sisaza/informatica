pi = 3.14159 

def area_circ(radio):
    '''Recibe un float o int,
    retorna el área (float o int) de un círculo con ese radio'''
    return pi*(radio**2) 

def perim_circ(radio):
    '''Recibe un float o int,
    retorna el perímetro (float o int) de un círculo con ese radio'''
    return 2*pi*radio 

def area_esf(radio):
    '''Recibe un float o int,
    retorna el área (float o int) de una esfera con ese radio'''
    return 4*pi*(radio**2) 

def vol_esf(radio):
    '''Recibe un float o int,
    retorna el volumen (float o int) de una esfera con ese radio''' 
    return (4/3)*pi*(radio**3)
