#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import lxml.html as lh
import pandas as pd
from bs4 import BeautifulSoup
import time
import datetime as dt
from datetime import date
from datetime import datetime


# In[2]:


todays_date=date.today()
Yeart=todays_date.year
time_str =( f"{Yeart}-08-15")

time_str 
todays_date


# In[3]:


DateT=datetime.strptime(time_str, '%Y-%m-%d').date()


# In[4]:


if todays_date > DateT:
    Yeart=Yeart+1 
    
else:
    Yeart=Yeart


z= Yeart-1995
z


# In[5]:


x=1995

Lig_list=[]
x=1995

Lig_list=[]

for r in range(z):
    lalurl = f"https://www.transfermarkt.com/laliga/einnahmenausgaben/wettbewerb/ES1/plus/0?ids=a&sa=&    saison_id={x}&saison_id_bis={x}&nat=&pos=&altersklasse=&w_s=&leihe=&intern=0"
    page=requests.get(lalurl,headers={'User-Agent': 'Custom'})
    t=pd.read_html(page.content)
    t[3]["Year"]=f'{x+1}-12-31'
    Lig_list.append(t[3])
    x=x+1
    time.sleep(2)

laltr=pd.concat(Lig_list)
    


# In[6]:


x=1995

EPL_list=[]


for r in range(z):
    eplurl = f"https://www.transfermarkt.com/premier-league/einnahmenausgaben/wettbewerb/GB1/plus/0?ids=a&sa=&    saison_id={x}&saison_id_bis={x}&nat=&pos=&altersklasse=&w_s=&leihe=&intern=0"
    page=requests.get(eplurl,headers={'User-Agent': 'Custom'})
    t=pd.read_html(page.content)
    t[3]["Year"]=f'{x+1}-12-31'
    EPL_list.append(t[3])
    x=x+1
    time.sleep(2)

EPLtr=pd.concat(EPL_list)


# In[7]:


x=1995

SER_list=[]


for r in range(z):
    serurl = f"https://www.transfermarkt.com/serie-a/einnahmenausgaben/wettbewerb/IT1/plus/0?ids=a&sa=&    saison_id={x}&saison_id_bis={x}&nat=&pos=&altersklasse=&w_s=&leihe=&intern=0"
    page=requests.get(serurl,headers={'User-Agent': 'Custom'})
    t=pd.read_html(page.content)
    t[3]["Year"]=f'{x+1}-12-31'
    SER_list.append(t[3])
    x=x+1
    time.sleep(2)

SERtr=pd.concat(SER_list)


# In[8]:


x=1995

BUN_list=[]


for r in range(z):
    bunurl = f"https://www.transfermarkt.com/bundesliga/einnahmenausgaben/wettbewerb/L1/plus/0?ids=a&sa=&    saison_id={x}&saison_id_bis={x}&nat=&pos=&altersklasse=&w_s=&leihe=&intern=0"
    page=requests.get(bunurl,headers={'User-Agent': 'Custom'})
    t=pd.read_html(page.content)
    t[3]["Year"]=f'{x+1}-12-31'
    BUN_list.append(t[3])
    x=x+1
    time.sleep(2)

BUNtr=pd.concat(BUN_list)


# In[9]:


x=1995

FRA_list=[]


for r in range(z):
    fraurl = f"https://www.transfermarkt.com/ligue-1/einnahmenausgaben/wettbewerb/FR1/plus/0?ids=a&sa=&    saison_id={x}&saison_id_bis={x}&nat=&pos=&altersklasse=&w_s=&leihe=&intern=0"
    page=requests.get(fraurl,headers={'User-Agent': 'Custom'})
    t=pd.read_html(page.content)
    t[3]["Year"]=f'{x+1}-12-31'
    FRA_list.append(t[3])
    x=x+1
    time.sleep(2)

FRAtr=pd.concat(FRA_list)


# In[10]:


x=1995

ERE_list=[]


for r in range(z):
    ereurl = f"https://www.transfermarkt.com/eredivisie/einnahmenausgaben/wettbewerb/NL1/plus/0?ids=a&sa=&    saison_id={x}&saison_id_bis={x}&nat=&pos=&altersklasse=&w_s=&leihe=&intern=0"
    page=requests.get(ereurl,headers={'User-Agent': 'Custom'})
    t=pd.read_html(page.content)
    t[3]["Year"]=f'{x+1}-12-31'
    ERE_list.append(t[3])
    x=x+1
    time.sleep(2)

