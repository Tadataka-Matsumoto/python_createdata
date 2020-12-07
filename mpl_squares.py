import matplotlib.pyplot as plt


input_values = [1, 2, 3, 4, 5]
squares = [1, 4 ,9 , 16, 25]


plt.style.use('seaborn')
# plt.style.use('Solarize_Light2')#p101
# plt.style.use('_classic_test_patch')#p101
# plt.style.use('bmh')#p101
# plt.style.use('classic')#p101

fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

#グラフのタイトルと軸のラベルと設定する
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#目盛ラベルのサイズを設定する
ax.tick_params(axis='both', labelsize=14)



plt.show()

