# Use a lightweight Python image
FROM python:3.12-slim

#Prevent python from buffering for TUI
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy only the requirements first to leverage Docker's cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your source code
COPY . .

# Set the command to run your tool
# This allows you to pass arguments directly to the docker run command
CMD ["python", "tui.py"]