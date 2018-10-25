import numpy as np

class Game:
    END = -1
    NOTMOVE = 0
    MOVE = 1

    RATE = 0.75

    number = np.zeros((4,4),dtype=int)
    Flag = NOTMOVE
    Score = 0

    def __init__(self, status = "当前得分:{}", tips = "wasd移动,r重新开始，按q退出", end = "您的最终得分为：{}"):
        self.status, self.tips, self.endstring = status, tips, end
        self.init()

#这里明显是个性能瓶颈，要不用个队列记录空闲位置
    def getpos(self):
        a = np.random.randint(0,4)
        b = np.random.randint(0,4)
        if self.number[a][b]:
            return self.getpos()
        return (a,b)

    def getnum(self):
        if np.random.randn() < self.RATE:
            return 2
        else:
            return 4

    def init(self):
        self.Flag = self.MOVE
        self.number.fill(0)
        self.number[self.getpos()] = self.getnum()
        self.number[self.getpos()] = self.getnum()
   
    def generate(self):
        if self.Flag == self.MOVE:
            self.number[self.getpos()] = self.getnum()
            self.Flag = self.NOTMOVE

    def add(self, aimpos, pos2):
        self.number[aimpos] += self.number[pos2]
        self.Score +=  self.number[pos2]
        self.number[pos2] = 0
        self.Flag = self.MOVE
        

    def move(self, aimpos, pos2):
        self.number[aimpos] = self.number[pos2]
        self.number[pos2] = 0
        self.Flag = self.MOVE


    def up(self):
        if self.Flag == self.END:
            return 
        for j in range(4):
            for i in range(4):
                if not self.number[i][j]:
                    z = i
                    while z < 3 and not self.number[z][j]:
                        z += 1
                    if self.number[z][j]:
                        self.move((i,j), (z,j))
                if self.number[i][j] and i > 0:
                    if self.number[i][j] == self.number[i-1][j]:
                        self.add((i-1,j), (i,j))
                        if not self.number[i][j]:
                            z = i
                            while z < 3 and not self.number[z][j]:
                                z += 1
                            if self.number[z][j]:
                                self.move((i,j), (z,j))

    def left(self):
        if self.Flag == self.END:
            return
        for i in range(4):
            for j in range(4):
                if not self.number[i][j]:
                    z = j
                    while z < 3 and not self.number[i][z]:
                        z += 1
                    if self.number[i][z]:
                        self.move((i,j), (i,z))
                if self.number[i][j] and j > 0:
                    if self.number[i][j] == self.number[i][j-1]:
                        self.add((i, j-1), (i, j))
                        if not self.number[i][j]:
                            z = j
                            while z < 3 and not self.number[i][z]:
                                z += 1
                            if self.number[i][z]:
                                self.move((i,j), (i,z))

    def down(self):
        if self.Flag == self.END:
            return
        for j in range(4):
            for i in range(3,-1,-1):
                if not self.number[i][j]:
                    z = i
                    while z > 0 and not self.number[z][j]:
                        z -= 1
                    if self.number[z][j]:
                        self.move((i, j), (z, j))
                if self.number[i][j] and i < 3:
                    if self.number[i][j] == self.number[i+1][j]:
                        self.add((i+1, j), (i, j))
                        if not self.number[i][j]:
                            z = i
                            while z > 0 and not self.number[z][j]:
                                z -= 1
                            if self.number[z][j]:
                                self.move((i, j), (z, j))

    def right(self):
        if self.Flag == self.END:
            return
        for i in range(4):
            for j in range(3,-1,-1):
                if not self.number[i][j]:
                    z = j
                    while z > 0 and not self.number[i][z]:
                        z -= 1
                    if self.number[i][z]:
                        self.move((i, j), (i, z))
                if self.number[i][j] and j < 3:
                    if self.number[i][j] == self.number[i][j+1]:
                        self.add((i, j+1), (i, j))
                        if not self.number[i][j]:
                            z = j
                            while z > 0 and not self.number[i][z]:
                                z -= 1
                            if self.number[i][z]:
                                self.move((i, j), (i, z))

    def __refresh(self):
        self.statusbar = self.status.format(self.Score)

    def show(self):
        self.__refresh()
        print(self.statusbar)
        print(self.number)
        print(self.tips)

    def content(self):
        if self.Flag == self.END:
            return '\n' + self.endstring.format(self.Score) 
        else:
            string = "目前获得分数为：" + str(self.Score) + '\n'
            '''
            string += '_' * (len(str(self.number)) // 4) + '\n' 
            for i in range(4):
                string += '|'
                for j in range(4):
                    if self.number[i][j] == 0:
                        string += ' _ '
                    else:
                        string += ' {} '.format(self.number[i][j])  
                string += '|\n'
            string += '_' * (len(str(self.number)) // 4) + '\n'
            '''
            string += str(self.number)             
        return  string

    def isEND(self):
        if self.Flag == self.NOTMOVE:
            if self.number.all():
                origin = self.number.copy()
                self.up()
                self.left()
                self.down()
                self.right()
                if (origin == self.number).all():
                    self.Flag = self.END
                else:
                    self.number = origin
                    

    def end(self):
        self.Flag = self.END
        print(self.endstring.format(self.Score))

    def main(self):
        self.init()
        self.show()

        while True:
            self.isEND()
            a = input()
            if a == 'w':
                self.up()
            elif a == 'a':
                self.left()
            elif a == 's':
                self.down()
            elif a == 'd':
                self.right()
            elif a == 'r':
                self.init()
                self.show()
                continue
            elif a == 'q':
                self.end()
                break
            else:
                continue
            self.generate()
            self.show()

if __name__ == '__main__':
    game = Game()
    game.main()
