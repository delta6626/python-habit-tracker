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
        chosen_habit.check_off_habit(datetime.now())
        chosen_habit.check_off_habit(datetime.now() + timedelta(days=1))

        self.assertEqual(
            len(chosen_habit.completions),
            30,
            "Test case failed: Habit completions are not being appended.",
        )
