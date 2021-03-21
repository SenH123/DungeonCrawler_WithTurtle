import turtle
import random
import time
import webbrowser #hemmelig

#-----Functions-----

def keys_activate(): # aktiverer knapper
    start_knapp.onclick(start,1) #lager en knapp som kaller på functionene "start"
    explore_knapp.onclick(explore,1)
    flee_knapp.onclick(flee,1)
    attack_knapp.onclick(attack,1)
    slash_knapp.onclick(slash,1)
    fireball_knapp.onclick(fireball,1)
    rest_knapp.onclick(rest,1)
    shady_knapp.onclick(shady,1)
    floor1_knapp.onclick(floor1,1)
    floor2_knapp.onclick(floor2,1)
    floor3_knapp.onclick(floor3,1)
    turtle.listen() #skjekker om det har kommet noen "events" eller inputer

def keys_deactivate(): # deaktiverer knapper
    explore_knapp.onclick(None,1) #når disse skjer så kaller den på ingenting
    flee_knapp.onclick(None,1)
    attack_knapp.onclick(None,1)
    slash_knapp.onclick(None,1)
    fireball_knapp.onclick(None,1)

def main_menu(): #startsiden
    screen.bgpic('Main menu.gif') #bakgrunns bilde

    #plasserer turtles
    text_MainM.color('black')
    text_MainM.goto(0,-10)
    text_exit.goto(-405,195)
    exit_knapp.goto(-405,205)
    shady_knapp.goto(395,205)
    shady_knapp.st()
    exit_knapp.st()

    exit_knapp.onclick(exitdef,1)
    keys_activate()

    start_knapp.st() # st = showturtle
    text_MainM.write('START', move=False, align='center', font=('Arial', 15, 'normal')) # Hele formaten til en tekst
    text_MainM.goto(395,195)
    text_MainM.write('SHADY', move=False, align='center', font=('Arial', 15, 'normal'))
    text_exit.write('EXIT', move=False, align='center', font=('Arial', 15, 'normal'))

def start(x,y): #start på spill
    game_running = True

    start_knapp.ht() #ht = hideturtle
    shady_knapp.ht()
    text_MainM.clear()
    start_knapp.clear()
    screen.bgpic(floorbg)
    sleeping.ht()
    attack_knapp.ht()
    flee_knapp.ht()
    text_attack.clear()

    text_expl.goto(395,-205)
    explore_knapp.goto(395,-195)
    flee_knapp.goto(-405,-195)
    attack_knapp.goto(-320,-195)
    slash_knapp.goto(-320,-195)
    fireball_knapp.goto(-235,-195)
    rest_knapp.goto(305,-195)

    status_def() # kaller status_def functionen

    explore_knapp.st()
    rest_knapp.st()

    text_expl.write('EXPLORE', move=False, align='center', font=('Arial', 13, 'normal'))
    text_expl.goto(305,-205)
    text_expl.write('REST', move=False, align='center', font=('Arial', 13, 'normal'))

def status_def(): #denne functionen bruker jeg til å opptatere statusene
    status.clear()

    status.color('white')
    status.goto(345,207)
    status.write(f'HEALTH:', move=False, align='center', font=('Arial', 15, 'normal'))
    status.goto(350,182)
    status.write('MANA:', move=False, align='center', font=('Arial', 15, 'normal'))
    status.goto(340,157)
    status.write('STAMINA:', move=False, align='center', font=('Arial', 15, 'normal'))
    status.goto(345,132)
    status.write('FLEES:', move=False, align='center', font=('Arial', 15, 'normal'))

    status.goto(405,205)
    status.color('red')
    status.write(user_health, move=False, align='center', font=('Arial', 18, 'normal'))
    status.goto(405,180)
    status.color('blue')
    status.write(user_mana, move=False, align='center', font=('Arial', 18, 'normal'))
    status.goto(405,155)
    status.color('green')
    status.write(user_stamina, move=False, align='center', font=('Arial', 18, 'normal'))
    status.color('white')
    status.goto(405,130)
    status.write(flees, move=False, align='center', font=('Arial', 18, 'normal'))

