import pandas

data=pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
gry_sq=len(data[data['Primary Fur Color']=="Gray"])
print(gry_sq)
cin_sq=len(data[data['Primary Fur Color']=="Cinnamon"])
print(cin_sq)
wht_sq=len(data[data['Primary Fur Color']=="Black"])
print(wht_sq)


data_dict={
    'Fur Color':['Gray','Cinnamon','Black'],
    "Count":[gry_sq,cin_sq,wht_sq]
}


print(data_dict)


df=pandas.DataFrame(data_dict)
df.to_csv('squirrel_fur_color.csv') 