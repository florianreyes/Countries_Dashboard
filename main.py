import streamlit as st
import requests
import json
import pandas as pd
import numpy as np

def get_country_info(name):
    url = "https://restcountries.com/v3.1/name/{}".format(name)
    response = requests.get(url)
    return response.json()

def get_all_countries():
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)
    countries = [country['name']['common'].lower() for country in response.json()]
    return countries

def display_country():
    st.title("Country Dashboard")
    st.markdown("---")
    country = st.selectbox("Choose a country", sorted(get_all_countries()))
    info = get_country_info(country)
    name = info[0]['name']['common']
    capital = info[0]['capital'][0]
    region = info[0]['region']
    languages = info[0]['languages']
    population = info[0]['population']
    area = round(info[0]['area'])
    borders = info[0]['borders']
    maps = info[0]['maps']['googleMaps']
    flag = info[0]['flag']
    lat = info[0]['latlng'][0]
    lng = info[0]['latlng'][1]

    #### SECTION 1
    st.markdown(" # {} {}".format(flag,name))
    st.markdown("---")

    col1,col2,col3,col4 = st.columns(4)
    col1.metric("Region", region)
    col2.metric("Area (KM2)", area)
    col3.metric("Population", population)
    col4.metric("Capital", capital)
    st.markdown(" #### {}".format(capital))

    ## Location of the country in map
    df = pd.DataFrame.from_dict({"latitude":[lat],"longitude":[lng]})
    st.map(df,zoom = 5)



    

def display_general_info():
    st.title("General Dashboard")
    st.write("This is the general dashboard")

def main():
    st.set_page_config(page_title="Dashboard", page_icon=":earth_americas:", layout="wide", initial_sidebar_state="expanded")
    with open('style.css') as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

    with st.sidebar:
        option = st.selectbox("Choose your dashboard",["Country", "General"])

    if option == "Country":
        display_country()
    if option == "General":
        display_general_info()

if __name__ == "__main__":
    main()




   

