from plotly.graph_objs import Bar, Layout#p121参照
from plotly import offline#p121参照

from die import Die#Dieクラスをインポート(p119参照)

#2個のD6サイコロを作成する(p123)
die_1 = Die()#インスタンス作成(p119参照)
die_2 = Die(10)#p125

#サイコロを転がし、結果をリストに格納する(p120参照)
results = []
for roll_num in range(100000):
    result = die_1.roll()+die_2.roll()#die1とdie2インスタンスにrollメソッド実行
    results.append(result)

#結果を分析する(p120参照)
frequencies = []
max_result = die_1.num_sides + die_2.num_sides#(p123)
for value in range(2, max_result+1):
    frequency = results.count(value)#こんな便利なメソッドあるんだ(p120参照)
    frequencies.append(frequency)

print(frequencies)#一応入れておく


#結果を可視化する(p121参照)
x_values = list(range(2, max_result+1))#つまり[2,3,4,5,6,...](p123)
data = [Bar(x=x_values, y=frequencies)]#Barクラスを設定中身は[[1,2,3,4,5,6],[x,xx,xxx,xxxx,xxxxx,xxxxxx]](p121)

x_axis_config = {'title': '結果', 'dtick':1}#軸の設定、辞書データの一要素として保存する(p123)
y_axis_config = {'title': '発生した回数'}
# my_layout = Layout(title='2個の6面のサイコロを1000回転がした結果',#p12
my_layout = Layout(title='6面のサイコロと10面サイコロを100000回転がした結果',
        xaxis=x_axis_config, yaxis=y_axis_config)#p125       
# offline.plot({'data':data, 'layout':my_layout}, filename='d6_d6.html')#p123
offline.plot({'data':data, 'layout':my_layout}, filename='d6_d10.html')#p125

