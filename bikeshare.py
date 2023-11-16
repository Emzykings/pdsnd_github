import time
import pandas as pd
import numpy as np
import json

from user_input import get_user_input

CITY_DATA = {'chicago': 'chicago.csv',
             'new york': 'new_york_city.csv',
             'washington': 'washington.csv'}

CITIES = ['chicago', 'new york', 'washington']

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']

DAYS = ['sunday', 'monday', 'tuesday', 'wednesday',
        'thursday', 'friday', 'saturday']


def get_user_filters():
    """
    Obtain user input for city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" for no month filter
        (str) day - name of the day of the week to filter by, or "all" for no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    while True:
        city = input('Which city do you want to explore: Chicago, New York, or Washington? \n> ').lower()
        if city in CITIES:
            break

    month = get_user_input('Provide a month name or \'all\' for no month filter.\n(e.g., all, january, february, ...)\n> ', MONTHS)

    day = get_user_input('Type a day of the week or \'all\' for no day filter.\n(e.g., all, monday, sunday)\n> ', DAYS)

    print('-' * 40)
    return city, month, day


def load_and_filter_data(city, month, day):
    """
    Load and filter data for the specified city, month, and day.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" for no month filter
        (str) day - name of the day of the week to filter by, or "all" for no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        month_index = MONTHS.index(month) + 1
        df = df[df['month'] == month_index]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_statistics(df):
    """Display statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    most_common_month = df['month'].value_counts().idxmax()
    print("The most common month is:", most_common_month)

    most_common_day_of_week = df['day_of_week'].value_counts().idxmax()
    print("The most common day of the week is:", most_common_day_of_week)

    most_common_start_hour = df['hour'].value_counts().idxmax()
    print("The most common start hour is:", most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_statistics(df):
    """Display statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    most_common_start_station = df['Start Station'].value_counts().idxmax()
    print("The most commonly used start station:", most_common_start_station)

    most_common_end_station = df['End Station'].value_counts().idxmax()
    print("The most commonly used end station:", most_common_end_station)

    most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most commonly used start station and end station: {}, {}"
          .format(most_common_start_end_station[0], most_common_start_end_station[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_statistics(df):
    """Display statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time:", total_travel_time)

    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time:", mean_travel_time)

    max_travel_time = df['Trip Duration'].max()
    print("Max travel time:", max_travel_time)

    print("Travel time for each user type:\n")
    group_by_user_trip = df.groupby(['User Type']).sum()['Trip Duration']
    for index, user_trip in enumerate(group_by_user_trip):
        print("  {}: {}".format(group_by_user_trip.index[index], user_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_statistics(df):
    """Display statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    print("Counts of user types:\n")
    user_counts = df['User Type'].value_counts()
    for index, user_count in enumerate(user_counts):
        print("  {}: {}".format(user_counts.index[index], user_count))

    print()

    if 'Gender' in df.columns:
        user_stats_gender(df)

    if 'Birth Year' in df.columns:
        user_stats_birth(df)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats_gender(df):
    """Display statistics of analysis based on the gender of bikeshare users."""
    print("Counts of gender:\n")
    gender_counts = df['Gender'].value_counts()
    for index, gender_count in enumerate(gender_counts):
        print("  {}: {}".format(gender_counts.index[index], gender_count))

    print()


def user_stats_birth(df):
    """Display statistics of analysis based on the birth years of bikeshare users."""
    birth_year = df['Birth Year']
    most_common_year = birth_year.value_counts().idxmax()
    print("The most common birth year:", most_common_year)
    most_recent = birth_year.max()
    print("The most recent birth year:", most_recent)
    earliest_year = birth_year.min()
    print("The most earliest birth year:", earliest_year)


def table_statistics(df, city):
    """Display statistics on bikeshare users."""
    print('\nCalculating Dataset Stats...\n')

    number_of_missing_values = np.count_nonzero(df.isnull())
    print("The number of missing

 values in the {} dataset : {}".format(city, number_of_missing_values))

    number_of_nonzero = np.count_nonzero(df['User Type'].isnull())
    print("The number of missing values in the \'User Type\' column: {}".format(number_of_nonzero))


def display_data(df):
    """Display raw bikeshare data."""
    row_length = df.shape[0]

    for i in range(0, row_length, 5):
        yes = input('\nWould you like to examine the particular user trip data? Type \'yes\' or \'no\'\n> ')
        if yes.lower() != 'yes':
            break

        row_data = df.iloc[i: i + 5].to_json(orient='records', lines=True).split('\n')
        for row in row_data:
            parsed_row = json.loads(row)
            json_row = json.dumps(parsed_row, indent=2)
            print(json_row)


def main():
    while True:
        city, month, day = get_user_filters()
        df = load_and_filter_data(city, month, day)

        time_statistics(df)
        station_statistics(df)
        trip_duration_statistics(df)
        user_statistics(df)
        table_statistics(df, city)

        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
