c=(input("want to encrypt  (1 ) or decrypter (2) : "))
a= list(input("enter the message :"))
l=len(a)
h=[]
b=int(input("enter the number of alphabets you want to skip :"))
alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encryption ():
    sym = ['!' , '#' , '$' , '%' , '&' , '(' , ')' , '*' , '+' , " " , "." , "?" , "/" , "," , ":"]
    z = ""
    for i in range (0,l):
        if sym.count(a[i])==0:
            d = alpha.index( a[i] ) + b
            if d<0 :
                d=d-1
            if d>25 or d<-25 :
                while d > 25 or d < -25 :
                    if d > 25 :
                        d = d - 25
                    else :
                        d = d + 25
            h.append(alpha[d])
        else :
            h.append(sym[sym.index(a[i])])
    for r in range (0,l):
        z=z+h[r]
    print(z)

def decription():
    sym = ['!' , '#' , '$' , '%' , '&' , '(' , ')' , '*' , '+' , " " , "." , "?" , "/" , "," , ":"]
    z = ""
    for i in range( 0 , l ) :
        if sym.count( a[i] ) == 0 :
            d = alpha.index( a[i] ) - b
            if d < 0 :
                d = d - 1
            if d > 25 or d < -25 :
                while d > 25 or d < -25 :
                    if d > 25 :
                        d = d - 25
                    else :
                        d = d + 25
            h.append( alpha[d] )
        else :
            h.append( sym[sym.index( a[i] )] )
    for r in range( 0 , l ) :
        z = z + h[r]
    print( z )


if c=="1":
    encryption()
elif c== "2" :
    decription()
