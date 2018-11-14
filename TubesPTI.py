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

'''

# --KAMUS--

# --ALGORITMA--

# BLOK INISIALISASI
# Import dependencies yang dibutuhkan
import pandas as pd
import matplotlib.pyplot as plt

# Fungsi mencari data Time Series jumlah orang abstein
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

# Agar pandas mencetak seluruh kolom dan baris yang diminta
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# Untuk dapat me-run kode ini, masukkan 'pip install xlrd'
# pada command prompt/terminal
# Memasukkan data file excel pada DataFrame
df = pd.read_excel("Absenteeism_at_work.xls",
                   sheet_name = "Absenteeism_at_work")

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
print("----------DATA 5 PEGAWAI PALING SERING ABSTEIN----------")
print(df["ID"].value_counts()[0:5])
print("----------DATA 5 PEGAWAI PALING JARANG ABSTEIN----------")
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
# Age                                Kuantitatif-Kontinu
# Work load Average/day              Kuantitatif-Kontinu
# Hit target                         Kuantitatif-Kontinu
# Disciplinary failure               Kategorikal-Biner   X
# Education                          Kategorikal-Nominal
# Son                                Kuantitatif-Diskrit X
# Social drinker                     Kategorikal-Biner   X
# Social smoker                      Kategorikal-Biner   X
# Pet                                Kuantitatif-Diskrit X
# Weight                             Kuantitatif-Kontinu
# Height                             Kuantitatif-Kontinu
# Body mass index                    Kuantitatif-Kontinu
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
print("ID:", df["ID"].values[df.idxmin()["ID"]],
      "-", df["ID"].values[df.idxmax()["ID"]])
print("Biaya Transport:", df["Transportation expense"].values[df.idxmin()["Transportation expense"]],
      "-", df["Transportation expense"].values[df.idxmax()["Transportation expense"]])
print("Jarak Tempat-tinggal:",
      df["Distance from Residence to Work"].values[df.idxmin()["Distance from Residence to Work"]],
      "-", df["Distance from Residence to Work"].values[df.idxmax()["Distance from Residence to Work"]])
print("Lama shift:", df["Service time"].values[df.idxmin()["Service time"]],
      "-", df["Service time"].values[df.idxmax()["Service time"]])
print("Umur:", df["Age"].values[df.idxmin()["Age"]],
      "-", df["Age"].values[df.idxmax()["Age"]])
print("Beban kerja:", df["Work load Average/day "].values[df.idxmin()["Work load Average/day "]],
      "-", df["Work load Average/day "].values[df.idxmax()["Work load Average/day "]])
print("Hit target:", df["Hit target"].values[df.idxmin()["Hit target"]],
      "-", df["Hit target"].values[df.idxmax()["Hit target"]])
print("Banyak anak:", df["Son"].values[df.idxmin()["Son"]],
      "-", df["Son"].values[df.idxmax()["Son"]])
print("Banyak peliharaan:", df["Pet"].values[df.idxmin()["Pet"]],
      "-", df["Pet"].values[df.idxmax()["Pet"]])
print("Berat badan:", df["Weight"].values[df.idxmin()["Weight"]],
      "-", df["Weight"].values[df.idxmax()["Weight"]])
print("Tinggi badan:", df["Height"].values[df.idxmin()["Height"]],
      "-", df["Height"].values[df.idxmax()["Height"]])
print("BMI:", df["Body mass index"].values[df.idxmin()["Body mass index"]],
      "-", df["Body mass index"].values[df.idxmax()["Body mass index"]])
print("Lama abstein:", df["Absenteeism time in hours"].values[df.idxmin()["Absenteeism time in hours"]],
      "-", df["Absenteeism time in hours"].values[df.idxmax()["Absenteeism time in hours"]])
print("")

# Pencarian data kosong
print("----------PERSENTASE DATA KOSONG---------")
for column in df.columns.values:
    if (column != "Disciplinary failure" and column != "Son" and
        column != "Social drinker" and column != "Social smoker" and column != "Pet"):
        print("Atribut", column, "memiliki", str(len(df.loc[df[column] == 0]) / len(df) * 100) + "% nilai kosong")
print("")

