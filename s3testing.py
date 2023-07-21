import boto3
from botocore.exceptions import NoCredentialsError
from django.conf import settings

def upload_image_to_s3(file_path):
    s3 = boto3.client('s3')
    bucket_name = 'imageforgeheroku'
    s3_key = 'image.jpg'  # The desired key for the uploaded file in the S3 bucket
    
    try:
        # Upload the file to S3
        s3.upload_file(file_path, bucket_name, s3_key)
        print(f"Image uploaded to S3 bucket '{bucket_name}' successfully!")
    except NoCredentialsError:
        print("Credentials not available!")

# Call the upload function with the file path of the image
file_path = 'media/image.jpg'
upload_image_to_s3(file_path)