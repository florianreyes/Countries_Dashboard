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
    info = get_country_info(country)[0]
    name = info['name']['common']
    capital = info.get('capital','No capital')[0]
    region = info.get('region')
    languages = info.get('languages')
    population = info.get('population')
    area = round(info.get('area'))
    borders = info.get('borders', 'No borders')
    maps = info.get('maps''googleMaps')
    currency = info.get('currencies')
    capital_info = info.get('capitalInfo')
    flag = info.get('flag')
    lat = info.get('latlng')[0]
    lng = info.get('latlng')[1]

    #### SECTION 1
    st.markdown(" # {} {}".format(flag,name))
    st.markdown("---")

    col1,col2,col3 = st.columns(3)
    col1.metric("Capital", capital)
    col2.metric("Area (KM2)", area)
    col3.metric("Population", population)

    ## Location of the country in map
    df = pd.DataFrame.from_dict({"latitude":[lat],"longitude":[lng]})
    st.map(df,zoom = 4)

    ####SECTION 2
    st.markdown("---")
    symbol = currency[list(currency.keys())[0]]['symbol']
    currency = str(list(currency.keys())[0])
    col4,col5,col6 = st.columns(3)
    col4.metric("Region", region)
    col5.metric("Language",languages[list(languages.keys())[0]])
    col6.metric("Currency","{}  {}".format(symbol,currency))
    st.markdown("---")
    st.subheader("Currency {}".format(currency))
    st.subheader("Borders {}".format(borders))
    st.subheader("Capital Information {}".format(capital_info))



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




   

