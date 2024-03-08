class Dice:
    def __init__(self):
        self.side1 = 0
        self.side2 = 0
        self.side3 = 0
        self.side4 = 0
        self.side5 = 0
        self.side6 = 0

    def set(self, side):
        self.side1 = side[0]
        self.side2 = side[1]
        self.side3 = side[2]
        self.side4 = side[3]
        self.side5 = side[4]
        self.side6 = side[5]

    def roll(self, d):
        if d == 'N':
            tmp = self.side1
            self.side1 = self.side2
            self.side2 = self.side6
            self.side6 = self.side5
            self.side5 = tmp
        elif d == 'E':
            tmp = self.side1
            self.side1 = self.side4
            self.side4 = self.side6
            self.side6 = self.side3
            self.side3 = tmp
        elif d == 'S':
            tmp = self.side1
            self.side1 = self.side5
            self.side5 = self.side6
            self.side6 = self.side2
            self.side2 = tmp
        elif d == 'W':
            tmp = self.side1
            self.side1 = self.side3
            self.side3 = self.side6
            self.side6 = self.side4
            self.side4 = tmp
        elif d == 'ES':
            tmp = self.side5
            self.side5 = self.side4
            self.side4 = self.side2
            self.side2 = self.side3
            self.side3 = tmp
    
    def print(self):
        print(self.side1, self.side2, self.side3, self.side4, self.side5, self.side6)

    def set_dice_direction(self, top_num, front_num):
        while True:
            if self.get_num('front') == front_num:
                if self.get_num('top') == top_num:
                    break
                else:
                    self.roll('ES')
                    continue
            elif self.get_num('top') == top_num:
                if self.get_num('front') == front_num:
                    break
                else:
                    self.roll('E')
                    continue
            self.roll('S')

    def get_num(self, side):
        num = 0
        if side == 'front':
            num = self.side1
        elif side == 'under':
            num = self.side2
        elif side == 'right':
            num = self.side3
        elif side == 'left':
            num = self.side4
        elif side == 'top':
            num = self.side5
        elif side == 'back':
            num = self.side6
        
        return num

dice = Dice()
dice.set(list(map(int, input().split())))

q = int(input())

for _ in range(q):
    t, f = map(int, input().split())

    dice.set_dice_direction(t, f)
    print(dice.get_num('right'))
