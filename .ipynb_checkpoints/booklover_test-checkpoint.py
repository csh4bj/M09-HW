import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        test_object = BookLover("Cameron Her", "csh4bj@virginia.edu", "Mystery")
        test_object.add_book("A Study in Scarlet", 5)
        
        self.assertTrue("A Study in Scarlet" in test_object.book_list['book_name'].values)

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        test_object = BookLover("Cameron Her", "csh4bj@virginia.edu", "Mystery")
        test_object.add_book("A Study in Scarlet", 5)
        test_object.add_book("A Study in Scarlet", 5)
        
        book_count = sum(test_object.book_list['book_name'] == "A Study in Scarlet")
        expected = 1
        self.assertEqual(book_count, expected)
        
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        test_object = BookLover("Cameron Her", "csh4bj@virginia.edu", "Mystery")
        test_object.add_book("A Study in Scarlet", 5)     
        
        self.assertTrue(test_object.has_read("A Study in Scarlet"))
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        # pass a book in the list and test if the answer is `True`.
        test_object = BookLover("Cameron Her", "csh4bj@virginia.edu", "Mystery")
        test_object.add_book("A Study in Scarlet", 5) 
        
        self.assertFalse(test_object.has_read("A Court of Thorns and Roses"))
        self.assertTrue(test_object.has_read("A Study in Scarlet"))
                        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        test_object = BookLover("Cameron Her", "csh4bj@virginia.edu", "Mystery")
        test_object.add_book("A Study in Scarlet", 5)
        test_object.add_book("In Cold Blood", 3)
        test_object.add_book("Tell No One", 4)
        test_object.add_book("Murder on Orient Express", 2)
        
        expected = 4
        self.assertEqual(test_object.num_books_read(), expected)
        
    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating >3 
        # Your test should check that the returned books have rating  >3
        
        test_object = BookLover("Cameron Her", "csh4bj@virginia.edu", "Mystery")
        test_object.add_book("A Study in Scarlet", 5)
        test_object.add_book("In Cold Blood", 3)
        test_object.add_book("Tell No One", 4)
        test_object.add_book("Murder on Orient Express", 2)  
        
        self.assertTrue((test_object.fav_books()["book_rating"]>3).all())
        
if __name__ == '__main__':
    
    unittest.main(verbosity=3)