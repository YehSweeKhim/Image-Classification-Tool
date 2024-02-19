import requests as re
import streamlit as st


# Define the FastAPI service URL
FASTAPI_URL = "http://fastapi:8000/predict"
MAX_FILE_SIZE_MB = 10
MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MB * 1024 * 1024

st.markdown("## Image Classification Tool")
st.markdown("This tool uses the ResNet50 model for image classification. Upload an image using the \"Browse files\" button or drag and drop it into the designated area to get started.")

# Upload an image
object_image = st.file_uploader("", type=['png','jpg','webp','jpeg'])

# Click predict button
submit = st.button('Predict')
if submit and object_image is not None:
        # Validate file type and size
        if object_image.type not in ['image/png', 'image/jpeg', 'image/webp']:
            st.error("Invalid file type. Please upload a PNG, JPEG, or WebP image.")
            st.stop()
        if len(object_image.getvalue()) > MAX_FILE_SIZE_BYTES:
            st.error(f"File size exceeds the maximum allowed size of {MAX_FILE_SIZE_MB} MB.")
            st.stop()
        
        # Display image
        st.image(object_image, caption="Uploaded Image")

        # Predict image
        files = {"file": object_image.getvalue()}
        response = re.post(FASTAPI_URL,files=files)
        predicted_classes = response.json()

        # Show classification result
        st.markdown("Classification Result:")
        for prediction in predicted_classes:
            name = prediction["name"]
            likelihood = prediction["likelihood"]
            st.text('- {}: {:.2f} likelihood'.format(name, likelihood))