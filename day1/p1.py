import os
class Dail:

    def __init__(self):
        self.curr_pos = 50
        self.key = 0


    def rotate(self, rotation):

        rotation = rotation.lower()
        direction =  rotation[0]
        rotations = int(rotation[1:])

        self.key += rotations //100
        rotations = rotations % 100

        if rotations % 100 == 0:
            return

        if direction == "r":
            if self.curr_pos + rotations > 100:
                self.key +=1
            self.curr_pos = (self.curr_pos + rotations) % 100
        elif direction =="l":
            prev_pos = self.curr_pos
            self.curr_pos =  self.curr_pos - rotations
            if self.curr_pos < 0:
                if prev_pos !=0:
                    self.key +=1
                self.curr_pos = self.curr_pos+100
        
        if self.curr_pos == 0:
            self.key +=1



dail = Dail()

with open("./P1input.txt","r") as f :
    f.seek(0)
    lines = f.readlines()


for line in lines:
    dail.rotate(line)


print(dail.key)
