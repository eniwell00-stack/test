#TASK PROJEKT
data_cls_el = ['Телефоны', "Ноутбуки", "Планшеты"]
data_el_firm = ['Apple', 'Huaway' , 'OnePluse']
data_tel_el_apl = ['Iphone 17', "Iphone 17 Pro", "Iphone 17 Pro Max"]
data_tel_el_huw = []
data_tel_el_opl = []
data_tel_el_apl_pr = [800000,100000,120000]

data_hom = []
data_hom_pr = []

data_sport = []
data_sport_pr = []

data_pl = []
data_pl_pr = []

basket = []
while True:
    print ("Если у вас есть корзина, вы можите ее открыть написав 'b' или просто нажать 'Enter' для продолжения")
    choice = input()
    if choice == 'b':
        print(f'Ваша корзина: {basket}')
        print('Вы можите удалить товар из корзины написав "b" или продолжить нажав "ENTER" ')
        choice = input()
        if choice == "b":
            print("Напишите место товара в корзине от 1 (Стоимость считать как отдельный элимент):")
            nums = int(input())
            if nums>0:
                basket.pop(nums-1)
                basket.pop(nums-1)
                print (f'Ваша текушая корзина {basket}')
            else:
                print("Ошибка")
                break
    choice = input("Хотите узнать доступные категории товаов? Если да то пожалуйста нажмите 'Enter' тначе нажмите 'q' ")
    if choice == 'q':
        break
    else:
        while True:
            print("Доступные категории товаров: 'Электроника', 'Товары для быта' 'Спортивная экипировка' 'Настольные игры' ")
            print('Хотите продолжить? Да/Нет')
            choice = input()
            if choice == 'Да':
                product = input("Введите категорию товаров: ")
                if product == 'Электроника':
                    print (f'Вы находитесь в разделе Электроники вот доступные подразделы товаров: {data_cls_el}')
                    catalog = input("Выберите подходяший каталог: ")
                    if catalog == "Телефоны":
                        print(f"Вы выбрали каталог телефонов. Теперь вы можите выбрать фирму из предложенных: {data_el_firm} ")
                        firm = input()
                        if firm == "Apple":
                            while True:
                                print('Хотите продолжить? Да/Нет')
                                choice = input()
                                if choice == 'Да':
                                    print(f"Доступые товары Apple: {data_tel_el_apl}")
                                    tel = input("Введите желаемый товар: ")
                                    if tel == 'Iphone 17':
                                        print(f'Вы выбрали Iphone 17 он стоит {data_tel_el_apl_pr[0]} руб')
                                        print(f'Хотите добавить его в корзину Да/Нет?')
                                        choice = input()
                                        if choice == 'Да':
                                            basket.append(data_tel_el_apl[0])
                                            basket.append(data_tel_el_apl_pr[0])
                                            print('Товар был успешно добавлен в корзину!')
                                        else:
                                            break
                                    elif tel == 'Iphone 17 Pro':
                                        print(f'Вы выбрали Iphone 17 Pro он стоит {data_tel_el_apl_pr[1]} руб')
                                        print(f'Хотите добавить его в корзину Да/Нет?')
                                        choice = input()
                                        if choice == 'Да':
                                            basket.append(data_tel_el_apl[1])
                                            basket.append(data_tel_el_apl_pr[1])
                                            print('Товар был успешно добавлен в корзину!')
                                        else:
                                            break
                                    elif tel == 'Iphone 17 Pro Max':
                                        print(f'Вы выбрали Iphone 17 Pro Max он стоит {data_tel_el_apl_pr[2]} руб')
                                        print(f'Хотите добавить его в корзину Да/Нет?')
                                        choice = input()
                                        if choice == 'Да':
                                            basket.append(data_tel_el_apl[2])
                                            basket.append(data_tel_el_apl_pr[2])
                                            print('Товар был успешно добавлен в корзину!')
                                        else:
                                            break
                                else:
                                    break
                else:
                    print ("Ошибка попробуйте выбрать категорию еще раз")
            else:
                break