import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
sheet = pd.read_csv("streamsheet.csv")
col1, col2 = st.beta_columns(2)
a = col1.number_input(label = "First Year",value = 1950,min_value = 1871,max_value = 2020)
b = col2.number_input(label = "Last Year",value = 1980,min_value = 1871,max_value = 2020)
sheet = sheet[sheet["Season"]>= a]
sheet = sheet[sheet["Season"]<= b]
teams = list(set(list(sheet["Team"])))
teamsheet = pd.DataFrame()
for i in teams:
    total = sheet[sheet["Team"]==i]["WAR"].sum()
    top10 = sheet[sheet["Team"]==i].sort_values(by = "WAR",ascending = False)[0:10]
    try:
        guy1 = top10.iloc[0]["Name"] + " (" + str(round(top10.iloc[0]["WAR"],1)) + ")"
    except:
        guy1 = ""
    try:
        guy2 = top10.iloc[1]["Name"] + " (" + str(round(top10.iloc[1]["WAR"],1)) + ")"
    except:
        guy2 = ""
    try:
        guy3 = top10.iloc[2]["Name"] + " (" + str(round(top10.iloc[2]["WAR"],1)) + ")"
    except:
        guy3 = ""
    try:
        guy4 = top10.iloc[3]["Name"] + " (" + str(round(top10.iloc[3]["WAR"],1)) + ")"
    except:
        guy4 = ""
    try:
        guy5 = top10.iloc[4]["Name"] + " (" + str(round(top10.iloc[4]["WAR"],1)) + ")"
    except:
        guy5 = ""
    teamsheet = teamsheet.append([[i,total,guy1,guy2,guy3,guy4,guy5]])
teamsheet.columns = ["Team","WAR","1st","2nd","3rd","4th","5th"]
teamsheet = teamsheet.sort_values(by = "WAR",ascending = False)
teamsheet = teamsheet.reset_index(drop = True)
st.dataframe(teamsheet.style.format({'WAR': '{:.1f}'}),height = 20000)