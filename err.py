"""""
调适python程序的2个功能:
    异常处理
    断言(Assertions)

"""""


""""异常处理: 如果不想在异常发生时结束程序,需在try里捕获它"""


# # 捕捉指定异常--->  try...except 异常名:
try:
    # 写需要捕捉的异常类型
    print(a)
    x = 1/0
    print("一旦遇到try里面的异常,try后面代码不会执行")

 # 一旦遇到try里面的异常类型就执行except里面的代码
except NameError:
    print("错误:不能使用没有定义的变量")
except ZeroDivisionError:
    print("错误:分母(除数)不能为0")

# print("程序正常结束")



# 捕捉多个异常---> try...except(异常名1,异常名2,):
try:
    print(a)
    x = 1 / 0

except (NameError, ZeroDivisionError):
    print("错误:表达不正确")

print("程序正常结束")




# 捕捉任意异常---> try...except(异常名1,异常名2,):
try:
    print(a)
    x = 1 / 0

# except 捕捉所有异常
# except:
# Exception可以捕捉大部分异常, 它是大部分异常的基类,
# except Exception:
except Exception as e:
    print("错误:表达不正确")

else:
    print("程序正常结束")




# 异常处理别名---> try...except Exception as 别名
try:
    pass
except Exception as exc:
    pass





try:
    pass
finally:
    pass



# 解发异常
raise Exception()

