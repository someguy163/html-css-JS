import functools
a ,b = map(int , input().split())

# reduce

num_list = [3,2,8,1,6,7]


# max_num = function.__reduce__(lambda x ,y : x if x>y else y ,num_list)
max_num = functools.reduce(lambda  x ,y : x if x>y else y ,num_list)


print(max_num)