import csv
import typing
from collections import namedtuple


class Row(typing.NamedTuple):
    route: str
    date: str
    daytype: str
    rides: int


def read_rides_as_named_tuples(filename):
    """
        Read the bus ride data as named tuples
    """
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            records.append(Row(route, date, daytype, rides))
    return records


if __name__ == '__main__':
    import tracemalloc

    tracemalloc.start()
    rows = read_rides_as_named_tuples('../../Data/ctabus.csv')
    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
