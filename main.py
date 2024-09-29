import requests
from datetime import timedelta, date, datetime
import json 
import os
import csv
from transformers import GPT2LMHeadModel, GPT2Tokenizer

api_key = "8dc8c80326786e0ffe2f69770368cc8f"
secret = "496f214a8fbd2d3e"
url = 'https://api.flickr.com/services/rest/?method=flickr.photos.search'
root = 'C:/Users/MSI/Desktop/photos'
step = 2
i = 0
j = step - 1
accuracy = 12
has_geo = 1 
minimum_taken_date = date(2017, 12, 1) # 2017
maximum_taken_date = date(2019, 1, 1) # 2019
lower_longitude = '7.87765'
lower_latitude = '32.92967'
upper_longitude = '11.21965'
upper_latitude = '37.27442'
bbox = lower_longitude + ',' + lower_latitude + ',' + upper_longitude + ',' + upper_latitude

def generate_travel_guide(location_data):
    gpt2_model = GPT2LMHeadModel.from_pretrained("gpt2")
    gpt2_tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

    # Placeholder for image description prompt
    image_description_prompt = f"A photo from {location_data['name']}."

    # Generate text description using GPT-2
    input_ids = gpt2_tokenizer.encode(image_description_prompt, return_tensors="pt")
    output = gpt2_model.generate(input_ids, max_length=100, num_beams=5, no_repeat_ngram_size=2)
    generated_text = gpt2_tokenizer.decode(output[0], skip_special_tokens=True)

    return generated_text

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)
date_range = []
for single_date in daterange(minimum_taken_date, maximum_taken_date):
    single_date_string = single_date.strftime('%Y-%m-%d')
    date_range.append(single_date_string)
date_length = len(date_range)
print("Date length: ", date_length)
params = dict(api_key=api_key,
              format='json',
              nojsoncallback='1',
              min_taken_date=date_range[i],
              max_taken_date=date_range[j],
              bbox=bbox,
              accuracy=accuracy,
              has_geo=has_geo)
resp = requests.get(url=url, params=params)
data = json.loads(resp.text)
with open('firstTry.json', 'w') as file_object:
    json.dump(data, file_object)
print('Created first try file')

DIR = "C:/Users/MSI/Desktop/app/"
x = 0
i = 0
j = step - 1
dataset = []
with open('./firstTry.json', 'r') as data_file:
    n = 0
    jdata = json.load(data_file)
    jdata_len = len(jdata['photos']['photo'])
    while n < jdata_len:
        new_corpus = {'id': jdata['photos']['photo'][n]['id'],
                      'owner': jdata['photos']['photo'][n]['owner'],
                      'secret': jdata['photos']['photo'][n]['secret']}
        dataset.append(new_corpus)
        n += 1
    x += 1
    i += step
    j += step
    n = 0
print('Total corpus added:', len(dataset))

url = 'https://api.flickr.com/services/rest/?method=flickr.photos.getInfo'
i = 0
dataset_length = len(dataset)
error_count = 0

while True:
    try:
        while i < dataset_length:
            params = dict(api_key=api_key,
                          format='json',
                          nojsoncallback='1',
                          photo_id=dataset[i]['id'],
                          secret=dataset[i]['secret'])
            resp = requests.get(url=url, params=params)
            data = json.loads(resp.text)
            file_object = open('getinfo/{0}.json' .format(dataset[i]['id']), 'w')
            json.dump(data, file_object)
            i += 1
            if i % 200 == 0:
                print('{0} / {1} JSON data created.' .format(i, dataset_length))
            error_count = 0
    except Exception as ex:
        error_count += 1
        print('{0} when trying to get data of {1}. Retrying...' .format(ex, dataset[i]['id']))
        if error_count > 5:
            pass
        else:
            continue
    break

print('Total JSON data created: {0}' .format(i))

i = 0
DIREC = 'getinfo/'
file_list = [f for f in os.listdir(DIREC) if '.json' in f]
num_files = len(file_list)
csv_columns = ['photo_id', 'owner_nsid', 'owner_location', 'dates_taken', 'location_latitude', 'location_longitude', 'description']
getinfo = []
print('Files found in the directory: ', num_files)

while True:
    try:
        for f in file_list:
            with open('getInfo/{0}'.format(f)) as data_file:
                jdata = json.load(data_file)
                new_corpus = {'photo_id': jdata['photo']['id'],
                              'owner_nsid': jdata['photo']['owner']['nsid'],
                              'owner_location': jdata['photo']['owner']['location'],
                              'dates_taken': jdata['photo']['dates']['taken'],
                              'location_latitude': jdata['photo']['location']['latitude'],
                              'location_longitude': jdata['photo']['location']['longitude'],
                              'description': jdata['photo']['description']['_content']}
                getinfo.append(new_corpus)
                i += 1
                if i % 500 == 0:
                    print('{0} / {1} files added to dictionary.' .format(i, num_files))
                    continue
    except Exception:
        print('{0} when trying to get data from to {1}' .format(Exception, f))
        pass
    break

try:
    with open('CSV/dirty.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in getinfo:
            writer.writerow(data)
except IOError:
    print("I/O error")

print('A new CSV file containing {0} rows has been created.' .format(i))

for item in dataset:
    travel_guide = generate_travel_guide({'name': item['owner']})
    print(f"Travel Guide for {item['owner']}:\n{travel_guide}\n")
    # Save the generated guide to a file
    with open(f'generated_guides/{item["owner"]}_guide.txt', 'w') as guide_file:
        guide_file.write(travel_guide)