EREtr=pd.concat(ERE_list)


# In[11]:


x=1995

POR_list=[]


for r in range(z):
    porurl = f"http://www.transfermarkt.com/liga-nos/einnahmenausgaben/wettbewerb/PO1/plus/0?ids=a&sa=&    saison_id={x}&saison_id_bis={x}&nat=&pos=&altersklasse=&w_s=&leihe=&intern=0"
    page=requests.get(porurl,headers={'User-Agent': 'Custom'})
    t=pd.read_html(page.content)
    t[3]["Year"]=f'{x+1}-12-31'
    POR_list.append(t[3])
    x=x+1
    time.sleep(2)

PORtr=pd.concat(POR_list)


# In[12]:


x=1995

Seg_list=[]


for r in range(z):
    segurl = f"https://www.transfermarkt.com/laliga2/einnahmenausgaben/wettbewerb/ES2/plus/0?    ids=a&sa=&saison_id={x}&saison_id_bis={x}&nat=&pos=&altersklasse=&w_s=&leihe=&intern=0"
    page=requests.get(segurl,headers={'User-Agent': 'Custom'})
    t=pd.read_html(page.content)
    t[3]["Year"]=f'{x+1}-12-31'
    Seg_list.append(t[3])
    x=x+1
    time.sleep(2)

Segtr=pd.concat(Seg_list)


# In[13]:


x=1995

chmp_list=[]


for r in range(z):
    chmpurl = f"https://www.transfermarkt.com/championship/einnahmenausgaben/wettbewerb/GB2/plus/0?ids=a&sa=&    saison_id={x}&saison_id_bis={x}&nat=&pos=&altersklasse=&w_s=&leihe=&intern=0"
    page=requests.get(chmpurl,headers={'User-Agent': 'Custom'})
    t=pd.read_html(page.content)
    t[3]["Year"]=f'{x+1}-12-31'
    chmp_list.append(t[3])
    x=x+1
    time.sleep(2)

chmptr=pd.concat(chmp_list)




# In[14]:


braurl = f"https://www.transfermarkt.com/campeonato-brasileiro-serie-a/einnahmenausgaben/wettbewerb/BRA1/plus/0?ids=a&sa=&    saison_id={1995}&saison_id_bis={1995}&nat=&pos=&altersklasse=&w_s=&leihe=&intern=0"
page=requests.get(braurl,headers={'User-Agent': 'Custom'})
t=pd.read_html(page.content)
t


# In[15]:


tralist=[laltr, EPLtr, EREtr, FRAtr,BUNtr,SERtr, PORtr, chmptr,Segtr]


# In[16]:


transfers_df= pd.concat(tralist)
transfers_df


# In[17]:


transfer_df=transfers_df[["club.1","club.2","Arrivals", "Year"]]


# In[18]:


transfer_df.head()


# In[19]:


transfer_df.columns=["Club", "Spending", "Revenue", "Year"]


# In[20]:


transfer_df.head()


# In[21]:


Snew = transfer_df["Spending"].str.split("€", n = 1, expand = True)
Sfin=Snew[1].str.split("m", n = 1, expand = True)
transfer_df["Spend"]=Sfin[0]


# In[22]:


Rnew = transfer_df["Revenue"].str.split("€", n = 1, expand = True)
Rfin=Rnew[1].str.split("m", n = 1, expand = True)
transfer_df["Rev"]=Rfin[0]


# In[23]:


transfer_df.dtypes


# In[24]:


transfer_df["Spend"].fillna(0, inplace=True)


# In[25]:



