import os
print("""     __________
    | ________ |
    ||________||
    |\"\"\"\"\"\"\"\"\"\"|
    |[M|#|C][-]|
    |[7|8|9][+]|
    |[4|5|6][x]|
    |[1|2|3][%]|
    |[.|O|:][=]|
    \"__________\"                           """)
r=int(input("first value :" ))
qu="y"
while qu == "y":
    va=int(input("second value :" ))
    def add(va1,va2) :
        return va1+va2
    def div (va1,va2):
        return va1/va2
    def sub (va1,va2):
        return va1-va2
    def mult(va1 , va2):
        return va1*va2
    match input("enter the operation type +,-,*,/"):
        case "+":
            r=add(r , va )
            print(f"result is : {r}")
        case "-"  :
            r=sub( r , va )
            print( f"result is : {r}" )
        case "*" :
            r=mult( r , va )
            print( f"result is : {r}" )
        case "/":
            r=div( r , va )
            print( f"result is : {r}" )
    qu=input("want to keep going ? (y or n )")
    if qu=="y":
        os.system( 'cls' )



