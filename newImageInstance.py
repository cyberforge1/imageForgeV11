import os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'll_project.settings'
django.setup()


from imageGeneration.models import Image
from saveImage import local_image_path

from django.utils import timezone
from imageGeneration.models import Image

from newPromptInstance import prompt_instance

import boto3
from botocore.exceptions import NoCredentialsError


# Create a new instance of the Image model
imageModel = Image()

    # Set the values for the fields
imageModel.text_field = prompt_instance
imageModel.datetime_field = timezone.now()
imageModel.image_field = local_image_path
imageModel.local_url = f'http://127.0.0.1:8000/media/{imageModel.image_field}'

# Save the instance to the database
imageModel.save()


# Print the field values
print("Text Field:", imageModel.text_field)
print("Datetime Field:", imageModel.datetime_field)
print("Image Field:", imageModel.image_field)
print("Local Image URL Field:", imageModel.local_url)
print("Specific Image Instance ID:", imageModel.id)
    
    
#create_image_instance()
image_model = Image.objects.latest('datetime_field')
s3_key = f"media/{image_model.image_field.name}"
# Define the S3 bucket details
bucket_name = 'imageforgeheroku'  # Replace with your S3 bucket name
print('This is the s3 key', s3_key)


def upload_image_to_s3(image_file):
    
    
    
    # Create an S3 client
    s3 = boto3.client('s3')
    bucket_name = 'imageforgeheroku'  # Replace with your S3 bucket name
    s3_key = f"media/{image_model.image_field.name}"
    
    try:
        # Upload the file to S3
        s3.upload_file(s3_key, bucket_name, s3_key)
        print(f"Image uploaded to S3 bucket '{bucket_name}' successfully!")
    except FileNotFoundError:
        print("The file was not found!")
    except NoCredentialsError:
        print("Credentials not available!")

# Call the upload function with the image file from the Image model instance
upload_image_to_s3(s3_key)



# Account ID/ARN: arn:aws:iam::876218180709:user/obj809

