df_81_01 = df[(df['tyear']>=1981) & (df['tyear']<=2001)]
df_81_01[['tyear','Agriculture','Industry','Forestry']]

year = df_81_01['tyear']

ag = df_81_01['Agriculture']/1000000
agric = ag.round(1)

ind = df_81_01['Industry']/1000000
industry = ind.round(1)

fo =  df_81_01['Forestry']/1000000
forestry = fo.round(1)
