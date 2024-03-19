FROM python:3.10.9

# Set the working directory to /app
WORKDIR /app

# Copy the Django project files to the container
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Run Django migrations and insert data
RUN python manage.py migrate
RUN python manage.py insertdata

# Expose port 443 for SSL
EXPOSE 443

# Run the Django development server with SSL
CMD ["python", "manage.py", "runsslserver", "--cert", "abnormal_certificate.crt", "--key", "abnormal.key", "0.0.0.0:443"]