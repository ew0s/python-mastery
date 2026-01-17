import csv


class RowWithSlots:
    __slots__ = ['route', 'date', 'daytype', 'rides']

    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


def read_rides_as_class_with_slots(filename):
    """
        Read the bus ride data as class with slots
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
            record = RowWithSlots(route, date, daytype, rides)
            records.append(record)
    return records

if __name__ == '__main__':
    import tracemalloc
    tracemalloc.start()
    rows = read_rides_as_class_with_slots('../../Data/ctabus.csv')
    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())