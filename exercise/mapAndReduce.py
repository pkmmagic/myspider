from functools import reduce



DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


    

def str2float(s):
    s1, s2 = s.split('.')
    def fn(x, y):
        return x * 10 + y
    def char2num(c):
        return DIGITS[c]
    return reduce(fn, map(char2num, s1)) + (reduce(fn, map(char2num, s2)))/(10**len(s2))


print('str2float(\'1123.4567\') =', str2float('1123.4567'))
if abs(str2float('1123.4567') - 1123.4567) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
