import matplotlib.pyplot as plt

# x_values = [1, 2, 3, 4, 5]#p104で追加
# y_values = [1, 4, 9, 16, 25]#p104で追加

x_values = range(1, 1001)#p105で変更
y_values = [x**2 for x in x_values]#p105で変更


plt.style.use('seaborn')#styleをseabornとする(p103)
fig, ax = plt.subplots()#p103
# ax.scatter(2, 4, s=200)#scatterメソッド登場,一つの点を描画(p103)
# ax.scatter(x_values, y_values, s=100)#p104で追加、5点の散布図となる
# ax.scatter(x_values, y_values, s=10, c='orange')#p105,106で点のサイズ変更とカラー追加、順序逆でも行ける！！
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)#(p105)

#グラフのタイトルと軸ラベルを設定する(p103)
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)


#目盛りラベルのサイズを設定する
ax.tick_params(axis='both', which='major', labelsize=14)#目盛ラベルのサイズ設定(p103)

# 各軸の範囲を設定する
ax.axis([0, 1100, 0, 1100000])#x軸の範囲(0～1100)とy軸の範囲(0～1100000)を設定(p105)

# plt.show()
plt.savefig('squares_plot.png', bbox_inches='tight')#余白を削除する場合の保存(p108)
# plt.savefig('squares_plot.png')#余白がある場合の保存(p108)あんまり変わらなかった。。。