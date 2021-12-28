import oci
from pyspark import SparkConf
from pyspark.sql import SparkSession, SQLContext

import os
from urllib import request
from urllib import parse
import json

url = "XXXXXX"
bot_key = "XXXXXX"
guid = "XXXXXX"
take = "XXXXXX"

bucketName = "XXXXXX"
namespace = "XXXXXX"

#Cria um spark session
def get_dataflow_spark_session(
    app_name="DataFlow", file_location=None, profile_name=None, spark_config={}):
		"""
		Get a Spark session in a way that supports running locally or in Data Flow.
		"""
		spark_builder = SparkSession.builder.appName(app_name)


		# Add in extra configuration.
		for key, val in spark_config.items():
			spark_builder.config(key, val)

		# Create the Spark session.
		session = spark_builder.getOrCreate()
		return session
	
def get_token_path(spark):
	token_key = "spark.hadoop.fs.oci.client.auth.delegationTokenPath"
	token_path = spark.sparkContext.getConf().get(token_key)
	return token_path

def get_authenticated_client(token_path, client):
	if token_path is None:
		# You are running locally, so use our API Key.
		config = oci.config.from_file()
		authenticated_client = client(config)
	else:
		# You are running in Data Flow, so use our Delegation Token.
		with open(token_path) as fd:
			delegation_token = fd.read()
		signer = oci.auth.signers.InstancePrincipalsDelegationTokenSigner(
			delegation_token=delegation_token
		)
		authenticated_client = client(config={}, signer=signer)
	return authenticated_client
	
def put_object(content, objectName):
	spark = get_dataflow_spark_session()
	token_path = get_token_path(spark)
	object_storage_client = get_authenticated_client(token_path, oci.object_storage.ObjectStorageClient)
	try:
		object_storage_client.put_object(namespace, bucketName, objectName, content)
		output = "Success: Put object '" + objectName + "' in bucket '" + bucketName + "'"
	except Exception as e:
		output = "Failed: " + str(e)

	print(output)
	return { "state": output }

def extract_blip_data(guid, take, bot_key):
	params = {"id": f"{guid}",
	"method": "get",
	"uri": f"/threads?$take={take}&refreshExpiredMedia=true"
	}
	query_string = parse.urlencode(params).encode('utf8')
	headers = {"Authorization": f"{bot_key}",
	"content-type": "application/json"}
	data = json.dumps(params).encode("utf-8")
	req = request.Request(url, data, headers)
	with request.urlopen(req) as f:
		res = f.read().decode()
	put_object(res, 'resposta.txt')
	print('Processo concluído.')

def main():
	extract_blip_data(guid, take, bot_key)

main()

