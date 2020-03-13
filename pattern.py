'''
# this is python program to make pattern given below:

A
A B
A B C
A B C D

alpha_list=["A","B","C","D"]
for x in range(len(alpha_list)):
    l=[]
    for y in range(x+1):
        l.append(alpha_list[y])
    print(" ".join(l))
    
#################################################################################    

# this is python program to make pattern given below:

*
* *
* * *
* * * *

for x in range(4):
    l=[]
    for y in range(x+1):
        l.append("*")
    print(" ".join(l))
    
##################################################################################

# this is python program to make patter given below:

      *
    * *
  * * *
* * * *

for x in range(4):
    l=[" "," "," "," "]
    for y in range(x+1):
        l[-(y+1)]="*"
    print(" ".join(l))

####################################################################################
# This is python program to make pattern given below:
   
* * *
 * *
  *
def pattern(a):
    pattern=[]
    for x in range(a):
        for y in range(a+(a-1)):
            if x==0:
                pattern.append("*")
            else:
                pattern[x-1]=" "
                pattern[-x]=" "
        print(" ".join(pattern)) 

pattern(3)
   

#####################################################################################
# this is python program to make pattern given below.
    
    *
   * *
  * * *
 * * * * 
* * * * *

def pyramid(n):
    for x in range(n):   // This is loop going on for row
        pattern=[]
        a=(n-1)-x       // number of spaces required in each row.
        for y in range(a):            
            pattern.append(" ")  
        for z in range(x+1):          // Above these loops are going on for columns.
            pattern.append("* ")
        print("".join(pattern))

pyramid(5)

###################################################################################
# This is python program to make pattern  given below.

   A
  B B
 C C C
D D D D

def alpha_pyramid(n):
    for x in range(n):        # This loop is going on for row
        pattern=[]
        k=(n-1)-x             # this k tells you the number of spaces in row
        for y in range(k):
            pattern.append(" ")
        for z in range(x+1):            # Above these loops are going on for columns
            pattern.append(chr(x+65)+" ")
        print("".join(pattern))        

alpha_pyramid(3)

################################################################################
# This is python program to make pattern given below.

   A
  B C
 D E F
G H I J

def alpha_pyramid(n):             
    count=0                          # this count tells you about alphabat iteration.
    for x in range(n):               # this loop is going for row.
        pattern=[]
        k=(n-1)-x                    # this k tells you about number of spaces in row
        for y in range(k):
            pattern.append(" ")
        for y in range(x+1):         # these above loops is going for columns.
            pattern.append(chr(count+65)+" ")
            count=count+1
        print("".join(pattern))

alpha_pyramid(3)   

##################################################################################
# This is python program to make pattern given below.

   *
  * *
 *   *
* * * *

def triangle_pattern(n):             # this is function for getting triangular pattern after giving number of rows.
    if n>3:
        for x in range(n):           # this loop is going on for rows
            pattern=[]
            k=(n-1)-x                # k tells you about the numbr of spaces in each row.
            for y in range(k):
                pattern.append(" ")
            for z in range(x+1):      # These above loops are going for columns.
                pattern.append("* ")
            if (1<x<n-1):               # these condition for removing the internal space of pyramid to make triangle.
                for a in range(k+1,len(pattern)-1):
                     pattern[a]="  " 
            print("".join(pattern))        
    else:
        print("Triangle pattern cannot be possible")
            

triangle_pattern(4)

###################################################################################
# This is python prgram to make patten given below.

* * * * *
*       *
*       *
*       *
* * * * *

def square_pattern(n):
    for x in range(n):
        pattern=[]
        for y in range(n):
            pattern.append("* ")
        if (0<x<n-1):
            for z in range(1,n-1):
                pattern[z]="  "
        print("".join(pattern))    

square_pattern(5)
'''
