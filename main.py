import pandas as pd
import matplotlib.pyplot as plt
import sys
import statistics

quit = False

old_data_df = pd.read_csv('/Data/Darrell/Computing Tech/phone_data-analysis_assessment/data/phone_brand&price.csv')

phone_df = pd.read_csv('/Data/Darrell/Computing Tech/phone_data-analysis_assessment/data/phone_brand&price.csv',
                            header=None,
                            names=['brand', 'price'])
                            #names=['brand', 'price(USD)'])
                            #names=['phone_name', 'brand', 'os', 'inches', 'resolution', 'battery', 'battery_type', 'ram(GB)', 'announcement_date', 'weight(g)', 'storage(GB)', 'video_720p', 'video_1080p', 'video_4K', 'video_8K', 'video_30fps', 'video_60fps', 'video_120fps', 'video_240fps', 'video_480fps', 'video_960fps', 'price(USD)'])

def getOriginalData():
    print(old_data_df)

def getUpdatedData():
    print(phone_df)

def getCharts():
    print('before try')

    try:
        
        print('before plot')
        phone_df.plot(      
                        kind='bar',
                        x='brand', 
                        y='price(USD)', 
                        color='blue',
                        alpha=0.3,
                        title='Phone Prices by Brand')
        print('after plot')
        plt.show()
        print('after show')
    
    except Exception as err:
        print('error encountered:')
        print(f'caught {err=}, {type(err)=}')

def getAnalysis():
    analysis_type = input('What data would you like to use? ')

    if analysis_type == 'price':
        statistical_data = input("Would you like to see the mean, median, mode, max or min of the price? ")
        getStatistical_Data(analysis_type, statistical_data)

    else:
        print('Please enter a valid option')

def getStatistical_Data(analysis_type, statistical_data):
    
    #print('INSIDE STATISTICAL DATA')
    #print('ANALYSIS TYPE')
    #print(analysis_type)
    #print('STATISTICAL TYPE')
    #print(statistical_data)

    if statistical_data == 'mean':
        #print(statistics.mean([analysis_type]))
        print(phone_df.mean(0,True,True))
    elif statistical_data == 'median':
        #print(statistics.median([analysis_type]))
        print(phone_df.median(0,True,True))
    elif statistical_data == 'mode':
        #print(statistics.mode([analysis_type]))
        print(phone_df.mode(0,True))
    elif statistical_data == 'max':
        print(phone_df.max(0,True, True))
    elif statistical_data == 'min':
        print(phone_df.min(0, True, True))
    else:
        print('Please enter valid option')

def userOptions():
    global quit

    print("""Welcome to the Phone Prices Data Explorer!
          
    Please select an option:
    1 - Show the original dataset
    2 - Show the updated Data Frame
    3 - Analyse the Mean, Median, or Mode of given data
    4 - Visualise phone prices by brand
    5 - Quit Program
        """)
    
    try:
        choice = int(input('Enter Selection: '))

        if choice == 1:
            getOriginalData()
        elif choice == 2:
            getUpdatedData()
        elif choice == 3: 
            getAnalysis()
        elif choice == 4:
            getCharts()
        elif choice == 5:
            quit = True
        else:
            print('A number between 1 and 5, come on!')

    except Exception as err:
        print('error encountered:')
        print(f'caught {err=}, {type(err)=}')
        print('Enter a number, it is not that hard.')
   

while not quit:
    userOptions()
