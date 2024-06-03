# import clipboard 
import streamlit as st # type: ignore
from langchain.prompts import PromptTemplate # type: ignore
from langchain_openai import ChatOpenAI   # type: ignore
from dotenv import load_dotenv # type: ignore
load_dotenv()

#-------------------------------------------------------------------------------------------
# Define the types of emails a candidate might send
emails = """
**1. Application Email**:
- **Purpose**: To apply for a specific job opening.
- **Content**: Includes a cover letter, resume, and any additional required documents.
- **Example Subject**: Application for [Job Title] Position

**2. Follow-Up Email**:
- **Purpose**: To inquire about the status of an application or express continued interest.
- **Content**: Polite inquiry about application status, reiteration of interest, and availability for further discussions.
- **Example Subject**: Follow-Up on Job Application for [Job Title] Position

**3. Thank-You Email**:
- **Purpose**: To thank the interviewer(s) for the opportunity to interview.
- **Content**: Expresses gratitude, reiterates interest, and may include a brief mention of something discussed during the interview.
- **Example Subject**: Thank You for the Interview - [Job Title] Position

**4. Acceptance Email**:
- **Purpose**: To formally accept a job offer.
- **Content**: Expresses gratitude for the offer, confirms acceptance, and may include any requested information, such as start date availability.
- **Example Subject**: Acceptance of Job Offer for [Job Title] Position

**5. Withdrawal Email**:
- **Purpose**: To withdraw an application from consideration.
- **Content**: States the decision to withdraw, expresses appreciation for the opportunity, and may include a brief reason for withdrawal (optional).
- **Example Subject**: Withdrawal of Application for [Job Title] Position

**6. Update Email**:
- **Purpose**: To provide updated information or qualifications.
- **Content**: Clearly states the update (e.g., completed course, obtained certification) and expresses continued interest in the position.
- **Example Subject**: Updated Information for [Job Title] Application
"""
#---------------------------------------------------------------------------------------------------



# Function to get the response back
def getLLMResponse(form_input, email_sender, email_recipient, email_style,Signature):
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.9)
    # Template for building the PROMPT
    template = """
    Write the entire email in proper structure (including the subject...) with {style} style on the topic: {email_topic}.
    Sender: {sender}
    Recipient: {recipient}
    Signature : {Signature}
    Email Text:
    """
    
    # Creating the final PROMPT
    prompt = PromptTemplate(
        input_variables=["style", "email_topic", "sender", "recipient","Signature"],
        template=template,
    )

    # Generating the response using LLM
    # Using 'invoke' function for the response
    response = llm.invoke(prompt.format(email_topic=form_input, sender=email_sender, recipient=email_recipient, style=email_style,Signature=Signature))
    return response

st.set_page_config(page_title="Generate Emails",
                   page_icon='📧',
                   layout='centered',
                   initial_sidebar_state='collapsed')

st.header("Generate Emails 📧")

with st.expander(f"**Types of Emails Used in the Job Hunting Process**"):
    st.write(emails)

form_input = st.text_area('Enter the email topic',placeholder='Application for Machine Learning Engineer Role at ExampleTech',height=200)

# Creating columns for the UI - To receive inputs from user
col1, col2, col3 = st.columns([10, 10, 5])
with col1:
    email_sender = st.text_input('Sender Name')
with col2:
    email_recipient = st.text_input('Recipient Name')
with col3:
    email_style = st.selectbox('Writing Style',
                               ('Formal', 'Appreciating', 'Not Satisfied', 'Neutral'),
                               index=0)

Signature = st.text_area('Signature: your contact details (job title, company, phone number, etc.)',
                         placeholder="""Abdul Samad \nMachine Learning Engineer \nExampleTech \nsamad.example@gmail.com \n+91-1234567890 \n """
                         ,height=100)
# st.write(Signature)
submit = st.button("Generate")

# When 'Generate' button is clicked, execute the below code
response=None
if submit:
    with st.spinner("Thinking ... "):
        response=getLLMResponse(form_input, email_sender, email_recipient, email_style,Signature)
    # clipboard.copy(f"{response.content}")
    # st.success("Text copied to clipboard!")
        st.write(response.content)
    

        