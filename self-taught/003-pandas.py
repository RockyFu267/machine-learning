import pandas
from IPython.display import display

data = {
    "name" : ["老八","卷毛","穿桑","顺妃","美东","外马儿","公巴佩","迪牛利亚","西洛","球王","求神"],
    "city" : ["北京","上海","北京","成都","广州","北京","上海","成都","广州","广州","广州"],
    "age" : ["8","9","10","11","22","23","22","9","8","25","8"],
    "height" : ["118","109","100","121","222","23","222","219","128","125","822"]
}
data_frame = pandas.DataFrame(data)
# display(data_frame[data_frame.city != "北京"])
print(data_frame[data_frame.city != "北京"])
