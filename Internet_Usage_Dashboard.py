import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title = "Internet Usage Dashboard",
                   page_icon = ":bar_chart:",
                   layout = "wide"
)   

@st.cache_data
def get_data_from_csv():
    giu_df = pd.read_csv('https://raw.githubusercontent.com/avt1993/GlobalInternetUsersDashBoard/main/Global%20Internet%20Users.csv')
    return giu_df

giu_df = get_data_from_csv()

unique_countries = giu_df["Entity"].unique()
pre_defined_option1 = "United States"
pre_defined_option2 = "Mexico"

# SIDEBAR

st.sidebar.header("Data Analysis Mode")
mode_selected = st.sidebar.selectbox(
    "Select Mode:",
    options = {"Single Country", "Compare Countries"}
)


if (mode_selected == "Single Country"):

    st.sidebar.header("Single Country Selection")

    country = st.sidebar.selectbox(
    "Select Country:", [pre_defined_option1] + list(unique_countries)
    )

    country_selected = giu_df.query(
        "Entity == @country"
    )

    country_selected['Increase In Users'] = country_selected['No. of Internet Users'].diff()
    country_selected['Percentage Increase'] = ((country_selected['Increase In Users'] / country_selected['No. of Internet Users'].shift()) * 100).round()
    country_selected = country_selected.drop(["Code", "Unnamed: 0"], axis = 1)
    country_selected.reset_index()

    st.title(f" {country}" + " Dataset")
    st.dataframe(country_selected, height = 400, width = 1600) 

    st.title(":bar_chart: " +  f" {country}" + " Line Charts")
    
    # TOTAL INTERNET USERS

    fig1, ax1 = plt.subplots()

    ax1.plot(country_selected['Year'], country_selected['No. of Internet Users'])
    fig1.tight_layout()
    ax1.fill_between(country_selected['Year'], country_selected['No. of Internet Users'], color='lightblue', alpha=0.5)
    plt.title('Total Internet Users from 1980 - 2020')
    plt.xlabel('Year')
    plt.ylabel('Total Users')
    plt.grid(True)

    # PERCENTAGE INCREASE IN INTERNET USERS FROM YEAR TO YEAR

    fig2, ax2 = plt.subplots()

    ax2.plot(country_selected['Year'], country_selected['Percentage Increase'])
    fig2.tight_layout()
    ax2.fill_between(country_selected['Year'], country_selected['Percentage Increase'], color='lightblue', alpha=0.5)
    plt.title('% Increase in Internet Users')
    plt.xlabel('Year')
    plt.ylabel('Percentage Increase')
    plt.grid(True)

    left_column, right_column = st.columns(2)
    left_column.pyplot(fig1, use_container_width = True)
    right_column.pyplot(fig2, use_container_width = True)


else:
    st.sidebar.header("Country Selection")

    country1 = st.sidebar.selectbox(
    "Select First Country:", [pre_defined_option1] + list(unique_countries)
    )
    country1_selected = giu_df.query(
    "Entity == @country1"
    )

    country2 = st.sidebar.selectbox(
    "Select Second Country:", [pre_defined_option2] + list(unique_countries)
    )
    country2_selected = giu_df.query(
    "Entity == @country2"
    )

    country1_selected['Increase In Users'] = country1_selected['No. of Internet Users'].diff()
    country1_selected['Percentage Increase'] = ((country1_selected['Increase In Users'] / country1_selected['No. of Internet Users'].shift()) * 100).round()
    country1_selected = country1_selected.drop(["Code", "Unnamed: 0"], axis = 1)

    country2_selected['Increase In Users'] = country2_selected['No. of Internet Users'].diff()
    country2_selected['Percentage Increase'] = ((country2_selected['Increase In Users'] / country2_selected['No. of Internet Users'].shift()) * 100).round()
    country2_selected = country2_selected.drop(["Code", "Unnamed: 0"], axis = 1)    

    st.title(f" {country1}" + " Dataset")
    st.dataframe(country1_selected, height = 400, width = 1600) 

    st.title(f" {country2}" + " Dataset")
    st.dataframe(country2_selected, height = 400, width = 1600) 


    st.title(":bar_chart:" + f" {country1}" + " VS " + f" {country2}" + " Comparison")

    fig1, ax1 = plt.subplots()
    ax1.plot(country1_selected['Year'], country1_selected['No. of Internet Users'], label = f" {country1}")
    ax1.plot(country2_selected['Year'], country2_selected['No. of Internet Users'], label = f" {country2}")
    plt.title("Total Internet Users from 1980 - 2020")
    plt.xlabel('Year')
    plt.ylabel('Internet Users')
    plt.grid(True)
    plt.legend()

    fig2, ax2 = plt.subplots()
    ax2.plot(country1_selected['Year'], country1_selected['Percentage Increase'], label = f" {country1}")
    ax2.plot(country2_selected['Year'], country2_selected['Percentage Increase'], label = f" {country2}")
    plt.title("Percentage (%) Change in Internet Usage")
    plt.xlabel('Year')
    plt.ylabel("% Increase in Internet Users")
    plt.grid(True)
    plt.legend()

    left_column, right_column = st.columns(2)
    left_column.pyplot(fig1, use_container_width = True)
    right_column.pyplot(fig2, use_container_width = True)