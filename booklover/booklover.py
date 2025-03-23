import pandas as pd

class BookLover:
    def __init__(self, name, email, fav_genre):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = 0
        self.book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})
        
    def add_book(self, book_name, rating):
        if not (0 <= rating <= 5): 
            print(f"Error: The rating must be an integer 0 to 5. You input: {rating}")
            return
        if not self.book_list.empty and book_name in self.book_list['book_name'].values:
            print(f"{book_name} is already in the book list.")
        else:
            new_book = pd.DataFrame({
                'book_name': [book_name],
                'book_rating': [rating]
            })
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1
            
    def has_read(self, book_name):
        return book_name in self.book_list['book_name'].values
    
    def num_books_read( self):
        return self.num_books
    
    def fav_books(self):
        return self.book_list[self.book_list['book_rating'] > 3]
    

if __name__ == '__main__':
    
    test_object = BookLover("Cameron Her", "csh4bj@virginia.edu", "Mystery")
    test_object.add_book("A Study in Scarlet", 5)
    test_object.add_book("In Cold Blood", 3)
    test_object.add_book("Tell No One", 4)
    test_object.add_book("Murder on Orient Express", 2)    
    