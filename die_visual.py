from plotly.graph_objs import Bar, Layout#p121
from plotly import offline#p121

from die import Die#Dieクラスをインポート(p119)

#D6を作成する
die = Die()#インスタンス作成(p119)

#サイコロを転がし、結果をリストに格納する(p120)
results = []
for roll_num in range(1000):
    result = die.roll()#dieインスタンスにrollメソッド実行
    results.append(result)

#結果を分析する
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)#こんな便利なメソッドあるんだ(p120)
    frequencies.append(frequency)

print(frequencies)#p120


#結果を可視化する(p121)
x_values = list(range(1, die.num_sides+1))#つまり[1,2,3,4,5,6](p121)
data = [Bar(x=x_values, y=frequencies)]#Barクラスを設定中身は[[1,2,3,4,5,6],[x,xx,xxx,xxxx,xxxxx,xxxxxx]](p121)

x_axis_config = {'title': '結果'}#軸の設定、辞書データの一要素として保存する(p122)
y_axis_config = {'title': '発生した回数'}
my_layout = Layout(title='6面のサイコロを1000回転がした結果',
        xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data':data, 'layout':my_layout}, filename='d6.html')

# print(results)
# print(frequencies)

