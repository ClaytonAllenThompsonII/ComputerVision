from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from .storages import S3Boto3Storage
from boto3.dynamodb import resource

@csrf_exempt
def upload_image(request):
    """
    Handle image upload requests.

    This view function receives POST requests containing the uploaded image file
    and selected inventory classification label in the 'image' and 'label' fields
    of the request body, respectively. It then saves the image to S3, stores the
    filename and label in DynamoDB, and returns a JSON response.

    Args:
        request: A Django HttpRequest object containing the uploaded image and label.

    Returns:
        A Django HttpResponse object with JSON response data.
    """

    if request.method == 'POST':
        # Get the uploaded image file
        image = request.FILES.get('image')

        # Check if image is present
        if not image:
            return HttpResponseBadRequest('Missing image file')

        # Get the selected label
        label = request.POST.get('label')

        # Check if label is present
        if not label:
            return HttpResponseBadRequest('Missing inventory classification label')

        # Get storage backend
        # Access AWS credentials from environment variables
        aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
        aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']

        storage = S3Boto3Storage(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            # Access S3 bucket name from environment variables
            bucket_name=os.environ['S3_BUCKET_NAME'],
            # Access AWS region name from environment variables
            region_name=os.environ['AWS_REGION_NAME']
        )

        # Generate unique filename
        filename = f'images/{uuid.uuid4()}{os.path.splitext(image.name)[1]}'

        # Save image to storage
        try:
            storage.save(filename, image)
        except Exception as e:
            return HttpResponseServerError(f'Error uploading image: {e}')

        # Create a DynamoDB client
        dynamodb = resource('dynamodb')
        table = dynamodb.Table('your_table_name')

        # Prepare item data
        item = {
            'filename': filename,
            'label': label,
            # Add any other relevant fields to the item
            # ...
        }

        # Save the item to DynamoDB
        try:
            table.put_item(Item=item)
        except Exception as e:
            logger.error(f'Error saving item to DynamoDB: {e}')

        # Prepare response data
        response_data = {
            'message': 'Image uploaded successfully!',
            'filename': filename,
            'url': storage.url(filename),
        }

        # Return JSON response
        return JsonResponse(response_data)

    else:
        return HttpResponseBadRequest('Invalid request method')

