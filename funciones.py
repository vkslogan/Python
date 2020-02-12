def describe_city(city, country = 'rusia'):
    """Display information about a country ."""
    print("\nviajaremos a " + country.title() + ".")
    print("y visitaremos " + city + ".")
describe_city(city='monaco')
    
def describe_city2(city, country, continent='EUROPE'):
    """Display information about a contint europe ."""
    print("\nrecorreremos " + continent + ".")
    print("y visitaremos " + country + ' para surfear en ' + city + ".")
describe_city2(city='marbella', country='SPAIN')
'''    
T-Shirt: Elabora un funcion llamada make_shirt() que acepte el tamano y el texto
que se imprimira en la playera. La funcion debera de imprimir el tamano y el texto
que se han enviado a la funcion
'''
def make_shirt(font_size, text):
    """Display information about a shirt."""
    print('tendra estas caracteristicas tu playera texto: ' + text + ' con el tamaño de letra ' + font_size + '.')
make_shirt(font_size= input('Introduce el tamaño de la letra: '), text= input('introduce el texto que aparecera en tu playera'))
    
'''
Playeras Grandes: Modifique la funcion make_shirt() de tal manera que el tamano
por default sea grande y el texto predefinido sea I <3 Python. Genere una playera
grande y mediana con el mensaje predeterminado, y genere una playera peque˜na con
un mensaje diferente.
'''
def make_shirt2(font_size='GDE', text='I <3 pyton'):
    """Display information about a shirt."""
    print( 'Vuestra playera esta lista' + font_size +'.' + text + '.')
make_shirt2()
    




