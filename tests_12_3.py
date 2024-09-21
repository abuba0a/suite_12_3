import unittest
import HumanMoveTest_1
import Runner_1 as runner
from unittest import TestCase


class TournamentTest(TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = HumanMoveTest_1.Runner('Усэйн', 10)
        self.runner_2 = HumanMoveTest_1.Runner('Андрей', 9)
        self.runner_3 = HumanMoveTest_1.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for test_key, test_value in cls.all_results.items():
            key_position = 1
            for key, value in test_value.items():
                key_position += 1

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_turn_1(self):
        turn_1 = HumanMoveTest_1.Tournament(90, self.runner_1, self.runner_3)
        result = turn_1.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        print(f'{result}')

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_turn_2(self):
        turn_2 = HumanMoveTest_1.Tournament(90, self.runner_2, self.runner_3)
        result = turn_2.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        print(f'{result}')

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_turn_3(self):
        turn_3 = HumanMoveTest_1.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        result = turn_3.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        print(f'{result}')


TournamentTest()


class RunnerTest(TestCase):
    is_frozen = False

    @unittest.skipUnless(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner_1 = runner.Runner('1')
        for i in range(10):
            runner_1.walk()
        self.assertEqual(runner_1.distance, 50)

    @unittest.skipUnless(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner_2 = runner.Runner('2')
        for i in range(10):
            runner_2.run()
        self.assertEqual(runner_2.distance, 100)

    @unittest.skipUnless(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner_1 = runner.Runner('1')
        runner_2 = runner.Runner('2')
        for i in range(10):
            runner_1.run()
        for i in range(10):
            runner_2.walk()
        self.assertNotEqual(runner_1.distance, runner_2.distance)


RunnerTest()
