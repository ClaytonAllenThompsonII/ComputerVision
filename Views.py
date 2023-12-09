from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from .storages import S3Boto3Storage

@csrf_exempt
def upload_image(request):
    """
    Handle image upload requests.

    This view function receives POST requests containing the uploaded image file
    in the 'image' field of the request body. It then saves the image to the
    configured storage backend (AWS S3 in this case) and returns a JSON response.

    Args:
        request: A Django HttpRequest object containing the uploaded image.

    Returns:
        A Django HttpResponse object with JSON response data.
    """

    if request.method == 'POST':
        # Get the uploaded image file
        image = request.FILES.get('image')

        # Check if image is present
        if not image:
            return HttpResponseBadRequest('Missing image file')

        # Get storage backend
        storage = S3Boto3Storage()

        # Generate unique filename
        filename = f'images/{uuid.uuid4()}{os.path.splitext(image.name)[1]}'

        # Save image to storage
        try:
            storage.save(filename, image)
        except Exception as e:
            return HttpResponseServerError(f'Error uploading image: {e}')

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