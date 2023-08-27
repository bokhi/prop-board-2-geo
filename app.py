import streamlit as st

def main():
    st.title('Property Listing Processor')
    listing = st.text_area('Paste your property listing here:', '')
    if st.button('Process'):
        st.write('Processing...')

if __name__ == "__main__":
    main()
