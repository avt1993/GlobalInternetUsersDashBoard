import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def plot_line_graph (country_selected, y_label_string, title_string, column_to_plot):
    fig, ax = plt.subplots()
    ax.plot(country_selected['Year'], country_selected[column_to_plot])
    fig.tight_layout()
    ax.fill_between(country_selected['Year'], country_selected[column_to_plot], color = 'lightblue', alpha = 0.5)
    plt.title(title_string)
    plt.xlabel('Year')
    plt.ylabel(y_label_string)
    plt.grid(True)

    return fig


def plot_multi_line_graph (country1_selected, country2_selected, y_label_string, title_string, column_to_plot):
    fig, ax = plt.subplots()
    ax.plot(country1_selected['Year'], country1_selected[column_to_plot], label = f" {country1}")
    ax.plot(country2_selected['Year'], country2_selected[column_to_plot], label = f" {country2}")
    plt.title(title_string)
    plt.xlabel('Year')
    plt.ylabel(y_label_string)
    plt.grid(True)
    plt.legend()

    return fig



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

    start_range = st.sidebar.slider('Start Range', min_value = giu_df['Year'].min(), max_value = giu_df['Year'].max(), value = giu_df['Year'].min())
    end_range = st.sidebar.slider('End Range', min_value = giu_df['Year'].min(), max_value = giu_df['Year'].max(), value = giu_df['Year'].max())

    country_selected = country_selected[(country_selected['Year'] >= start_range) & (country_selected['Year'] <= end_range)]

    country_selected['Increase In Users'] = country_selected['No. of Internet Users'].diff()
    country_selected['Percentage Increase'] = ((country_selected['Increase In Users'] / country_selected['No. of Internet Users'].shift()) * 100).round()
    country_selected = country_selected.drop(["Code", "Unnamed: 0"], axis = 1)
    country_selected.reset_index()


    st.title("Dataset - " + f" {country}")
    st.dataframe(country_selected, height = 300, width = 1600) 



    st.title(":bar_chart: " +  f" {country}" + " Line Charts")

    # TOTAL INTERNET USERS
    fig1 = plot_line_graph(country_selected, 'Total Users', 'Total Internet Users from 1980 - 2020', 'No. of Internet Users')

    # PERCENTAGE INCREASE IN INTERNET USERS FROM YEAR TO YEAR
    fig2 = plot_line_graph(country_selected, 'Percentage (%) Increase', 'Increase (%) in Internet Users', 'Percentage Increase')

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

    min_year = giu_df['Year'].min()
    min_year = int(min_year)
    max_year = giu_df['Year'].max()
    max_year = int(max_year)

    start_range = st.sidebar.slider('Start Range', min_value = min_year, max_value = max_year, value = min_year)
    end_range = st.sidebar.slider('End Range', min_value = min_year, max_value = max_year, value = max_year)

    country1_selected = country1_selected[(country1_selected['Year'] >= start_range) & (country1_selected['Year'] <= end_range)]
    country2_selected = country2_selected[(country2_selected['Year'] >= start_range) & (country2_selected['Year'] <= end_range)]

    country1_selected['Increase In Users'] = country1_selected['No. of Internet Users'].diff()
    country1_selected['Percentage Increase'] = ((country1_selected['Increase In Users'] / country1_selected['No. of Internet Users'].shift()) * 100).round()
    country1_selected = country1_selected.drop(["Code", "Unnamed: 0"], axis = 1)

    country2_selected['Increase In Users'] = country2_selected['No. of Internet Users'].diff()
    country2_selected['Percentage Increase'] = ((country2_selected['Increase In Users'] / country2_selected['No. of Internet Users'].shift()) * 100).round()
    country2_selected = country2_selected.drop(["Code", "Unnamed: 0"], axis = 1)    

    st.title("Dataset - " + f" {country1}")
    st.dataframe(country1_selected, height = 300, width = 1600) 

    st.title("Dataset - " + f" {country2}")
    st.dataframe(country2_selected, height = 300, width = 1600) 



    st.title(":bar_chart:" + f" {country1}" + " VS " + f" {country2}" + " Comparison")

    fig1 = plot_multi_line_graph(country1_selected, country2_selected, 'Internet Users', "Total Internet Users from 1980 - 2020", 'No. of Internet Users')
    fig2 = plot_multi_line_graph(country1_selected, country2_selected, "% Increase in Internet Users", "Percentage (%) Change in Internet Usage", 'Percentage Increase')

    left_column, right_column = st.columns(2)
    left_column.pyplot(fig1, use_container_width = True)
    right_column.pyplot(fig2, use_container_width = True)