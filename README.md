Photo Upload Website with Django and AWS S3
This project demonstrates a simple photo upload website built with Django and AWS S3. Users can upload photos from their iPhones using a web interface and label them with pre-defined categories. The uploaded images are securely stored in an AWS S3 bucket, and their filenames and labels are persisted in DynamoDB.

Features:

* Upload photos from iPhone
* Label photos with predefined categories using a dropdown menu
* Store images in AWS S3 bucket
* Save image filenames and labels in DynamoDB
* Django backend for handling upload requests
* HTML and JavaScript for user interface

Requirements:
* Python 3.x
* Django
* django-storages
* django-boto3 (for interacting with DynamoDB)
* AWS account with S3 bucket and DynamoDB table

Setup:
1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install the required Python packages:
'''
    pip install django django-storages django-boto3
'''
4. Configure your AWS credentials and S3 bucket details in settings.py.
5. Configure your DynamoDB table details in settings.py.
6. Run the development server:
    '''
    python manage.py runserver
    '''

Usage:

1. Visit the website in your web browser.
2. Select an image from your iPhone.
3. Choose a label from the dropdown menu.
4. Click the upload button.
5. The image will be uploaded to your S3 bucket, its filename and label will be saved in DynamoDB, and a success message will be displayed.

