import time
from config import *
#TODO: meer commentaar

class RotaryGame:
    last_rotary_encoder_position = 0  
    current_ring = 0
    current_position = 0  
    kleur = [
        (2,1,2),     # 0 achtergrond (lichtpaars)
        (20,0,0),    # 1 verboden op te staan (rood)
        (0,0,0)      # 2 doel (zwart)
    ]
    cursor_color = (30, 30, 30)
    timing_interval = 1.0
    last_background_update = 0
    timer_count = 0
    start_time_game = 0
    level = 1

    def startGame(self):
        numpixel0 = NUM_PIXELS[0]
        numpixel1 = NUM_PIXELS[1]
    
        self.current_ring = 0
        self.current_position = 0
        self.achtergrond_patroon = [
         [0 for i in range(NUM_PIXELS[0])],
         [0 for i in range(NUM_PIXELS[1])]
        ]
        
        self.flush_rotary_encoder()

        #TODO shortcuts voor achtergrondpatroon
       
        if self.level==1:
            self.start_time_game = 0
            self.current_ring = 1
            self.current_position = numpixel1*3//4
            self.achtergrond_patroon[0][0] = 2

        elif self.level==2:
            self.current_position = numpixel0//2
            self.achtergrond_patroon[0][0] = 2

        elif self.level==3:
            self.current_ring = 1
            self.achtergrond_patroon[0][numpixel0//2-1] = 2

        elif self.level==4:
            self.current_ring = 1
            self.current_position = numpixel1//2
            self.achtergrond_patroon[0][0] = 2
            self.achtergrond_patroon[1][numpixel1//4] = 1
            self.achtergrond_patroon[1][numpixel1*3//4] = 1

        elif self.level==5:
            self.achtergrond_patroon[0][numpixel0//2+1] = 2
            
            self.achtergrond_patroon[1][0] = 1
            self.achtergrond_patroon[1][numpixel1//2] = 1
            self.draaiRing(1,1)
            
            self.achtergrond_patroon[0][numpixel0*1//4] = 1
            self.achtergrond_patroon[0][numpixel0*3//4] = 1

        elif self.level==6:
            self.current_ring = 1
            self.current_position = numpixel1//3
            
            self.achtergrond_patroon[0][numpixel0//8] = 2
            
            self.achtergrond_patroon[1][numpixel1*1//4-1] = 1
            self.achtergrond_patroon[1][numpixel1*3//4+2] = 1
            
            self.achtergrond_patroon[0][numpixel0*0//4] = 1
            self.achtergrond_patroon[0][numpixel0*1//4] = 1
            self.achtergrond_patroon[0][numpixel0*2//4] = 1
            self.achtergrond_patroon[0][numpixel0*3//4] = 1
            
        elif self.level==7:
            self.current_ring = 1
            self.current_position = 2
            for pos in range (numpixel0//4):
                self.achtergrond_patroon[0][pos] = 1
            for pos in range (numpixel0//4-2):
                self.achtergrond_patroon[0][numpixel0//2+pos] = 1
            for pos in range (numpixel1//4-1):
                self.achtergrond_patroon[1][numpixel1//4 + pos] = 1
            for pos in range (numpixel1//4 -2):
                self.achtergrond_patroon[1][numpixel1*3//4 + pos] = 1

            self.achtergrond_patroon[0][numpixel0//3] = 2

        elif self.level==8:
            self.current_ring = 1
            self.current_position = numpixel1//2
            self.achtergrond_patroon[0][0] = 1
            self.achtergrond_patroon[1][numpixel1*1//4] = 1
            self.achtergrond_patroon[1][numpixel1*3//4] = 1

            self.achtergrond_patroon[1][0] = 2
            self.timing_interval = 0.02
            
        elif self.level==9:
            self.current_ring = 1
            self.current_position = numpixel1//2-5
            self.achtergrond_patroon[0][0] = 1
            self.achtergrond_patroon[1][numpixel1*1//4] = 1
            self.achtergrond_patroon[1][numpixel1*3//4] = 1
            self.achtergrond_patroon[1][numpixel1*1//2] = 1
            self.achtergrond_patroon[1][0] = 1
            self.achtergrond_patroon[1][numpixel1-4] = 2
            self.draaiRing(1,2)
            
            self.timing_interval = 0.015
        
        elif self.level==10:
            self.current_ring = 0
            self.current_position = numpixel0//2
            self.achtergrond_patroon[0][0] = 2
            self.achtergrond_patroon[1][numpixel1*3//4] = 1
            self.achtergrond_patroon[1][numpixel1//4] = 1
            self.draaiRing(1,4)
            
        elif self.level==11:
            self.current_ring = 1
            self.current_position = numpixel1//2
            self.achtergrond_patroon[1][0] = 2
            self.achtergrond_patroon[0][0] = 1
            self.timing_interval = 0.015

        elif self.level==12:
            self.current_ring = 0
            self.current_position = 0
            self.achtergrond_patroon[0][numpixel0//2+3] = 2
            self.achtergrond_patroon[1][0] = 1
            self.achtergrond_patroon[1][numpixel1//2] = 1
            self.achtergrond_patroon[0][numpixel0//4*3+2] = 1
            self.achtergrond_patroon[0][numpixel0//4*3-5] = 1
            self.timing_interval = 1.2/numpixel1
            for pos in range (6):
                self.achtergrond_patroon[0][pos+12] = 1
            for pos in range (3):
                self.achtergrond_patroon[0][numpixel0//2-pos-3] = 1

        elif self.level==13:
            self.current_ring = 1
            self.current_position = 20
            self.achtergrond_patroon[1][0] = 2
            for pos in range (numpixel1//4):
                self.achtergrond_patroon[1][pos+1] = 1
            for pos in range (numpixel1//4):
                self.achtergrond_patroon[1][numpixel1-10+pos] = 1
            for pos in range (numpixel0//6):
                self.achtergrond_patroon[0][pos*6] = 1

        elif self.level==14:
            self.current_ring = 0
            self.current_position = 0
            self.achtergrond_patroon[1][numpixel1//2-1] = 2
            for pos in range (numpixel0//4*3+1):
                self.achtergrond_patroon[0][pos+5] = 1
            for pos in range (3):
                self.achtergrond_patroon[1][numpixel1//2-6+pos] = 1
            for pos in range (3):
                self.achtergrond_patroon[1][numpixel1//2+2+pos] = 1

        elif self.level==15:
            self.current_ring = 0
            self.current_position = numpixel0//2+3
            self.achtergrond_patroon[0][3] = 2
            for pos in range (numpixel0//6):
                self.achtergrond_patroon[0][pos*6] = 1
            self.achtergrond_patroon[1][numpixel1//2] = 1
            self.achtergrond_patroon[1][0] = 1
            self.draaiRing(1,2)
            self.timing_interval = 2/numpixel1

        elif self.level==16:
            self.current_ring = 0
            self.current_position = numpixel0//2
            self.achtergrond_patroon[0][0] = 2
            for pos in range (3):
                self.achtergrond_patroon[0][pos+1] = 1
            for pos in range (3):
                self.achtergrond_patroon[0][numpixel0-3+pos] = 1
            self.achtergrond_patroon[1][0] = 1
            self.achtergrond_patroon[1][numpixel1//3*2] = 1
            self.achtergrond_patroon[1][numpixel1//3] = 1
            self.draaiRing(1,2)
            self.timing_interval = 0.04
            self.timer_count = 1

        elif self.level==17:
            self.timer_count = 0
            self.achtergrond_patroon[0][numpixel0//2] = 2
            self.achtergrond_patroon[0][numpixel0*1//5] = 1
            self.achtergrond_patroon[0][numpixel0*2//5] = 1
            self.achtergrond_patroon[0][numpixel0*4//6] = 1
            self.achtergrond_patroon[0][numpixel0*5//6] = 1
            self.achtergrond_patroon[1][numpixel1//4] = 1
            self.achtergrond_patroon[1][numpixel1*3//4] = 1
            self.timing_interval = 2.8/numpixel1
    
    def timerEvent(self):
        numpixel0 = NUM_PIXELS[0]
        numpixel1 = NUM_PIXELS[1]
        
        if self.level==8:
            self.draaiRing(0,1)
        elif self.level==9:
            self.draaiRing(0,1)
        elif self.level==11:
            self.draaiRing(0,1)
        elif self.level==12:
            self.draaiRing(1,1)
        elif self.level==15:
            self.draaiRing(1,1)
        elif self.level==16:
            if self.timer_count%3 == 0:
                self.draaiRing(1,1)
            links = numpixel0 - self.timer_count
            rechts = self.timer_count
            self.achtergrond_patroon[0][0] = 2
            for pos in range (1,numpixel0):
                self.achtergrond_patroon[0][pos] = 0
            for pos in range (3):
                self.achtergrond_patroon[0][pos+1] = 1
            for pos in range (3):
                self.achtergrond_patroon[0][numpixel0-3+pos] = 1

            self.achtergrond_patroon[0][links] = 1
            self.achtergrond_patroon[0][rechts] = 1
            if rechts >= links:
                self.timer_count=1
            else:
                self.timer_count = self.timer_count+1
        elif self.level==17:
            self.draaiRing(1,1)
            if self.timer_count %3 == 0:
                self.draaiRing(0,1)
            self.timer_count = self.timer_count+1
                
        self.checkEndLevel()

    def onButtonPressed(self):
        if self.start_time_game == 0:
            self.start_time_game = time.monotonic()
        old_ring = self.current_ring
        self.current_ring = 1-old_ring
        self.current_position = (round(self.current_position*NUM_PIXELS[self.current_ring]/NUM_PIXELS[old_ring]))% NUM_PIXELS[self.current_ring]
        self.updatePixels()
        self.checkEndLevel()
        
    def onRotary(self,steps):
        if self.start_time_game == 0:
            self.start_time_game = time.monotonic()

        step = 1 if steps > 0 else -1 if steps < 0 else 0
        for count in range (abs(steps)):
            self.current_position = (self.current_position + step) % NUM_PIXELS[self.current_ring]
            if self.level==10 and self.current_ring==0:
                self.draaiRing(0,step)
            elif self.level==11 and self.current_ring==1:
                self.draaiRing(1,step)
            elif self.level==13 and self.current_ring==1:
                self.draaiRing(1,step)
            elif self.level==13 and self.current_ring==0:
                self.draaiRing(0,step)
            elif self.level==14 and self.current_ring==1:
                self.draaiRing(1,step)
            elif self.level==15 and self.current_ring==0:
                self.draaiRing(0,step)
            self.updatePixels()
            self.checkEndLevel()

    def checkEndLevel(self):
        status = self.achtergrond_patroon[self.current_ring][self.current_position]
        if status == 1: # cursor komt op rode pixel
            #failed, game over start level again
            self.ledShowGameOver()
            self.startGame()
        elif status == 2: # doelpixel bereikt
            #yes, next level
            self.ledShowNextLevel()
            self.level = self.level+1
            print(self.level)
            if self.level==18:
                self.endGameShow()
                self.level=1
            self.startGame()

    def ledShowGameOver(self):
        time.sleep(0.1)
        ring = self.current_ring
        for i in range(NUM_PIXELS[ring]//2+1):
            pos1 = (self.current_position+i)%NUM_PIXELS[ring]
            pos2 = (self.current_position-i)%NUM_PIXELS[ring]
            pixels[pos1+LED_START[ring]] = (25,0,0)
            pixels[pos2+LED_START[ring]] = (25,0,0)
            pixels.show()
            time.sleep(0.01)
        ring = 1-ring
        for i in range(NUM_PIXELS[ring]):
            pixels[i+LED_START[ring]] = (25,0,0)
        pixels.show()
        time.sleep(1)
        #TODO licht laten dimmen


    def ledShowNextLevel(self):
        ring = self.current_ring
        for i in range(NUM_PIXELS[ring]//2):
            pos1 = (self.current_position+i)%NUM_PIXELS[ring]
            pos2 = (self.current_position-i)%NUM_PIXELS[ring]
            pixels[pos1+LED_START[ring]] = (0,0,25)
            pixels[pos2+LED_START[ring]] = (0,0,25)
            pixels.show()
            time.sleep(0.01)
            
        ring = 1-ring
        for i in range(NUM_PIXELS[ring]//2,0,-1):
            pos1 = (self.current_position+i)%NUM_PIXELS[ring]
            pos2 = (self.current_position-i)%NUM_PIXELS[ring]
            pixels[pos1+LED_START[ring]] = (0,0,25)
            pixels[pos2+LED_START[ring]] = (0,0,25)
            pixels.show()
            time.sleep(0.01)
        time.sleep(0.200)
        #TODO: licht laten dimmen
        
        
    def endGameShow(self):
        playtime = time.monotonic()-self.start_time_game
        minutes = playtime//60
        seconds = round(playtime)%60
        for ring in range (2):
            for i in range(NUM_PIXELS[ring]):
                pixels[i+LED_START[ring]] = (0,0,0)
        for i in range(min(minutes,NUM_PIXELS[1])):
            pixels[i+LED_START[1]] = (0,0,25)
        for i in range(min(seconds*NUM_PIXELS[0]/60,NUM_PIXELS[0])):
            pixels[i+LED_START[0]] = (0,0,25)
        pixels.show()
        time.sleep(10)
        
    def flush_rotary_encoder(self):
        self.last_rotary_encoder_position = encoder.position
        
    def draaiRing(self,ringnr,stappen):
        self.achtergrond_patroon[ringnr] = self.achtergrond_patroon[ringnr][-stappen:] + self.achtergrond_patroon[ringnr][:-stappen]
            
    def updatePixels(self):
        for ring in range (2):
            for i in range(NUM_PIXELS[ring]):
                pixels[i+LED_START[ring]] = self.kleur[self.achtergrond_patroon[ring][i]]

        # Add foreground pixel to current pattern
        pixels[self.current_position+LED_START[self.current_ring]] = self.cursor_color       
        pixels.show()
        
    def loop(self):
        switch_button.update()
        if switch_button.fell:
            game.onButtonPressed()

        switch_rotarybutton.update()
        if switch_rotarybutton.fell:
            game.onButtonPressed()
            
        # Check rotary encoder movement immediately
        new_position = encoder.position
        if new_position != self.last_rotary_encoder_position:
            steps = new_position - self.last_rotary_encoder_position
            self.last_rotary_encoder_position = new_position
            game.onRotary(steps) # calls flush_rotary_encoder

        # calls timerEvent() every timing_interval seconds
        current_time = time.monotonic()
        if current_time - self.last_background_update >= self.timing_interval:
            self.timerEvent()
            self.last_background_update = current_time
            
        self.updatePixels()
        
    def run(self):
        self.startGame()
        while True:
            self.loop()

# main
game = RotaryGame()
game.run()
