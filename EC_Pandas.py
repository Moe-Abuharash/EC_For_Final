# Using the provided csv file and pandas dataframe, create a dataframe from the file.
# The csv file consists of 20 employees that have listed their preference to work on
# the given dates. Their preference range is from 1 - 13 (1 being the most preferred).
# Come up with the optimal solution that meets the staffing needs and employee preference.

# Constraints:

# Employees should only be scheduled to work two shifts (2 days)
# 3-4 employees per shift (ideally 3)

# Output should be presented in a way that is easy to read/understand - (excel sheet or pandas dataframe)

from os import name
import pandas as pd

file_object = open('Holiday Schedule Ranking 2019.csv', 'r')

data = pd.read_csv(file_object, index_col=0).T

file_object.close()

file_object = open('Holiday Schedule Ranking 2019.csv', 'r')

schedule = pd.read_csv(file_object, index_col=0)

for c in schedule.columns:
    schedule[c].values[:] = 0

print(schedule)

data['col_sum'] = data.apply(lambda x: x.sum(), axis=1)

print(data)

data = data.sort_values(by='col_sum', ascending=False)

data = data.T

print(data)

for date in data.columns:

    date_series = data[date].nsmallest(5, keep='all')
    slot_count = 0

    print(date)
    print(date_series)

    for x in date_series:

        # if schedule.loc[name] > 2:
        #   schedule.at[name, date] = 1
            slot_count += 1
        if slot_count == 3:
            break

schedule.replace(0, '', inplace=True)

schedule.to_csv('final_schedule.csv')

print('Done')
