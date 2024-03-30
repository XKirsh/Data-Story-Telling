import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (replace with your actual file path)
file_path = 'micro_world.csv'
df = pd.read_csv(file_path, encoding='latin1')

# Title and header
st.title("Financial Inclusion Insights")
st.header("Exploring Micro World Data")

# Age distribution
st.subheader("Distribution of Respondent Ages")
fig = plt.figure(figsize=(12, 6))
sns.histplot(data=df, x='age', bins=20, kde=True)
plt.title('Distribution of Respondent Ages')
plt.xlabel('Age')
plt.ylabel('Count')
st.pyplot(fig)

# Insight: Analyze the age distribution to identify potential age groups that might require more targeted financial inclusion efforts. Are there any younger or older demographics that seem underrepresented?

# Gender distribution
st.subheader("Gender Distribution of Respondents")
fig = plt.figure(figsize=(6, 6))
df['female'].value_counts().plot.pie(autopct='%1.1f%%', labels=['Male', 'Female'])
plt.title('Gender Distribution of Respondents')
plt.ylabel('')
st.pyplot(fig)

# Insight: Understanding the gender distribution helps inform gender-specific financial inclusion strategies. Does the data suggest a need for initiatives focused on including women in financial services?

# Education level
st.subheader("Education Level of Respondents")
fig = plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='educ')
plt.title('Education Level of Respondents')
plt.xlabel('Education Level')
plt.ylabel('Count')
st.pyplot(fig)

# Insight: The education level distribution can help tailor financial literacy programs. Does the data indicate a need for programs with varying levels of complexity to cater to different educational backgrounds? 

# Household income quintile distribution
st.subheader("Household Income Quintile Distribution")
fig = plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='inc_q')
plt.title('Household Income Quintile Distribution')
plt.xlabel('Income Quintile')
plt.ylabel('Count')
st.pyplot(fig)

# Insight: Analyzing income distribution highlights economic disparities and guides inclusive financial product designs. Does the data reveal a significant low-income population that could benefit from specifically designed financial products?

# Reasons for no mobile money account
st.subheader("Reasons for No Mobile Money Account")
reason_columns = ['fin13_1a', 'fin13_1b', 'fin13_1c', 'fin13_1d']
reason_labels = ['Too Far', 'Too Expensive', 'Lack Documentation', 'Other']
reason_counts = [df[reason_col].sum() for reason_col in reason_columns]

fig = plt.figure(figsize=(10, 6))
sns.barplot(x=reason_labels, y=reason_counts)
plt.title('Reasons for No Mobile Money Account')
plt.xlabel('Reason')
plt.ylabel('Count')
st.pyplot(fig)

# Insight: Understanding the barriers to mobile money adoption helps improve accessibility and address concerns. Does a particular reason stand out, suggesting a need for targeted solutions (e.g., increasing agent presence, lowering fees, simplifying documentation)?
