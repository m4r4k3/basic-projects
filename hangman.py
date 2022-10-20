import random
print(""" _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       """)
l = 'ANT BABOON BADGER BAT BEAR BEAVER CAMEL CAT CLAM COBRA COUGAR COYOTE CROW DEER DOG DONKEY DUCK EAGLE FERRET FOX FROG GOAT GOOSE HAWK LION LIZARD LLAMA MOLE MONKEY MOOSE MOUSE MULE NEWT OTTER OWL PANDA PARROT PIGEON PYTHON RABBIT RAM RAT RAVEN RHINO SALMON SEAL SHARK SHEEP SKUNK SLOTH SNAKE SPIDER STORK SWAN TIGER TOAD TROUT TURKEY TURTLE WEASEL WHALE WOLF WOMBAT ZEBRA'.split()
cib=len(l)
b=random.randint(0,cib)
c=l[b]
z=len(c)
g=list(c)
n=0
r=[]
lives=0
HANGMAN_PICS = ['''
     +---+
         |
         |
         |
       ===''', '''
     +---+
     O   |
         |
         |
       ===''', '''
      +---+
       O   |
       |   |
           |
         ===''', '''
       +---+
       O   |
      /|   |
           |
         ===''', '''
       +---+
      O   |
     /|\  |
          |
          ===''', '''
       +---+
       O   |
      /|\  |
      /    |
           ===''', '''
       +---+
       O   |
      /|\  |
      / \  |
         ===''']
#how many _
for a in range (0,z) :
    r.append("_")
sd=r.count("_")
while sd != 0 and lives != 6:
    print( r )
    a=input("letter : ").upper()
    z = len( c )
    n=0
    k=0
    if a in r :
        print("you already guessed this letter ")
#cheking if the letter is right
    else :
        while n!= z :
            if g[n]== a  :
                r[n]=a
                k=+1
                print("{0} correct".format(a))
            n = n + 1
            sd = r.count( "_" )
        if k==0  :
            lives = lives + 1
            print(HANGMAN_PICS[lives])
            print("you lose a life 💔")

if sd ==0 :
    print(""""           (_)                          
 __      __ _  _ __   _ __    ___  _ __ 
 \ \ /\ / /| || '_ \ | '_ \  / _ \| '__|
  \ V  V / | || | | || | | ||  __/| |   
   \_/\_/  |_||_| |_||_| |_| \___||_|   
                                        
                                        """)
elif lives == 6 :
    print("you lose the word was : ",c)