transfer_df=transfer_df.replace({
"UD Salamanca (liq.)":"UD Salamanca",
"CP Mérida (diss.)":"CP Mérida",
"CF Extremadura (diss.)":"CF Extremadura",
"CD Logroñés (liq.)":"CD Logroñés",
"Granada 74 CF (liq.)":"Granada CF",
"Club Atlético Marbella (liq.)":"Atlético Marbella",
"Sestao Sport Club (liq.)":"Sestao SC",
"Real Madrid Castilla":"Real Madrid B",
      
"AC Parma":"Parma AC",
"Milan AC":"AC Milan",
"Juventus FC":"Juventus",
"Torino Calcio":"Torino FC",
"AC Fiorentina":"ACF Fiorentina",
"Parma FC":"Parma AC",
"Parma Calcio 1913":"Parma AC",
"Florentia Viola":"ACF Fiorentina",
"SPAL":"SPAL 2013 Ferrara",
"UC Sampdoria":"Sampdoria",
"FC Internazionale":"Inter",
"Inter Milan":"Inter",
"Robur Siena":"AC Siena",
"FC Messina Peloro":"FC Messina",
"FC Girondins Bordeaux":"Girondins Bordeaux",
"RC Strasbourg Alsace":"RC Strasbourg",
"AS Nancy-Lorraine":"FC Nancy",
"ES Troyes AC":"Troyes AF",
"FC Sochaux-Montbéliard":"FC Sochaux",
"CS Sedan-Ardennes":"CS Sedan",
"Le Mans Union Club 72":"Le Mans UC 72",
"Le Mans FC":"Le Mans UC 72",
"SCO Angers":"Angers SCO",
"Stade Brest 29":"Stade Brest",
"FC Istres Ouest Provence":"FC Istres",
"Bayer 04 Leverkusen":"Bayer Leverkusen",
"Twente Enschede FC":"FC Twente",
"Vitesse Arnhem":"Vitesse",
"De Graafschap Doetinchem":"De Graafschap",
"Go Ahead Eagles Deventer":"Go Ahead Eagles",
"Cambuur-Leeuwarden bvo":"SC Cambuur",
"SC Cambuur-Leeuwarden":"SC Cambuur",
"Willem II Tilburg":"Willem II",
"SBV Excelsior Rotterdam":"SBV Excelsior","UD Salamanca (liq.)":"UD Salamanca" ,
"UE Lleida (liq.)":"UE Lleida" ,
"CD Badajoz 1905":"CD Badajoz" ,
"Club Polideportivo Ejido (liq.)":"Polideportivo Ejido" ,
  
     "CF Extremadura (diss.)":"CF Extremadura" ,
  
     "Ciudad Murcia (liq.)":"Ciudad de Murcia" ,
  
     "CD Logroñés (liq.)":"CD Logroñés" ,
  
     "Real Jaén CF":"Real Jaén" ,
  
     "Real Madrid Castilla":"Real Madrid B" ,
  
     "CF Reus Deportiu (liq.)":"CF Reus Deportiu" ,
  
     "Terrassa FC":"Terrassa CF" ,
  
     "CP Mérida (diss.)":"CP Mérida" ,
  
     "CD Ourense (liq.)":"CD Ourense" ,
  
     "Lorca Deportiva CF (liq.)":"Lorca Deportiva" ,
  
     "Alicante CF (liq.)":"Alicante CF" ,
  
     "UD Vecindario (liq.)":"UD Vecindario" ,
  
     "Real Unión Club":"Real Unión" ,
  
     "Universidad de Las Palmas (liq.)":"Universidad Las Palmas" ,
  
     "Cultural Leonesa":"CD Leonesa" ,
  
     "CF Rayo Majadahonda":"Rayo Majadahonda" ,
  
     "Granada 74 CF (liq.)":"Granada CF" ,
  
     "Sestao Sport Club (liq.)":"Sestao SC" ,
  
     "Club Atlético Marbella (liq.)":"Atlético Marbella" ,
"Atlético de Madrid": "Atlético Madrid"})


# In[26]:


transfer_df["Rev"].fillna(0, inplace=True)


# In[27]:


transfer_df


# In[28]:


th1=transfer_df["Spend"].str.split("Th.", n = 1, expand = True)


# In[29]:


th2=transfer_df["Rev"].str.split("Th.", n = 1, expand = True)


# In[30]:


transfer_df["Spend"]=th1[0]
transfer_df["Spend(m/Thousand)"]=th1[1]
transfer_df["Rev"]=th2[0]
transfer_df["Rev(m/Thousand)"]=th2[1]


# In[31]:


transfer_df["Spend"]=transfer_df["Spend"].astype(str).astype(float)

transfer_df["Rev"]=transfer_df["Rev"].astype(str).astype(float)


# In[32]:


transfer_df["Spend(m/Thousand)"].fillna(0, inplace=True)


# In[33]:


transfer_df["Rev(m/Thousand)"].fillna(0, inplace=True)


# In[34]:


import numpy as np


# In[35]:



