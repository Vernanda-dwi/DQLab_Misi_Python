#memisahkan nama pada customer_name menjadi dua kolom yaitu nama_depan dan nama_belakang
#1 mengambil kolom
import pandas as pd 
dataku = pd.read_excel('SuperStore.xlsx')
dataku_awal = dataku.head() # menampilkan 5 data awal
dataku = dataku[['Customer_Name']] #menampilkan data pada kolom customer name

#2 memisahkan kolomnya
data1 = pd.read_excel('SuperStore.xlsx')
data2 = data1['Customer_Name'].str.split(' ', n=1, expand=True)

#3 memanggil kolom nama depan dan belakang saja
data1['Nama_Depan'] = data2[0]
data1['Nama_Belakang'] = data2[1]
#print(data1[['Nama_Depan','Nama_Belakang']].head())

#3 memanggil kolom nama depan dan belakang dan memasukkannya ke data superstore (namun kolom customer name tidak terhapus)
data1['Nama_Depan'] = data2[0]
data1['Nama_Belakang'] = data2[1]
print(data1.head())


#3 memanggil kolom nama depan dan belakang dan memasukkannya ke data superstore (namun kolom customer name terhapus)
data1['Nama_Depan'] = data2[0]
data1['Nama_Belakang'] = data2[1]
data1 = data1.drop(columns=['Customer_Name']) #menghapus suatu kolom
#print(data1.head())







