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

import streamlit as st
from streamlit.report_thread import get_report_ctx
from streamlit.server.server import Server

def get_state():
    ctx = get_report_ctx()
    session_id = ctx.session_id
    session_info = Server.get_current()._get_session_info(session_id)

    if session_info is None:
        raise RuntimeError("Couldn't get your Streamlit Session object.")

    return session_info.session._session_state

def main():
    st.title('Property Listing Processor')
    listing = st.text_area('Paste your property listing here:', '')
    state = get_state()
    if 'result' not in state:
        state['result'] = None
    if st.button('Process'):
        state['result'] = process_listing(listing)
        st.write('Processing...')
        st.write(state['result'])

    if state['result'] is not None:
        # Create a map centered at the location and add a marker
        m = folium.Map(location=[state['result']['location']['lat'], state['result']['location']['long']], zoom_start=16)
        folium.Marker(
            [state['result']['location']['lat'], state['result']['location']['long']], 
            popup=f"Price: {state['result']['price']}", 
            tooltip="Property Location"
        ).add_to(m)

        # Display the map
        st_folium(m, width=725)

if __name__ == "__main__":
    main()
