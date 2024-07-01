# Use the official Ubuntu base image
FROM ubuntu:latest

# Update the package list and install Python3 and pip
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set up a virtual environment
RUN python3 -m venv /opt/venv

# Activate the virtual environment and upgrade pip
RUN /opt/venv/bin/pip install --upgrade pip

# Install the required Python package within the virtual environment
RUN /opt/venv/bin/pip install -qU langchain-openai

# Copy the Python script into the container
COPY script.py /app/script.py

# Set the working directory
WORKDIR /app

# Ensure the virtual environment is used for the script
ENV PATH="/opt/venv/bin:$PATH"

# Command to run the script
CMD ["python3", "script.py"]

