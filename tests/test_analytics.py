import unittest
import analytics
from datetime import datetime
from utilities import build_demo_data


class TestAnalytics(unittest.TestCase):
    def setUp(self):
        self.habits = build_demo_data()

    def test_get_all_habits_returns_all_names(self):
        all_habit_names = analytics.get_all_habits(self.habits)

        for habit in self.habits:
            self.assertIn(habit.name, all_habit_names, "Test case failed:")

    def test_get_habit_details_returns_all_details(self):
        chosen_habit = self.habits[0]
        habit_details = analytics.get_habit_details(chosen_habit)
        attributes_to_check = [
            "name",
            "description",
            "periodicity",
            "created at",
            "completions",
        ]

        for attribute in attributes_to_check:
            self.assertIn(attribute, habit_details.lower(), "Test case failed:")

    def test_group_habits_by_periodicity_returns_all_periodicities(self):
        grouped_habits = analytics.group_habits_based_on_periodicity(self.habits)
        periodicities = ["daily", "weekly"]

        for periodicity in periodicities:
            self.assertIn(periodicity, grouped_habits.lower(), "Test case failed: ")

    def test_get_longest_streak_for_daily_habit_with_perfect_streak(self):
        chosen_habit = self.habits[0]
        streak = analytics.get_longest_streak_for_habit(chosen_habit)

        self.assertEqual(streak, 28, "Test case failed: ")

    def test_get_longest_streak_for_daily_habit_with_broken_streak(self):
        chosen_habit = self.habits[1]
        streak = analytics.get_longest_streak_for_habit(chosen_habit)

        self.assertEqual(streak, 14)
