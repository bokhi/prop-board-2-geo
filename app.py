import os
import openai
from dotenv import load_dotenv
import streamlit as st
import folium
from streamlit_folium import folium_static

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

function_descriptions = [
    {
        "name": "extract_info_from_listing",
        "description": "Categorise & extract key info from a property listing, such as location, price, etc.",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "array",
                    "items": {
                        "type": "number"
                    },
                    "description": "The longitude and latitude of the property"
                },
                "price": {
                    "type": "number",
                    "description": "The price of the property"
                }
            },
            "required": ["location", "price"]
        }
    }
]

def process_listing(listing):
    prompt = f"Please extract key information from this property listing: {listing} "
    message = [{"role": "user", "content": prompt}]

    response = openai.ChatCompletion.create(
        model="gpt-4-0613",
        messages=message,
        functions = function_descriptions,
        function_call="auto"
    )

    return {
        'location': {
            'lat': response['choices'][0]['message']['content']['location']['lat'],
            'long': response['choices'][0]['message']['content']['location']['long']
        },
        'price': response['choices'][0]['message']['content']['price']
    }

def main():
    st.title('Property Listing Processor')
    listing = st.text_area('Paste your property listing here:', '')
    if st.button('Process'):
        result = process_listing(listing)
        st.write('Processing...')
        st.write(result)

        # Create a map centered at the location
        m = folium.Map(location=[result['location']['lat'], result['location']['long']], zoom_start=16)
        folium.Marker(
            [result['location']['lat'], result['location']['long']], 
            popup=f"Price: {result['price']}", 
            tooltip="Property Location"
        ).add_to(m)


        # Display the map
        folium_static(m)

if __name__ == "__main__":
    main()
