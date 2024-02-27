# Crypto Technical Analysis and Data Storage
This Python code is designed to retrieve technical analysis data for three popular cryptocurrencies (Bitcoin, Ethereum, and Ripple) from the Technical Analysis API, and then store the retrieved data in Amazon S3 and Amazon Kinesis.
![Crypto_Analysis](https://th.bing.com/th/id/OIG4.wwkCWMFRm7d83XdsGI2H?w=400&h=400&c=6&r=0&o=5&pid=ImgGn)

## Functions
• `get_crypto_data()`: Gets the technical analysis data for all three cryptocurrencies from the Technical Analysis API.
• `send_to_kinesis(crypto_data)`: Sends the retrieved data to the Amazon Kinesis data stream.
• `save_to_s3(crypto_data)`: Saves the retrieved data to an Amazon S3 bucket.

## Dependencies
• [requests](https://requests.readthedocs.io/): A Python library for making HTTP requests.
• [json](https://docs.python.org/3/library/json.html): A Python library for working with JSON data.
• [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html): The AWS SDK for Python.

to install all dependencies, run: `> pip install -r requirements.txt`.

## Configuration
1. Replace YOUR_API_KEY with your Technical Analysis API key.
2. Replace YOUR_DATA_STREAM_NAME with the name of your Amazon Kinesis data stream.
3. Replace YOUR_BUCKET_NAME with the name of your Amazon S3 bucket.

## Run Code:
To execute this Code you can use the following command in terminal or cmd: 
`> python crypto_analysis.py`