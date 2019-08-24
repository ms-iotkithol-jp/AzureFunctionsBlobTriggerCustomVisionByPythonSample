import logging
import io, http.client, urllib.request, urllib.parse, urllib.error, base64

import azure.functions as func


cv_prediction_key = '< Custom Vision - Prediction Key >'
cv_url = '< Custom Vision - URL >'
cv_endpoint = '< Custom Vision Endpoint >'
cv_iteration_id = '< Iteration Id >'

def main(myblob: func.InputStream, outputBlob: func.Out[func.InputStream]):
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")
    headers = {
        # Request headers
        'Content-Type': 'application/octet-stream',
        'Prediction-key': cv_prediction_key,
    }
    conn = http.client.HTTPSConnection(cv_url)
    conn.request("POST", cv_endpoint, myblob.read(), headers)
    response = conn.getresponse()
    data = response.read()
    logging.info(f"Predicted : {data}")
    outputBlob.set(data)

    # if you want to use following style please add azure-cognitiveservices-vision-customvision into requirements.txt
    #predictor = CustomVisionPredictionClient(cv_prediction_key,  endpoint=cv_endpoint)
    #predicted = predictor.predict_image(
    #    cv_project_id,
    #    myblob.getvalue(),
    #    iteration_id=cv_iteration_id)
    