def monster_status(): #opptatering av monsterets status
    #statusen til monsteret
    monster_status_turtle.clear()

    monster_status_turtle.goto(0,205)
    monster_status_turtle.color('red')
    monster_status_turtle.write(f'{monster_health}/{max_monsterHP}', move=False, align='center', font=('Arial', 25, 'normal'))
    
def explore(x,y): #utforskning
    global user_stamina,find_monster,in_combat,explored_times,floor,max_monsterHP,floor_prog,floor,floorbg,monster_health,lowest_monster_dmg,highest_monster_dmg,monster_pic,flees #gjør at amn kan endre variabler som er utenfor functionen

    user_stamina-=10 #Variabel opptatering
    explored_times+=4

    
    if explored_times > floor_prog: #skjekker om du skal til neste "floor"

        #variabel opptatering
        explored_times-=explored_times
        flees+=2

        if floor < 3: #floor tre er spesiell
            floor_prog+=2

        else:
            floor_prog-=4
            find_monster = True

            if floor_prog < 0:
                floor_prog = 1

        floor+=1
        max_monsterHP=50*floor
        monster_health = max_monsterHP
        lowest_monster_dmg+=15
        highest_monster_dmg+=15

        #Skjekker hvilket monster som skal ut
        if floor == 2:
            monster_pic = 'Mudmonster'
        elif floor == 3:
            monster_pic = 'Pig'
        elif floor == 4:
            monster_pic = 'Dragon'

        floorbg = f'floor{floor}.gif'
        screen.bgpic(floorbg)

        keys_deactivate() #deaktivering

        text_expl.goto(395,-205)
        text_expl.write('EXPLORE', move=False, align='center', font=('Arial', 13, 'normal'))
        text_expl.goto(305,-205)

        text_MainM.goto(0,150)
        text_MainM.color('red')

        for i in range(3): # blinker en tekst, gjør den mer synlig
            text_MainM.write('You discovered the next floor!', move=False, align='center', font=('Arial', 20, 'normal'))
            time.sleep(0.3)
            text_MainM.clear()
            time.sleep(0.3)

        keys_activate()#aktiverer knapper

        text_expl.goto(395,-205)
        text_expl.write('EXPLORE', move=False, align='center', font=('Arial', 13, 'normal'))
        text_expl.goto(305,-205)
        text_expl.write('REST', move=False, align='center', font=('Arial', 13, 'normal'))

    if floor == 2:
        floor1_knapp.goto(-320,205)
        floor1_knapp.st()
        text_expl.goto(-320,200)
        text_expl.write('BACK F', move=False, align='center', font=('Arial', 14, 'normal'))
    
    elif floor == 3:
        floor2_knapp.goto(-320,205)
        floor1_knapp.ht()
        floor2_knapp.st()
        text_expl.goto(-320,200)
        text_expl.write('BACK F', move=False, align='center', font=('Arial', 14, 'normal'))
    
    elif floor == 4:
        floor3_knapp.ht()
        floor3_knapp.goto(-320,205)
        floor3_knapp.st()
        text_expl.goto(-320,200)
        text_expl.write('BACK F', move=False, align='center', font=('Arial', 14, 'normal'))
        max_monsterHP = 2000
        monster_health = max_monsterHP
        lowest_monster_dmg = 25
        highest_monster_dmg = 100

            

    if floor < 3: #floor tre er spesiel
        find_monster = random.choice(find_monster_list) #tar random om å møte på monster

    if find_monster and user_stamina > 0: 
        in_combat = True #variabel opptatering

        find_monster_list.remove(True) #minsker sjansen til å møte på monster
        if not True in find_monster_list: #om sjansen er for liten
            find_monster_list.append(True)
            find_monster_list.append(True)

        explore_knapp.ht()
        rest_knapp.ht()
        text_expl.clear()

        #endrer posisjonene på turtlene
        monster.goto(20,-100)

        #endrer på outputen i programmet
        monster.shape(f'{monster_pic}.gif')
        monster.st()
        monster_status()

        #info til bruker om hva som skjedde
        text_MainM.goto(0,150)
        text_MainM.color('red')

        keys_deactivate() #deaktivering
        for i in range(3): # blinker en tekst, gjør den mer synlig
            text_MainM.write('You encounterd a monster!', move=False, align='center', font=('Arial', 20, 'normal'))
            time.sleep(0.3)
            text_MainM.clear()
            time.sleep(0.3)

        text_attack.clear()
        text_expl.clear()
        attack_knapp.st()
        flee_knapp.st()

        keys_activate()#aktiverer knapper

        text_expl.goto(-405,-205)
        text_expl.write('FLEE', move=False, align='center', font=('Arial',15, 'normal'))
        text_expl.goto(-320,-205)
        text_expl.write('ATTACK', move=False, align='center', font=('Arial',14, 'normal'))

        if floor > 1:
            text_expl.goto(-320,200)
            text_expl.write('BACK F', move=False, align='center', font=('Arial',14, 'normal'))
        
    status_def()

    
    find_monster = 'nothing'
    find_monster_list.append(True) #øker sjansen til å møte monster

