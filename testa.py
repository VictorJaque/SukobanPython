def create_level_1(level):
    x = 0
    y = 0
    teck = []  
    with open("first_level.sokoban") as f:
        for rad in f:
            for tecken in rad:
                x = x + 1
                if tecken == '\n':
                 y = y + 1
                 x = 0
                if tecken != " ":
                   teck.append({'symb': tecken, 'posy': y, 'posx': x})
 
        return(teck)

def display_level(teck): 
 rad1 = [                    ]
 rad2 = []
 displaylevel = rad1 + rad2
 i = 0
 for l in teck:
  while i < teck[i]['posx']:
   rad1.append(" ")
   i = i + 1
  if teck[i]['posy'] == 0:
    #rad1.append((" "*teck[0]['posx']))
    rad1.append([teck[i]['symb'], teck[i]['posx']])
  else: 
   rad2.append({'symb', 'posx'})
  i = i + 1
 return(rad1)
 return(rad2)
 return(displaylevel)

level = 1
teck = create_level_1(level)
teck = display_level(teck)
print(teck)

