# <h1 align = "center"> **Global Internet Usage - Streamlit Dashboard** </h1>

# <h2 align = "left"> **Project Description** </h2>
The following dashboard will visually present an overview of data collected on global internet usage from 1980 to 2020 and how internet accesibility has increased over the years. This dashboard was developed using streamlit. Streamlit is an open-source python-based library framework to build and share machine learning and data science web apps.
The following dashboard analyzes a dataset that contains information about internet users from 1980 - 2020 by Year and Country. The following columns make up our dataframe:
- Entity (Country)
- Year
- Cellular Subscription  - Mobile phone subscriptions per 100 people. This number can get over 100 when the average person has more than one subscription to a mobile service.
- No. of Internet Users - Number of people using the Internet in every country.
- Broadband Subscription - The number of fixed broadband subscriptions per 100 people.   
- Increase In Users - Total increase in users from one year to the next.
- Percentage Increase - Total increase in users from one year to the next represented in percentage.

# <h2 align = "left"> **Dashboard Layout** </h2>
The dashboard layout consists of to main parts: 
- Sidebar - Contains interactive widgets to control the behavior or parameters of the dashboard.
- Main Window - Main window where the data tables and visualizations are displayed based on the user's inputs from the sidebar.

# <h2 align = "left"> **Sidebar Widgets** </h2>
The sidebar contains the following widgets:
- A dropdown menu to select the Data Analysis Mode. The following options: "Single Country" or "Compare Countries".
- Drop down menus to select one country or multiple countries depending on the data analysis mode previously selected.
- Sliders to select a specific range of years to be displayed in the main window.

# <h2 align = "left"> **Main Window** </h2>
The main window contains the following visualizations:
- One or more data tables from the country/countries selected from the sidebar.
- Two line charts that represent the total internet users and the total percentage increase in internet users by year.
- Two scatter plots tht show the relationship between internet users and cellular subscriptions/broadband subscriptions.







# <h2 align = "left"> **Link to Streamlit Dashboard App** </h2>
https://avt1993-globalinternetusersdash-internet-usage-dashboard-4rpows.streamlit.app



