class cources:
    def __init__(self):
        print("courses information.")
class bca(cources):
    def degree(self):
        print("Bacholo of computer application (BCA)")
        print("Duration: 3")
        print("Focus: computer programming, database, web development ,software engineering")
class btech(cources):
    def degree(self):
        print("about btech")
class bsc(cources):
    def degree(self):
        print("Bacholor if science (bsc)")
        print("Duration: 3")
        print("Focus: Physics,chemistry,mathemaics and biology")
class bba(cources):
    def degree(self):
        print("about bba")
class ba(cources):
    def degree(self):
        print("about ba")



class viewbca(bca):
    def __init__(self):
        bca().degree()
        
class viewbtech(btech):
    def __init__(self):
        btech().degree()
        
class viewbsc(bsc):
    def __init__(self):
        bsc().degree()
        
class viewbba(bba):
    def __init__(self):
        bba().degree()
        
class viewba(ba):
    def __init__(self):
        ba().degree()
        
        
ob1=viewbca()
ob2=viewbtech()
ob3=viewbsc()
ob4=viewbba()
ob5=viewba()