from uuid import uuid4
from datetime import datetime
from constants import Periodicity, PERIODICITY_DAY_COUNT


class Habit:
    def __init__(
        self,
        id: str | None,
        name: str,
        description: str,
        periodicity: Periodicity,
        created_at: datetime,
        completions: list[datetime],
    ):
        self.id = id or str(uuid4())
        self.name = name
        self.description = description
        self.periodicity = periodicity
        self.created_at = created_at
        self.completions = completions

    def check_off_habit(self, check_off_datetime: datetime) -> None:
        self.completions.append(check_off_datetime)

    def get_elapsed_periods(self, datetime_of_check: datetime) -> int:
        elapsed_days_since_creation = (datetime_of_check - self.created_at).days
        return elapsed_days_since_creation // PERIODICITY_DAY_COUNT[self.periodicity]
