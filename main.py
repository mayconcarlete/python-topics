#dependency injection test:
from dependency_injection.controller import CreateUserExample

create_user_example = CreateUserExample()
create_user_example.handle({'name':"mayckids"})

#.env:
from environment.environment import printa

print('printa-----')
printa()

#argv
#Printa os valores passados como parametros, começando por 1 pois o elemento 0 é o endereço do arquivo executado.
import sys
print('argv-----')
print(sys.argv[1]) 

