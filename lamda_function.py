import boto3
s3 = boto3.client('s3')

test for pullrequest

# Call S3 to list current buckets
response = s3.list_buckets()

buckets = [bucket['Name'] for bucket in response['Buckets']]

# Print out the bucket list
print("Bucket List: %s" % buckets)

BUCKET_NAME = 'athena-test-new1'
DATABASE = 'sampledb'
TABLE = 'elb_logs'
S3_OUTPUT = 's3://athena-test-new1'

resource = boto3.resource('s3')
udst_dstl = resource.Bucket(BUCKET_NAME)
obj = s3.get_object(Bucket=BUCKET_NAME, Key='input.csv')

query1 = obj['Body'].read()
query1 = query1.decode('utf-8')

def run_query(query, database, s3_output):
    client = boto3.client('athena')
    response = client.start_query_execution(
        QueryString=query,
        QueryExecutionContext={
            'Database': database
            },
        ResultConfiguration={
            'OutputLocation': s3_output,
            }
        )
    print('Execution ID: ' + response['QueryExecutionId'])
    return response

res = run_query(query1, DATABASE, S3_OUTPUT)
# athena client
athena = boto3.client('athena')

# get query execution id
query_execution_id = res['QueryExecutionId']
print(query_execution_id)

# get query execution
query_status = athena.get_query_execution(QueryExecutionId=query_execution_id)

print(query_status)
