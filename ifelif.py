# transport = input( 'какой транспорт вы выбираете: самолет, поезд, автобус: ')

# if transport == 'самолет':
#     ticket_tupe = input('каким классом вы хотите лететь: эконом, бизнес: ')
#     if ticket_tupe == 'эконом':
#             place = input('где бы вы хотите сидеть: у одна,  в проходе: ')
#     else:
#             place = 'у вас бизнес зал'
# elif transport == 'поезд':
#     tikcet_tupe = input (' как вы хотите ехать: купе, плацкарт: ')
#     if tikcet_tupe == 'купе':
#         place = input(' выбирите одно из свободных мест:12, 55, 77')
#     elif tikcet_tupe == 'плацкар':
#         print (' в плацкарде не осталось мест!')
#         exit()
# elif transport == 'автобус':
#     tikcet_tupe =  input(' как вы хотите ехать: сидя, стоя ')
#     if tikcet_tupe == 'сидя':
#         place = input(' выбирите место: 5, 7, 8')

#     else:
#         place = 'где угодно'
# else:
#         print(' такого транспорта нет! ')
#         exit()


# print(' ок внесите оплату')
# print( f'Вы выбрали: {transport} ваше место: {place} ' )



buffet = input('что закажете: шаурму, самса, пирожок: ')

if buffet == 'шаурма': 
    filling = input('какую начинку вы хотите: мясо, курица: ')
    if filling == 'мясо': 
        howmany = input('сколько хотите: ')
        warm = input('нужно ли согревать: да, нет: ')
        drink = input('что будете пить: чай, кофе, кола, миниралка: ')
        client = ('')
        exit()
else:
    print('такого блюда нет')
    exit()
if buffet == 'самса': 
    filling = input('какую начинку вы хотите: мясо, курица, сыр: ')
    if filling == 'сыр': 
        wait = input('самса сыром закончились, будите ждать: да, нет:')
        howmany = input('сколько хотите: ')
        warm = input('нужно ли согревать: да, нет: ')
        drink = input('что будете пить: чай, кофе, кола, миниралка: ')
        client = ('клиент напиток не взял') 
        exit()
if buffet == 'пирожок': 
    filling = input('какую начинку вы хотите: кортофель, капуста: ')
    if filling == 'капуста': 
        wait = input(' пирожок с капустой вчерашний, будите брать: да, нет:')
        howmany = input('сколько хотите: ')
        warm = input('нужно ли согревать: да, нет: ')
        drink = input('что будете пить: чай, кофе, кола, миниралка: ')
        client = ('')
print( f'Вы заказали : {buffet} с {filling} {howmany} шт, {drink} {client} ')