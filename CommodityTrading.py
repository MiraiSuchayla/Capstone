# PURWADHIKA CAPSTONE 
# JCDSOH01-00 - Mirai Suchayla 

#                                                       - Commodity Trading -
# ----------------------------------------------------------------------------------------------------------------
# GLOBAL VARIABLE

print('\nWelcome to Suchay\'s Commodity Trading and Investment journey!')

print('\nToday\'s News : https://www.nytimes.com/2025/07/15/us/politics/trump-tariffs-inflation.html')

dict_trading = {
    'No' : [1,2,3,4,5,6],
    'com' : ['Gold', 'Coal', 'Oil', 'Wheat', 'Coffee', 'Acid'],
    'unit' : ['ozt', 'MT', 'bbl', 'bu', 'lbs', 'L'],
    'comp' :['Antan', 'Adari', 'Chepron', 'Indodrink', 'Nesple', 'Petrikimia'],
    'qty' : [15,92,67,89,5,43],
    'price' : [400,15,20,100,800,80]
}

dict_porfo = {
    'No' : [1,2],
    'com' : ['Gold', 'Coffee'],
    'unit' : ['ozt', 'lbs'],
    'qty' : [10,12],
    'price' : [200,610],
}
#   'Profits' : [dict_trading[5][1], dict_trading[5][2]] -> showing the current price, so can see how much changing

dict_process = {
    'No' : [1,2,3,4,5,6],
    'com' : ['Gold', 'Coal', 'Oil', 'Wheat', 'Coffee', 'Acid'],
    'product' : ['Jewelry', 'Steel', 'Gasoline', 'Noodles', 'Roasted beans', 'Detergents'],
    'invest' : [900, 20, 25, 50, 600, 30],
    'sell' : [1570, 100, 82, 220, 1500, 150]
}

list_product = {'No':[], 'com':[], 'unit':[], 'qty':[], 'price':[]}

Balance = 3500

# ----------------------------------------------------------------------------------------------------------------
# FUNCTION

def com_list():
    print('\n-Commodity List-\n')
    print(f'{'No':<4} | {'Commodity':<9} | {'Unit':<5}| {'Company':<10} | {'Qty':<4} | {'Price(USD)':<8}')
    print("─────┼───────────┼──────┼────────────┼──────┼───────────")
    for i in range(len(dict_trading['No'])):
        print(f"{dict_trading['No'][i]:<4} | {dict_trading['com'][i]:<9} | {dict_trading['unit'][i]:<4} | {dict_trading['comp'][i]:<10} |{dict_trading['qty'][i]:<5} | {dict_trading['price'][i]:<8}")

def porfo():
    print('\n-My Portofolio-\n')
    print(f'{'No':<4} | {'Commodity':<9} | {'Unit':<5} | {'Qty':<4} | {'I.Price(USD)':<8}')
    print("─────┼───────────┼───────┼──────┼────────────")
    for j in range(len(dict_porfo['No'])):
        print(f'{dict_porfo['No'][j]:<4} | {dict_porfo['com'][j]:<9} | {dict_porfo['unit'][j]:<5} | {dict_porfo['qty'][j]:<4} | {dict_porfo['price'][j]:<8}')

def process():
    print('-Commodity Processing Investment-\n')
    print(f'{'No':<4} | {'Commodity':<9} | {'Product':<13} | {'Invest(USD)':<11} | {'Sell Price(USD)':<12}')
    print("─────┼───────────┼───────────────┼─────────────┼────────────")
    for k in range(len(dict_process['No'])):
        print(f'{dict_process['No'][k]:<4} | {dict_process['com'][k]:<9} | {dict_process['product'][k]:<13} | {dict_process["invest"][k]:<11} | {dict_process["sell"][k]:<12}')


def menu_1():
    com_list()

