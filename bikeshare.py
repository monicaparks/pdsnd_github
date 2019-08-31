import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
DAYS = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']

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

    city = input("Please enter the city whose data you'd like to explore (Chicago, New York City, Washington): ").lower()
    while city not in ['chicago', 'new york city', 'washington']:
        city = input("Oops, that's not a valid city. Please enter the city whose data you'd like to explore (Chicago, New York, Washington): ").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Please enter the month whose data you'd like to explore (January, February, March, April, May, June, or ALL): ").lower()
    while month not in MONTHS:
        month = input("Oops, that's not a valid month. Please enter the month whose data you'd like to explore (January, February, March, April, May, June, or ALL): ").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please enter the day of the week whose data you'd like to explore (Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or ALL): ").lower()
    while day not in DAYS:
        day = input("Oops, that's not a valid month. Please enter the day of the week whose data you'd like to explore (Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or ALL): ").lower()

    print("Thank you. Filtering data by: City: ",city.title(),", Month(s): ", month.title(),", Day(s): ", day.title(), ".")
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

    # Read in data file
    df = pd.read_csv(CITY_DATA[city])

    # Convert start time to timestamp
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Separate and filter by month
    df['month'] = df['Start Time'].dt.month
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = MONTHS.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # Separate and filter by day
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print("The most popular month for travel was: " + MONTHS[popular_month-1].title())
    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("The most popular day for travel was: " + popular_day)
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("The most popular hour to start travel was: " + str(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    print("The most popular start station was: " + popular_start)

    # TO DO: display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    print("The most popular end station was: " + popular_end)

    # TO DO: display most frequent combination of start station and end station trip
    combination = (df['Start Station'] + " to " + df['End Station']).mode()[0]
    print("The most popular trip combination was: " + str(combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    duration = df['Trip Duration'].sum()
    print("The total travel time (in seconds) was: " + str(duration))

    # TO DO: display mean travel time
    mean = df['Trip Duration'].mean()
    print("The mean travel time (in seconds) was: " + str(mean))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    users = df['User Type'].value_counts()
    print("The different users and their counts are: \n" + str(users))
    print("\n")

    # TO DO: Display counts of gender
    if city == 'chicago.csv' or city == 'new_york_city.csv':
        gender = df['Gender'].value_counts()
        print("The different genders and their counts are: \n" + str(gender))
        print("\n")

    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth = int(df['Birth Year'].min())
        recent_birth = int(df['Birth Year'].max())
        common_birth = df['Birth Year'].mode()[0]
        common_birth = int(common_birth)
        print("The earliest birth year was: " + str(earliest_birth))
        print("The most recent birth year was: " + str(recent_birth))
        print("The most common birth year was: " + str(common_birth))

    else:
        print("Sorry, no gender or birth data available\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
