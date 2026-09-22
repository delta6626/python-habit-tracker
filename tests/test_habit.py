import unittest
from datetime import datetime, timedelta
from Habit import Habit
from utilities import build_demo_data
from constants import RECORD_IDS


class TestHabit(unittest.TestCase):
    """
    Unittest test class for testing the Habit class.
    """

    def setUp(self):
        """
        Load the demo/testing data used by the test cases.
        """

        self.habits = build_demo_data()

    def test_habit_id_is_automatically_generated(self):
        """
        Check whether a habit ID is automatically generated when none is provided.
        """

        habit = Habit(
            None, "Test habit", "Test habit description", "daily", datetime.now(), []
        )

        self.assertIsNotNone(
            habit.id, "Test case failed: Habit ID is NOT being generated automatically."
        )

    def test_provided_habit_id_is_preserved(self):
        """
        Check whether a provided habit ID is preserved when creating a habit.
        """

        chosen_habit = self.habits[0]
        self.assertEqual(
            chosen_habit.id,
            RECORD_IDS[0],
            "Test case failed: Provided Habit ID is not being preserved.",
        )

    def test_check_off_habit_appends_completion(self):
        """
        Check whether checking off a habit appends the completion timestamp
        to its 'completions' list.
        """

        chosen_habit = self.habits[0]
        initial_count = len(chosen_habit.completions)
        chosen_habit.check_off_habit(datetime.now())
        chosen_habit.check_off_habit(datetime.now() + timedelta(days=1))

        self.assertEqual(
            len(chosen_habit.completions),
            initial_count + 2,
            "Test case failed: Habit completions are not being appended.",
        )

    def test_daily_habit_period_number_same_day(self):
        """
        Check whether a daily habit remains in the first period when the
        datetime used to check the habit is still within its creation day.
        """

        chosen_habit = self.habits[0]

        same_day_offsets = [
            timedelta(milliseconds=1),
            timedelta(seconds=1),
            timedelta(minutes=1),
            timedelta(hours=1),
        ]

        for offset in same_day_offsets:
            period = chosen_habit.get_current_period_number(
                chosen_habit.created_at + offset
            )

            self.assertEqual(
                period,
                1,
                "Test case failed: Habit period number changed within the same day of its creation.",
            )

    def test_daily_habit_period_number_next_day(self):
        """
        Check whether a daily habit moves to the second period when the
        datetime used to check the habit is one day after its creation date.
        """

        chosen_habit = self.habits[0]
        next_day_period_number = chosen_habit.get_current_period_number(
            chosen_habit.created_at + timedelta(days=1)
        )

        self.assertEqual(
            next_day_period_number,
            2,
            "Test case failed: Habit period number is incorrect on the day after its creation.",
        )

    def test_daily_habit_period_number_many_days_later(self):
        """
        Check whether the period number for a daily habit increases correctly
        when the datetime used to check the habit is several days after its
        creation date.
        """

        d = 7
        chosen_habit = self.habits[0]
        period_number = chosen_habit.get_current_period_number(
            chosen_habit.created_at + timedelta(days=d)
        )

        self.assertEqual(
            period_number,
            d + 1,
            "Test case failed: Habit period number is incorrect several days after its creation.",
        )

    def test_weekly_habit_period_number_same_week(self):
        """
        Check whether a weekly habit remains in the first period when the
        datetime used to check the habit is within the first week of its
        creation.
        """

        chosen_habit = self.habits[3]

        same_week_offsets = [
            timedelta(milliseconds=1),
            timedelta(seconds=1),
            timedelta(minutes=1),
            timedelta(hours=1),
            timedelta(days=1),
            timedelta(days=3),
            timedelta(days=6),
        ]

        for offset in same_week_offsets:
            period_number = chosen_habit.get_current_period_number(
                chosen_habit.created_at + offset
            )

        self.assertEqual(
            period_number,
            1,
            "Test case failed: Habit period number changed within the first week of its creation.",
        )

    def test_weekly_habit_period_number_next_week(self):
        """
        Check whether a weekly habit moves to the second period when the
        datetime used to check the habit is seven days after its creation date.
        """

        chosen_habit = self.habits[3]

        period_number = chosen_habit.get_current_period_number(
            chosen_habit.created_at + timedelta(days=7)
        )

        self.assertEqual(
            period_number,
            2,
            "Test case failed: Habit period number is incorrect in the week after its creation.",
        )

    def test_weekly_habit_period_number_many_weeks_later(self):
        """
        Check whether the period number for a weekly habit increases correctly
        when the datetime used to check the habit is several weeks after its
        creation date.
        """

        weeks = 3
        chosen_habit = self.habits[3]

        period_number = chosen_habit.get_current_period_number(
            chosen_habit.created_at + timedelta(days=weeks * 7)
        )

        self.assertEqual(
            period_number,
            weeks + 1,
            "Test case failed: Habit period number is incorrect several weeks after its creation.",
        )
