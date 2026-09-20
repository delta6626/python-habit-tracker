import unittest
from datetime import datetime, timedelta
from Habit import Habit
from utilities import build_demo_data
from constants import RECORD_IDS


class TestHabit(unittest.TestCase):
    def setUp(self):
        self.habits = build_demo_data()

    def test_habit_id_is_automatically_generated(self):
        habit = Habit(
            None, "Test habit", "Test habit description", "daily", datetime.now(), []
        )

        self.assertIsNotNone(
            habit.id, "Test case failed: Habit ID is NOT being generated automatically."
        )

    def test_provided_habit_id_is_preserved(self):
        chosen_habit = self.habits[0]
        self.assertEqual(
            chosen_habit.id,
            RECORD_IDS[0],
            "Test case failed: Provided Habit ID is not being preserved.",
        )

    def test_check_off_habit_appends_completion(self):
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
                "Test case failed: Daily habit current period number changed within the same day.",
            )

    def test_daily_habit_period_number_next_day(self):
        chosen_habit = self.habits[0]
        next_day_period_number = chosen_habit.get_current_period_number(
            chosen_habit.created_at + timedelta(days=1)
        )

        self.assertEqual(
            next_day_period_number,
            2,
            "Test case failed: Daily habit current period number is incorrect on the next day.",
        )

    def test_daily_habit_period_number_many_days_later(self):
        d = 7
        chosen_habit = self.habits[0]
        next_day_period_number = chosen_habit.get_current_period_number(
            chosen_habit.created_at + timedelta(days=d)
        )

        self.assertEqual(
            next_day_period_number,
            d + 1,
            "Test case failed: Daily habit current period number is incorrect several days later.",
        )
