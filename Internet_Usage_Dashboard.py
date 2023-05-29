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


# SIDEBAR
st.sidebar.header("Single Country")
country = st.sidebar.selectbox(
    "Select Country:",
    options = giu_df["Entity"].unique()
)

country_selected = giu_df.query(
    "Entity == @country"

)
country_selected['Increase In Users'] = country_selected['No. of Internet Users'].diff()
country_selected['Percentage Increase'] = ((country_selected['Increase In Users'] / country_selected['No. of Internet Users'].shift()) * 100).round()
country_selected = country_selected.drop(["Code", "Unnamed: 0"], axis = 1)
country_selected.reset_index()


st.title(":bar_chart: Single Country Dataframe")
st.dataframe(country_selected) 






st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.header("Comparison Between Countries")
country1 = st.sidebar.selectbox(
    "Select First Country:",
    options = giu_df["Entity"].unique()
)
country2 = st.sidebar.selectbox(
    "Select Second Country:",
    options = giu_df["Entity"].unique()
)

country1_selected = giu_df.query(
    "Entity == @country1"
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










# MAINPAGE
st.title(":bar_chart: Single Country Line Charts")
st.markdown("##")


# TOTAL INTERNET USERS CHART

fig, ax = plt.subplots()

ax.plot(country_selected['Year'], country_selected['No. of Internet Users'])
ax.fill_between(country_selected['Year'], country_selected['No. of Internet Users'], color='lightblue', alpha=0.5)
plt.title('Total Internet Users from 1980 - 2020')
plt.xlabel('Year')
plt.ylabel('Total Internet Users')
plt.grid(True)

#st.pyplot(fig)

# PERCENTAGE INCREASE IN INTERNET USERS FROM YEAR TO YEAR

fig1, ax1 = plt.subplots()

ax1.plot(country_selected['Year'], country_selected['Percentage Increase'])
ax1.fill_between(country_selected['Year'], country_selected['Percentage Increase'], color='lightblue', alpha=0.5)
plt.title('% Increase in Internet Users')
plt.xlabel('Year')
plt.ylabel('Percentage Increase')
plt.grid(True)

#st.pyplot(fig1)

left_column, right_column = st.columns(2)
left_column.pyplot(fig, use_container_width = True)
right_column.pyplot(fig1, use_container_width = True)



st.title(":bar_chart: Line Charts Between Countries")
st.markdown("##")

fig2, ax2 = plt.subplots()
ax2.plot(country1_selected['Year'], country1_selected['No. of Internet Users'], label = country1_selected["Entity"].unique())

ax2.plot(country2_selected['Year'], country2_selected['No. of Internet Users'], label = country2_selected["Entity"].unique())

plt.title("Total Internet Users from 1980 - 2020")
plt.xlabel('Year')
plt.ylabel('Total Internet Users')
plt.grid(True)
plt.legend()



fig3, ax3 = plt.subplots()
ax3.plot(country1_selected['Year'], country1_selected['Percentage Increase'], label = country1_selected["Entity"].unique())

ax3.plot(country2_selected['Year'], country2_selected['Percentage Increase'], label = country2_selected["Entity"].unique())

plt.title("Comparison Between Both Countries")
plt.xlabel('Year')
plt.ylabel("% Increase in Internet Users")
plt.grid(True)
plt.legend()



left_column, right_column = st.columns(2)
left_column.pyplot(fig2, use_container_width = True)
right_column.pyplot(fig3, use_container_width = True)