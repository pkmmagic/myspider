import re
st = 'zbz中'

t = re.sub(r'[^\x00-\x7f]', ' ', st)

print (t)