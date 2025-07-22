# PURWADHIKA CAPSTONE 1
# JCDSOH01-00 - Mirai Suchayla 

#                                                       - Commodity Trading -
# ----------------------------------------------------------------------------------------------------------------

# Welcome sign and latest news update
print('\nWelcome to Suchay\'s Commodity Trading and Investment journey!')

print('\nToday\'s News : https://www.nytimes.com/2025/07/15/us/politics/trump-tariffs-inflation.html')

# Trading Dictionary 
dict_trading = {
    'No' : [1,2,3,4,5,6],
    'com' : ['Gold', 'Coal', 'Oil', 'Wheat', 'Coffee', 'Acid'],
    'unit' : ['ozt', 'MT', 'bbl', 'bu', 'lbs', 'L'],
    'comp' :['Antan', 'Adari', 'Chepron', 'Indodrink', 'Nesple', 'Petrikimia'],
    'qty' : [15,92,67,89,5,43],
    'price' : [400,15,20,100,800,80]
}

# User's Portofolio Dictionary 
dict_porfo = {
    'No' : [1,2],
    'com' : ['Gold', 'Coffee'],
    'unit' : ['ozt', 'lbs'],
    'qty' : [10,12],
    'price' : [200,610],
}

# Processing and Investment Dictionary
dict_process = {
    'No' : [1,2,3,4,5,6],
    'com' : ['Gold', 'Coal', 'Oil', 'Wheat', 'Coffee', 'Acid'],
    'product' : ['Jewelry', 'Steel', 'Gasoline', 'Noodles', 'Roasted beans', 'Detergents'],
    'invest' : [900, 20, 25, 50, 600, 30],
    'sell' : [1570, 100, 82, 220, 1500, 150]
}

# User's End Product list
list_product = {'No':[], 'com':[], 'unit':[], 'qty':[], 'price':[]}

# Initial Balance for today's trading
Balance = 3500

# ----------------------------------------------------------------------------------------------------------------
# FUNCTION

# Show commodity trading list
def com_list():
    print('\n-Commodity List-\n')
    print(f'{'No':<4} | {'Commodity':<9} | {'Unit':<5}| {'Company':<10} | {'Qty':<4} | {'Price(USD)':<8}')
    print("─────┼───────────┼──────┼────────────┼──────┼───────────")
    for i in range(len(dict_trading['No'])):
        print(f"{dict_trading['No'][i]:<4} | {dict_trading['com'][i]:<9} | {dict_trading['unit'][i]:<4} | {dict_trading['comp'][i]:<10} |{dict_trading['qty'][i]:<5} | {dict_trading['price'][i]:<8}")

# Show portofolio list
def porfo():
    print('\n-My Portofolio-\n')
    print(f'{'No':<4} | {'Commodity':<9} | {'Unit':<5} | {'Qty':<4} | {'I.Price(USD)':<8}')
    print("─────┼───────────┼───────┼──────┼────────────")
    for j in range(len(dict_porfo['No'])):
        print(f'{dict_porfo['No'][j]:<4} | {dict_porfo['com'][j]:<9} | {dict_porfo['unit'][j]:<5} | {dict_porfo['qty'][j]:<4} | {dict_porfo['price'][j]:<8}')

# Show Processing list
def process():
    print('-Commodity Processing Investment-\n')
    print(f'{'No':<4} | {'Commodity':<9} | {'Product':<13} | {'Invest(USD)':<11} | {'Sell Price(USD)':<12}')
    print("─────┼───────────┼───────────────┼─────────────┼────────────")
    for k in range(len(dict_process['No'])):
        print(f'{dict_process['No'][k]:<4} | {dict_process['com'][k]:<9} | {dict_process['product'][k]:<13} | {dict_process["invest"][k]:<11} | {dict_process["sell"][k]:<12}')

# Run menu 1 : Current commodity watchlist
def menu_1():
    com_list()

