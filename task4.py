import seaborn as sns
df = sns.load_dataset("titanic")

#kadın ve erkek sayıları
df.groupby("sex").size()

#Her bir sutuna ait unique değerlerin sayısını bulunuz

import pandas as pd
count_of_unique = [len(df[col].unique()) for col in df.columns]

#pclass değişkeninin unique değerlerinin sayısını bulunuz.
countOf_pclass_unique = [len(df["pclass"].unique())]

#pclass ve parch değişkeninin değerlerinin sayısını bulunuz.
pclass_count = df['pclass'].nunique()
parch_count = df['parch'].nunique()

#embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz ve tekrar kontrol ediniz.
type(df["embarked"])
df["embarked"].astype("category")

#embarked değeri C olanların tüm bilgelerini gösteriniz
df[df["embarked"] == "C"]

#embarked değeri S olmayanların tüm bilgelerini gösteriniz.
df[df["embarked"] != "S"]

#Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz
result = df[(df['age'] < 30) & (df['sex'] == 'female')]

# Fare'i 500'den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz.
result = df[(df["fare"]>500) | (df["age"]>70)]

#Her bir değişkendeki boş değerlerin toplamını bulunuz.
df.columns.isna().sum()

#who değişkenini dataframe’den çıkarınız.
df.drop("who",axis=1)

#deck değikenindeki boş değerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz.
df["deck"].fillna(df["deck"].mode(), inplace=True)

#age değikenindeki boş değerleri age değişkenin medyanı ile doldurunuz.
df["age"].fillna(df["age"].median(),inplace=True)

#survived değişkeninin pclass ve cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz.
df.groupby(["pclass", "sex"])["survived"].agg(["sum","count","mean"])

#30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 vericek bir fonksiyon yazın. Yazdığınız fonksiyonu kullanarak titanik veri
#setinde age_flag adında bir değişken oluşturunuz oluşturunuz. (apply ve lambda yapılarını kullanınız).

#that's the standard function
def set_labels():
    arr_of_labels = []
    for col in df["age"]:
        if col < 30:
            arr_of_labels.append(1)
        else:
            arr_of_labels.append(0)

    df["age_flag"] = arr_of_labels
#this is the version of apply and lambda
df["age_flag"] = df["age"].apply(lambda x : 1 if x < 30 else 0)


#Tips dataseti yükleyin
df_tips = sns.load_dataset("tips")

#Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.
df_tips.groupby("time")["total_bill"].agg(["max","min","mean"])

#günlere ve time göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz
df_tips.groupby(["day","time"])["total_bill"].agg(["min","max","mean"])
#burada gelen NaN değerlere engel olmak için şu kod kullanılabilir
df_tips.groupby(["day","time"])["total_bill"].agg(["min","max","mean"]).fillna(0)
#böylece boş değerler yerine 0 vermiş olduk.

#Lunch zamanına ve kadın müşterilere ait total_bill ve tip değerlerinin day'e göre toplamını, min, max ve ortalamasını bulunuz.
group_women_lunch = df_tips[(df_tips["sex"] == "Female") & (df_tips["time"] == "Lunch")]
group_women_lunch.groupby("day")["total_bill","tip"].agg(["sum","min","max","mean"])

#size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir? (loc kullanınız).
(df_tips[(df_tips["size"]<3) & (df_tips["total_bill"]>10)]).mean()

#total_bill_tip_sum adında yeni bir değişken oluşturunuz. Her bir müşterinin ödediği totalbill ve tip in toplamını versin.
df_tips["total_bill_tip_sum"] = df_tips["total_bill"] + df_tips["tip"]
df_tips.groupby(df_tips.index)["total_bill_tip_sum"].sum()

#total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e atayınız.
sorted_df = df_tips.total_bill_tip_sum.sort_values(ascending = False)[:30]




