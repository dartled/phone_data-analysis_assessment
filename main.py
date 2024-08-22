# modules
import pandas as pd
import matplotlib.pyplot as plt
import sys

# global variables
quit = False

# read the csv file
phone_data_df = pd.read_csv('data/updated_all_phones_AUSTRALIA_2022-2023.csv')

print("   ================================================")
print("""   WELCOME TO THE PHONE DATA EXPLORER""")

# define functions
def getOriginalData():
    print(phone_data_df)


def showTableWindow():
     # create a table window
    table_figure, ax = plt.subplots()

    #hide axes
    table_figure.patch.set_visible(False)
    ax.axis('off')
    table_window = ax.table(cellText=phone_data_df.values,colLabels=phone_data_df.columns,loc='center')
        
    table_window.auto_set_font_size(False)
    table_window.set_fontsize(7)

    print('Data is loading....please wait for the new window to pop up')
    plt.show()
    

def addRow():
    # insert new row on top and then print the new data table
    print('Input the following data')

   
    phone_name = input('phone_name: ')
    brand = input('brand: ')
    os = input('os: ') 
    inches = input('inches: ') 
    resolution = input('resolution: ') 
    battery = input('battery: ') 
    battery_type = input('battery_type: ') 
    ram = input('ram(GB): ') 
    announcement_date = input('announcement_date: ') 
    weight = input('weight(g): ') 
    storage = input('storage(GB): ') 
    price = input('price: ')

    # add the new row to the top
    new_row = pd.DataFrame({'phone_name':phone_name, 'brand':brand, 'os':os, 
               'inches':inches, 'resolution':resolution, 'battery':battery, 
               'battery_type':battery_type, 'ram(GB)':ram, 
               'announcement_date':announcement_date, 'weight(g)':weight, 'storage(GB)':storage, 
               'price':price},index=[0])
    
    updated_phone_data_df = pd.concat([new_row,phone_data_df.loc[:]]).reset_index(drop=True)
    print('New row added')
    print('=====UPDATED TABLE=====')
    print(updated_phone_data_df)    
        

def showCharts():
   # 
    try:

        print("""       ==================CHARTS===================
          
        Please select the chart you want to generate:
        1 - Maximum Price by Brand
        2 - Price by Phone Name
        3 - RAM by Phone Name
        4 - Storage by Phone Name
        5 - Battery Life by Phone Name
        6 - Screen Size (inch) by Phone Name
        7 - Weight(g) by Phone Name
        8 - Maximum Battery Life by Brand       
       ================================================""")

        choice = int(input('Enter Selection: '))

        if choice == 1:
           getChart('brand','price', 'Maximum Price by Brand')   
        elif choice == 2:
             getChart('phone_name','price', 'Price by Phone Name')         
        elif choice == 3: 
            getChart('phone_name','ram(GB)',  'RAM by Phone Name') 
        elif choice == 4:
            getChart('phone_name','storage(GB)', 'Storage by Phone Name') 
        elif choice == 5:
            getChart('phone_name','battery', 'Battery Life by Phone Name') 
        elif choice == 6:
            getChart('phone_name','inches', 'Screen Size(inches) by Phone Name') 
        elif choice == 7:
            getChart('phone_name','inches', 'Weight(g) by Phone Name')     
        elif choice == 8:
            getChart('brand', 'battery', 'Maximum battery Life by Brand')
        else:
            print('Please choose between 1 and 8!')
 

        #open the chart window
        plt.show()
       
    except ValueError as val_err:
         print('Please enter a valid number')

    except Exception as err:
        print('error encountered:')
        print(f'caught {err=}, {type(err)=}')


def getChart(x_name,y_name,chart_title):

    try:
        if(x_name == 'brand'):
            brand_data_df= phone_data_df.groupby(x_name)[y_name].max(0,True, True)
            print(brand_data_df)

            brand_data_df.plot(      
                        kind='bar',
                        x=x_name, fontsize=5,
                        y=y_name, 
                        color='blue',
                        alpha=0.3,
                        title=chart_title)

        else:
            phone_data_df.plot(      
                        kind='bar',
                        x=x_name, fontsize=5,
                        y=y_name, 
                        color='blue',
                        alpha=0.3,
                        title=chart_title)
        plt.show()
    
    except Exception as err:
        print('error encountered:')
        print(f'caught {err=}, {type(err)=}')


def getAnalysis():
    
        statistical_data = input("What would you like to calculate? [mean, median, mode, max, min or all] :  ")
        
        if statistical_data in ('mean', 'median', 'mode', 'max', 'min'):
            getStatistical_Data(statistical_data)
        elif statistical_data == 'all':  
            getAllStatistical_Data()
        else:
            print('Please enter a valid option')    


def getStatistical_Data( statistical_data):
        
    if statistical_data == 'mean':
        print(phone_data_df.mean(0,True,True))
    elif statistical_data == 'median':
        print(phone_data_df.median(0,True,True))
    elif statistical_data == 'mode':
        print(phone_data_df.mode(0,True))
    elif statistical_data == 'max':
        print(phone_data_df.max(0,True, True))
    elif statistical_data == 'min':
        print(phone_data_df.min(0, True, True))
    else:
        print('Please enter a valid option')


def getAllStatistical_Data():

    print('=====MEAN=====')  
    print(phone_data_df.mean(0,True,True))
    print('=====MEDIAN=====')  
    print(phone_data_df.median(0,True,True))
    print('=====MODE=====')  
    print(phone_data_df.mode(0,True))
    print('=====MAX=====')  
    print(phone_data_df.max(0,True, True))
    print('=====MIN=====')  
    print(phone_data_df.min(0, True, True))
  

def userOptions():
    global quit

    print("""   ================================================
          
    Please select an option:
    1 - Show the Original Table in Text
    2 - Show the Original Table in Window
    3 - Analyse the Data (Mean,Median,Mode,Max,Min)
    4 - View Charts
    5 - Insert New Row      
    6 - Quit Program
   ================================================""")
    
    try:
        choice = int(input('Enter Selection: '))

        if choice == 1:
            getOriginalData()
        elif choice == 2:    
            showTableWindow()
        elif choice == 3: 
            getAnalysis()
        elif choice == 4:
            showCharts()
        elif choice == 5:
            addRow()     
        elif choice == 6:
            quit = True
        else:
            print('Please enter a number between 1 and 6!')
    
    except ValueError as val_err:
         print('Please enter a valid number')

    except Exception as err:
        print('Program Error:')
        print(f'caught {err=}, {type(err)=}')
        
   

while not quit:
    userOptions()
