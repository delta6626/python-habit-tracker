from uuid import uuid4
from typing import Literal
from datetime import datetime, timedelta

Periodicity = Literal["daily", "weekly"]

periodicity_day_count:dict[Periodicity, int] = {
    "daily": 1,
    "weekly":7
}

class Habit:
    def __init__(self, name:str, description:str, periodicity:Periodicity, created_at:datetime, completions:list[datetime]):
        self.id = str(uuid4())
        self.name = name
        self.description = description
        self.periodicity = periodicity
        self.created_at = created_at
        self.completions = completions

    def complete_habit(self)->None:
        self.completions.append(datetime.now())

    def get_elapsed_periods(self, datetime_of_check:datetime)->int:
         elapsed_days_since_creation = (datetime_of_check - self.created_at).days
         return elapsed_days_since_creation // periodicity_day_count[self.periodicity]