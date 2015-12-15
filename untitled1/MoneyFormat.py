__author__ = 'joe'

def moneyChange(money):
    strValue = str(money)
    isNegative = False
    if strValue[0] == '-':
        isNegative = True
        strValue = strValue[1:]
    strMoney = strValue.split('.')
    strTemp = []

    while(len(strMoney[0]) - 1)/3:
        strTemp.append(strMoney[0][-3:])
        strMoney = strMoney[0][:-3]

    strTemp.append(strMoney[0])
    strTemp.reverse()
    myDoller = ','.join(strTemp)+'.'+strMoney[1]
    if isNegative:
        myDoller = '-' + myDoller
    return myDoller

class MoneyFormat(object):
    def __init__(self, value = 0.0):
        self.value = moneyChange(value)
    def update(self, value = None):
        self.value = moneyChange(value)
    def __repr__(self):
        return repr(self.value)
    def __str__(self):
        val = '$'
        if self.value[0] == '-':
            val = '-$'+ self.value[1:]
        else:
            val += self.value
        return val
    def __nonzero__(self):
        return bool(self.value)

cash = MoneyFormat(1118.98988)
print cash
