from enum import Enum, auto

class WeekStr:
    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"

def is_weekend_str(week_day):
    return week_day == WeekStr.SATURDAY or week_day == WeekStr.SUNDAY



class AutoName (Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name

class Color(AutoName):
    BLUE = auto()
    GREEN = auto()
    RED = auto()

blue = Color.BLUE
green = Color.GREEN
print(blue.name, blue.value)
print(green.name, green.value)


#
# class Week(Enum):
#     MONDAY = 1
#     TUESDAY = 2
#     WEDNESDAY = 3
#     THURSDAY = 4
#     FRIDAY = 5
#     SATURDAY = 6
#     SUNDAY = 7
#
#     def is_weekend_(self):
#         return self.value >5
#
#     def is_earlier_in_week(self, other_day):
#         return self.value < other_day.value
#
# monday = Week.MONDAY
# saturday = Week.SATURDAY
# print(monday.is_weekend_())
# print(saturday.is_weekend_())