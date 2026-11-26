# def callback(num) :
#     #global count
#     num -= 1
#     if(num == 0) :
#         print("Count Reached zero. Stopping executed.")
#         return
#     print("callback function executed. count",num)
#     callback(num)
#     print("callback function executed. count",num)

# callback(3)

# # 1에서 10까지 더하기
def add_numbers(start, end) :
    if end <= start :
        return 1
    return end + add_numbers(start, end-1)

print(add_numbers(1, 10))

# def add_number(start, end) :
#     foo = ((start + end) * end) / 2
#     print("foo:", foo)

# add_number(1,10000000)

def factorial(n) :
    if n <= 0:
        return 1
    print("n:",n)
    foo = factorial(n-1)
    print("n:",n)
    return n * foo

print(factorial(5))
########################################
# def countdown(n) :
#     if n <= 0:
#         print("발사!!!")
#         return
#     print(n)
#     countdown(n-1)

def countdown(n) :
    for i in range(n,0,-1) :
        print(i)
    print("발사!!!")

countdown(5)

def print_stars(n) :
    if n <= 0 :
        return
    print("*" * n)
    print_stars(n - 1)

print_stars(5)

# 9x9 구구단 출력
def mutiplication_table() :
    for i in range(1, 10) :
        for j in range(1, 10) :
                print(f"{i} x {j} = {i * j}")
        print()
mutiplication_table()

def power(base,exponent) :
    if exponent == 0 :
        return 1
    return base * power(base, exponent - 1)

power(1,4)

def arr_sum(arr,n) :
    if n <= 0:
        return 0
    return arr[n - 1] + arr_sum(arr, n - 1)

arr = [1, 2, 3, 4, 5]
print(arr_sum(arr,5))