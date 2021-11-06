import pandas as pd
df = pd.read_excel('naturescapedatabase.ods')
df['type'].replace({'Trees':'Tree', 'Shrubs and Bushes':'Shrub','Perennials':'Understorey', 'Ferns':'Understorey', 'Ground Cover':'Understorey'}, inplace=True)
df['foliageType'].replace({'E':'Evergreen','D':'Deciduous'}, inplace=True)
# print (df)

def createSppPara(filtered_df):
    final_paragraph = ''
    for _, row in filtered_df.iterrows():
        final_paragraph += "Common name: {}\nScientific name: {}\nTree, Shrub, Understorey: {}\nMaximum height: {} metre/s\nDeciduous or Evergreen: {}\nNotes: {}\n\n".\
            format(row["nameCommon"], row["nameScientific"], row["type"], row["maxheightM"], row["foliageType"], row["notes"])
    return (final_paragraph)

userChoice1 = input ('Choose 1 for Sun, 2 for Partial Sun, 3 for Shade')
userChoice2 = input ('Choose 1 for Dry, 2 for Moist, 3 for Wet')
if userChoice1 == "1":
    dfSun = df[df["checkSun"] == True]
    if userChoice2 == "1":
        dfSunDry = dfSun[dfSun["checkDry"] == True]
        print(createSppPara(dfSunDry))
    elif userChoice2 == "2":
        dfSunMoist = dfSun[dfSun["checkMoist"] == True]
        print(createSppPara(dfSunMoist))
    elif userChoice2 == "3":
        dfSunWet = dfSun[dfSun["checkWet"] == True]
        print(createSppPara(dfSunWet))
    else:
        print ('please enter 1, 2 or 3')

if userChoice1 == "2":
    dfPartialSun = df[df["checkPartialSun"] == True]
    if userChoice2 == "1":
        dfPartialSunDry = dfPartialSun[dfPartialSun["checkDry"] == True]
        print(createSppPara(dfPartialSunDry))
    elif userChoice2 == "2":
        dfPartialSunMoist = dfPartialSun[dfPartialSun["checkMoist"] == True]
        print(createSppPara(dfPartialSunMoist))
    elif userChoice2 == "3":
        dfPartialSunWet = dfPartialSun[dfPartialSun["checkWet"] == True]
        print(createSppPara(dfPartialSunWet))
    else:
        print ('please enter 1, 2 or 3')

if userChoice1 == "3":
    dfShade = df[df["checkShade"] == True]
    if userChoice2 == "1":
        dfShadeDry = dfShade[dfShade["checkDry"] == True]
        print(createSppPara(dfShadeDry))
    elif userChoice2 == "2":
        dfShadeMoist = dfShade[dfShade["checkMoist"] == True]
        print(createSppPara(dfShadeMoist))
    elif userChoice2 == "3":
        dfShadeWet = dfShade[dfShade["checkWet"] == True]
        print(createSppPara(dfShadeWet))
    else:
        print ('please enter 1, 2 or 3')

    


