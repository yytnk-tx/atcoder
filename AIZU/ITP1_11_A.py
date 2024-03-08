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
            # self.side3 = self.side3
            # self.side4 = self.side4
        elif d == 'E':
            tmp = self.side1
            self.side1 = self.side4
            self.side4 = self.side6
            self.side6 = self.side3
            self.side3 = tmp
            # self.side2 = self.side2
            # self.side5 = self.side5
        elif d == 'S':
            tmp = self.side1
            self.side1 = self.side5
            self.side5 = self.side6
            self.side6 = self.side2
            self.side2 = tmp
            # self.side3 = self.side3
            # self.side4 = self.side4
        elif d == 'W':
            tmp = self.side1
            self.side1 = self.side3
            self.side3 = self.side6
            self.side6 = self.side4
            self.side4 = tmp
            # self.side2 = self.side2
            # self.side5 = self.side5

    def get_side_num(self, side_num):
        num = 0
        if side_num == 1:
            num = self.side1
        elif side_num == 2:
            num = self.side2
        elif side_num == 3:
            num = self.side3
        elif side_num == 4:
            num = self.side4
        elif side_num == 5:
            num = self.side5
        elif side_num == 6:
            num = self.side6
        
        return num

dice = Dice()
dice.set(list(map(int, input().split())))

roll_directions = input()

for d in roll_directions:
    dice.roll(d)

print(dice.get_side_num(1))
