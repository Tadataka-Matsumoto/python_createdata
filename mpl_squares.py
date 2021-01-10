import matplotlib.pyplot as plt#p97で登場


input_values = [1, 2, 3, 4, 5]#p100で追加（グラフを見やすくするため）
squares = [1, 4 ,9 , 16, 25]#p97で登場


plt.style.use('seaborn')#組み込みのseaborn登場p102
# plt.style.use('Solarize_Light2')#p101
# plt.style.use('_classic_test_patch')#p101
# plt.style.use('bmh')#p101
# plt.style.use('classic')#p101

fig, ax = plt.subplots()#p97で登場、変数figは生成された図全体、axは図の中の一つのプロットを表す(p97-p98)
# ax.plot(squares)#p97の元のグラフ(x軸に該当するものがないとy軸のみが表示される)
ax.plot(input_values, squares, linewidth=3)#p99で変更追加のlinewidhは線の太さ(p99)

#グラフのタイトルと軸のラベルと設定する(P99)
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#目盛ラベルのサイズを設定する(p99)
ax.tick_params(axis='both', labelsize=14)#axis=bothはx軸、y軸ともにメモリを付ける(p99)



plt.show()#p97で登場、関数でmatplotlibのビューアーを開いてグラフを表示する

