import boto3
import uuid
from datetime import datetime
from botocore.exceptions import ClientError

def add_to_dynamodb(aws_creds, table_name, user_data):
    """Add user data to DynamoDB table."""
    aws_access_key, aws_secret_key, aws_region,instance_id = aws_creds
    
    # Verify credentials
    if not aws_access_key or not aws_secret_key:
        print("❌ AWS credentials are missing or empty")
        return False, None
    
    try:
        print(f"Connecting to AWS DynamoDB in region {aws_region}...")
        
        # Initialize DynamoDB client
        dynamodb = boto3.resource(
            'dynamodb',
            region_name=aws_region,
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key
        )
        
        # Check if table exists, if not, create it
        dynamodb_client = boto3.client(
            'dynamodb',
            region_name=aws_region,
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key
        )
        
       
        # Use the table
        table = dynamodb.Table(table_name)
        
        # Generate a unique ID
        subscription_id = str(uuid.uuid4())
        
        # Add timestamp
        timestamp = datetime.now().isoformat()
        
        # Insert data
        print(f"Adding data to table {table_name}...")
        table.put_item(
            Item={
                'User_id': subscription_id,
                'email': user_data['email'],
                'keyword': user_data['keyword'],
                'location': user_data['location'],
                'timestamp': timestamp
            }
        )
        
        print(f"✅ Data added to DynamoDB with ID: {subscription_id}")
        return True, subscription_id
    except ClientError as e:
        print(f"❌ DynamoDB error: {e}")
        error_code = getattr(e, 'response', {}).get('Error', {}).get('Code')
        if error_code == 'InvalidSignatureException':
            print("   This is likely due to incorrect AWS credentials")
        return False, None
    except Exception as e:
        print(f"❌ Error: {e}")
        return False, None