def menu_2():
    print(f'\nYour commodity watchlist: {', '.join(dict_trading['com'])}.')
    while True:
        inp = input(f'Which commodity would you like to remove from watchlist? ').capitalize()
        if inp in dict_trading['com']:
            i = dict_trading['com'].index(inp)
            
            for key in dict_trading:
                dict_trading[key].pop(i)

            print('\nRemove accomplished!')
            break
        else:
            print('\nCommodity not found')

def menu_3():
    porfo()
    global Balance
    print(f'\nYour trading balance is USD {Balance}')

def menu_4():
    com_list()

    while True:
        while True:
            buy_com = input(f'\nWhich commodity would you like to purchase? ').capitalize()
            if buy_com in dict_trading['com']:
                i = dict_trading['com'].index(buy_com)
                break
            else:
                print('\nCommodity not found')

        while True:
            buy_qty = int(input(f'\nHow many units of {buy_com} would you like to purchase: '))
            if buy_qty > dict_trading['qty'][i]:
                print(f'\nThe amount of {buy_com} you ask exceeds the availability in today\'s market')
            else:
                Addnum = str(len(dict_porfo['No']) + 1)
                Addunit = dict_trading['unit'][i]
                Addprice = dict_trading['price'][i]

                spending = Addprice * buy_qty
                global Balance
                while True:
                    if spending > Balance:
                        print(f'Balance insufficient')
                        break
                    else:
                        Balance -= spending
                        print(f'''\nPurchase successful! 
You spent USD {spending}, and your remaining balance is USD {Balance}.''')
                    
                    if buy_com in dict_porfo['com']:
                        j = dict_porfo['com'].index(buy_com)
                        newprice = int(((dict_porfo['price'][j] * dict_porfo['qty'][j]) + dict_trading['price'][i] * buy_qty) / (dict_porfo['qty'][j] + buy_qty))
                        dict_porfo['price'][j] = newprice
                        dict_porfo['qty'][j] += buy_qty
                    else:
                        dict_porfo['No'].append(Addnum)
                        dict_porfo['com'].append(buy_com)
                        dict_porfo['unit'].append(Addunit)
                        dict_porfo['qty'].append(buy_qty)
                        dict_porfo['price'].append(Addprice)
                    break
                    
                break
        reinput = input('\nWould you like to do another purchases? (Y/N): ').upper()
        if reinput == 'N':
            break

def menu_5():
    print('\n\'You can only perform a refining transaction for one type of commodity per trading day\'\n')
    process()
    global Balance
    print(f'\nYour trading balance is USD {Balance}')
    porfo()
    
    while True:
        process_com = input('\nWhich commodity would you like to proceed to end-use product? ').capitalize()
        if process_com in dict_porfo['com']:
            Index = dict_porfo['com'].index(process_com)
            break
        else:
            print('\nCommodity not found')
        
    while True:
        process_qty = int(input(f'\nHow many units of {process_com} would you like to process? '))
        if process_qty <= dict_porfo['qty'][Index]:
            i_index = dict_process['com'].index(process_com)
            total_invest = process_qty * dict_process['invest'][i_index]
            while True:
                if total_invest > Balance:
                    print(f'\nBalance insufficient')
                    break
                else:
                    invested = dict_process['invest'][i_index] + dict_porfo['price'][Index]
                    profit = process_qty * (dict_process['sell'][i_index] - invested)

                    Balance -= total_invest
            
                    print(f'''\nRequest Successful! 
Your {process_com} will be processed into {dict_process['product'][i_index]}, 
and you will gain an estimated profit of USD {profit}''')
                    print(f'Your trading balance is USD {Balance}')

                    list_product['No'].append(str(len(list_product['No']) + 1))
                    list_product['com'].append(process_com)
                    list_product['unit'].append(dict_porfo['unit'][Index])
                    list_product['qty'].append(process_qty)
                    list_product['price'].append(dict_process['sell'][i_index])
                    break
            break
        else:
            print(f'\nThe amount of {process_com} you ask exceeds the availability amount in your portofolio')
        
