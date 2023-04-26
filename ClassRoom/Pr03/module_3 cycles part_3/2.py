# Написать программу - конвертер валют.
# Реализовать общее с пользователем через меню.
while True:    
    n=int(input('n='))
    #x=int(input('Введите валюту')
    print('vybor')
    print('2', 'евро')
    print('5', 'фунты')
    choise=('vas vybor')
    if choise==1:
        res=n*77
        print("res:,res")
    elif choise==2:
        res=n*12
        print("res:,res")
    else: 
        print ("неправильний ввод")
        print("продолжить работу ")
        print("1, да") 
        print("2, нет")
        choice=int(input("vas vybor"))
        if choice==1:
            print("ok")
        if choice==2:
            break     
    