# Use a lean, official Python image for CPU projects
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Set environment variable to prevent prompts
ENV DEBIAN_FRONTEND=noninteractive

# 1. Install necessary system packages (libgl1, etc., required by OpenCV/PyTorch/etc.)
RUN apt-get update && \
    apt-get install -y \
        libgl1 \
        libsm6 \
        libxext6 \
    && rm -rf /var/lib/apt/lists/*

# 2. Copy the requirements file
COPY requirements.txt .

# 3. Install all dependencies from the file
# This installs PyTorch (CPU), EasyOCR, and all dependencies at the specified versions.
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the application code and image
COPY main.py .
COPY Tesla.png . 

# Define the command to run your script
CMD ["python", "main.py"]