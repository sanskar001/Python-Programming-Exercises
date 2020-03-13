# This is python program to understand the progression class hierarchy.
# progression:
#            - Arithmetic progression
#            - Geometric  progression
#            - fibonacci progression.

# progression class
class progression:
    def __init__(self,start=0):
        self.current = start
    
    def advance(self):
        self.current+= 1
    
    def __next__(self):
        if self.current is None:
            raise StopIteration()
        else:
            answer = self.current
            self.advance()
            return answer
    
    def __iter__(self):
        return self
    
    def print_progression(self,n):
        return " ".join(str(next(self)) for i in range(n))
    
# arithmetic progression class
class arithmetic_progression(progression):
    def __init__(self,start=0,comman_diff=1):
        super().__init__(start)
        self.comman_diff = comman_diff
    
    def advance(self):
        self.current = self.current + self.comman_diff

# Geometric progression
class geometric_progression(progression):
    def __init__(self,start=1,comman_ratio=2):
        super().__init__(start)
        self.comman_ratio = comman_ratio
    
    def advance(self):
        self.current = self.current * self.comman_ratio

# fibonacci progression
class fibonacci_progression(progression):
    def __init__(self,first=0,second=1):
        super().__init__(first)
        self.previous = second
    
    def advance(self):
        self.previous,self.current = self.current,self.previous+self.current
    

p1 = progression()
print(f"p1:{p1.print_progression(10)}")
a1 = arithmetic_progression(3,2)
print(f"Ap1:{a1.print_progression(10)}")
g1 = geometric_progression(3,3)
print(f"Gp1:{g1.print_progression(10)}")
f1 = fibonacci_progression()
print(f"Fp1:{f1.print_progression(10)}")
