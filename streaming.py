import boto3
from botocore.exceptions import ClientError

class LiveStreamManager:
    def __init__(self):
        self.ivs_client = boto3.client('ivs')
    
    def create_channel(self, stream_name: str):
        try:
            response = self.ivs_client.create_channel(
                name=stream_name,
                type='STANDARD',
                authorized=False
            )
            return response['channel']
        except ClientError as e:
            print(f"Error creating channel: {e}")
            return None
    
    def generate_stream_token(self, channel_arn: str, user_id: str):
        try:
            response = self.ivs_client.create_participant_token(
                channelArn=channel_arn,
                userId=user_id
            )
            return response['participantToken']
        except ClientError as e:
            print(f"Error generating stream token: {e}")
            return None
