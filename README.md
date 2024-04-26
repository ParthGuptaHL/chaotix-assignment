# text_to_image_app

Welcome to text_to_image_app! This Django project utilizes Celery to parallelly call an API asynchronously, converting text into images. The images generated from the API calls are stored in the 'images' folder, and their locations are recorded in an SQLite database included in the project.

## Setup

1. **Python Environment**: Make sure you have Python installed on your system. You can download and install Python from [here](https://www.python.org/downloads/).

    Create a new environment using:
    ```bash
    python3 -m venv env
    ```

    Activate it using
    ```bash
    source ./env/bin/activate
    ```

2. **Clone the Repository**: Clone this repository to your local machine:

    ```bash
    git clone https://github.com/your_username/text_to_image_app.git
    ```

3. **Navigate to Project Directory**: Move into the project directory:

    ```bash
    cd text_to_image_app
    ```

4. **Install Requirements**: Install the required Python packages using pip:

    ```bash
    pip install -r requirements.txt
    ```

5. **Set Environment Variables**: Create a `.env` file in the project root directory and add the following environment variables(also mentioned in .env.example):

    ```plaintext
    API_HOST=<your_api_url>
    STABILITY_API_KEY=<your_api_secret_key>
    ```

    Replace `<your_api_url>` and `<your_api_secret_key>` with the appropriate values.

6. **Run Migrations**: Apply database migrations to create necessary database tables:

    ```bash
    python manage.py migrate
    ```

## Running the Application

1. **Start Django Server**: Run the Django development server:

    ```bash
    python manage.py runserver
    ```

2. **Initiate Celery Worker**: Open a new terminal window, navigate to the project directory, and start a Celery worker:

    ```bash
    celery -A text_to_image_app.celery worker --loglevel=info
    ```

3. **Make API Requests**: You can make API requests using cURL or any HTTP client. Example cURL request:

    ```bash
    curl --location 'http://127.0.0.1:8000/generate/'
    ```

    This will trigger the parallel API calls to generate images.

## Celery Configuration
- Use your desired configuration in settings.py to run the celery worker

## Directory Structure

- **text_to_image_app/**: Django project directory.
    - **text_to_image_generator/**: Django app directory.
    - **images/**: Folder to store generated images.
    - **.env**: Environment variables file.
    - **db.sqlite3**: SQLite database file.
    - **requirements.txt**: Packages required file

## Additional Notes

- Be sure to install Redis in your system
- Ensure that the Celery worker is running in the background to process tasks asynchronously.
- Check the `settings.py` file for any additional configurations specific to your environment.
- Modify the `API_URL` and `API_SECRET_KEY` in the `.env` file according to your API credentials.
- Feel free to explore and customize the codebase to fit your requirements!
