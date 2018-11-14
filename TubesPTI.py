# Program Analisis Data
#

'''
### CATATAN PENTING ###
Untuk dapat me-run kode ini, masukkan 'pip install xlrd'
pada command prompt/terminal

Data yang digunakan pada program ini dapat diunduh dari
https://archive.ics.uci.edu/ml/datasets/Absenteeism+at+work
Tempatkan program & file data pada folder yang sama
### ------- ------- ###

### TODO LIST OZER ###
- Buat filenya bisa user input
- Cek keberadaan file excel
- Orang paling sering bolos v
### ---- ---- ---- ###


PENGGUNAAN FUNGSI-FUNGSI
GetTimeSeries - Mendapatkan time series Bulan-Tahun terhadap jumlah orang absen
GetMonthLabel - Mengubah bulan dalam angka menjadi dalam kata-kata
GetFixedData - Mengambil data pertama tiap orang
               (untuk menentukan nilai data diskrit tiap orang)

'''

# --KAMUS--

# --ALGORITMA--

# BLOK INISIALISASI
# Import dependencies yang dibutuhkan
import pandas as pd
import matplotlib.pyplot as plt

# Fungsi mencari data Time Series jumlah orang absen
def GetTimeSeries (df):

    # Untuk mencari banyak data
    month = 0
    timeStampCount = 0
    monthList = df["Month of absence"].values
    for monthData in monthList:
        if (month != monthData and monthData != 0):
            month = monthData
            timeStampCount += 1

    # Fill DataFrame Time Series
    inputData = {}
    inputData["Month"] = [0 for i in range(timeStampCount)]
    inputData["Count"] = [0 for i in range(timeStampCount)]
    year = 2007
    month = 0
    timeStampCount = 0
    count = 1
    for monthData in monthList:
        if (month != 0):
            if (month != monthData):
                inputData["Month"][timeStampCount] = str(GetMonthLabel(month)) + " " + str(year)
                inputData["Count"][timeStampCount] = count
                
                month = monthData
                if (month == 1):
                    year += 1

                count = 1
                
                timeStampCount += 1
            else:
                count += 1
        else:
            month = monthData
    
    returnData = pd.DataFrame(data = inputData["Count"], index = inputData["Month"])
    return returnData

def GetMonthLabel (n):
    if (n == 1):
        return "January"
    elif (n == 2):
        return "February"
    elif (n == 3):
        return "March"
    elif (n == 4):
        return "April"
    elif (n == 5):
        return "May"
    elif (n == 6):
        return "June"
    elif (n == 7):
        return "July"
    elif (n == 8):
        return "August"
    elif (n == 9):
        return "September"
    elif (n == 10):
        return "October"
    elif (n == 11):
        return "November"
    elif (n == 12):
        return "December"

#
def GetFixedData(df):
    idCount = len(df["ID"].value_counts())
    inputData = {}
    for column in df.columns.values:
        inputData[column] = [0 for i in range(idCount)]

    for column in df.columns.values:
        for i in range(idCount):
            inputData[column][i] = df.loc[df["ID"] == (i + 1)][column].values[0]

    returnData = pd.DataFrame(data = inputData)
    return returnData

# Agar pandas mencetak seluruh kolom dan baris yang diminta
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# Untuk dapat me-run kode ini, masukkan 'pip install xlrd'
# pada command prompt/terminal
# Memasukkan data file excel pada DataFrame
df = pd.read_excel("Absenteeism_at_work.xls",
                   sheet_name = "Absenteeism_at_work")

# N = Nominal, O = Ordinal, B = Binary, D = Discrete, C = Continuous
dataType = ["D", "N", "N", "N", "N", "D", "D",
            "D", "D", "C", "C", "B", "N", "D",
            "B", "B", "D", "D", "D", "D", "C"]

# Menuliskan jumlah kolom dan baris
print("Jumlah kolom pada data:", len(df.columns))
print("Jumlah baris pada data:", len(df))
print("")

# Mengambil sampel data (baris pertama)
print("----------DATA 5 BARIS PERTAMA----------")
print(df.loc[0:5])
print("")

# Mengambil sampel data (data maksimum minimum)
banyakPegawai = len(df["ID"].value_counts())
print("----------DATA 5 PEGAWAI PALING SERING ABSEN----------")
print(df["ID"].value_counts()[0:5])
print("----------DATA 5 PEGAWAI PALING JARANG ABSEN----------")
print(df["ID"].value_counts()[banyakPegawai - 5:banyakPegawai].sort_values())
print("")

# Makna tiap atribut
# ID                                 Kuantitatif-Diskrit
# Reason for absence                 Kategorikal-Nominal
# Month of absence                   Kategorikal-Nominal
# Day of the week                    Kategorikal-Nominal
# Seasons                            Kategorikal-Nominal
# Transportation expense             Kuantitatif-Diskrit
# Distance from Residence to Work    Kuantitatif-Diskrit
# Service time                       Kuantitatif-Diskrit
# Age                                Kuantitatif-Diskrit
# Work load Average/day              Kuantitatif-Kontinu
# Hit target                         Kuantitatif-Kontinu
# Disciplinary failure               Kategorikal-Biner   X
# Education                          Kategorikal-Nominal
# Son                                Kuantitatif-Diskrit X
# Social drinker                     Kategorikal-Biner   X
# Social smoker                      Kategorikal-Biner   X
# Pet                                Kuantitatif-Diskrit X
# Weight                             Kuantitatif-Diskrit
# Height                             Kuantitatif-Diskrit
# Body mass index                    Kuantitatif-Diskrit
# Absenteeism time in hours          Kuantitatif-Kontinu

# Kemungkinan nilai data kategorikal
print("----------NILAI-NILAI ALASAN----------")
print(df["Reason for absence"].value_counts().sort_index())
print("")
# Ini kopas referensi dari website

print("----------NILAI-NILAI BULAN----------")
print(df["Month of absence"].value_counts().sort_index())
print("")

print("----------NILAI-NILAI HARI----------")
print(df["Day of the week"].value_counts().sort_index())
print("")
# 2 = Senin, 3 = Selasa, 4 = Rabu, 5 = Kamis, 6 = Jumat

print("----------NILAI-NILAI MUSIM----------")
print(df["Seasons"].value_counts().sort_index())
print("")
# 1 = Musim Panas, 2 = Musim Gugur, 3 = Musim Dingin, 4 = Musim Semi

print("----------NILAI-NILAI PENDIDIKAN----------")
print(df["Education"].value_counts().sort_index())
print("")
# 1 = SMA, 2 = Sarjana, 3 = Magister, 4 = Doktor

# Range nilai kuantitatif
print("----------RANGE-RANGE ATRIBUT KUANTITATIF----------")
for i in range(len(df.columns)):
    if (dataType[i] == "D" or dataType[i] == "C"):
        columnName = df.columns.values[i]
        print(str(columnName) + ":", df[columnName].values[df.idxmin()[columnName]],
              "-", df[columnName].values[df.idxmax()[columnName]])
print("")

# Pencarian data kosong
print("----------PERSENTASE DATA KOSONG---------")
for column in df.columns.values:
    if (column != "Disciplinary failure" and column != "Son" and
        column != "Social drinker" and column != "Social smoker" and column != "Pet"):
        print("Atribut", column, "memiliki", str(len(df.loc[df[column] == 0]) / len(df) * 100) + "% nilai kosong")
print("")

