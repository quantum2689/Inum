# Use the official Python image with the specific version
FROM python:3.11.5-slim

# Set the working directory
WORKDIR /app

# Copy the requirements directly if you have them, otherwise install packages later
# COPY requirements.txt .

# Install the necessary packages
RUN pip install --no-cache-dir streamlit tensorflow pillow numpy

# Copy the local code to the container
COPY . .

# Expose the port that Streamlit will run on
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "gui.py","--theme.base="dark""]