def flee(x,y): #rømming
    global explored_times,user_health,user_mana,user_stamina,monster_ANI,monster_pic,flees

    if flees > 0:
        flees-=1
        in_combat = False

        monster_ANI = '3'
        monster_status_turtle.clear()
        monster.shape(f'{monster_pic}{monster_ANI}.gif')
        time.sleep(1)
        monster.ht()

        text_expl.clear()
        status.clear()
        attack_knapp.ht()
        flee_knapp.ht()
        slash_knapp.ht()
        fireball_knapp.ht()

        blinking.goto(0,500)
        blinking.speed(1)
        blinking.st()
        blinking.goto(0,0)

        sleeping.st()
        blinking.ht()

        main_menu()

        user_health = max_user_health
        user_stamina = max_user_stamina
        user_mana = max_user_mana

def rest(x,y): #hviling
    global user_health,user_mana,user_stamina,max_user_health,max_user_mana,max_user_stamina
    game_running = False

    text_expl.clear()
    status.clear()
    explore_knapp.ht()
    rest_knapp.ht()

    blinking.goto(0,500)
    blinking.speed(1)
    blinking.st()
    blinking.goto(0,0)
    blinking.speed(0)

    sleeping.st()
    blinking.ht()

    main_menu()

    user_health = max_user_health
    user_stamina = max_user_stamina
    user_mana = max_user_mana

def attack(x,y): #angrep
    attack_modeON = True

    #hviser alle angripene dine
    attack_knapp.ht()
    
    text_attack.goto(-320,-205)
    slash_knapp.st()
    text_attack.write('SLASH', move=False, align='center', font=('Arial',13, 'normal'))

    text_attack.goto(-235,-205)
    fireball_knapp.st()
    text_attack.write('FIREBALL', move=False, align='center', font=('Arial',13, 'normal'))

    if floor > 1:
        text_expl.goto(-320,200)
        text_expl.write('BACK F', move=False, align='center', font=('Arial', 14, 'normal'))

