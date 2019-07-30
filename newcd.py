import os
import argparse
def search(title):
    suitable = []
    unverified = [os.getcwd()]
    while unverified:
        parent = unverified.pop()
        if os.path.isdir(parent):
            try:
                children = os.listdir(parent)
            except (PermissionError,NotADirectoryError):
                continue
            for child in children:
                address = os.path.normpath(parent + os.sep + child)
                unverified.append(address)
                if child == title:
                    suitable.append(address)
    return suitable

def upgratecd():
    catalog = str(input('Введите название каталога: ')
    if len(catalog) > 0:
        result = search(catalog)
    else:
        print ('Вы не вели название.')
        return upgratecd()
    lenresult = len(result)
    if lenresult == 0:
        print ('Каталог с данным названием не найден')
        return upgratecd()
    elif lenresult == 1:
        return result.pop()
    else:
        print('Найденно больше одного католога:')
        for i in range(lenresult):
            print(str(i) + ' - ' + result[i])
        inputnumber = int(input('Выберите нужный каталог: '))
        while inputnumber > lenresult:
            inputnumber = int(input('Выберите нужный каталог: '))
        return result.pop(inputnumber)

def executor():
    catalog = upgratecd()
    os.chdir(catalog)
    command = str(input(catalog + r'-> '))
    while command != 'exit':
        os.system(command)
        command = str(input(catalog + r'-> '))

executor()
