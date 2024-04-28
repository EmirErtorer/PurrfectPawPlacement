# Project Setup Instructions
Welcome to the setup guide for PurrfectPawPlacement. Follow the instructions below to get the development environment up and running.

# Prerequisites
Before beginning, ensure you have the following installed:

  1) Python (3.10 or higher recommended)
  2) pip (Python package manager)

# Install dependencies
This project uses a virtual environment to manage dependencies.

# Setup the project
  a) If you are using Linux or Windows Subsystem for Linux (WSL), use the shell script provided:
	  ./start_project.sh
  b) If you are using Windows (PowerShell or CMD), use the batch script provided:
	  start_project.bat

# Running the Application
After running the setup script, the Django development server should start automatically.
Access the application through your web browser at http://127.0.0.1:8000/registration/login

# Testing Users
General User: EmirE  Password: root1234
Shelter User: K1L2M3N4O5P  Password: root1234

# Additional Notes
The scripts will handle virtual environment creation, dependency installations, database migrations, and server startup.

# Troubleshooting
Permission Errors: Ensure you have execution permissions for the scripts. For Linux/WSL, you might need to run:   chmod +x start_project.sh.
Dependency Issues: Make sure all dependencies listed in requirements.txt are compatible with your Python version. Upgrade pip if necessary using python -m pip install --upgrade pip.