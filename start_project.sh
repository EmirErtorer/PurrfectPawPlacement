#!/bin/bash
echo "Setting up the Django Project Environment..."

# Step 1: Create a Virtual Environment
echo "Creating a virtual environment..."
python3 -m venv env
if [ $? -ne 0 ]; then
    echo "Failed to create a virtual environment."
    exit 1
fi

# Step 2: Activate the Virtual Environment
echo "Activating the virtual environment..."
source env/bin/activate
if [ $? -ne 0 ]; then
    echo "Failed to activate the virtual environment."
    exit 1
fi

# Step 3: Install Requirements
echo "Installing requirements from requirements.txt..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "Failed to install required packages."
    exit 1
fi

# Step 4: Run Migrations
echo "Running makemigrations and migrate..."
python manage.py makemigrations
python manage.py migrate
if [ $? -ne 0 ]; then
    echo "Failed to run migrations."
    exit 1
fi

# Step 5: Start the Django Development Server
echo "Starting the Django server..."
echo "Go to adress: http://127.0.0.1:8000/registration/login/ "
python manage.py runserver


echo "Script completed."
