import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

uploaded_file = st.file_uploader("micro_world.csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, encoding='latin1')

    # Question: How is the distribution of respondent ages in the dataset?
    st.write("## Distribution of Respondent Ages")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.histplot(data=df, x='age', bins=20, kde=True, ax=ax)
    plt.title('Distribution of Respondent Ages')
    plt.xlabel('Age')
    plt.ylabel('Count')
    st.pyplot(fig)

    # Insight: Understanding the age distribution can help identify age groups that may need more financial inclusion efforts.
    # For instance, if a significant portion of the population falls in younger age groups, targeted financial literacy programs could be beneficial.

    # Question: What is the proportion of females in the dataset?
    st.write("## Gender Distribution of Respondents")
    fig, ax = plt.subplots(figsize=(6, 6))
    df['female'].value_counts().plot.pie(autopct='%1.1f%%', labels=['Male', 'Female'], ax=ax)
    plt.title('Gender Distribution of Respondents')
    plt.ylabel('')
    st.pyplot(fig)

    # Insight: Knowing the gender distribution can inform gender-specific financial inclusion strategies.
    # Tailoring financial products and services to address the specific needs and preferences of women can be crucial for achieving financial inclusion.

    # Question: How does education level vary among respondents?
    st.write("## Education Level of Respondents")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(data=df, x='educ', ax=ax)
    plt.title('Education Level of Respondents')
    plt.xlabel('Education Level')
    plt.ylabel('Count')
    st.pyplot(fig)

    # Insight: Understanding education levels can help tailor financial literacy programs.
    # Individuals with lower education levels might benefit from more basic financial literacy programs, while those with higher education could be targeted with more complex financial products and services.

    # Question: What is the distribution of household income quintiles?
    st.write("## Household Income Quintile Distribution")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(data=df, x='inc_q', ax=ax)
    plt.title('Household Income Quintile Distribution')
    plt.xlabel('Income Quintile')
    plt.ylabel('Count')
    st.pyplot(fig)

    # Insight: Knowing the income distribution can highlight economic disparities and guide inclusive financial product designs.
    # Financial institutions can develop products and services that cater to the needs of low-income populations, promoting financial inclusion for all.

    # Question: How does the usage of mobile money accounts vary across different reasons for not having one?
    reason_columns = ['fin13_1a', 'fin13_1b', 'fin13_1c', 'fin13_1d']
    reason_labels = ['Too Far', 'Too Expensive', 'Lack Documentation', 'Other']
    reason_counts = [df[reason_col].sum() for reason_col in reason_columns]

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=reason_labels, y=reason_counts, ax=ax)
    plt.title('Reasons for No Mobile Money Account')
    plt.xlabel('Reason')
    plt.ylabel('Count')
    st.pyplot(fig)

    # Insight: Understanding the barriers to mobile money adoption can help improve accessibility and address concerns.
    # By addressing issues like distance to service points, affordability, and documentation requirements, financial institutions can increase mobile money adoption and promote financial inclusion.