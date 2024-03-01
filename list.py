# numbers=[1,2,3,4,5,6,7,8,9]
#
# sq_num=[num*num for num in numbers]
#
# print(sq_num)
#
#
#
# numbers = [1,2,3,4,5,6,7,8,9,10]
#
#
# even_list=[num for num in numbers if num%2 ==0]
# print(even_list)
#
# odd_list=[num for num in numbers if num%2 !=0]
# print(odd_list)
#
#


#
# with open("file1.txt") as file1:
#     list1 = file1.readlines()
#
# with open("file2.txt") as file2:
#     list2 = file2.readlines()
#
#
# result=[int(num) for num in list1 if num in list2]
#
# print(result)


weather_c=eval(input("Enter the temperature in Celsius:"))

weather_f={day:temp*9/5 +32 for (day,temp) in weather_c.items()}
print(weather_f)
