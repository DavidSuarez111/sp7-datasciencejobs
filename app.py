import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Data Science Salary Analysis")
#Run functions 
def data():
    """_summary_
    This function will generate the dataset to be used by graphing functions as long as the csv file has the name: data_science_salaries.csv
    and is in the root of the directory. 
    Returns:
        _type_: _description_
    """
    ds_market = pd.read_csv("data_science_salaries.csv")
    ds_full_time = ds_market[ds_market["employment_type"]=="Full-time"]
    return ds_full_time

def avg_salary_by_experience_bar_graph(df):
    """_summary_
    Generates a bar graph of average salary grouped by experience level.
    Parameters:
    df (pd.DataFrame): A DataFrame containing 'experience_level' and 'salary_in_usd' columns.

    Returns:
    fig (plotly.graph_objects.Figure): A Plotly bar chart figure
    """
    #Ensure columns exist
    if 'experience_level' not in df.columns or 'salary_in_usd' not in df.columns:
        raise ValueError("DataFrame must contain 'experience_level' and 'salary_in_usd' columns")
    # Group by experience level and compute the average salary
    avg_salary = df.groupby('experience_level', as_index=False)['salary_in_usd'].mean()
    
    # Create the bar chart
    
    fig = px.bar(avg_salary, x='experience_level', y='salary_in_usd', 
                 title="Average Salary by Experience Level",
                 labels={'salary_in_usd': 'Average Salary', 'experience_level': 'Experience Level'},
                 color='experience_level')

    return fig
#Function to make a scatterplot
def salary_by_work_model_histogram(df): 
    """_summary_
    Generates an histogram of salary by work models  
    Args:
        df (_type_): A df containing "work_models" and "salary_in_usd" as columns
    """
    if "work_models" not in df.columns or "salary_in_usd" not in df.columns: 
        raise ValueError("Dataframe must contain 'work_models' and 'salary_in_usd' columns.")
    hist = px.histogram(df, x="salary_in_usd", color="work_models", 
                   title="Salary Distribution by Work Model",
                   labels={"salary_in_usd": "Salary (USD)", "work_models": "Work Model"},
                   nbins=10, barmode="overlay")  # Overlayed histograms
    return hist
st.markdown("<br><br>", unsafe_allow_html=True)
st.header('Do you wonder about how the experience level of data workers impact its salary?')
st.markdown("<br>", unsafe_allow_html=True)
st.subheader("Press the button to find out!")
st.markdown("<br>", unsafe_allow_html=True)
hist_button = st.button("I Will make a bar graph button!") # Make a button.
st.markdown("<br>", unsafe_allow_html=True)        
if hist_button: #When pressing the button
    #Write the action being made and deploy the graph of according information. 
    st.write('Here is the Average Salary by Experience Level Bar Graph:')
            
    # crear un histograma
    fig = avg_salary_by_experience_bar_graph(data()) #use the function of data to return a df to be used on the function to make a bar graph. 
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
st.markdown("<br><br>", unsafe_allow_html=True)
st.header("Distribution of Salary by Employment Type")
st.markdown("<br>", unsafe_allow_html=True)           
st.subheader("Do you want to see how the employment type impacts on the salary made or how many workers are under each employment type?")
st.markdown("<br>", unsafe_allow_html=True)
st.subheader("Click on the checkmark to find out!")
st.markdown("<br>", unsafe_allow_html=True)

build_histogram = st.checkbox('I am the checkmark')
if build_histogram: #If the checkbox get clicked: 
    st.write('Now Showing: Salary histogram by work model.')
    hist =   salary_by_work_model_histogram(data())
    st.plotly_chart(hist, use_container_width=True)       

