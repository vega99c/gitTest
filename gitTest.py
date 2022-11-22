# print("git Test")
# print("hello world")
# print("Thied")

# mylist = [x*x for x in range(3)]
# for i in mylist:
#     print(i)

# for i in mylist:
#     print(i)

# mygenerator = (x*x for x in range(3))

# for i in mygenerator:
#     print(i)

# for i in mygenerator:
#     print(i)


# def create_generator():
#     mylist = range(3)
#     for i in mylist:
#         yield i*i

# mygenerator = create_generator()
# print(mygenerator)

# for i in mygenerator:
#     print(i)


from random import randint

def random_nunber_generator(n):
    count = 0
    while count < n:
        yield randint(1,100)
        count += 1

g = random_nunber_generator(5)

# print(g)

# print(next(g))
# print(next(g))
# print(next(g))

# print(next(g))
# print(next(g))
# print(next(g))

# h = random_nunber_generator(5)
# print(next(h))
# print(next(h))
# print(next(h))

# list1 = [1,2,3,4,5]
# iterator = iter(list1)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))


# print(next(iterator))
# print(next(iterator))
# # print(next(iterator))

# for i in iterator:    
#     print(i)



# def square(x):
#     return x * x

# def my_map(func, arg_list):
#     result = []
#     for i in arg_list:
#         result.append(func(i))
#     return result

# num_list = [1,2,3,4,5]

# squares = my_map(square, num_list)

# print(squares)

def simple_html_tag(tag, msg):
    print('<{0}>{1}<{0}>'.format(tag,msg))

simple_html_tag('h1', '심플 헤딩 타이틀')

print('-' * 30)


def html_tag(tag):
    def wrap_text(msg):
        print(print('<{0}>{1}<{0}>'.format(tag,msg)))

    return wrap_text


print_h1 = html_tag('h1')
print(print_h1)
print_h1('첫 번째 헤딩 타이틀')
print_h1('두 번째 헤딩 타이틀')

print_p = html_tag('p')
print_p('이것은 패러그래프 입니다.')



