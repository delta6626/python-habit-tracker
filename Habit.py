from typing import Literal
from datetime import datetime, timedelta

Periodicity = Literal["daily", "weekly"]

periodicity_day_count:dict[Periodicity, int] = {
    "daily": 1,
    "weekly":7
}

class Habit:
    def __init__(self, name:str, periodicity:Periodicity, created_at:datetime, completions:list[datetime]):
        self.name = name
        self.periodicity = periodicity
        self.created_at = created_at
        self.completions = completions

    def complete_habit(self)->None:
        self.completions.append(datetime.now())

    def is_streak_broken(self, datetime_of_check:datetime)->bool:
        elapsed_days_since_creation = (datetime_of_check - self.created_at).days
        completed_periods = elapsed_days_since_creation // periodicity_day_count[self.periodicity]

        if completed_periods > 0 and len(self.completions) == 0:
            return True

        for i in range(0, completed_periods):
            period_start = self.created_at + timedelta(days = periodicity_day_count[self.periodicity] * i)
            period_end = self.created_at + timedelta(days = periodicity_day_count[self.periodicity] * (i+1))

            has_completion_for_current_period = False

            for completion in self.completions:
                if period_start <= completion < period_end:
                    has_completion_for_current_period = True
                    break

            if not has_completion_for_current_period:
                return True

        return False

    def get_current_streak(self):
        pass