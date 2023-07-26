# final-project-of-python-internship
This project is the final project of the Python Internship program. It is a web application built using Django, Django Rest Framework, and other Python libraries to fetch data from Yahoo Finance, store it in a MySQL database, and provide API endpoints to access the data.

Setup
1.Clone the repository to your local machine.
2.Create a virtual environment and activate it

python -m venv venv
source venv/bin/activate   # On Windows, use: venv\Scripts\activate

Install the required dependencies:
pip install -r requirements.txt

Make sure to have MySQL installed and create a new database for this project.

Update the database settings in the settings.py file to connect to your MySQL database:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

Run the initial database migrations:
python manage.py migrate

Run the initial database migrations:
python manage.py migrate

Create a superuser for accessing the Django admin interface (optional):
python manage.py createsuperuser

Running the Project
To start the development server, run the following command:
python manage.py runserver

The development server will be accessible at http://127.0.0.1:8000/

API Endpoints
/fetch-data/: This endpoint triggers the web scraper to fetch data from Yahoo Finance, stores it in the database, and returns a JSON response of the scraped data.

/get-all-data/: This endpoint returns a JSON response of all the data stored in the database.

Proper Logging Strategy
The project is equipped with proper logging to record success and failure events. The success_logger logs successful events such as data fetching and database storage at the INFO level, while the failure_logger logs failure events like failed data fetching or storage errors at the ERROR level. Logs are saved in separate success.log and failure.log files in the project directory.

Process Flow Diagram
The process flow diagram showcases the workflow of the project, including data fetching, storage, and API endpoints.

Conclusion
This project demonstrates the integration of Django, Django Rest Framework, MySQL database, web scraping, and logging to build a web application that fetches and stores financial data from Yahoo Finance and provides API access to the data. It serves as a practical application of Python programming skills, web development, and data handling.


Please make sure to replace `'your_database_name'`, `'your_database_user'`, and `'your_database_password'` with your actual MySQL database credentials. Additionally, adjust the package versions based on your project's requirements.
