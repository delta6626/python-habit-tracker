from uuid import uuid4
from datetime import datetime
from constants import Periodicity, PERIODICITY_DAY_COUNT


class Habit:
    """
    Stores the state and behavior of an individual habit.
    """

    def __init__(
        self,
        id: str | None,
        name: str,
        description: str,
        periodicity: Periodicity,
        created_at: datetime,
        completions: list[datetime],
    ):
        """
        Initialize a habit with all of its details.
        """

        self.id = id or str(uuid4())
        self.name = name
        self.description = description
        self.periodicity = periodicity
        self.created_at = created_at
        self.completions = completions

    def check_off_habit(self, check_off_datetime: datetime) -> None:
        """
        Record a completion for the habit.
        """

        self.completions.append(check_off_datetime)

    def get_current_period_number(self, datetime_of_check: datetime) -> int:
        """
        Calculate the ongoing period number for a habit, based on its
        creation date, periodicity and the provided datetime.
        """

        elapsed_days_since_creation = (datetime_of_check - self.created_at).days
        return (
            elapsed_days_since_creation // PERIODICITY_DAY_COUNT[self.periodicity]
        ) + 1
