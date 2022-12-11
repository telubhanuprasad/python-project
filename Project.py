N=int(input("Number of pieces N = "))

#N is taken as input for number of cake pieces

def equal_size(n):
    if n%2==0:
        print("The cake can be cut into equal sized pieces")
    else:
        print("The cake cannot be cut into equal sized pieces")

#The cake can be cut into equal number of pieces for N is any positive integer.

def any_size(n):
    if n%2==0:
        print("The cake can be cut into pieces any size")
    else:
        print("The cake cannot be cut into pieces of any size")

#The cake can be cut into pieces of any size for N is any positive integer

def no_equal(n):
    print("It is not possible to cut the cake such that no two pieces are equal")
    print("NOTE:")
    print("Since the angles of the opposite cake pieces are vertically opposite angles the opposite pieces in the cake are equal")

#The cake cannot be cut such that no two pieces are equal, because the angle of opposite cake pieces are vertically opposite angles. 

equal_size(N)
any_size(N)
no_equal(N)
