# myColor=input('Please input your color: ')
# if (myColor=='red' or myColor=='RED'):
#   print('your color is red')
# else: 
#   print('your color is not red')

userNum = float(input('please input a number: '))
# if (userNum >=5.0 and userNum<=10.0):
#   print('your number,',userNum, ', is between 5 and ten')
# else:
#   print(userNum,'is not between 5 and ten')

if (userNum ==0):
  print('Your number is zero')
elif (userNum % 2 ==0 and userNum<0):
  print('your number is negative even')
elif (userNum %2==0 and userNum>0):
  print('your number is positive even')
elif (userNum%2 != 0 and userNum<0):
  print('your number is negative odd')
elif (userNum%2 != 0 and userNum>0):
  print('your number is positive odd')
