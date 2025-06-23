import streamlit as st
from scrap import *
from parse import *


# Adding title to UI
st.title("AI Web Scrapper")

# Input box for urls to scrap
url = st.text_input("Enter URL : ")

# LOGIC
if st.button("Scrap Site"):
    st.write("Scrapping the Site...")
    
    result = scrapeWebsite(url)
    body_content = extractBodyContent(result)
    
    clean_content = cleanBodyContent(body_content)
    
    st.session_state.dom_content = clean_content
    
    with st.expander("View DOM Content"):
        st.text_area("DOM Content",clean_content,height=300)
        
if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse? ")
    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content...")
            
            dom_chunks = splitDOMcontent(st.session_state.dom_content)
            
            result = parseWithOllama(dom_chunks,parse_description)
            st.write(result)
            
            

    
    