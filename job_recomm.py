import streamlit as st
import pickle
import pandas as pd

# Function to recommend jobs
def recommend(job_title):
    if job_title in data['jobtitle'].values:
        print('title')
        job_index = data[data['jobtitle'] == job_title].index[0]
        distances = similarity[job_index]
        job_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        recommended_jobs = []
        for i in job_list:
            recommended_jobs.append(data.iloc[i[0]][['company', 'employmenttype_jobstatus', 'joblocation_address', 'jobtitle', 'skills']])
        return recommended_jobs
    else:
        print('skills')
        job_index = data[data['skills'] == job_title].index[0]                                                            
        distances = similarity[job_index]
        job_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        recommended_jobs = []
        for i in job_list:
            recommended_jobs.append(data.iloc[i[0]][['company', 'employmenttype_jobstatus', 'joblocation_address', 'jobtitle', 'skills']])
        return recommended_jobs
# Load dataset and similarity matrix
Job_dict = pickle.load(open('/home/tushar/job/Job_recom.pkl', 'rb'))
data = pd.DataFrame(Job_dict)
similarity = pickle.load(open('/home/tushar/job/job_similiar.pkl', 'rb'))
# print(data.head(3))

# Page configuration
st.set_page_config(
    page_title="Job Recommendation System",
    page_icon="🔍",
    layout="wide"
)

# Page title and introduction
st.title("🔍 Job Recommendation System")
st.markdown("""
Welcome to the **Job Recommendation System**!  
Select a job title below to find the top 5 recommendations tailored to your choice.  
This system uses advanced machine learning techniques to bring you the most relevant job opportunities.
""")

# Sidebar for user interaction
# st.sidebar.header("Search Preferences")
# select_job_name = st.sidebar.selectbox(
#     "Select a Job Title",
#     data['jobtitle'].values,
#     help="Choose a job title to get similar recommendations."

# )

text_search = st.text_input("Search videos by title or speaker", value="")

if text_search:
    st.write(text_search)
    recommendations = recommend(text_search)

    for idx, rec in enumerate(recommendations):
        st.markdown(f"""
        #### {idx + 1}. {rec['jobtitle']}
        - **Company**: {rec['company']}
        - **Employment Type**: {rec['employmenttype_jobstatus']}
        - **Location**: {rec['joblocation_address']}
        - **Required Skills**: {rec['skills']}
        """)
        st.divider()


# if st.sidebar.button('Get Recommendations'):
#     st.markdown("### Recommended Jobs for:")
#     st.write(f"**{select_job_name}**")
#     recommendations = recommend(select_job_name)
    
#     # Display recommendations in a professional format
#     for idx, rec in enumerate(recommendations):
#         st.markdown(f"""
#         #### {idx + 1}. {rec['jobtitle']}
#         - **Company**: {rec['company']}
#         - **Employment Type**: {rec['employmenttype_jobstatus']}
#         - **Location**: {rec['joblocation_address']}
#         - **Required Skills**: {rec['skills']}
#         """)
#         st.divider()

# Footer
# st.markdown("---")
# st.markdown("💼 Powered by AI | Designed with ❤️ using Streamlit")

# # Styling
# st.markdown("""
#     <style>
#         .sidebar .sidebar-content {
#             background-color: #f8f9fa;
#             padding: 10px;
#         }
#         h1, h3, h4 {
#             color: #1f77b4;
#         }
#         .stMarkdown {
#             font-size: 16px;
#             font-family: Arial, sans-serif;
#         }
#     </style>
# """, unsafe_allow_html=True)