def slash(x,y): #et spesielt angrep
    global user_health,monster_health,max_user_stamina,victory,lowest_user_dmg,highest_user_dmg,monsters_death,max_user_health,max_user_mana,lowest_monster_dmg,highest_monster_dmg,monster_pic,monster_ANI,user_stamina #alle variablene jeg trenger

    if user_stamina > 10:

        keys_deactivate() #deaktiverer knapper
        user_stamina-=10

        text_attack.goto(-320,-205)
        text_attack.write('SLASH', move=False, align='center', font=('Arial',13, 'normal'))
        text_attack.goto(-235,-205)
        text_attack.write('FIREBALL', move=False, align='center', font=('Arial',13, 'normal'))
        text_expl.goto(-405,-205)
        text_expl.write('FLEE', move=False, align='center', font=('Arial',15, 'normal'))

        user_hit = random.choice(hit) #om angrepet til personen skal treffe monsteret
        monster_hit = random.choice(hit)

        #skjekker hva som har skjedd
        if user_hit and monster_hit: 
            user_dmg = random.randint(lowest_user_dmg,highest_user_dmg) #randomiserer hvor mye liv man skal ta
            monster_dmg = random.randint(lowest_monster_dmg,highest_monster_dmg)

        elif user_hit and not monster_hit:
            user_dmg = random.randint(lowest_user_dmg,highest_user_dmg)
            monster_dmg = 0

        elif monster_hit and not user_hit:
            user_dmg = 0
            monster_dmg = random.randint(lowest_monster_dmg,highest_monster_dmg)

        elif not user_hit and not monster_hit:
            user_dmg = 0
            monster_dmg = 0

        #angrep animasjon
        attackANI.shape('Slash.gif')
        attackANI.goto(200,70)
        attackANI.speed(8)
        attackANI.st()
        attackANI.goto(-100,-200)
        attackANI.ht()

        #minuserer livet basert på angrepet
        monster_health-=user_dmg

        if monster_health < 0: #det er rart hvis livet til monsteret går under 0
            monster_health = 0
        elif user_health < 0:
            user_health = 0

        monster_status()

        #viser hvor mye dmg du tok
        distance = 0
        for i in range(3): #denne for i in rage bruker jeg til å lage en dmg hvise effekt
            text_MainM.goto(20,distance)
            text_MainM.write(user_dmg, move=True, align='center', font=('Arial',13, 'normal'))
            time.sleep(0.2)
            text_MainM.clear()
            distance+=30

        if monster_health > 0: #skjekker monsterets liv
            user_health-=monster_dmg

            if monster_hit: #lager monster angrep animasjon
                monster_ANI = '1'
                monster.shape(f'{monster_pic}{monster_ANI}.gif')
                time.sleep(0.2)
                DMG.st()
                time.sleep(0.1)
                DMG.ht()
                monster.shape(f'{monster_pic}.gif')

                status_def()

                distance = 0
                for i in range(3):
                    text_MainM.goto(390,distance)
                    text_MainM.write(f'-{monster_dmg} HEALTH!', move=True, align='center', font=('Arial',13, 'normal'))
                    time.sleep(0.2)
                    text_MainM.clear()
                    distance+=30

                if user_health <= 0: #skjekker om man er død
                    monster_status_turtle.clear()
                    status.clear()
                    text_exit.clear()
                    text_attack.clear()
                    text_expl.clear()

                    text_expl.ht()
                    flee_knapp.ht()
                    slash_knapp.ht()
                    exit_knapp.ht()
                    fireball_knapp.ht()
                    floor1_knapp.ht()
                    floor2_knapp.ht()
                    floor3_knapp.ht()
                    gameover.st()

            if user_health > 0:
                keys_activate() #aktiverer knappene

                text_attack.goto(-320,-205)
                text_attack.write('SLASH', move=False, align='center', font=('Arial',13, 'normal'))
                text_attack.goto(-235,-205)
                text_attack.write('FIREBALL', move=False, align='center', font=('Arial',13, 'normal'))
                text_expl.goto(-405,-205)
                text_expl.write('FLEE', move=False, align='center', font=('Arial',15, 'normal'))

        elif monster_health <= 0: #om man har seiret
            in_combat = False

            monster_status_turtle.clear()

            for i in range(3):
                monster.st()
                time.sleep(0.5)
                monster.ht()
                time.sleep(0.3)

            flee_knapp.ht()
            slash_knapp.ht()
            fireball_knapp.ht()
            text_expl.clear()
            text_attack.clear()

            #variabel opptatering
            monsters_death+=1
            monster_health = max_monsterHP

            lowest_user_dmg+=1
            highest_user_dmg+=1

            max_user_health+=8
            max_user_mana+=6
            max_user_stamina+=10


            explore_knapp.st()
            rest_knapp.st()
            keys_activate()

            text_expl.goto(395,-205)
            text_expl.write('EXPLORE', move=False, align='center', font=('Arial', 13, 'normal'))
            text_expl.goto(305,-205)
            text_expl.write('REST', move=False, align='center', font=('Arial', 13, 'normal'))

    if user_health > 0:
        status_def()
            
