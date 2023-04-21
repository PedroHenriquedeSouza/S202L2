from database.Database import Database
from DAO.ZoologicoDAO import ZoologicoDAO
from zoologicoCLI import ZoologicoCLI
from model.Animal import Animal

cli = ZoologicoCLI()

flag = True

while(flag):
    cli.menu()
    selectedOption = int(input())

    if (selectedOption == 1):
        cli.createAnimal()
    elif (selectedOption == 2):
        cli.readAnimal()
    elif (selectedOption == 3):
        cli.createAnimal()
    elif (selectedOption == 4):
        cli.createAnimal()
    else:
        print("Opção Inválida!")
        flag = False
