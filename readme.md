# Inum

This project is a web application built with Streamlit and TensorFlow that predicts handwritten digits from the MNIST dataset. The application allows users to upload an image of a digit, and it returns the predicted digit using a pre-trained model.

## Features

- Upload an image of a handwritten digit.
- The image is preprocessed (grayscale, resized, normalized) and passed to a TensorFlow model.
- The model predicts the digit, and the result is displayed on the web interface.

## Requirements

- Python 3.11.5
- Docker (optional, for containerized deployment)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/mnist-streamlit-app.git
cd mnist-streamlit-app
```

## Install Python Dependencies
```bash
pip install streamlit tensorflow pillow numpy
```

## Run the Application

```bash
streamlit run gui.py  --theme.base="dark"
```


