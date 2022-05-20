class Practice :
    def __init__(self,First,Last) :
        self.First=First
        self.Last = Last
        self.Akthay = First +' '+Last

    def fullName(self):
        return '{}{}'.format(self.Last,self.First) #Format jis hisaab se rakhna hy 

        
p1 = Practice('Sharjeel', 'Sohail')
print(p1.Akthay) #Data Type se Output

print(p1.fullName) #Function se output