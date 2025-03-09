# Use official Python image as base
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the application files
COPY app.py requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask runs on
EXPOSE 5000

# Run the application with Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
