class Dice:
    def __init__(self):
        self.side = [0] * 6

    def set(self, side):
        self.side = side.copy()

    def roll(self, d):
        if d == 'N':
            tmp = self.side[0]
            self.side[0] = self.side[1]
            self.side[1] = self.side[5]
            self.side[5] = self.side[4]
            self.side[4] = tmp
        elif d == 'E':
            tmp = self.side[0]
            self.side[0] = self.side[3]
            self.side[3] = self.side[5]
            self.side[5] = self.side[2]
            self.side[2] = tmp
        elif d == 'S':
            tmp = self.side[0]
            self.side[0] = self.side[4]
            self.side[4] = self.side[5]
            self.side[5] = self.side[1]
            self.side[1] = tmp
        elif d == 'W':
            tmp = self.side[0]
            self.side[0] = self.side[2]
            self.side[2] = self.side[5]
            self.side[5] = self.side[3]
            self.side[3] = tmp
        elif d == 'ES':
            tmp = self.side[4]
            self.side[4] = self.side[3]
            self.side[3] = self.side[1]
            self.side[1] = self.side[2]
            self.side[2] = tmp
    
    def print(self):
        print(*self.side)

    def is_dice_match(self, dice):
        is_match = False
        roll_pattern = ('N', 'W', 'N', 'W', 'N', 'W')

        if self.side == dice.side:
            is_match = True

        for d in roll_pattern:
            if is_match:
                break

            dice.roll(d)
            for _ in range(4):
                dice.roll('ES')
                if self.side == dice.side:
                    is_match = True

        return is_match    

    def set_dice_direction(self, top_num, front_num):
        for _ in range(9):
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
            num = self.side[0]
        elif side == 'under':
            num = self.side[1]
        elif side == 'right':
            num = self.side[2]
        elif side == 'left':
            num = self.side[3]
        elif side == 'top':
            num = self.side[4]
        elif side == 'back':
            num = self.side[5]
        
        return num

dice1, dice2 = Dice(), Dice()
dice1.set(list(map(int, input().split())))
dice2.set(list(map(int, input().split())))

if dice1.is_dice_match(dice2):
    print('Yes')
else:
    print('No')
