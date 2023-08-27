import streamlit as st
import folium
from streamlit_folium import st_folium

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

        # Create a map centered at the location and add a marker
        m = folium.Map(location=[result['location']['lat'], result['location']['long']], zoom_start=16)
        folium.Marker(
            [result['location']['lat'], result['location']['long']], 
            popup=f"Price: {result['price']}", 
            tooltip="Property Location"
        ).add_to(m)

        # Display the map
        st_folium(m, width=725)

if __name__ == "__main__":
    main()