def fireball(x,y): #et spesielt angrep
    global user_health,monster_health,max_user_stamina,victory,lowest_user_dmg,highest_user_dmg,monsters_death,max_user_health,max_user_mana,user_mana,monster_pic,monster_ANI,user_stamina

    if user_mana > 30:

        keys_deactivate() #deaktiverer knapper
        user_mana-=45

        text_attack.goto(-320,-205)
        text_attack.write('SLASH', move=False, align='center', font=('Arial',13, 'normal'))
        text_attack.goto(-235,-205)
        text_attack.write('FIREBALL', move=False, align='center', font=('Arial',13, 'normal'))
        text_expl.goto(-405,-205)
        text_expl.write('FLEE', move=False, align='center', font=('Arial',15, 'normal'))

        user_hit = True
        monster_hit = random.choice(hit) #om angrepet til personen skal treffe monsteret

        #skjekker hva som har skjedd
        if user_hit and monster_hit: 
            user_dmg = random.randint(lowest_user_dmg+10,highest_user_dmg+10) #randomiserer hvor mye liv man skal ta
            monster_dmg = random.randint(3,30)

        elif user_hit and not monster_hit:
            user_dmg = random.randint(lowest_user_dmg+10,highest_user_dmg+10)
            monster_dmg = 0

        elif monster_hit and not user_hit:
            user_dmg = 0
            monster_dmg = random.randint(5,30)

        elif not user_hit and not monster_hit:
            user_dmg = 0
            monster_dmg = 0

        #angrep animasjon
        attackANI.goto(0,-50)
        attackANI.shape('fireball.gif')
        attackANI.st()
        time.sleep(0.3)
        attackANI.shape('fireball1.gif')
        time.sleep(0.3)
        attackANI.ht()

        #minuserer livet basert på angrepet
        monster_health-=user_dmg

        if monster_health < 0: #det er rart hvis livet til monsteret går under 0
            monster_health = 0
        elif user_health < 0:
            user_health = 0

        monster_status()

        #viser hvor mye dmg du tok
        distance = 0
        for i in range(3): #denne for i in rage bruker jeg til å lage en dmg hvise effekt
            text_MainM.goto(20,distance)
            text_MainM.write(user_dmg, move=True, align='center', font=('Arial',13, 'normal'))
            time.sleep(0.2)
            text_MainM.clear()
            distance+=30

        if monster_health > 0: #skjekker monsterets liv
            user_health-=monster_dmg

            if monster_hit: #lager monster angrep animasjon
                monster_ANI = '1'
                monster.shape(f'{monster_pic}{monster_ANI}.gif')
                time.sleep(0.2)
                DMG.st()
                time.sleep(0.1)
                DMG.ht()
                monster.shape(f'{monster_pic}.gif')

                status_def()

                distance = 0
                for i in range(3):
                    text_MainM.goto(390,distance)
                    text_MainM.write(f'-{monster_dmg} HEALTH!', move=True, align='center', font=('Arial',13, 'normal'))
                    time.sleep(0.2)
                    text_MainM.clear()
                    distance+=30

                if user_health <= 0:
                    monster_status_turtle.clear()
                    status.clear()
                    text_exit.clear()
                    text_attack.clear()

                    text_expl.ht()
                    flee_knapp.ht()
                    slash_knapp.ht()
                    exit_knapp.ht()
                    gameover.st()

            if user_health > 0:
                keys_activate() #aktiverer knappene
                
                text_attack.goto(-320,-205)
                text_attack.write('SLASH', move=False, align='center', font=('Arial',13, 'normal'))
                text_attack.goto(-235,-205)
                text_attack.write('FIREBALL', move=False, align='center', font=('Arial',13, 'normal'))
                text_expl.goto(-405,-205)
                text_expl.write('FLEE', move=False, align='center', font=('Arial',15, 'normal'))

        elif monster_health <= 0: #om man har seiret
            in_combat = False

            monster_status_turtle.clear()

            for i in range(3):
                monster.st()
                time.sleep(0.5)
                monster.ht()
                time.sleep(0.3)

            flee_knapp.ht()
            slash_knapp.ht()
            fireball_knapp.ht()
            text_expl.clear()
            text_attack.clear()

            #variabel opptatering
            monsters_death+=1
            monster_health = max_monsterHP

            lowest_user_dmg+=1
            highest_user_dmg+=1

            max_user_health+=8
            max_user_mana+=6
            max_user_stamina+=10

            explore_knapp.st()
            rest_knapp.st()
            keys_activate()

            text_expl.goto(395,-205)
            text_expl.write('EXPLORE', move=False, align='center', font=('Arial', 13, 'normal'))
            text_expl.goto(305,-205)
            text_expl.write('REST', move=False, align='center', font=('Arial', 13, 'normal'))

    status_def()

