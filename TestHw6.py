import unittest
from hw6 import find_zero, sort_halfsorted, bubble, selection, insertion
from TestHelpers import generate_halfsorted, is_sorted

# TODO: implement tests for sort_halfsorted


class Test_SortHalfSorted(unittest.TestCase):
    def test_halfsorted_bubble(self):
        # use sort_halfsorted(L, bubble) to test
        for pattern in ["random", "reverse", "sorted"]:
            with self.subTest(pattern=pattern):
                for n in range(1, 50):
                    with self.subTest(n=n):
                        for i in range(n):
                            with self.subTest(i=i):
                                # create different halfsorted lists
                                L, _ = generate_halfsorted(
                                    n, idx_zero=i, pattern=pattern
                                )

                                # Make a copy for comparison
                                L_copy = L.copy()

                                # Sort with bubble sort
                                sort_halfsorted(L, bubble)

                                # Compare the elements in the original list with the sorted
                                self.assertCountEqual(L, L_copy)

                                # Check if the list has been sorted
                                self.assertTrue(is_sorted(L))

    def test_halfsorted_selection(self):
        # use sort_halfsorted(L, selection) to test
        for pattern in ["random", "reverse", "sorted"]:
            with self.subTest(pattern=pattern):
                for n in range(1, 50):
                    with self.subTest(n=n):
                        for i in range(n):
                            with self.subTest(i=i):
                                # Create different halfsorted lists
                                L, _ = generate_halfsorted(
                                    n, idx_zero=i, pattern=pattern
                                )

                                # Make a copy for comparison
                                L_copy = L.copy()

                                # Sort with selection sort
                                sort_halfsorted(L, selection)

                                # Compare the elements in the list with the sorted
                                self.assertCountEqual(L, L_copy)

                                # Check if list has been sorted
                                self.assertTrue(is_sorted(L))

    def test_halfsorted_insertion(self):
        # use sort_halfsorted(L, insertion) to test
        for pattern in ["random", "reverse", "sorted"]:
            with self.subTest(pattern=pattern):
                for n in range(1, 50):
                    with self.subTest(n=n):
                        for i in range(n):
                            with self.subTest(i=i):
                                # Create different halfsorted lists
                                L, _ = generate_halfsorted(
                                    n, idx_zero=i, pattern=pattern
                                )

                                # Make a copy for comparison
                                L_copy = L.copy()

                                # Sort with insertion sort
                                sort_halfsorted(L, insertion)

                                # Compare the elements in the list with the sorted
                                self.assertCountEqual(L, L_copy)

                                # Check list has been sorted
                                self.assertTrue(L, is_sorted(L))


# Test provided for you
class Test_FindZero(unittest.TestCase):
    def test1_allLengthsAllIndices(self):
        """Tests find_zero for every possible index, for lists from 1 to 100 items

        Lists
        -----
           '-' and '+' denote negative and positive ingeters, respectively
                                idx_zero
           n = 1
              L = [0]           0

           n = 2
              L = [0, +]        0
              L = [-, 0]        1

           n = 3
              L = [0, +, +]     0
              L = [-, 0, +]     1
              L = [-, -, 0]     2

           n = 4
              L = [0, +, +, +]  0
              L = [-, 0, +, +]  1
              L = [-, -, 0, +]  2
              L = [-, -, -, 0]  3
           ...
           n = 100
              L = [0, ..., +]   0
              ...
              L = [-, ..., 0]   99
        """

        # note the use of `subTest`. These all count as 1 unittest if they pass,
        # but all that fail will be displayed independently
        for pattern in ["random", "reverse", "sorted"]:
            with self.subTest(pattern=pattern):
                for n in range(1, 50):
                    with self.subTest(n=n):
                        for i in range(n):
                            with self.subTest(i=i):
                                L, idx_zero = generate_halfsorted(
                                    n, idx_zero=i, pattern=pattern
                                )
                                self.assertEqual(find_zero(L), idx_zero)


unittest.main()
