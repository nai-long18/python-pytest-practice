class calculator:
    def add(self,*args):
        result=0
        for i in args:
            result=result+i
        return result