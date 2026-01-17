import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

#Data Load
RAJASTHAN=pd.read_csv("D:/labour_project/rajasthan_new.csv",encoding="cp1252")
#Title
st.set_page_config(page_title="Industrial Workforce Dashboard", layout="wide")
st.title("Industrial Human Resource Geo-Visualization")
oly_total=RAJASTHAN[RAJASTHAN['NIC Name']=='Total']
gy=pd.RangeIndex(start=0,stop=len(oly_total),step=1)
oly_total.set_index(gy,inplace=True) 

MainWorkers_Total_Persons=oly_total.iloc[1:34,7].sum()
MainWorkers_Total_Males=oly_total.iloc[1:34,8].sum()
MainWorkers_Total_Females=oly_total.iloc[1:34,9].sum()
Main_Workers_Rural_Persons=oly_total.iloc[1:34,10].sum()
Main_Workers_Rural_Males=oly_total.iloc[1:34,11].sum()
Main_Workers_Rural_Female=oly_total.iloc[1:34,12].sum()
Main_Workers_Urban_Persons=oly_total.iloc[1:34,13].sum()
Main_Workers_Urban_Males=oly_total.iloc[1:34,14].sum()
Main_Workers_Urban_Females=oly_total.iloc[1:34,15].sum()
Marginal_Workers_Total_Persons=oly_total.iloc[1:34,16].sum()
Marginal_Workers_Total_Males=oly_total.iloc[1:34,17].sum()
Marginal_Workers_Total_Females=oly_total.iloc[1:34,18].sum()
Marginal_Workers_Rural_Persons=oly_total.iloc[1:34,19].sum()
Marginal_Workers_Rural_Males=oly_total.iloc[1:34,20].sum()
Marginal_Workers_Rural_Females=oly_total.iloc[1:34,21].sum()
Marginal_Workers_Urban_Persons=oly_total.iloc[1:34,22].sum()
Marginal_Workers_Urban_Males=oly_total.iloc[1:34,23].sum()
Marginal_Workers_Urban_Females=oly_total.iloc[1:34,24].sum()

contain1=st.container()
col1, col2 = contain1.columns(2, border=True)
with col1:
    st.write("STATE - RAJASTHAN")
with col2:
    st.write("STATE CODE : 8")
def calculate_disCode(state):
    counts=state['District Code'].unique()
    return counts
dst_count=calculate_disCode(RAJASTHAN)
contain2=st.container(border=True)
col1, col2 = contain2.columns(2, border=True)
with col1:
    st.write("Total No of District",len(dst_count))
with col2:
    st.write()
st.write(RAJASTHAN)
#margin workers
st.subheader('Marginal workers total : 2307752')
contain4=st.container()
col1, col2, col3 = contain4.columns(3, border=True)
with col1:
    total_df1 = pd.DataFrame({
        "diff1": ["Main Workers", "Margin Workers"],
        "Workers_filed1": [MainWorkers_Total_Persons, Marginal_Workers_Total_Persons]
        })
    fig_gender = px.bar(
        total_df1,
        x="diff1",
        y="Workers_filed1",
        title="Workforce Distribution"
    )
    st.plotly_chart(fig_gender, use_container_width=True)
with col2:
    st.write('MainWorkers_Total_Persons:',Marginal_Workers_Total_Persons)
    gender_df1 = pd.DataFrame({
        "Gender1": ["Male", "Female"],
        "Workers1": [MainWorkers_Total_Males, MainWorkers_Total_Females]
        })
    fig_gender = px.bar(
        gender_df1,
        x="Gender1",
        y="Workers1",
        title="Gender-wise Workforce Distribution"
    )
    st.plotly_chart(fig_gender, use_container_width=True)
with col3:
    st.write('Marginal_Workers_Rural_Persons',Marginal_Workers_Rural_Persons)
    st.write('Marginal_Workers_Urban_Persons',Marginal_Workers_Urban_Persons)
    work_df2 = pd.DataFrame({
        "Area1": ["Rural", "Urban"],
        "Values1": [Marginal_Workers_Rural_Persons, Marginal_Workers_Urban_Persons]
        })
    fig_area = px.pie(
    work_df2,
    names="Area1",
    values="Values1",
    title="Rural vs Urban Workforce"
    )

    st.plotly_chart(fig_area)
st.subheader('Main workers total : 9017944')
contain3=st.container()
col1, col2, col3 = contain3.columns(3, border=True)
with col1:
    total_df = pd.DataFrame({
        "diff": ["Main Workers", "Margin Workers"],
        "Workers_filed": [MainWorkers_Total_Persons, Marginal_Workers_Total_Persons]
        })
    fig_gender = px.bar(
        total_df,
        x="diff",
        y="Workers_filed",
        title="Workforce Distribution"
    )
    st.plotly_chart(fig_gender, use_container_width=True)
with col2:
    st.write('MainWorkers_Total_Persons:',MainWorkers_Total_Persons)
    gender_df = pd.DataFrame({
        "Gender": ["Male", "Female"],
        "Workers": [Marginal_Workers_Total_Males, Marginal_Workers_Total_Females]
        })
    fig_gender = px.bar(
        gender_df,
        x="Gender",
        y="Workers",
        title="Gender-wise Workforce Distribution"
    )
    st.plotly_chart(fig_gender, use_container_width=True)
with col3:
    st.write('Main_Workers_Rural_Persons',Main_Workers_Rural_Persons)
    st.write('Main_Workers_Urban_Persons',Main_Workers_Urban_Persons)
    work_df1 = pd.DataFrame({
        "Area": ["Rural", "Urban"],
        "values": [Main_Workers_Rural_Persons, Main_Workers_Urban_Persons]
        })
    fig_area = px.pie(
    work_df1,
    names="Area",
    values="values",
    title="Rural vs Urban Workforce"
    )

    st.plotly_chart(fig_area)



sunburst_df = RAJASTHAN[
    (RAJASTHAN["Division"] != 0) &
    (RAJASTHAN["Group"] != 0) &
    (RAJASTHAN["Class"] != 0)]
fig_treemap = px.treemap(
    sunburst_df,
    path=["Division", "Group", "Class"],
    values="Main Workers - Total -  Persons",
    title="Workforce Distribution by Industry"
)

st.plotly_chart(fig_treemap, use_container_width=True)

def loopers(dtsa):
    for tr in dtsa:
        dtsa['total_workers']=dtsa.iloc[1:len(oly_total)+1,7]+dtsa.iloc[1:len(oly_total)+1,16]
loopers(oly_total)
new_oly=oly_total.iloc[1:len(oly_total)+1,:]

coords = pd.read_csv("D:/labour_project/rajasthan_district_lat_lon.csv")
lat=list(coords['lat'])
log=list(coords['lon'])
new_oly['latitude']=lat
new_oly['logitude']=log
#st.write(new_oly)
fig = px.scatter_map(new_oly, lat="latitude", 
                     lon="logitude",color="District Code",
                       size="total_workers",
                  color_continuous_scale=px.colors.cyclical.IceFire,
                    size_max=15, zoom=5, title="Rajasthan District-wise Total Workers Distribution")
fig.update_layout(mapbox_style="open-street-map")
st.plotly_chart(fig, use_container_width=True)