import streamlit as st
import os
import soundfile as sf
import librosa

# Title of the app
st.title("Sound Segregator")

# File uploader for multiple files
uploaded_files = st.file_uploader("Choose audio files", type=["wav", "mp3", "flac"], accept_multiple_files=True)

# Output directory
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Output file format options
file_format = st.selectbox("Choose output file format", ["wav", "mp3"])

# Advanced settings on main screen
st.header("Advanced Settings")
fft_size = st.slider("FFT Size", 256, 8192, 2048)
hop_length = st.slider("Hop Length", 64, 1024, 512)

# Function to process a single file
def process_file(uploaded_file):
    # Save the uploaded file temporarily
    input_path = os.path.join(output_dir, uploaded_file.name)
    with open(input_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Load audio file
    y, sr = librosa.load(input_path, sr=None)

    # Segregate audio with advanced settings
    harmonic, percussive = librosa.effects.hpss(y, margin=(1.0, 1.0), kernel_size=fft_size, hop_length=hop_length)

    # Display input file name
    st.subheader(f"Results for {uploaded_file.name}")

    # Save and display download links for each component
    component_names = ['harmonic', 'percussive']
    components = [harmonic, percussive]
    for i, component in enumerate(components):
        output_filename = os.path.join(output_dir, f"{os.path.splitext(uploaded_file.name)[0]}_{component_names[i]}.{file_format}")
        sf.write(output_filename, component, sr, format=file_format)
        st.audio(output_filename, format=f"audio/{file_format}")
        st.download_button(
            label=f"Download {component_names[i]}",
            data=open(output_filename, "rb").read(),
            file_name=output_filename
        )

# Segregation button
if st.button("Start Segregation"):
    if uploaded_files is not None:
        # Process each uploaded file
        for uploaded_file in uploaded_files:
            process_file(uploaded_file)
