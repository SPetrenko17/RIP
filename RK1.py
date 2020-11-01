# вариант запроса Д
# вариант предметной области 16 : книга - книжный магазин
from operator import itemgetter
from data.data import stores, one_to_many, many_to_many


def task1():
    print('Задание Д1')
    res1 = []
    for i in one_to_many:
        if i[0][-2:] == "er":
            res1.append(i[0:3:2])
    print(res1)


def task2():
    print('\nЗадание Д2')
    res2_unsorted = []
    for o in stores:
        o_books = list(filter(lambda i: i[2] == o.name, one_to_many))
        if len(o_books) > 0:
            o_pages = [pages for _, pages, _ in o_books]
            o_pages_sum = sum(o_pages)
            o_pages_count = len(o_pages)
            o_pages_average = o_pages_sum / o_pages_count
            res2_unsorted.append((o.name, int(o_pages_average)))
    res2 = sorted(res2_unsorted, key=itemgetter(1), reverse=True)
    print(res2)


def task3():
    print('\nЗадание Д3')
    res3 = {}
    for o in stores:
        if o.name[0] == "C":
            o_books = list(filter(lambda i: i[2] == o.name, many_to_many))
            o_books_titles = [x for x, _, _ in o_books]
            res3[o.name] = o_books_titles
    print(res3)


def main():
    task1()
    task2()
    task3()


if __name__ == '__main__':
    main()
