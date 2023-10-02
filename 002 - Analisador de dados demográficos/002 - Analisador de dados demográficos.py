import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male'] ['age'].mean(), 2)

    # What is the percentage of people who have a Bachelor's degree?
    bachelors_degree = df[df['education'] == 'Bachelors']
    total_degree = df['education']
    percentage_bachelors = round((len(bachelors_degree) / len(total_degree)) *100, 2)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # percentage with salary >50K
    higher_50k = higher_education[higher_education.salary == '>50K']
    lower_50k = lower_education[lower_education.salary == '>50K']
    higher_education_rich = round((len(higher_50k) / len(higher_education)) * 100, 2)
    lower_education_rich = round((len(lower_50k) / len(lower_education)) * 100, 2)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min = df[df['hours-per-week'] == min_work_hours]
    num_min_workers = len(num_min)

    num_min_rich = num_min[num_min.salary == '>50K']
    rich_percentage = round((len(num_min_rich) / num_min_workers) * 100, 2)

    # What country has the highest percentage of people that earn >50K?
    total_country = df['native-country'].value_counts()
    m50k = df[df['salary'] == '>50K']
    count_country = m50k['native-country'].value_counts()
    cc_tc = (count_country / total_country)

    highest_earning_country = cc_tc.idxmax()
    highest_earning_country_percentage = round((cc_tc.max()) * 100, 2)

    # Identify the most popular occupation for those who earn >50K in India.
    india_pop = df.loc[df['native-country'] == 'India']
    india_pop_50 = india_pop[india_pop.salary == '>50K']
    occupation_india = india_pop_50['occupation'].value_counts()
    top_IN_occupation = occupation_india.idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

calculate_demographic_data()