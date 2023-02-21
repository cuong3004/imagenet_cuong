import urllib.request
import zipfile
import os

url = 'https://github.com/tensorflow/models/archive/refs/tags/v2.11.0.zip'
file_name = 'v2.11.0.zip'

urllib.request.urlretrieve(url, file_name)

with zipfile.ZipFile(file_name, 'r') as zip_ref:
    zip_ref.extractall()

os.rename('models-2.11.0', 'models')

