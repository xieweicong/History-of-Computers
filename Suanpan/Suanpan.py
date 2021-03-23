import time

class OneBall():
    def __init__(self):
        self.isUsed = False


class FourBall():
    def __init__(self):
        self.isUsed = False


class OneZhu():
    def __init__(self):
        self.oneBall_1 = OneBall()
        self.oneBall_2 = OneBall()
        self.oneBall_3 = OneBall()
        self.oneBall_4 = OneBall()
        self.fourBall = FourBall()
        self.zhu = [self.oneBall_1, self.oneBall_2, self.oneBall_3, self.oneBall_4]

    def showNowOne(self):
        k = 0
        print("|",end='')
        for i in range(4):
            if self.zhu[i].isUsed:
                k += 1
        for _ in range(4-k):
            print("・",end='')
        print(" ",end=''),
        print(" ",end=''),
        for _ in range(k):
            print("・",end='')
        print("|",end='')
        if self.fourBall.isUsed:
            print("・",end='')
            print(" ",end=''),
            print(" ",end=''),
        else:
            print(" ",end=''),
            print(" ",end=''),
            print("・",end='')
        print("|",end='')
        print(self.mynums())
        print('\n')

    def beZero(self):
        self.fourBall.isUsed = False
        for i in range(4):
            self.zhu[i].isUsed = False

    def mynums(self):
        mynum = 0
        for i in range(4):
            if self.zhu[i].isUsed:
                mynum += 1
        if self.fourBall.isUsed:
            mynum += 5
        return mynum

    def add(self, num):
        num = int(num)
        if not self.fourBall.isUsed and num>=5:
            self.fourBall.isUsed = True

            num -= 5
        for i in range(4):
            if not self.zhu[i].isUsed and num!=0:
                self.zhu[i].isUsed = True
                num -= 1
        if num == 0:
            return False
        elif not self.fourBall.isUsed and num < 5:
            self.fourBall.isUsed = True
            num -= 5
            for i in range(-num):
                self.zhu[-i].isUsed = False
            return False
        else:
            num -= 1
            self.beZero()
            if not self.fourBall.isUsed and num>=5:
                self.fourBall.isUsed = True
                num -= 5
            for i in range(4):
                if not self.zhu[i].isUsed and num>=1:
                    self.zhu[i].isUsed = True
                    num -= 1
            return True

    def subtract(self, num):
        num = int(num)
        if self.fourBall.isUsed and num>=5:
            self.fourBall.isUsed = False
            num -= 5
        for i in range(1, 5):
            if self.zhu[-i].isUsed and num!=0:
                self.zhu[-i].isUsed = False
                num -= 1
        if num == 0:
            return False
        elif self.fourBall.isUsed and num <= 5:
            self.fourBall.isUsed = False
            num -= 5
            for i in range(-num):
                self.zhu[i].isUsed = True
            return False
        else:
            num -= 1
            self.fourBall.isUsed = True
            for i in range(4):
                self.zhu[i].isUsed = True
            if num <= 4:
                for i in range(num):
                    self.zhu[-i].isUsed = False
                return True
            else:
                self.fourBall.isUsed = False
                num -= 5
                for i in range(num):
                    self.zhu[-i].isUsed = False
                return True

    



class Abacus():
    def __init__(self):
        self.oneZhu_1 = OneZhu()
        self.oneZhu_2 = OneZhu()
        self.oneZhu_3 = OneZhu()
        self.oneZhu_4 = OneZhu()
        self.oneZhu_5 = OneZhu()
        self.oneZhu_6 = OneZhu()
        self.oneZhu_7 = OneZhu()
        self.oneZhu_8 = OneZhu()
        self.abacus = [self.oneZhu_1, self.oneZhu_2, self.oneZhu_3, self.oneZhu_4,
                       self.oneZhu_5, self.oneZhu_6, self.oneZhu_7, self.oneZhu_8]

    def showNow(self):
        for i in range(8):
            self.abacus[i].showNowOne()

    def beZero(self):
        for i in range(len(self.abacus)):
            self.abacus[i].beZero
        self.showNow()

    def add(self, a):
        a = list(str(a))
        if len(a) != 8:
            for i in range(8-len(a)):
                a.insert(0, "0")
        for i in range(1, len(a)+1):
            if self.abacus[-i].add(a[-i]):
                self.abacus[-i-1].add(1)
            self.showNow()
            time.sleep(1)
            print("----------------------------------------------------------------")
            
    def subtract(self, a):
        a = list(str(a))
        if len(a) != 8:
            for i in range(8-len(a)):
                a.insert(0, "0")
        for i in range(1, len(a)+1):
            if self.abacus[-i].subtract(a[-i]):
                self.abacus[-i-1].showNowOne(1)
            self.showNow()
            time.sleep(1)
            print("----------------------------------------------------------------")


oneAbacus = Abacus()
next = 'yes'
while next=='yes':
    print("+ - zero")
    how = input()
    if how == '+':
        oneAbacus.add(input())
        oneAbacus.showNow()
    elif how == '-':
        oneAbacus.subtract(input())
        oneAbacus.showNow()
    elif how == 'zero':
        oneAbacus.beZero()
    print('继续 yes or no')
    next = input()

# a = []
# for i in range(2):
#     a.append(OneZhu())
# a[0].add(2)
# a[0].showNowOne()
# a[0].subtract(8)
# a[0].showNowOne()
