import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'micro_world.csv'
df = pd.read_csv(file_path, encoding='latin1')

st.title("Financial Inclusion Insights")
st.header("Exploring Micro World Data")

st.subheader("Distribution of Respondent Ages")
st.write("Question: How is the distribution of respondent ages in the dataset?")
fig = plt.figure(figsize=(12, 6))
sns.histplot(data=df, x='age', bins=20, kde=True)
plt.title('Distribution of Respondent Ages')
plt.xlabel('Age')
plt.ylabel('Count')
st.pyplot(fig)
st.write("Insight: Understanding the age distribution can help identify age groups that may need more financial inclusion efforts.")

st.subheader("Gender Distribution of Respondents")
st.write("Question: What is the proportion of females in the dataset?")
fig = plt.figure(figsize=(6, 6))
df['female'].value_counts().plot.pie(autopct='%1.1f%%', labels=['Male', 'Female'])
plt.title('Gender Distribution of Respondents')
plt.ylabel('')
st.pyplot(fig)
st.write("Insight: Knowing the gender distribution can inform gender-specific financial inclusion strategies.")

st.subheader("Education Level of Respondents")
st.write("Question: How does education level vary among respondents?")
fig = plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='educ')
plt.title('Education Level of Respondents')
plt.xlabel('Education Level')
plt.ylabel('Count')
st.pyplot(fig)
st.write("Insight: Understanding education levels can help tailor financial literacy programs.")

st.subheader("Household Income Quintile Distribution")
st.write("Question: What is the distribution of household income quintiles?")
fig = plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='inc_q')
plt.title('Household Income Quintile Distribution')
plt.xlabel('Income Quintile')
plt.ylabel('Count')
st.pyplot(fig)
st.write("Insight: Knowing the income distribution can highlight economic disparities and guide inclusive financial product designs.")

st.subheader("Reasons for No Mobile Money Account")
st.write("Question: How does the usage of mobile money accounts vary across different reasons for not having one?")
reason_columns = ['fin13_1a', 'fin13_1b', 'fin13_1c', 'fin13_1d']
reason_labels = ['Too Far', 'Too Expensive', 'Lack Documentation', 'Other']
reason_counts = [df[reason_col].sum() for reason_col in reason_columns]

fig = plt.figure(figsize=(10, 6))
sns.barplot(x=reason_labels, y=reason_counts)
plt.title('Reasons for No Mobile Money Account')
plt.xlabel('Reason')
plt.ylabel('Count')
st.pyplot(fig)
st.write("Insight: Understanding the barriers to mobile money adoption can help improve accessibility and address concerns.")
