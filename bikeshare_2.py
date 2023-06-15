"""
Submitted by: Annabel
Date: 13th June, 2023
"""

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
              

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\n')
    print('Hello! Let\'s explore some US bikeshare data!')

    # Get user input for city (chicago, new york city, washington). Handle invalid inputs.

    while True:
        city = input("Please enter the name of the city (chicago, new york city, washington): ").lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print("Invalid city! Please try again.")
    print('\n')
    month = None
    day = None
    while True:
        filter_value = input("Would you like to filter the data by month, day, both or not at all? Type none for no time filter:").lower()

        if filter_value in ['month', 'day', 'both', 'none']:
            if filter_value == 'month':
                # Get user input for month (all, january, february, ..., june)
                while True:
                    month = input("\nWhich month? (january, february, ..., june): ").lower()
                    if month in ['january', 'february', 'march', 'april', 'may', 'june']:
                        break
                    else:
                        print("Invalid month! Please try again.")

            elif filter_value == 'day':
                # Get user input for day of week (all, monday, tuesday, ..., sunday)
                while True:
                    day = input("\nWhich day? (monday, tuesday, wednesday, thursday, friday, saturday, sunday): ").lower()
                    if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
                        break
                    else:
                        print("Invalid day! Please try again.")
            elif filter_value == 'both':
                # Get user input for month (all, january, february, ..., june)
                while True:
                    month = input("\nWhich month? (january, february, ..., june): ").lower()
                    if month in ['january', 'february', 'march', 'april', 'may', 'june']:
                        break
                    else:
                        print("Invalid month! Please try again.")

                # Get user input for day of week (all, monday, tuesday, ..., sunday)
                while True:
                    day = input("\nWhich day? (monday, tuesday, wednesday, thursday, friday, saturday, sunday): ").lower()
                    if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
                        break
                    else:
                        print("Invalid day! Please try again.")
            else:
                print(' ')
            break
        else:
            print("Invalid input! Please try again.")
              
    print('\n')
    print('-'*40)
    
    return city, month, day,filter_value

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != None:
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if  day != None:
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    month_count = df['month'].value_counts()[popular_month]
    print('Most Popular Month:', popular_month, ', Count:', month_count)


    # Display the most common day of the week
    df['day_of_week'] = df['Start Time'].dt.day_name()
    popular_day = df['day_of_week'].mode()[0]
    day_count = df['day_of_week'].value_counts()[popular_day]
    print('Most Popular Day of Week:', popular_day, ', Count:', day_count)

    # Display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    hour_count = df['hour'].value_counts()[popular_hour]
    print('Most Popular Start Hour:', popular_hour, ', Count:', hour_count)

    print("\nTime stats took %s seconds.\n" % (time.time() - start_time))
    print('-'*40)
    
    
    
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    start_time1 = time.time()
    # Display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    start_station_count = df['Start Station'].value_counts()[popular_start_station]
    print('Most Commonly Used Start Station:', popular_start_station, ', Count:', start_station_count)
    print("This took %s seconds." % (time.time() - start_time1))
    print('\n')
   
    start_time2 = time.time()
    # Display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    end_station_count = df['End Station'].value_counts()[popular_end_station]
    print('Most Commonly Used End Station:', popular_end_station, ', Count:', end_station_count)
    print("This took %s seconds." % (time.time() - start_time2))
    print('\n')

    start_time3 = time.time()
    # Display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + ' to ' + df['End Station']
    popular_trip = df['Trip'].mode()[0]
    trip_count = df['Trip'].value_counts()[popular_trip]
    print('Most Frequent Trip:', popular_trip, ', Count:', trip_count)
    print("This took %s seconds." % (time.time() - start_time3))

    print("\n Staion stats took total of %s seconds.\n" % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # find total travel time
    total_travel_time = float(df['Trip Duration'].sum())

    # find mean travel time
    mean_travel_time = float(df['Trip Duration'].mean())

    #find count
    trip_duration_count = df['Trip Duration'].value_counts().sum()
    
    #Display total travel time, Counting and Avg travel time
    print('Total Duration:', total_travel_time, ', Count: ',trip_duration_count, ', Average Duration:', mean_travel_time)
    print("\nTrip duration stats took total of %s seconds.\n" % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    start_time1 = time.time()
    # Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    print('Counts of User Types:\n', user_type_counts)
    print("This took %s seconds." % (time.time() - start_time1))
    print('\n')
    
    start_time2 = time.time()
    # Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print('Counts of Gender:\n', gender_counts)

    else:
        print('Gender information is not available for this dataset.')
    print("This took %s seconds." % (time.time() - start_time2))
    print('\n')
    
    
    start_time3 = time.time()
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth_year = df['Birth Year'].min()
        print('Earliest Birth Year:', int(earliest_birth_year))

        most_recent_birth_year = df['Birth Year'].max()
        print('Most Recent Birth Year:', int(most_recent_birth_year))

        most_common_birth_year = df['Birth Year'].mode()[0]
        print('Most Common Birth Year:', int(most_common_birth_year))
    else:
        print('Birth year information is not available for this dataset.')
    print("This took %s seconds." % (time.time() - start_time3))

    print("\nUser stats took total of %s seconds.\n" % (time.time() - start_time))
    print('-'*40)

def main():
   

   while True:
    
        option=input('\n\n****************************************MAIN MENU****************************************n\n1- See raw data. \n2- View stats after filtering the records. \n...Press any other key to quit\n\nEnter your choice: ')
        
        # Prompt the user to see raw data
        if option=='1':
            while True:
                city = input("Please enter the name of the city (chicago, new york city, washington): ").lower()
                if city in ['chicago', 'new york city', 'washington']:
                    break
                else:
                    print("Invalid city! Please try again.")
            df_raw = pd.read_csv(CITY_DATA[city])
            start_row = 0
            print(df_raw.iloc[start_row:start_row + 5])
            start_row += 5
            while True:
                print('-'*40)
                show_raw_data = input('\nWould you like to see 5 more lines of raw data?\n \nYES -> continue checking stats \nNO -> go to main menu \n(Press any other key to quit)\n\n Enter your choice: ')
                if show_raw_data.lower() == 'yes':
                    # Display 5 lines of raw data
                    print(df_raw.iloc[start_row:start_row + 5])
                    start_row += 5
                elif show_raw_data.lower() == 'no':
                    main()
                else:
                    print('\n\n')
                    break

            
            
        if option=='2':    
            while True:
                city, month, day,filter_value = get_filters()
                print('ALL THE FOLLOWING STATS ARE CALCULATED WHEN THE FILTER IS APPLIED ON ', filter_value)
                print('-'*40)
                df = load_data(city, month, day)

                time_stats(df)
                station_stats(df)
                trip_duration_stats(df)
                user_stats(df)

                check_stats = input('\nWould you like to continue checking stats?\n \nYES -> continue checking stats \nNO -> go to main menu \n(Press any other key to quit) \n\n Enter your choice: ')
                if check_stats.lower() == 'no':
                    main()
                elif check_stats.lower() != 'yes' and check_stats.lower() != 'no':
                    quit()

        else:
            quit()
            
            
            

if __name__ == "__main__":
	main()
