import unittest
from datetime import datetime, timedelta
from Habit import Habit


class TestHabit(unittest.TestCase):
    def test_habit_id_is_automatically_generated(self):
        habit = Habit(
            None, "Test habit", "Test habit description", "daily", datetime.now(), []
        )

        self.assertIsNotNone(
            habit.id, "Test case failed: Habit ID is NOT being generated automatically."
        )

    def test_provided_habit_id_is_preserved(self):
        habit_id = "test_id"
        habit = Habit(
            habit_id,
            "Test habit",
            "Test habit description",
            "daily",
            datetime.now(),
            [],
        )

        self.assertEqual(
            habit.id,
            habit_id,
            "Test case failed: Provided Habit id is NOT being preserved in Habit instance.",
        )

    def test_check_off_habit_appends_completion(self):
        habit = Habit(
            None, "Test habit", "Test habit description", "daily", datetime.now(), []
        )

        habit.check_off_habit(datetime.now())
        habit.check_off_habit(datetime.now() + timedelta(days=1))

        self.assertEqual(
            len(habit.completions),
            2,
            "Test case failed: Completions are NOT being appended as expected.",
        )
