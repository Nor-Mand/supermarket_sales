# Importing dependencies
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# SECTION STYLE SETTINGS

# Head
title = "Analysis Pipeline for SUPERMARKET SALES"
description = """
    --> Using Pandas for analysis
    --> Using Matplotlib for Visualization
    --> Using Seaborn for static data visualization"""
dataSet = "https://www.kaggle.com/datasets/aungpyaeap/supermarket-sales?select=supermarket_sales+-+Sheet1.csv"
author = "Normand Terceros Laredo"
website = "https://normand.dev"
github = "https://github.com/Nor-Mand"

# NavBar
subtitle = "\x1b[0;30;43m **** Welcome to data analysis for Supermarket Sales in Myanmar **** \x1b[0m"

# Head lines
main_line = ("=" * 100)
sub_line = ("*" * 100)
padding = (" " * 7)

# Show Information
print(main_line)
print("Title:", title)
print("Description:", description)
print("Dataset:", dataSet)
print("Author:", author)
print("Website:", website)
print(main_line)
print(padding + subtitle)
print(sub_line)

# SECTION DATA INFORMATION
"""
    the variable "smf" is to refer the dataset  supermarket.csv 'Super Market Data Frame,
    you can use the complete name if you want, but remeber is more 
    dificult to manipulate when you need to use methods to get information.
"""
# Reading data
smf = pd.read_csv('supermarket_sales.csv')
# set format values number
pd.options.display.float_format = '{:,.2f}'.format
# convert date object to datetime
smf['Date'] = pd.to_datetime(smf['Date'])

# GET NAMES OF IMPORTANT COLUMNS
# using method set to delete repeated  names
getNameCities = set(smf['City'])

# put in list
cities = list(getNameCities)
cities.sort()


# Main function
def main():
    menu()


# Main menu options
def menu():
    print()
    print("Please, select one of the following options:")

    choice = input("""
    1 -- Display information of Dataset
    2 -- Display Global per City
    3 -- Display Global by Gender
    4 -- Display Global by Product
    5 -- Display Method of payment
    6 -- Display Daily sales per country
    7 -- Exit.

    \x1b[1;37;43m Please enter your choice:\x1b[0m""")
    print("\n")
    if choice == "1":
        show_information()
    elif choice == "2":
        get_global_sales()
    elif choice == "3":
        get_global_gender()
    elif choice == "4":
        get_global_product()
    elif choice == "5":
        get_method_payment()
    elif choice == "6":
        get_daily_sales()
    elif choice == "7":
        print("\x1b[5;30;42m Thank you!!!, Don't forget give me your feedback to my email normandlaredo@gmail.com \x1b[0m")
    else:
        print("\033[101m You must only select a number from the list \033[0m")
        print("Please try again")
        menu()


# Sub menu for Choices
def option_submenu():
    choice = input("""\x1b[0;30;43m options: 1-Go Back Main menu,  2-Exit the program\x1b[0m
        Please enter your choice: """)

    if choice == "1":
        menu()
    elif choice == "2":
        print("\n")
        print("\x1b[5;30;42m Thank you!!!, Don't forget give me your feedback to my email normandlaredo@gmail.com \x1b[0m")
    else:
        print("\033[101m You must only select a number from the list \033[0m")
        print("Please try again")
        option_submenu()


# Choice 1
def show_information():

    print("\n")
    print('\x1b[0;30;44m ******* Name of Dataset: "SUPERMARKET SALES *******" \x1b[0m')
    print("\n")
    print("\x1b[0;30;47m Number of rows and columns:\x1b[0m", smf.shape)
    print()
    print("\x1b[0;30;47m First 5 rows object: \x1b[0m")
    print(smf.head(5))
    print()
    print("\x1b[0;30;47m Names all Keys: \x1b[0m")
    print(smf.keys())
    print()
    print("\x1b[0;30;47m Data type: \x1b[0m")
    print(smf.dtypes)
    print("\n")
    option_submenu()


# Choice 2
def get_global_sales():

    get_keys = smf[['City', 'Total']]
    result = get_keys.groupby(['City']).sum().reset_index()
    grand_total = get_keys['Total'].sum()
    ax = sns.barplot(data=result, x='City', y='Total', errwidth=0)
    ax.bar_label(ax.containers[0])
    plt.show()
    print("\n")
    print('\x1b[0;30;44m *******  GLOBAL SALES PER CITIES IN MYANMAR *******" \x1b[0m')
    print(result)
    print()
    print("\x1b[0;30;47m Grand Total: \x1b[0m", grand_total)
    print("\n")
    option_submenu()


# Choice 3
def get_global_gender():

    get_keys = smf[['Gender', 'Total']]
    result = get_keys.groupby(['Gender']).sum().reset_index()
    grand_total = get_keys['Total'].sum()
    ax = sns.barplot(data=result, x='Gender', y='Total', errwidth=0)
    ax.bar_label(ax.containers[0])
    plt.show()
    print("\n")
    print('\x1b[0;30;44m *******  GLOBAL SALES PER GENDER IN MYANMAR *******" \x1b[0m')
    print(result)
    print()
    print("\x1b[0;30;47m Grand Total: \x1b[0m", grand_total)
    print("\n")
    option_submenu()


# Choice 4
def get_global_product():
    get_keys = smf[['Product line', 'Total']]
    result = get_keys.groupby(['Product line']).sum().reset_index()
    grand_total = get_keys['Total'].sum()
    get_keys_rating = smf[['Total', 'Rating', 'Product line']]
    sns.set(rc={'figure.figsize': (15, 8)})
    sns.scatterplot(data=get_keys_rating, x='Total', y='Rating', hue='Product line', s=100, color=".2", marker="+")
    plt.show()
    ax = sns.barplot(data=result, x='Product line', y='Total', errwidth=0)
    ax.bar_label(ax.containers[0])
    plt.show()
    print("\n")
    print('\x1b[0;30;44m *******  GLOBAL SALES PER PRODUCTS IN MYANMAR *******" \x1b[0m')
    print(result)
    print()
    print("\x1b[0;30;47m Grand Total: \x1b[0m", grand_total)
    print("\n")
    option_submenu()


# Choice 5
def get_method_payment():

    get_keys = smf[['Total', 'Payment']]
    result = get_keys.groupby(['Payment']).sum().reset_index()
    ax = sns.barplot(data=result, x='Payment', y='Total', errwidth=0)
    ax.bar_label(ax.containers[0])
    plt.show()
    print("\n")
    print('\x1b[0;30;44m *******  METHOD OF PAYMENT USING IN MYANMAR *******" \x1b[0m')
    print(result)
    print()
    print("\n")
    option_submenu()


# Choice 6
def get_daily_sales():

    get_keys = smf[['City', 'Date', 'Gender', 'Total']]

    print()
    print("\x1b[0;30;44m Please, enter one of the following cities names:\x1b[0m")

    for city in cities:
        print(f"""
               {city}""")
    city_input = input("""
           Please type the city name: """)
    print()

    find_city = get_keys[get_keys['City'] == city_input]
    find_city.sort_values(by=['Date'])
    if len(find_city) > 0:
        sns.set(rc={'figure.figsize': (15, 8)})
        sns.lineplot(data=find_city, x='Date', y='Total', hue='Gender', linewidth=2)
        plt.show()
        print(find_city)
        print()

    else:
        print(f"\033[101m Invalid city!. You must to write a valid city of the list. \033[0m")
        print("Please try again")
        return get_daily_sales()

    option_submenu()


main()