transfer_df['Spend_raw']= np.where(transfer_df["Spend(m/Thousand)"]==0, transfer_df["Spend"]*1000000, 
                                   transfer_df["Spend"]*1000)

transfer_df['Rev_raw']= np.where(transfer_df["Rev(m/Thousand)"]==0, transfer_df["Rev"]*1000000, 
                                   transfer_df["Rev"]*1000)



# In[36]:


transfer_df["Rev_raw"].fillna(0, inplace=True)


# In[37]:


transfer_df["Club"]=transfer_df["Club"].astype("string")
transfer_df.dtypes


# In[63]:



transfer_df=transfer_df.replace({
"UD Salamanca (liq.)":"UD Salamanca",
"CP Mérida (diss.)":"CP Mérida",
"CF Extremadura (diss.)":"CF Extremadura",
"CD Logroñés (liq.)":"CD Logroñés",
"AC Parma":"Parma AC",
"Milan AC":"AC Milan",
"Juventus FC":"Juventus",
"Torino Calcio":"Torino FC",
"AC Fiorentina":"ACF Fiorentina",
"Parma FC":"Parma AC",
"Parma Calcio 1913":"Parma AC",
"Florentia Viola":"ACF Fiorentina",
"SPAL":"SPAL 2013 Ferrara",
"UC Sampdoria":"Sampdoria",
"FC Internazionale":"Inter",
"Inter Milan":"Inter",
"Robur Siena":"AC Siena",
"FC Messina Peloro":"FC Messina",
"FC Girondins Bordeaux":"Girondins Bordeaux",
"RC Strasbourg Alsace":"RC Strasbourg",
"AS Nancy-Lorraine":"FC Nancy",
"ES Troyes AC":"Troyes AF",
"FC Sochaux-Montbéliard":"FC Sochaux",
"CS Sedan-Ardennes":"CS Sedan",
"Le Mans Union Club 72":"Le Mans UC 72",
"Le Mans FC":"Le Mans UC 72",
"SCO Angers":"Angers SCO",
"Stade Brest 29":"Stade Brest",
"FC Istres Ouest Provence":"FC Istres",
"Bayer 04 Leverkusen":"Bayer Leverkusen",
"Twente Enschede FC":"FC Twente",
"Vitesse Arnhem":"Vitesse",
"De Graafschap Doetinchem":"De Graafschap",
"Go Ahead Eagles Deventer":"Go Ahead Eagles",
"Cambuur-Leeuwarden bvo":"SC Cambuur",
"SC Cambuur-Leeuwarden":"SC Cambuur",
"Willem II Tilburg":"Willem II",
"SBV Excelsior Rotterdam":"SBV Excelsior",
"Vicenza Calcio":"Lanerossi Vicenza",
"Piacenza FC":"Piacenza Calcio",
"Delfino Pescara 1936":"Pescara Calcio","Atlético de Madrid": "Atlético Madrid"})


# In[64]:


transfer_df.loc[transfer_df["Club"]=="Lanerossi Vicenza"]


# In[65]:



transfer_df.columns=["Club","Year","Transfer_Spend","Transfer_Revenue"]

transfer_df=transfer_df.drop_duplicates()


# In[66]:


transfer_df.to_csv('transfers.csv', index=False)
transfer_df.head(20)


# In[42]:


from sqlalchemy import create_engine
connection_string = "postgres:123@localhost:5432/Soccer-Story"
engine = create_engine(f'postgresql://{connection_string}')


# In[43]:


engine.table_names()


# In[44]:


transfer_df.to_sql(name = "transfer", con=engine, if_exists = 'replace', index = True)


# In[67]:


transfer_df.to_excel('transfers.xlsx', index=False)
transfer_df.to_csv('transfer.csv',index=False)


# In[46]:


x=2005

BRA_list=[]


for r in range(16):
    braurl = f"https://www.transfermarkt.com/campeonato-brasileiro-serie-a/einnahmenausgaben/wettbewerb/BRA1/plus/0?ids=a&sa=&    saison_id={x}&saison_id_bis={x}&nat=&pos=&altersklasse=&w_s=&leihe=&intern=0"
    page=requests.get(braurl,headers={'User-Agent': 'Custom'})
    t=pd.read_html(page.content)
    t[3]["Year"]=f'{x}-12-31'
    BRA_list.append(t[3])
    x=x+1
    t
BRAtr=pd.concat(BRA_list)


# In[47]:


BRAtr.tail()


# In[ ]:




