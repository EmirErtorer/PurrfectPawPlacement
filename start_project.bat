@echo off
echo Setting up the Django Project Environment...

:: Step 1: Create a Virtual Environment
echo Creating a virtual environment...
python -m venv env
if %errorlevel% neq 0 goto Error

:: Step 2: Activate the Virtual Environment
echo Activating the virtual environment...
call env\Scripts\activate
if %errorlevel% neq 0 goto Error

:: Step 3: Install Requirements
echo Installing requirements from requirements.txt...
pip install -r requirements.txt
if %errorlevel% neq 0 goto Error

:: Step 4: Run Migrations
echo Running makemigrations and migrate...
python manage.py makemigrations
python manage.py migrate
if %errorlevel% neq 0 goto Error

:: Step 5: Start the Django Development Server
echo Starting the Django server...
python manage.py runserver
echo go to the address: http://127.0.0.1:8000/registration/login

goto End

:Error
echo There was an error setting up the Django environment.
pause

:End
echo Script completed.
pause