def exitdef(x,y): #går ut av spillet
    exit()

def shady(x,y): #Hmmm...
    webbrowser.open('https://youtu.be/dQw4w9WgXcQ')

def floor1(x,y):
    global explored_times,user_health,user_mana,user_stamina,monster_ANI,monster_pic,flees,floorbg,explored_times,floor,floor_prog,max_monsterHP,monster_health,highest_monster_dmg,lowest_monster_dmg
    floor = 1
    floor_prog = 3
    floorbg = f'floor{floor}.gif'
    explored_times = 0
    highest_monster_dmg = 37
    lowest_monster_dmg = 3 

    in_combat = False
    monster_ANI = '3'

    monster_status_turtle.clear()
    monster.shape(f'{monster_pic}{monster_ANI}.gif')
    time.sleep(1)

    monster.ht()
    text_expl.clear()
    status.clear()
    attack_knapp.ht()
    flee_knapp.ht()
    slash_knapp.ht()
    fireball_knapp.ht()
    explore_knapp.ht()
    rest_knapp.ht()
    floor1_knapp.ht()

    blinking.goto(0,500)
    blinking.speed(1)
    blinking.st()
    blinking.goto(0,0)
    sleeping.st()
    blinking.ht()

    main_menu()

    user_health = max_user_health
    user_stamina = max_user_stamina
    user_mana = max_user_mana
    monster_pic = 'Goblin'
    max_monsterHP = 50
    monster_health = max_monsterHP

def floor2(x,y):
    global explored_times,user_health,user_mana,user_stamina,monster_ANI,monster_pic,flees,floorbg,explored_times,floor,floor_prog,max_monsterHP,monster_health,highest_monster_dmg,lowest_monster_dmg
    floor = 2
    floor_prog = 5
    floorbg = f'floor{floor}.gif'
    explored_times = 0
    highest_monster_dmg = 50
    lowest_monster_dmg = 10 

    in_combat = False
    monster_ANI = '3'

    monster_status_turtle.clear()
    monster.shape(f'{monster_pic}{monster_ANI}.gif')
    time.sleep(1)

    monster.ht()
    text_expl.clear()
    status.clear()
    attack_knapp.ht()
    flee_knapp.ht()
    slash_knapp.ht()
    fireball_knapp.ht()
    explore_knapp.ht()
    rest_knapp.ht()
    floor2_knapp.ht()

    blinking.goto(0,500)
    blinking.speed(1)
    blinking.st()
    blinking.goto(0,0)
    sleeping.st()
    blinking.ht()

    main_menu()

    user_health = max_user_health
    user_stamina = max_user_stamina
    user_mana = max_user_mana
    monster_pic = 'Mudmonster'
    max_monsterHP = 100
    monster_health = max_monsterHP

def floor3(x,y):
    global explored_times,user_health,user_mana,user_stamina,monster_ANI,monster_pic,flees,floorbg,explored_times,floor,floor_prog,max_monsterHP,monster_health,highest_monster_dmg,lowest_monster_dmg
    floor = 3
    floor_prog = 3
    floorbg = f'floor{floor}.gif'
    explored_times = 0 
    lowest_monster_dmg = 20
    highest_monster_dmg = 70

    in_combat = False
    monster_ANI = '3'

    monster_status_turtle.clear()
    monster.shape(f'{monster_pic}{monster_ANI}.gif')
    time.sleep(1)

    monster.ht()
    text_expl.clear()
    status.clear()
    attack_knapp.ht()
    flee_knapp.ht()
    slash_knapp.ht()
    fireball_knapp.ht()
    explore_knapp.ht()
    rest_knapp.ht()
    floor3_knapp.ht()

    blinking.goto(0,500)
    blinking.speed(1)
    blinking.st()
    blinking.goto(0,0)
    sleeping.st()
    blinking.ht()

    main_menu()

    user_health = max_user_health
    user_stamina = max_user_stamina
    user_mana = max_user_mana
    monster_pic = 'Pig'
    max_monsterHP = 150
    monster_health = max_monsterHP