# Run menu 2 : Delete commodity watchlist
def menu_2():
    print(f'\nYour commodity watchlist: {', '.join(dict_trading['com'])}.')
    
    # User input commodity user's would like to remove
    while True:
        inp = input(f'\nWhich commodity would you like to remove from watchlist? ').capitalize()
        if inp in dict_trading['com']:
            i = dict_trading['com'].index(inp)
            
            # For loop to delete values by index using pop
            for key in dict_trading:
                dict_trading[key].pop(i)

            print('\nRemove accomplished!')
            break
        else:
            print('\nCommodity not found')


# Run menu 3 : Your Portofolio and Trading Balance
def menu_3():
    porfo()
    global Balance      # Global for keep the balance updated
    print(f'\nYour trading balance is USD {Balance}')

# Run menu 4 : Buy Commodity
def menu_4():
    com_list()

    # Loop for user input purchasing
    while True:
        
        # Buy commodity loop 
        while True:
            buy_com = input(f'\nWhich commodity would you like to purchase? ').capitalize()
            
            # Condition if commodity user's inputed is in trading list
            if buy_com in dict_trading['com']:
                i = dict_trading['com'].index(buy_com)
                break
            else:
                print('\nCommodity not found')
        
        # Quantity of buy commodity loop
        while True:
            buy_qty = int(input(f'\nHow many units of {buy_com} would you like to purchase: '))
            
            # Condition if commodity quantity user's inputed is sufficient
            if buy_qty > dict_trading['qty'][i]:
                print(f'\nThe amount of {buy_com} you ask exceeds the availability in today\'s market')
            else:
                # Request processed while quantity sufficient
                Addnum = str(len(dict_porfo['No']) + 1)     
                Addunit = dict_trading['unit'][i]           
                Addprice = dict_trading['price'][i]         

                # Calculating spending
                spending = Addprice * buy_qty
                global Balance
                while True:
                    if spending > Balance:
                        print(f'Balance insufficient')
                        break
                    else:
                        # Spending success, and balance reduced by spending
                        Balance -= spending
                        print(f'''\nPurchase successful! 
You spent USD {spending}, and your remaining balance is USD {Balance}.''')
                    
                    # Check if commodity user's buy in already in portofolio
                    if buy_com in dict_porfo['com']:
                        j = dict_porfo['com'].index(buy_com)
                        newprice = int(((dict_porfo['price'][j] * dict_porfo['qty'][j]) + dict_trading['price'][i] * buy_qty) / (dict_porfo['qty'][j] + buy_qty))
                        dict_porfo['qty'][j] += buy_qty     # Updated quantity
                        dict_porfo['price'][j] = newprice   # Adjusted price
                    else:
                    # If is a new commodity user has, add using append
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

# Run menu 5 : Refining/processing your commodity
def menu_5():
    print('\n\'You can only perform a refining transaction for one type of commodity per trading day\'\n')
    process()
    global Balance
    print(f'\nYour trading balance is USD {Balance}')
    porfo()
    
    # User input refining commodity
    while True:
        process_com = input('\nWhich commodity would you like to proceed to end-use product? ').capitalize()
        
        # Check if the commodity user's would like to process is in the portfolio list
        if process_com in dict_porfo['com']:
            Index = dict_porfo['com'].index(process_com)
            break
        else:
            print('\nCommodity not found')
        
    while True:
        
        # User input quantity of refining commodity
        process_qty = int(input(f'\nHow many units of {process_com} would you like to process? '))
        
        # Check if quantity is sufficient
        if process_qty <= dict_porfo['qty'][Index]:
            i_index = dict_process['com'].index(process_com)
            
            # Calculate total invest 
            total_invest = process_qty * dict_process['invest'][i_index]
            while True:
                
                # Check if balance is sufficient for investing
                if total_invest > Balance:
                    print(f'\nBalance insufficient')
                    break
                else:
                    
                    # While sufficient, request processed
                    invested = dict_process['invest'][i_index] + dict_porfo['price'][Index]     # Total asset fund
                    profit = process_qty * (dict_process['sell'][i_index] - invested)           # Profit from estimated selling price reduced by total asset fund

                    # Adjusting balance by reducing with total investment process
                    Balance -= total_invest
            
                    print(f'''\nRequest Successful! 
Your {process_com} will be processed into {dict_process['product'][i_index]}, 
and you will gain an estimated profit of USD {profit}''')
                    print(f'Your trading balance is USD {Balance}')

                    # Add product data to product user's list
                    list_product['No'].append(str(len(list_product['No']) + 1))
                    list_product['com'].append(process_com)
                    list_product['unit'].append(dict_porfo['unit'][Index])
                    list_product['qty'].append(process_qty)
                    list_product['price'].append(dict_process['sell'][i_index])

                    # Reducing quantity of commodity processed from portfolio
                    dict_porfo['qty'][Index] -= process_qty
                    break
            break
        else:
            print(f'\nThe amount of {process_com} you ask exceeds the availability amount in your portofolio')

