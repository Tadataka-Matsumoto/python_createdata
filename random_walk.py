from random import choice#必p208にある。randomはpython標準ライブラリ()

class RandomWalk:
    """ランダムウォークを生成するためのクラス"""

    def __init__(self, num_points=5000):
        """ランダムウォークの属性を初期化する(p109)"""
        self.num_points = num_points

        #すべてのランダムウォークは(0, 0)から開始する(p109)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):#(p110)
        """ランダムウォークのすべての点を計算する"""
        while len(self.x_values) < self.num_points:

            #移動する方向と距離を決定する(p110)
            x_direction = choice([1, -1])#randomからchoiseを読んだ
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            #どこにも移動しない場合は結果を破棄する(p110)
            if x_step == 0 and y_step == 0:
                continue#必p142に説明あり！！

            #新しい位置を計算する
            x = self.x_values[-1] + x_step#[-1]は最後の配列必p53参照(p110)
            y = self.y_values[-1] + y_step

            self.x_values.append(x)#p110
            self.y_values.append(y)





