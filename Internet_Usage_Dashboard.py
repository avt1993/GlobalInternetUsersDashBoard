import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title = "Internet Usage Dashboard",
                   page_icon = ":bar_chart:",
                   layout = "wide"
)   

giu_df = pd.read_csv('/Users/antoniovillardaga/Documents/Python/GlobalInternetUsersDashBoard/Global Internet Users.csv')

# SIDEBAR
st.sidebar.header("Country")
country = st.sidebar.selectbox(
    "Select Country:",
    options = giu_df["Entity"].unique()
)

country_selected = giu_df.query(
    "Entity == @country"

)

#st.dataframe(country_selected.reset_index()) 


# MAINPAGE
st.title(":bar_chart: Internet Users")
st.markdown("##")


fig, ax = plt.subplots()

ax.plot(country_selected['Year'], country_selected['No. of Internet Users'])
plt.title('Total Internet Users from 1980 - 2020')
plt.xlabel('Year')
plt.ylabel('Total Internet Users')
plt.grid(True)

st.pyplot(fig)

