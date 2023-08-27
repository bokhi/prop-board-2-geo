import streamlit as st
import folium
from streamlit_folium import folium_static

def process_listing(listing):
    # This is a dummy function for now
    return {
        'location': {
            'lat': 51.5074,
            'long': -0.1278
        },
        'price': 1000000
    }

def main():
    st.title('Property Listing Processor')
    listing = st.text_area('Paste your property listing here:', '')
    if st.button('Process'):
        result = process_listing(listing)
        st.write('Processing...')
        st.write(result)

        # Create a map centered at the location
        m = folium.Map(location=[result['location']['lat'], result['location']['long']])

        # Display the map
        folium_static(m)

if __name__ == "__main__":
    main()
