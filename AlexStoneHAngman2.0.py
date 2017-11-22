from __future__ import print_function # use Python 3.0 printing
def word_search(word):
    letter1 = raw_input('letter 1:')
    life = 3
    if letter1 == word[0:1]:
        a = letter1
    else:
        a = '_'
    if letter1 == word[1:2]:
        b = letter1
    else:
        b = '_'   
    if letter1 == word[2:3]:
        c = letter1
    else:
        c = '_'
    if letter1 == word[3:4]:
        d = letter1
    else:
        d = '_' 
    if letter1 == word[4:5]:
        e = letter1
    else:
        e = '_'
    if letter1 == word[5:6]:
        f = letter1
    else:
        f = '_' 
    if letter1 == word[0:1] or letter1 == word[1:2] or letter1 == word[2:3] or letter1 == word[3:4] or letter1 == word[4:5] or letter1 == word[5:6]:
        life = life
    else:
        life = life-1
    print(a,b,c,d,e,f)
    print('letters used: ',letter1)
    print('lives: ',life)
    letter2 = raw_input('letter 2:')
    if letter2 == word[0:1]:
        a2 = letter2
    else:
        a2 = '_'
    if letter2 == word[1:2]:
        b2 = letter2
    else:
        b2 = '_'   
    if letter2 == word[2:3]:
        c2 = letter2
    else:
        c2 = '_'
    if letter2 == word[3:4]:
        d2 = letter2
    else:
        d2 = '_' 
    if letter2 == word[4:5]:
        e2 = letter2
    else:
        e2 = '_'
    if letter2 == word[5:6]:
        f2 = letter2
    else:
        f2 = '_' 
    if letter2 == word[0:1] or letter2 == word[1:2] or letter2 == word[2:3] or letter2 == word[3:4] or letter2 == word[4:5] or letter2 == word[5:6]:
        life = life
    else:
        life = life-1
    if a != '_':
        a2 = a
    if b != '_':
        b2 = b
    if c != '_':
        c2 = c
    if d != '_':
        d2 = d
    if e != '_':
        e2 = e
    if f != '_':
        f2 = f
    print(a2,b2,c2,d2,e2,f2)
    print('letters used: ',letter1,letter2)
    print('lives: ',life)
    letter3 = raw_input('letter 3:')
    if letter3 == word[0:1]:
        a3 = letter3
    else:
        a3 = '_'
    if letter3 == word[1:2]:
        b3 = letter3
    else:
        b3 = '_'   
    if letter3 == word[2:3]:
        c3 = letter3
    else:
        c3 = '_'
    if letter3 == word[3:4]:
        d3 = letter3
    else:
        d3 = '_' 
    if letter3 == word[4:5]:
        e3 = letter3
    else:
        e3 = '_'
    if letter3 == word[5:6]:
        f3 = letter3
    else:
        f3 = '_' 
    if letter3 == word[0:1] or letter3 == word[1:2] or letter3 == word[2:3] or letter3 == word[3:4] or letter3 == word[4:5] or letter3 == word[5:6]:
        life = life
    else:
        life = life-1
    if a2 != '_':
        a3 = a2
    if b2 != '_':
        b3 = b2
    if c2 != '_':
        c3 = c2
    if d2 != '_':
        d3 = d2
    if e2 != '_':
        e3 = e2
    if f2 != '_':
        f3 = f2
    if life <= 0:
        print('GAME OVER')
    else:
        print(a3,b3,c3,d3,e3,f3)
        print('letters used: ',letter1,letter2,letter3)
        print('lives: ',life)
        letter4 = raw_input('letter 4:')  
    if letter4 == word[0:1]:
        a4 = letter4
    else:
        a4 = '_'
    if letter4 == word[1:2]:
        b4 = letter4
    else:
        b4 = '_'   
    if letter4 == word[2:3]:
        c4 = letter4
    else:
        c4 = '_'
    if letter4 == word[3:4]:
        d4 = letter4
    else:
        d4 = '_' 
    if letter4 == word[4:5]:
        e4 = letter4
    else:
        e4 = '_'
    if letter4 == word[5:6]:
        f4 = letter4
    else:
        f4 = '_' 
    if letter4 == word[0:1] or letter4 == word[1:2] or letter4 == word[2:3] or letter4 == word[3:4] or letter4 == word[4:5] or letter4 == word[5:6]:
        life = life
    else:
        life = life-1
    if a3 != '_':
        a4 = a3
    if b3 != '_':
        b4 = b3
    if c3 != '_':
        c4 = c3
    if d3 != '_':
        d4 = d3
    if e3 != '_':
        e4 = e3
    if f3 != '_':
        f4 = f3
    if life <= 0:
        print('GAME OVER')
    else:
        print(a4,b4,c4,d4,e4,f4)
        print('letters used: ',letter1,letter2,letter3,letter4)
        print('lives: ',life)
    letter5 = raw_input('letter 5:')
    if letter5 == word[0:1]:
        a5 = letter5
    else:
        a5 = '_'
    if letter5 == word[1:2]:
        b5 = letter5
    else:
        b5 = '_'   
    if letter5 == word[2:3]:
        c5 = letter5
    else:
        c5 = '_'
    if letter5 == word[3:4]:
        d5 = letter5
    else:
        d5 = '_' 
    if letter5 == word[4:5]:
        e5 = letter5
    else:
        e5 = '_'
    if letter5 == word[5:6]:
        f5 = letter5
    else:
        f5 = '_' 
    if letter5 == word[0:1] or letter5 == word[1:2] or letter5 == word[2:3] or letter5 == word[3:4] or letter5 == word[4:5] or letter5 == word[5:6]:
        life = life
    else:
        life = life-1
    if a4 != '_':
        a5 = a4
    if b4 != '_':
        b5 = b4
    if c4 != '_':
        c5 = c4
    if d4 != '_':
        d5 = d4
    if e4 != '_':
        e5 = e4
    if f4 != '_':
        f5 = f4
    if life <= 0:
        print('GAME OVER')
    else:
        print(a5,b5,c5,d5,e5,f5)
        print('letters used: ',letter1,letter2,letter3,letter4,letter5)
        print('lives: ',life)
    letter6 = raw_input('letter 6:')
    if letter6 == word[0:1]:
        a6 = letter6
    else:
        a6 = '_'
    if letter6 == word[1:2]:
        b6 = letter6
    else:
        b6 = '_'   
    if letter6 == word[2:3]:
        c6 = letter6
    else:
        c6 = '_'
    if letter6 == word[3:4]:
        d6 = letter6
    else:
        d6 = '_' 
    if letter6 == word[4:5]:
        e6 = letter6
    else:
        e6 = '_'
    if letter6 == word[5:6]:
        f6 = letter6
    else:
        f6 = '_' 
    if letter6 == word[0:1] or letter6 == word[1:2] or letter6 == word[2:3] or letter6 == word[3:4] or letter6 == word[4:5] or letter6 == word[5:6]:
        life = life
    else:
        life = life-1
    if a5 != '_':
        a6 = a5
    if b5 != '_':
        b6 = b5
    if c5 != '_':
        c6 = c5
    if d5 != '_':
        d6 = d5
    if e5 != '_':
        e6 = e5
    if f5 != '_':
        f6 = f5
    if life > 0:
        print(a6,b6,c6,d6,e6,f6)
        print('letters used: ',letter1,letter2,letter3,letter4,letter5,letter6)
        print('lives: ',life)
    else:
        print('GAME OVER')     