#Setup
screen = turtle.Screen()
screen.setup(900,500) #sier start størrelsen og hvor skjermen skal dukke opp
turtle.ht() # ht = hideturtle
turtle.pu() # pu = penup
turtle.speed(0)

#---------Laging av Turtles---------

#Tekst turtles
text_MainM = turtle.clone()
text_exit = turtle.clone()
text_expl = turtle.clone()
text_attack = turtle.clone()
status = turtle.clone()
monster_status_turtle = turtle.clone()

#Knappe format til andre knapper
exit_knapp = turtle.clone()#cloner turtlen
exit_knapp.shape('circle') #registrerer formen på turtlen
exit_knapp.shapesize(4)
exit_knapp.color('orange') #fargen på turtlen

explore_knapp = exit_knapp.clone()
flee_knapp = exit_knapp.clone()
attack_knapp = exit_knapp.clone()
slash_knapp = exit_knapp.clone()
fireball_knapp = exit_knapp.clone()
rest_knapp = exit_knapp.clone()
shady_knapp = exit_knapp.clone()
floor1_knapp = exit_knapp.clone()
floor2_knapp = exit_knapp.clone()
floor3_knapp = exit_knapp.clone()


#monster
monster = turtle.clone()
turtle.register_shape('Goblin.gif') #henter bilde
monster.shape('Goblin.gif') #registrerer bilde på turtle
turtle.register_shape('Goblin1.gif')
turtle.register_shape('Goblin3.gif')
turtle.register_shape('Mudmonster.gif')
turtle.register_shape('Mudmonster1.gif')
turtle.register_shape('Mudmonster3.gif')
turtle.register_shape('Pig.gif')
turtle.register_shape('Pig1.gif')
turtle.register_shape('Pig3.gif')
turtle.register_shape('Dragon.gif')
turtle.register_shape('Dragon1.gif')

#Egene turtles
start_knapp = turtle.clone()
start_knapp.shape('square')
start_knapp.shapesize(2,15)
start_knapp.color('orange')

#bilde turtles
DMG = turtle.clone()
turtle.register_shape('red.gif')
DMG.shape('red.gif')

floorbg = 'floor1.gif'

gameover = turtle.clone()
turtle.register_shape('gameover.gif')
gameover.shape('gameover.gif')

sleeping = turtle.clone()
turtle.register_shape('Sleeping.gif')
sleeping.shape('Sleeping.gif')

blinking = turtle.clone()
turtle.register_shape('Blinking.gif')
blinking.shape('Blinking.gif')

#angrep animation turtles
attackANI = turtle.clone()
turtle.register_shape('Slash.gif')
attackANI.shape('Slash.gif')
turtle.register_shape('fireball.gif')
turtle.register_shape('fireball1.gif')

#--------Variabler som opptateres gjennom koden--------

#bruker variabler
user_health = 100
max_user_health = 100 #sier høyeste verdi på "user_health"
user_stamina = 100
max_user_stamina = 100
user_mana = 100
max_user_mana = 100
lowest_user_dmg = 7
highest_user_dmg = 43

#monster variabeler
monster_health = 50
max_monsterHP = 50
monsters_death = 0
find_monster_list = [True,True,False]
lowest_monster_dmg = 3
highest_monster_dmg = 37
monster_pic = 'Goblin'
monster_ANI = '1'

#spillvariabler
in_combat = False
attack_modeON = False
hit = [True,True,False]
explored_times = 0
game_running = False
floor = 1
floor_prog = 3
flees = 3




main_menu() #starter spillet
turtle.done()