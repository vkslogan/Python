
'''
Usuarios: Genere una clase llamada User con dos atributos first_name y last_name,
agregue mas atributos que se utilizan para cuentas de usuario. Desarrolle un metodo
describe_user() que imprima de manera ordenada y detallada la infomacion del
usuario. Genere un segundo atributo greet_user() que imprima un saludo personalido
para el usuario. Cree 10 usuarios y ejecute los dos metodos para cada usuario
'''

class User():
    """Clasequeayudaadescribirunperro"""
    def __init__(self, first_name, last_name):
        """Inicializa los atributos first name y last_name"""
        self.first_name = first_name
        self.last_name = last_name
    def describe_user(self):
        """Metodo que Describe a un usuario"""
        print('nombre completo es: ', self.first_name + self.last_name)
    def greet_user(self):
        """Saludo personalizado"""
        print(self.first_name.title() +" cuentame un chiste ")
    def genero(self):
        """Genero de la persona"""
        print('El generto de', self.first_name, 'es: Masculino')
    def genero_F(self):
        """Genero de la persona"""
        print('El generto de', self.first_name, 'es: Femenino')
    
usuario = User('edgar','Diaz')
print("El nombre del usuario es: "+ usuario.first_name.title() +".")
print("El apellido del usuario es: ", usuario.last_name)
usuario.first_name
usuario.describe_user()
usuario.greet_user()
usuario.genero()

usuario = User('miguel','Martinez')
print("El nombre del usuario es: "+ usuario.first_name.title() +".")
print("El apellido del usuario es: ", usuario.last_name)
usuario.first_name
usuario.describe_user()
usuario.greet_user()
usuario.genero()
#-----------------------------------------------------------

usuario = User('Dali','hernandez')
print("El nombre del usuario es: "+ usuario.first_name.title() +".")
print("El apellido del usuario es: ", usuario.last_name)
usuario.first_name
usuario.describe_user()
usuario.greet_user()
usuario.genero()
#------------------------------------------
usuario = User('Dali','hernandez')
print("El nombre del usuario es: "+ usuario.first_name.title() +".")
print("El apellido del usuario es: ", usuario.last_name)
usuario.first_name
usuario.describe_user()
usuario.greet_user()
usuario.genero()
#----------------------------------
usuario = User('diana','Rangel')
print("El nombre del usuario es: "+ usuario.first_name.title() +".")
print("El apellido del usuario es: ", usuario.last_name)
usuario.first_name
usuario.describe_user()
usuario.greet_user()
usuario.genero_F()
#----------------------------------
usuario = User('luisa','Justo')
print("El nombre del usuario es: "+ usuario.first_name.title() +".")
print("El apellido del usuario es: ", usuario.last_name)
usuario.first_name
usuario.describe_user()
usuario.greet_user()
usuario.genero_F()
#----------------------------------
usuario = User('brenda','Ruiz')
print("El nombre del usuario es: "+ usuario.first_name.title() +".")
print("El apellido del usuario es: ", usuario.last_name)
usuario.first_name
usuario.describe_user()
usuario.greet_user()
usuario.genero_F()
#------------------------------------------
usuario = User('javier','hernandez')
print("El nombre del usuario es: "+ usuario.first_name.title() +".")
print("El apellido del usuario es: ", usuario.last_name)
usuario.first_name
usuario.describe_user()
usuario.greet_user()
usuario.genero()