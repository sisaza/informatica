def area_cuad(lado):
    '''Recibe un float o int,
    retorna el área (float o int) de un cuadrado con ese lado'''  
    return lado*lado

def perim_cuad(lado): 
    '''Recibe un float o int,
    retorna el perímetro (float o int) de un cuadrado con ese lado'''  
    return 4*lado

def area_cubo(lado): 
    '''Recibe un float o int,
    retorna el área (float o int) de un cubo con ese lado'''  
    return 6*area_cuad(lado)

def vol_cubo(lado): 
    '''Recibe un float o int,
    retorna el volumen (float o int) de un cubo con ese lado'''  
    return lado*lado*lado
