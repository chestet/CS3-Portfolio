class Publication:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def get_title(self):
        print(f"Title: {self.title}")
    def get_author(self):
        print(f"Author: {self.author}")
    def set_title(self, title):
        self.title = title
    def set_author(self, author):
        self.author = author
    def display_info(self):
        self.get_title()
        self.get_author()

class Book(Publication):
    def __init__(self, title, author, number_of_pages):
        super().__init__(title, author)
        self.number_of_pages = number_of_pages
    def get_number_of_pages(self):
        return f"Number of pages: {self.number_of_pages}"
    def set_number_of_pages(self, number_of_pages):
        if number_of_pages > 0:
            self.number_of_pages = number_of_pages
        else:
            print("The number of pages must be positive.")
            
class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.issue_number = issue_number
    def get_issue_number(self):
        return f"Issue number: {self.issue_number}"
    def set_issue_number(self, issue_number):
        if issue_number > 0:
            self.issue_number = issue_number
        else:
            print("The issue number must be positive")

# Creating objects
pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = Magazine("National Geographic", "Various Authors", 202)

# Printing the information
print("Publication Information:")
pub1.display_info()

print("\nBook Information:")
book1.set_number_of_pages(-310)  # setting invalid value on attribute
book1.display_info()
print(book1.get_number_of_pages())

print("\nMagazine Information:")
mag1.display_info()
print(mag1.get_issue_number())
    
    
