import unittest
import tests_12_3


RT_test = unittest.TestSuite()
RT_test.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
RT_test.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(RT_test)
