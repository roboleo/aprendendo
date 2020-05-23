import utils
import sorts

bookshelf = utils.load_books('books_small.csv')
long_bookshelf = utils.load_books('books_large.csv')
print(len(long_bookshelf))

def by_title_ascending(book_a, book_b):
  title_a = book_a['title_lower']
  title_b = book_b['title_lower']
  for i in range(len(title_a)):
    if ord(title_a[i]) > ord(title_b[i]):
      return True
    elif ord(title_a[i]) < ord(title_b[i]):
      return False
  return True

def by_author_ascending(book_a, book_b):
  author_a = book_a['author_lower']
  author_b = book_b['author_lower']
  for i in range(len(author_a)):
    if ord(author_a[i]) > ord(author_b[i]):
      return True
    elif ord(author_a[i]) < ord(author_b[i]):
      return False
  return True

def by_total_lenght(book_a, book_b):
  sum_a = len(book_a['author_lower']) + len(book_a['title_lower'])
  sum_b = len(book_a['author_lower']) + len(book_a['title_lower'])
  return sum_a >= sum_b

# VERSION COPY
bookshelf_v1 = bookshelf.copy()
bookshelf_v2 = bookshelf.copy()
long_bookshelf_v1 = long_bookshelf.copy()

# SORTING
sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)
sort_2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)
sort_3 = sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2)-1,by_author_ascending)

#sort_4 = sorts.bubble_sort(long_bookshelf, long_bookshelf)
sort_4 = sorts.quicksort(long_bookshelf, 0, len(long_bookshelf)-1,by_total_lenght)
#SHOWING
for book in bookshelf_v2:
  print(book['author'])


