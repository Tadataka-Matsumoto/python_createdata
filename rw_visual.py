import matplotlib.pyplot as plt

from random_walk import RandomWalk#(p111)

#プログラムが動作している間、新しいランダムウォークを作成し続ける(p112)
while True:

    #ランダムウォークを作成する(p111)
    # rw = RandomWalk()#ランダムウォークのインスタンスrwを作成
    rw = RandomWalk(50000)#50000点にしてみる(p116)
    rw.fill_walk()#fill_walk関数を実行する

    #ランダムウォークの点を描画する(p111)
    plt.style.use('classic')#classicを今回は使う
    fig, ax = plt.subplots()
    # ax.scatter(rw.x_values, rw.y_values, s=15)#リストのx_valueとy_valueを読んでs=15ポイントでプロット(p111)
    point_numbers = range(rw.num_points)#p114
    # ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
    #     edgecolors='none', s=15)#p114
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
        edgecolors='none', s=1)#s=1にする！！(p116)

    #開始点と終了点を強調する(p115)
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
        s=100)

    #軸を削除する(p115)
    # ax.get_xaxis().set_visible(False)
    # ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("別のランダムウォークを生成する?(y/n):")#p113で追加
    if keep_running == 'n':
        break
