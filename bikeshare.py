import time
import pandas as pd
import numpy as np

CITY_DATA = {   'washington': 'washington.csv',
                'chicago': 'chicago.csv',
                'new york': 'new_york_city.csv'
               }

#changes for refactoring branch
#declaring global strings
city_list = ['chicago','new york','washington']
months_list = ['','january','february','march','april','may','june']
day_list = ['','monday','tuesday','wednesday','thusday','friday','satday','sunday']
preference_list = ['number','words']
error = '------------- Did you select the correct option -------------\n'
output_error = '------------- There is no information for the inputs you have provided -------------\n'
blank = '------------- Leave blank to select all the options provided -------------\n'
dash_len = '------------------------------------------------------------------------------------------------------------------------'
tips = '------------- Remember to type complete words than numbers -------------'
def get_filters():

    print('Hello! Let\'s explore some US bikeshare data!')
    #get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
            
    while True :
        city = input('Select the city you need to see the data for: \n1.Chicago \n2.New York \n3.Wishington \n'+str(blank)).lower()
        if city not in city_list:
            print ( error )
            continue
        else:
            print('********* You have selected ',city,' *********')
            break
                


    #get user input for month (all, january, february, ... , june)
    while True :
        month = input('Which month you want to select for the data to be displayed: \n1.January \n2.February \n3.March \n4.April \n5.May \n6.June \n'+blank).lower()
        if month not in months_list:
            print ( error )
            continue
        else:
            break


    #get user input for day of week (all, monday, tuesday, ... sunday)
    while True :
        day = input('Which day you wnat to select for the data to be displayed: \n1.Monday \n2.Tuesday \n3.Wednesday \n4.Thursday \n5.Friday \n6.Saturday \n7.Sunday \n'+blank).lower()
        if day not in day_list:
            print ( error )
            continue
        else:
            break
             

    print(dash_len)
    return city, month, day


def load_data(city, month, day):
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != '':
        # use the index of the months list to get the corresponding int
        month = months_list.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != '':
        
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    #Displays statistics on the most frequent times of travel.

    print('\nCalculating most frequent times of travel from the data...\n')
    start_time = time.time()

    #display the most common month
    frequent_month= df['month'].mode()[0]
    print('Common Month:',frequent_month)

    #display the most common day of week
    frequent_day= df['day'].mode()[0]
    print('Common Day:',frequent_day)

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    
    #display the most common start hour
    rush_hour = df['hour'].mode()[0]
    print('Rush Hour:',rush_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))    
    print(dash_len)



def station_stats(df):
    #Displays statistics on the most popular stations and trip.
    start_time = time.time()

    print('\nCalculating most frequent stations and trip...\n')

    #display most commonly used start station
    frequent_start_station=df["Start Station"].mode()[0]
    print (frequent_start_station)


    # display most commonly used end station
    frequent_end_station=df["End Station"].mode()[0]
    print (frequent_end_station)


    #display most frequent combination of start station and end station trip
    frequent_trips= df.groupby(['Start Station','End Station']).count().idxmax().head(1)
    print('The most frequent start station and end station trip : \n',frequent_trips)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print(dash_len)

def trip_duration_stats(df):
    #Displays statistics on the total and average trip duration.

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    #display total travel time
    travel_duration = df['Trip Duration'].count()
    print('Total travel time',travel_duration)


    #display mean travel time
    mean_travel_duration = df['Trip Duration'].mean()
    print('Mean travel time',mean_travel_duration)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print(dash_len)



def user_stats(df):
    #Displays statistics on bikeshare users.
    start_time = time.time()

    print('\nCalculating User Stats...\n')

    #Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User_types: \n', user_types)

    #Display counts of gender

    try:
        Gender = df['Gender'].value_counts()
        print('Gender:\n',Gender)
    except KeyError :
        print ( 'Gender: ',output_error)

    #Display earliest, most recent, and most common year of birth
    try:
        earliest = df['Birth Year'].max()
        most_recent = df['Birth Year'].min()
        most_common_year = df['Birth Year'].mode()
        print ('\n\nEarliest year of birth:',earliest,'\n Most recent year of birth:',most_recent,'\n Common year of birth:',most_common_year)
    except KeyError :
        print ( 'Birth of yesr: ',output_error)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print(dash_len)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)


        show_data = input('\nWould you like to see the raw data? Enter yes\n')
        start = 0
        end = 5
        while show_data.lower() == 'yes':
            print(df.iloc[start:end])
            show_data1 = input('\nWould you like to see the raw data again? Enter yes.\n')
            if show_data1.lower() == 'yes':
                start+= 5
                end += 5
            else:
                break



        restart = input('\nWould you like to restart? Enter yes.\n')
        if restart.lower() != 'yes':
            break




if __name__ == "__main__":
   main()