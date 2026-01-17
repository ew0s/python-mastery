import tracemalloc
from collections import Counter, defaultdict
from pprint import pprint
from typing import List

from Exercises.ex2_1.read_rides_as_dictionary import read_rides_as_dictionary

if __name__ == '__main__':
    rows = read_rides_as_dictionary('../../Data/ctabus.csv')

    # Task 1
    routes_count = Counter(row['route'] for row in rows)
    pprint('There are {} routes in Chicago'.format(len(routes_count)))

    # Task 2
    sum_filtered_rides = sum(row['rides'] for row in rows if row['route'] == '22' and row['date'] == '02/02/2011')
    pprint('There are {} rides on route 22 at 02/02/2011'.format(sum_filtered_rides))

    # Task 3
    rides_count_by_route = Counter()
    for row in rows:
        rides_count_by_route[row['route']] += row['rides']

    for route, count in rides_count_by_route.most_common(3):
        pprint('There are {} rides on route {}'.format(count, route))

    # Task 4
    rides_by_year = defaultdict(Counter)
    for row in rows:
        year = row['date'].split('/')[2]
        rides_by_year[year][row['route']] += row['rides']

    diffs = rides_by_year['2011'] - rides_by_year['2001']
    for route, diff in diffs.most_common(5):
        print(route, diff)