# Run menu 6 : Sell Your Commodity and Product        
def menu_6():

    # Deciding selling items
    inputfive = int(input('\nWould you like to sell a commodity (1)? or a product (2)? '))
    global Balance
    if inputfive == 1:
        porfo()

        # User input sell commodity
        while True:
            sell_com = input('\nWhich commodity you\'d like to sell? ').capitalize()
            
            # Check if commodity is in the list
            if sell_com in dict_porfo['com']:
                s_index = dict_porfo['com'].index(sell_com)
                s_unit = dict_porfo['unit'][s_index]
                break
            else:
                print('\nCommodity not found in your portofolio')
        
        # User input quantity of sell commodity
        while True:
            sell_qty = int(input(f'\nHow many units of {sell_com} would you like to sell? '))
            
            # Condition if quantity is sufficient
            if sell_qty <= dict_porfo['qty'][s_index]:
                w_index = dict_trading['com'].index(sell_com)

                total_sell = dict_trading['price'][w_index] * sell_qty                  # Calculate total asset fund
                total_profits = total_sell - (dict_porfo['price'][s_index] * sell_qty)  # Calculate total estimated profits

                print(f'''\nCongratulation! You successfully sold {sell_qty} {s_unit} {sell_com} for a USD {total_sell}. 
You earn profit of USD {total_profits}, which has been automatically added to your balance''')
                
                # Update balance by adding profits
                Balance += total_sell
                dict_porfo['qty'][s_index] -= sell_qty
                break
            else:
                print(f'\nYour request exceeds the available amount of {sell_com} in your portofolio')

    elif inputfive == 2:
        
        # Show user's product-end list
        print('\n-End Produk-', '\n')
        print(f'{'No':<4} | {'Commodity':<9} | {'Unit':<4} | {'Qty':<4} | {'Price(USD)':<10}')
                
        for i in range(len(list_product['No'])):
            print(f"{list_product['No'][i]:<4} | {list_product['com'][i]:<9} | {list_product['unit'][i]:<4} | {list_product['qty'][i]:<4} | {list_product['price'][i]:<10}")
        
        p_sell = list_product['com'][0] 
        p_unit = list_product['unit'][0]
        
        # Due to the end-product list is only one, user input directly asking for quantity 
        while True:
            sell_proqty = int(input(f'\nHow many units of {p_sell} would you like to sell? '))
            
            # Condition if quantity is sufficient
            if sell_proqty <= list_product['qty'][0]:
                x_index = dict_trading['com'].index(p_sell)
                y_index = dict_porfo['com'].index(p_sell)
                z_index = dict_process['com'].index(p_sell)
                
                buy = dict_porfo['price'][y_index] * sell_proqty            # calculating total buy commodity
                invest = dict_process['invest'][z_index] * sell_proqty      # Calculating total of investment for refining

                total_sellPro = list_product['price'][0] * sell_proqty      # Calculating total money earn
                total_profitsPro = total_sellPro - (buy + invest)           # Calculating total profit

                print(f'''\nCongratulation! You have successfully sold {sell_proqty} {p_unit} {p_sell} for a USD {total_sellPro}. 
You earn profit of USD {total_profitsPro}, which has been automatically added to your balance''')
                
                # Adjusting balance
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
        print('\nYour choice is invalid, please input number between 1-7 on main menu page: ')
        mainmenu()
        
mainmenu()


# This script is 100% belong to owner, kindly email her for further assistant
# suchaymirai@gmail.com