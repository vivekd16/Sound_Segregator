# Sound Segregator

## Overview
This project is a web-based audio segregation tool that uses `librosa` for harmonic-percussive source separation (HPSS). It allows users to upload audio files and separate them into harmonic and percussive components.

## Features
- Separate audio tracks into harmonic and percussive components
- Support for various audio formats (WAV, MP3, FLAC)
- Interactive web interface using Streamlit
- Adjustable FFT size and hop length for audio processing

## Installation
1. Clone the repository
2. Create a virtual environment
3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Web Application
Run the Streamlit app:
```bash
streamlit run app.py
```

## Live Demo
Check out the live demo on Hugging Face Spaces: [Sound Segregator Demo](https://huggingface.co/spaces/Vivek6041/Sound_Segregator)

## Dependencies
- Librosa
- Streamlit
- SoundFile
- NumPy
- SciPy

## Deployment
This project can be deployed on platforms like Hugging Face Spaces and GitHub. Ensure all dependencies are listed in `requirements.txt` and the app is configured to run using Streamlit.
