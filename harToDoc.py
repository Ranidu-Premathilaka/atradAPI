import json5 as json
import shutil
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description='Process a HAR file into JSON.')
parser.add_argument('har_file', type=str, help='The path to the HAR file to process')
args = parser.parse_args()

# Open and load the test.har file
with open(args.har_file, 'r') as file:
    print("Insered file opened. Loading data")
    har_data = json.load(file)
print("Insered Data loaded")

# Create a backup of doc.json
shutil.copy('doc.json', 'doc_backup.json')
print("Backup created")

# Opening the Output file to avoid redudency
with open('doc.json', 'r') as file:
    data = json.load(file)
print("Output file opened")

allowedTypes = ['xhr', 'fetch']
removedParams = ['dojo.preventCache']
validResponseTypes =['application/json','text/html']

entryCount = len(har_data['log']['entries'])
currentCount = 0
newAdded = 0

for entry in har_data['log']['entries']:
    currentCount += 1
    print(f"Processing {currentCount}/{entryCount}")

    if entry['_resourceType'] in allowedTypes:
         
        url = entry['request']['url'].split('?')[0]
        method = entry['request']['method']
        responseType = entry['response']['content']['mimeType']

        if responseType not in validResponseTypes:
            continue

        parameters = {}
        if method == 'GET':
            for param in entry['request']['queryString']:
                if param['name'] in removedParams:
                    continue
                parameters[param['name']] = param['value']

        elif method == 'POST':
            for param in entry['request']['postData']['params']:
                if param['name'] in removedParams:
                    continue
                parameters[param['name']] = param['value']
        
        if url in data:
            check = False
            for actionElement in data[url]:
                if actionElement['params'] == parameters:
                    check = True
                    break
            if check:
                continue
        else:
            data[url] = []
        
        response = entry['response']['content']['text']
        #print(response)
        try:
            response = json.loads(response)
        except:
            try:
                response = response.decode("utf-8")
                response.replace("'",'"')
                response = json.loads(response)
            except:
                print("Couldn't parse json file. Printing response")
                #print(response)
                response = False



        #setting all the data
        data[url].append({
                "method": method,
                "header": {},
                "params": parameters,
                "responseType": responseType,
                "response": response
        })

        newAdded += 1

# Write the updated data dictionary to doc.json in JSON format
with open('doc.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Doc Updated newly added entries: ", newAdded)