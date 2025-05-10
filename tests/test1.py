# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# driver = webdriver.Chrome()
# driver.get(
#     "https://v5.vost.pw/tip/tv/3408-a-rank-party-wo-ridatsu-shita-ore-wa-moto-oshiego-tachi-to-meikyuu-shinbu-wo-mezasu.html")
from setuptools.command.build_ext import if_dl


# def add_logs (func):
#     def wrapper (*args,**kwargs):
#         print(1)
#         func(*args,**kwargs)
#         print(2)
#         return func
#     return wrapper
#
#
# @ add_logs
# def fdf (**kwargs):
#     print(kwargs)
#     print(*kwargs.items())
#     print(kwargs)
#
# fdf (a=234,n=43)
# # x = list(range(2,1834,3))
# # print(x)

my_list = [x**2 for x in range(2,9000,6)]
print(my_list)
new_list = map(lambda x: x**2, range(2,9000,6))
print(list(new_list))
new_gener = [x/2 if x % 2 == 0  else x   for x in range(2,90)]
print(new_gener)

# new_gener = (x for x in range(2,90) if x % 2 == 0)
# print(new_gener)
#
#
# for x in list(new_gener):
#     print(x)
#     # if i.__index__() == 10:
#     #     print(i)