import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january', 'february', 'march', 'april', 'may', 'june','all']
days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all' ]


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Please select one of the city: chicago, new york city or washington :").lower()
        if city in CITY_DATA:
            print(format(city), "is selected!")
            break
        else:
            print("It is invalid selection! Please select one of the city: chicago, new york city or washington!")
    
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Please select one of the months or all: january, february, march, april, may, june or all: ").lower()
        if month in months:
            print (format(month), "is selected!")
            break
        else:
            print("It is invalid selection! Please select one of the months or all: january, february, march, april, may, june or all")
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)  
    while True:
        day = input("Please select a day of the week or all: monday, tuesday, wednesday, thursday, friday, saturday, sunday or all: ").lower()
        if day in days:
            print(format(day), "is selected!")
            break
        else:
            print("It is invalid selection! Please select a day of the week or all: monday, tuesday, wednesday, thursday, friday, saturday, sunday or all!")

                
    print('-'*40)
    return city, month, day


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
    
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time']= pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['weekday'] = df['Start Time'].dt.weekday
    
    if month != 'all':
        month_name=['january','february','march','april','may','june']
        month= month_name.index(month)+ 1
        df=df[df['month'] == month]
    
    if day != 'all':
        day_name=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        day=day_name.index(day) + 1
        df=df[df['weekday']== day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month']=df['Start Time'].dt.month
    most_common_month = df['month'].mode()[0]
    print('Most common month', most_common_month)

    
    # TO DO: display the most common day of week
    most_common_day = df['weekday'].mode()[0]
    print('Most common day of week', most_common_day)

    
    # TO DO: display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    most_common_hour= df['hour'].mode()[0]
    print('Most common hour of the day', most_common_hour)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    
    # TO DO: display most commonly used start station
    common_start_station =df['Start Station'].mode().values[0]
    print('Most commonly used Start Station', common_start_station)

    
    # TO DO: display most commonly used end station
    common_end_station =df['End Station'].mode().values[0]
    print('Most commonly used End Station',common_end_station)

    
    # TO DO: display most frequent combination of start station and end station trip
    df['start_end'] = df['Start Station']+ 'to' + df['End Station']
    most_frequent = df['start_end'].mode().values[0]
    print('Most frequent start and stop station', most_frequent)

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    trip_duration = df['Trip Duration'].sum()
    print('Total Travel Time',trip_duration)

    # TO DO: display mean travel time
    mean_travel=df['Trip Duration'].mean()
    print('Mean Travel Time', mean_travel)

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    number_of_usertype = df['User Type'].value_counts()
    print('Count of User Types', number_of_usertype)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        number_of_gender = df['Gender'].value_counts()
        print('Count of Gender', number_of_gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        the_earliest= df['Birth Year'].min()
        most_recent=df['Birth Year'].max()
        most_common=df['Birth Year'].mode()[0]
        print('Earliest Bithday', the_earliest)
        print('Most Recent', most_recent)
        print('Most Common', most_common)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def display_data (df):
    """Ask if the user want to see the first 5 and the next 5 data"""
    
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while True:
        if view_data == 'no':
            break
        else:
            
            print(df.iloc[start_loc:start_loc+5])
            start_loc += 5
            view_data = input("Do you wish to continue?: ").lower() 
    
    
    
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)   

        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

    
    