def menu_6():
    inputfive = int(input('\nWould you like to sell a commodity (1)? or a product (2)? '))
    global Balance
    if inputfive == 1:
        porfo()

        while True:
            sell_com = input('\nWhich commodity you\'d like to sell? ').capitalize()
            if sell_com in dict_porfo['com']:
                s_index = dict_porfo['com'].index(sell_com)
                s_unit = dict_porfo['unit'][s_index]
                break
            else:
                print('\nCommodity not found in your portofolio')
        
        while True:
            sell_qty = int(input(f'\nHow many units of {sell_com} would you like to sell? '))
            if sell_qty <= dict_porfo['qty'][s_index]:
                w_index = dict_trading['com'].index(sell_com)

                total_sell = dict_trading['price'][w_index] * sell_qty
                total_profits = total_sell - (dict_porfo['price'][s_index] * sell_qty)

                print(f'''\nCongratulation! You successfully sold {sell_qty} {s_unit} {sell_com} for a USD {total_sell}. 
You earn profit of USD {total_profits}, which has been automatically added to your balance''')
                
                Balance += total_sell
                dict_porfo['qty'][s_index] -= sell_qty
                break
            else:
                print(f'\nYour request exceeds the available amount of {sell_com} in your portofolio')

    elif inputfive == 2:
        print('\n-End Produk-', '\n')
        print(f'{'No':<4} | {'Commodity':<9} | {'Unit':<4} | {'Qty':<4} | {'Price(USD)':<10}')
                
        for i in range(len(list_product['No'])):
            print(f"{list_product['No'][i]:<4} | {list_product['com'][i]:<9} | {list_product['unit'][i]:<4} | {list_product['qty'][i]:<4} | {list_product['price'][i]:<10}")
        
        p_sell = list_product['com'][0] 
        p_unit = list_product['unit'][0]
        while True:
            sell_proqty = int(input(f'\nHow many units of {p_sell} would you like to sell?'))
            if sell_proqty <= list_product['qty'][0]:
                x_index = dict_trading['com'].index(p_sell)
                y_index = dict_porfo['com'].index(p_sell)
                z_index = dict_process['com'].index(p_sell)
                
                buy = dict_porfo['price'][y_index] * sell_proqty
                invest = dict_process['invest'][z_index] * sell_proqty

                total_sellPro = list_product['price'][0] * sell_proqty
                total_profitsPro = total_sellPro - (buy + invest)    

                print(f'''Congratulation! You have successfully sold {sell_proqty} {p_unit} {p_sell} for a {total_sellPro}. 
You earn profit of USD {total_profitsPro}, which has been automatically added to your balance''')
                
                Balance += total_sellPro
                break
            else:
                print(f'\nYour request exceeds the available amount of {p_sell} in your product list')
            
    else:
        print('Option not found')

# ----------------------------------------------------------------------------------------------------------------
# MAIN MENU

def mainmenu():
    print('''
    - Mainmenu -
          
    1. Current commodity watchlist
    2. Delete commodity watchlist
    3. Your Portofolio and Trading Balance
    4. Buy Commodity
    5. Refining/processing your commodity
    6. Sell Your Commodity and Product
    7. Exit ''')

    inputmenu = int(input(f'\nPlease enter the menu number you\'d like to select: '))

    if inputmenu == 1:
        menu_1()
        mainmenu()
    elif inputmenu == 2:
        menu_2()
        mainmenu()
    elif inputmenu == 3:
        menu_3()
        mainmenu()
    elif inputmenu == 4:
        menu_4()
        mainmenu()
    elif inputmenu == 5:
        menu_5()
        mainmenu()
    elif inputmenu == 6:
        menu_6()
        mainmenu()
    elif inputmenu == 7:
        print('\nHave a great day dan happy cuan!\n')
    else:
        print('\nYour choice is invalid, please input number between 1-5 on main menu page: ')
        mainmenu()
        
mainmenu()


# This script is 100% belong to owner, kindly email her for further assistant
# suchaymirai@gmail.com