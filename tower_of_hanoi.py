# Tower of hanoi
# Here num variable for number of rings placed in first tower.
count=0
def Tower_of_hanoi(num,Beg="first",mid="second",last="third"):
    if num>=1:
        Tower_of_hanoi(num-1,Beg,last,mid)
        print(Beg,"to",last)
        global count
        count=count+1
        Tower_of_hanoi(num-1,mid,Beg,last)

Tower_of_hanoi(4)
print("number of steps for doing this task:",count)