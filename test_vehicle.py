import unittest
import vehicle

class TestVehicle(unittest.TestCase):
    def test_move(self):
        with self.subTest('Move up and down'):
            v = vehicle.Vehicle('t')
            v.add_pos(0,0)
            v.add_pos(0,1)
            v.move(1)

            self.assertEqual(v.pos[0][0], 0)
            self.assertEqual(v.pos[1][0], 0)
            
            self.assertEqual(v.pos[0][1], 1)
            self.assertEqual(v.pos[1][1], 2)

            v.move(-1)
            self.assertEqual(v.pos[0][0], 0)
            self.assertEqual(v.pos[1][0], 0)
            
            self.assertEqual(v.pos[0][1], 0)
            self.assertEqual(v.pos[1][1], 1)

        with self.subTest('Move left and right'):
            v = vehicle.Vehicle('t')
            v.add_pos(0,0)
            v.add_pos(1,0)
            v.move(1)
            self.assertEqual(v.pos[0][0], 1)
            self.assertEqual(v.pos[1][0], 2)
            
            self.assertEqual(v.pos[0][1], 0)
            self.assertEqual(v.pos[1][1], 0)

            v.move(-1)
            self.assertEqual(v.pos[0][0], 0)
            self.assertEqual(v.pos[1][0], 1)
            
            self.assertEqual(v.pos[0][1], 0)
            self.assertEqual(v.pos[1][1], 0)
if __name__ == '__main__':
    unittest.main()            