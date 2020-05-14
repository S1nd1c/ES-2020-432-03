import datetime
from unittest.mock import Mock

# Save a couple of test days
friday = datetime.datetime(year=2020, month=5, day=15)
saturday = datetime.datetime(year=2020, month=5, day=16)

# Mock datetime to control today's date
datetime = Mock()

def is_weekday():
    today = datetime.datetime.today()
    # Monday == 0, Sunday == 6
    return (0 <= today.weekday() < 5)

# Mock --> tuesday
datetime.datetime.today.return_value = friday
assert is_weekday()
# Mock --> saturday
datetime.datetime.today.return_value = saturday
assert not is_weekday()