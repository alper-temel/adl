import pandas as pd
import numpy as np
import streamlit as st

st.markdown("""
                <style>
                    .css-h5rgaw.egzxvld1
                {
                    visibility: hidden;
                }
                </style>
            """, 
            unsafe_allow_html = True)

st.markdown("# :violet[ADL DİLİM ÇALIŞMASI] 	:car: :hocho:")

kullanim_tarzi = st.file_uploader("Kullanım Tarzı Dosyasını Yükleyin ", type = ["xls", "xlsx", "csv"])
if kullanim_tarzi is not None:
     st.dataframe(pd.read_excel(kullanim_tarzi))
else:
    st.caption("Lütfen Excel Dosyasını Kontrol Edin")

input_text = st.text_input("Dönemi Yazınız: ")
st.write("Yazılacak Dönem, ", input_text)

uploaded_excel = st.file_uploader(label = "**Dilimlenecek Excel Dosyasını Seçin** :knife:", type = ["xls", "xlsx", "csv"])
if uploaded_excel is not None:
     st.dataframe(pd.read_excel(uploaded_excel, header = 1))
else:
    st.caption("Lütfen Excel Dosyasını Kontrol Edin")
    
@st.cache(suppress_st_warning=True)
def ADL():
    if uploaded_excel is not None:
         uploaded_excel.seek(0)
         data = pd.read_excel(uploaded_excel, header = 1)
    if kullanim_tarzi is not None:
         kullanim_tarzi.seek(0)
         kullanım_tarzı = pd.read_excel(kullanim_tarzi)
    
    markakodu = data["MarkaKodu"]
    markakodu = list(map(str, markakodu))
    
    tipkodu = data["TipKodu"]
    tipkodu = list(map(str, tipkodu))
    
    yeni_markakodu = []
    for i in markakodu:
        if len(i) == 1:
            i = "00" + i
        elif len(i) == 2:
            i = "0" + i
        else:
            i = i
        yeni_markakodu.append(i)
    
    yeni_tipkodu = []
    for i in tipkodu:
        if len(i) == 1:
            i = "000" + i
        elif len(i) == 2:
            i = "00" + i
        elif len(i) == 3:
            i = "0" + i
        else:
            i = i
        yeni_tipkodu.append(i)
        
    yeni_data = pd.DataFrame()
    yeni_data["marka_kodu"] = yeni_markakodu
    yeni_data["tip_kodu"] = tipkodu
    yeni_data["MarkaTip_kodu"] = yeni_data["marka_kodu"] + yeni_data["tip_kodu"]
    yeni_data["marka_adı"] = data["MarkaAdı"]
    yeni_data["tip_adı"] = data["TipAdı"]
    yeni_data = yeni_data.iloc[:, 2:]
    
    data_2023 = pd.concat([yeni_data,data[data.columns[4:][0]]], axis = 1)
    data_2022 = pd.concat([yeni_data,data[data.columns[4:][1]]], axis = 1)
    data_2021 = pd.concat([yeni_data,data[data.columns[4:][2]]], axis = 1)
    data_2020 = pd.concat([yeni_data,data[data.columns[4:][3]]], axis = 1)
    data_2019 = pd.concat([yeni_data,data[data.columns[4:][4]]], axis = 1)
    data_2018 = pd.concat([yeni_data,data[data.columns[4:][5]]], axis = 1)
    data_2017 = pd.concat([yeni_data,data[data.columns[4:][6]]], axis = 1)
    data_2016 = pd.concat([yeni_data,data[data.columns[4:][7]]], axis = 1)
    data_2015 = pd.concat([yeni_data,data[data.columns[4:][8]]], axis = 1)
    data_2014 = pd.concat([yeni_data,data[data.columns[4:][9]]], axis = 1)
    data_2013 = pd.concat([yeni_data,data[data.columns[4:][10]]], axis = 1)
    data_2012 = pd.concat([yeni_data,data[data.columns[4:][11]]], axis = 1)
    data_2011 = pd.concat([yeni_data,data[data.columns[4:][12]]], axis = 1)
    data_2010 = pd.concat([yeni_data,data[data.columns[4:][13]]], axis = 1)
    data_2009 = pd.concat([yeni_data,data[data.columns[4:][14]]], axis = 1)
    
    data_2023 = data_2023.loc[data_2023[data.columns[4:][0]] != 0]
    data_2022 = data_2022.loc[data_2022[data.columns[4:][1]] != 0]
    data_2021 = data_2021.loc[data_2021[data.columns[4:][2]] != 0]
    data_2020 = data_2020.loc[data_2020[data.columns[4:][3]] != 0]
    data_2019 = data_2019.loc[data_2019[data.columns[4:][4]] != 0]
    data_2018 = data_2018.loc[data_2018[data.columns[4:][5]] != 0]
    data_2017 = data_2017.loc[data_2017[data.columns[4:][6]] != 0]
    data_2016 = data_2016.loc[data_2016[data.columns[4:][7]] != 0]
    data_2015 = data_2015.loc[data_2015[data.columns[4:][8]] != 0]
    data_2014 = data_2014.loc[data_2014[data.columns[4:][9]] != 0]
    data_2013 = data_2013.loc[data_2013[data.columns[4:][10]] != 0]
    data_2012 = data_2012.loc[data_2012[data.columns[4:][11]] != 0]
    data_2011 = data_2011.loc[data_2011[data.columns[4:][12]] != 0]
    data_2010 = data_2010.loc[data_2010[data.columns[4:][13]] != 0]
    data_2009 = data_2009.loc[data_2009[data.columns[4:][14]] != 0]
    
    data_2023["ModelYıl"] = data.columns[4:][0]
    data_2022["ModelYıl"] = data.columns[4:][1]
    data_2021["ModelYıl"] = data.columns[4:][2]
    data_2020["ModelYıl"] = data.columns[4:][3]
    data_2019["ModelYıl"] = data.columns[4:][4]
    data_2018["ModelYıl"] = data.columns[4:][5]
    data_2017["ModelYıl"] = data.columns[4:][6]
    data_2016["ModelYıl"] = data.columns[4:][7]
    data_2015["ModelYıl"] = data.columns[4:][8]
    data_2014["ModelYıl"] = data.columns[4:][9]
    data_2013["ModelYıl"] = data.columns[4:][10]
    data_2012["ModelYıl"] = data.columns[4:][11]
    data_2011["ModelYıl"] = data.columns[4:][12]
    data_2010["ModelYıl"] = data.columns[4:][13]
    data_2009["ModelYıl"] = data.columns[4:][14]
    
    data_2023 = data_2023.rename(columns = {data.columns[4:][0]: 'Bedel'})
    data_2022 = data_2022.rename(columns = {data.columns[4:][1]: 'Bedel'})
    data_2021 = data_2021.rename(columns = {data.columns[4:][2]: 'Bedel'})
    data_2020 = data_2020.rename(columns = {data.columns[4:][3]: 'Bedel'})
    data_2019 = data_2019.rename(columns = {data.columns[4:][4]: 'Bedel'})
    data_2018 = data_2018.rename(columns = {data.columns[4:][5]: 'Bedel'})
    data_2017 = data_2017.rename(columns = {data.columns[4:][6]: 'Bedel'})
    data_2016 = data_2016.rename(columns = {data.columns[4:][7]: 'Bedel'})
    data_2015 = data_2015.rename(columns = {data.columns[4:][8]: 'Bedel'})
    data_2014 = data_2014.rename(columns = {data.columns[4:][9]: 'Bedel'})
    data_2013 = data_2013.rename(columns = {data.columns[4:][10]: 'Bedel'})
    data_2012 = data_2012.rename(columns = {data.columns[4:][11]: 'Bedel'})
    data_2011 = data_2011.rename(columns = {data.columns[4:][12]: 'Bedel'})
    data_2010 = data_2010.rename(columns = {data.columns[4:][13]: 'Bedel'})
    data_2009 = data_2009.rename(columns = {data.columns[4:][14]: 'Bedel'})
    
    data_final = pd.concat([data_2023, data_2022, data_2021, data_2020, data_2019, data_2018, data_2017, data_2016, 
                            data_2015, data_2014, data_2013, data_2012, data_2011, data_2010, data_2009], axis = 0)
    
    kullanım_tarzı = kullanım_tarzı.rename(columns = {'REF': 'MarkaTip_kodu'})
    kullanım_tarzı["Kullanım_Tarzı"] = kullanım_tarzı["KT"]
    kullanım_tarzı = kullanım_tarzı.iloc[:, 2:]
    
    markakodu_kt = kullanım_tarzı["marka_kodu"]
    markakodu_kt = list(map(str, markakodu_kt))
    
    tipkodu_kt = kullanım_tarzı["tip_kodu"]
    tipkodu_kt = list(map(str, tipkodu_kt))
    
    yeni_markakodu_kt = []
    for i in markakodu_kt:
        if len(i) == 1:
            i = "00" + i
        elif len(i) == 2:
            i = "0" + i
        else:
            i = i
        yeni_markakodu_kt.append(i)
    
    yeni_tipkodu_kt = []
    for i in tipkodu_kt:
        yeni_tipkodu_kt.append(i)
        
    kt_data = pd.DataFrame()
    kt_data["marka_kodu"] = yeni_markakodu_kt
    kt_data["tip_kodu"] = yeni_tipkodu_kt
    kt_data["MarkaTip_kodu"] = kt_data["marka_kodu"] + kt_data["tip_kodu"]
    kt_data["KT"] = kullanım_tarzı["Kullanım_Tarzı"]
    
    adl_ = pd.merge(data_final, kt_data, on = 'MarkaTip_kodu', how = 'left')
    alınacak_baslıklar = ['MarkaTip_kodu', 'tip_adı', 'ModelYıl', 'KT', 'Bedel']
    
    adl = pd.DataFrame()
    for i in alınacak_baslıklar:
        aa = adl_[i]
        adl = pd.concat([adl, aa], axis = 1)
        
    otomobil = adl.loc[adl["KT"] == "OTOMOBİL"]
    suv = adl.loc[adl["KT"] == "SUV"]
    kamyonet = adl.loc[adl["KT"] == "KAMYONET"]
    
    otomobil = otomobil.sort_values(by = ["Bedel"])
    
    otomobil_düşük_1 = otomobil.iloc[0:round(len(otomobil) * 0.01), :]
    otomobil_düşük_1["Dilim"] = "%1"
    otomobil_yüksek_1 = otomobil.iloc[round(len(otomobil)-len(otomobil)*0.01): , :]
    otomobil_yüksek_1["Dilim"] = "%99"
    
    otomobil_dilimler = otomobil.iloc[round(len(otomobil) * 0.01): , :]
    otomobil_dilimler = otomobil_dilimler.iloc[:round(len(otomobil_dilimler) - len(otomobil_yüksek_1)), :]
    
    otomobil_dilim_1 = otomobil_dilimler.iloc[0:round(len(otomobil_dilimler)/10), :]
    otomobil_dilim_1["Dilim"] = "Dilim_1"
    
    otomobil_dilim_2 = otomobil_dilimler.iloc[len(otomobil_dilim_1):len(otomobil_dilim_1) + round(len(otomobil_dilimler)/10), :]
    otomobil_dilim_2["Dilim"] = "Dilim_2"
    
    otomobil_dilim_3 = otomobil_dilimler.iloc[len(otomobil_dilim_1)*2:len(otomobil_dilim_1)*2 + round(len(otomobil_dilimler)/10), :]
    otomobil_dilim_3["Dilim"] = "Dilim_3"
    
    otomobil_dilim_4 = otomobil_dilimler.iloc[len(otomobil_dilim_1)*3:len(otomobil_dilim_1)*3 + round(len(otomobil_dilimler)/10), :]
    otomobil_dilim_4["Dilim"] = "Dilim_4"
    
    otomobil_dilim_5 = otomobil_dilimler.iloc[len(otomobil_dilim_1)*4:len(otomobil_dilim_1)*4 + round(len(otomobil_dilimler)/10), :]
    otomobil_dilim_5["Dilim"] = "Dilim_5"
    
    otomobil_dilim_6 = otomobil_dilimler.iloc[len(otomobil_dilim_1)*5:len(otomobil_dilim_1)*5 + round(len(otomobil_dilimler)/10), :]
    otomobil_dilim_6["Dilim"] = "Dilim_6"
    
    otomobil_dilim_7 = otomobil_dilimler.iloc[len(otomobil_dilim_1)*6:len(otomobil_dilim_1)*6 + round(len(otomobil_dilimler)/10), :]
    otomobil_dilim_7["Dilim"] = "Dilim_7"
    
    otomobil_dilim_8 = otomobil_dilimler.iloc[len(otomobil_dilim_1)*7:len(otomobil_dilim_1)*7 + round(len(otomobil_dilimler)/10), :]
    otomobil_dilim_8["Dilim"] = "Dilim_8"
    
    otomobil_dilim_9 = otomobil_dilimler.iloc[len(otomobil_dilim_1)*8:len(otomobil_dilim_1)*8 + round(len(otomobil_dilimler)/10), :]
    otomobil_dilim_9["Dilim"] = "Dilim_9"
    
    otomobil_dilim_10 = otomobil_dilimler.iloc[len(otomobil_dilim_1)*9:len(otomobil_dilim_1)*9 + round(len(otomobil_dilimler)/10), :]
    otomobil_dilim_10["Dilim"] = "Dilim_10"
    
    otomobil_adl = pd.concat([otomobil_düşük_1, otomobil_dilim_1, otomobil_dilim_2, otomobil_dilim_3, otomobil_dilim_4,
                              otomobil_dilim_5, otomobil_dilim_6, otomobil_dilim_7, otomobil_dilim_8, otomobil_dilim_9,
                              otomobil_dilim_10, otomobil_yüksek_1], axis = 0)
    
    suv = suv.sort_values(by = ["Bedel"])
    
    suv_düşük_1 = suv.iloc[0:round(len(suv) * 0.01), :]
    suv_düşük_1["Dilim"] = "%1"
    suv_yüksek_1 = suv.iloc[round(len(suv)-len(suv)*0.01): , :]
    suv_yüksek_1["Dilim"] = "%99"
    
    suv_dilimler = suv.iloc[round(len(suv) * 0.01): , :]
    suv_dilimler = suv_dilimler.iloc[:round(len(suv_dilimler) - len(suv_yüksek_1)), :]
    
    suv_dilim_1 = suv_dilimler.iloc[0:round(len(suv_dilimler)/10), :]
    suv_dilim_1["Dilim"] = "Dilim_1"
    
    suv_dilim_2 = suv_dilimler.iloc[len(suv_dilim_1):len(suv_dilim_1) + round(len(suv_dilimler)/10), :]
    suv_dilim_2["Dilim"] = "Dilim_2"
    
    suv_dilim_3 = suv_dilimler.iloc[len(suv_dilim_1)*2:len(suv_dilim_1)*2 + round(len(suv_dilimler)/10), :]
    suv_dilim_3["Dilim"] = "Dilim_3"
    
    suv_dilim_4 = suv_dilimler.iloc[len(suv_dilim_1)*3:len(suv_dilim_1)*3 + round(len(suv_dilimler)/10), :]
    suv_dilim_4["Dilim"] = "Dilim_4"
    
    suv_dilim_5 = suv_dilimler.iloc[len(suv_dilim_1)*4:len(suv_dilim_1)*4 + round(len(suv_dilimler)/10), :]
    suv_dilim_5["Dilim"] = "Dilim_5"
    
    suv_dilim_6 = suv_dilimler.iloc[len(suv_dilim_1)*5:len(suv_dilim_1)*5 + round(len(suv_dilimler)/10), :]
    suv_dilim_6["Dilim"] = "Dilim_6"
    
    suv_dilim_7 = suv_dilimler.iloc[len(suv_dilim_1)*6:len(suv_dilim_1)*6 + round(len(suv_dilimler)/10), :]
    suv_dilim_7["Dilim"] = "Dilim_7"
    
    suv_dilim_8 = suv_dilimler.iloc[len(suv_dilim_1)*7:len(suv_dilim_1)*7 + round(len(suv_dilimler)/10), :]
    suv_dilim_8["Dilim"] = "Dilim_8"
    
    suv_dilim_9 = suv_dilimler.iloc[len(suv_dilim_1)*8:len(suv_dilim_1)*8 + round(len(suv_dilimler)/10), :]
    suv_dilim_9["Dilim"] = "Dilim_9"
    
    suv_dilim_10 = suv_dilimler.iloc[len(suv_dilim_1)*9:len(suv_dilim_1)*9 + round(len(suv_dilimler)/10), :]
    suv_dilim_10["Dilim"] = "Dilim_10"
    
    suv_adl = pd.concat([suv_düşük_1, suv_dilim_1, suv_dilim_2, suv_dilim_3, suv_dilim_4, suv_dilim_5, suv_dilim_6,
                         suv_dilim_7, suv_dilim_8, suv_dilim_9, suv_dilim_10, suv_yüksek_1], axis = 0)
    
    kamyonet = kamyonet.sort_values(by = ["Bedel"])
    
    kamyonet_düşük_1 = kamyonet.iloc[0:round(len(kamyonet) * 0.01), :]
    kamyonet_düşük_1["Dilim"] = "%1"
    kamyonet_yüksek_1 = kamyonet.iloc[round(len(kamyonet)-len(kamyonet)*0.01): , :]
    kamyonet_yüksek_1["Dilim"] = "%99"
    
    kamyonet_dilimler = kamyonet.iloc[round(len(kamyonet) * 0.01): , :]
    kamyonet_dilimler = kamyonet_dilimler.iloc[:round(len(kamyonet_dilimler) - len(kamyonet_yüksek_1)), :]
    
    kamyonet_dilim_1 = kamyonet_dilimler.iloc[0:round(len(kamyonet_dilimler)/10), :]
    kamyonet_dilim_1["Dilim"] = "Dilim_1"
    
    kamyonet_dilim_2 = kamyonet_dilimler.iloc[len(kamyonet_dilim_1):len(kamyonet_dilim_1) + round(len(kamyonet_dilimler)/10), :]
    kamyonet_dilim_2["Dilim"] = "Dilim_2"
    
    kamyonet_dilim_3 = kamyonet_dilimler.iloc[len(kamyonet_dilim_1)*2:len(kamyonet_dilim_1)*2 + round(len(kamyonet_dilimler)/10), :]
    kamyonet_dilim_3["Dilim"] = "Dilim_3"
    
    kamyonet_dilim_4 = kamyonet_dilimler.iloc[len(kamyonet_dilim_1)*3:len(kamyonet_dilim_1)*3 + round(len(kamyonet_dilimler)/10), :]
    kamyonet_dilim_4["Dilim"] = "Dilim_4"
    
    kamyonet_dilim_5 = kamyonet_dilimler.iloc[len(kamyonet_dilim_1)*4:len(kamyonet_dilim_1)*4 + round(len(kamyonet_dilimler)/10), :]
    kamyonet_dilim_5["Dilim"] = "Dilim_5"
    
    kamyonet_dilim_6 = kamyonet_dilimler.iloc[len(kamyonet_dilim_1)*5:len(kamyonet_dilim_1)*5 + round(len(kamyonet_dilimler)/10), :]
    kamyonet_dilim_6["Dilim"] = "Dilim_6"
    
    kamyonet_dilim_7 = kamyonet_dilimler.iloc[len(kamyonet_dilim_1)*6:len(kamyonet_dilim_1)*6 + round(len(kamyonet_dilimler)/10), :]
    kamyonet_dilim_7["Dilim"] = "Dilim_7"
    
    kamyonet_dilim_8 = kamyonet_dilimler.iloc[len(kamyonet_dilim_1)*7:len(kamyonet_dilim_1)*7 + round(len(kamyonet_dilimler)/10), :]
    kamyonet_dilim_8["Dilim"] = "Dilim_8"
    
    kamyonet_dilim_9 = kamyonet_dilimler.iloc[len(kamyonet_dilim_1)*8:len(kamyonet_dilim_1)*8 + round(len(kamyonet_dilimler)/10), :]
    kamyonet_dilim_9["Dilim"] = "Dilim_9"
    
    kamyonet_dilim_10 = kamyonet_dilimler.iloc[len(kamyonet_dilim_1)*9:len(kamyonet_dilim_1)*9 + round(len(kamyonet_dilimler)/10), :]
    kamyonet_dilim_10["Dilim"] = "Dilim_10"
    
    kamyonet_adl = pd.concat([kamyonet_düşük_1, kamyonet_dilim_1, kamyonet_dilim_2, kamyonet_dilim_3, kamyonet_dilim_4,
                              kamyonet_dilim_5, kamyonet_dilim_6, kamyonet_dilim_7, kamyonet_dilim_8, kamyonet_dilim_9,
                              kamyonet_dilim_10, kamyonet_yüksek_1], axis = 0)
    
    adl_dilim = pd.concat([otomobil_adl, suv_adl, kamyonet_adl], axis = 0)
    adl_dilim["Dönem"] = input_text
  
    return st.dataframe(adl_dilim)

veri = st.button(label = "ADL Hazırla", on_click = ADL)
indir = st.download_button(label = "ADL İndir :rocket:", data = veri)
