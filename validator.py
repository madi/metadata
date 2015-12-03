#!/usr/bin/python

from __future__ import print_function
import os,sys
import glob
import argparse
import json
import logging
import urllib2

#===========================

# used function written by Tom Kralidis
# https://gist.github.com/tomkralidis/275a5f1bc70d21dbda12

def validate_inspire_metadata(metadata):
    """validate metadata against INSPIRE metadata validation service"""

    success = None

    host = 'http://inspire-geoportal.ec.europa.eu'
    endpoint = 'GeoportalProxyWebServices/resources/INSPIREResourceTester'

    url = '{0}/{1}'.format(host, endpoint)

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'text/plain'
        }

    request = urllib2.Request(url, data = metadata, headers = headers)
    response = urllib2.urlopen(request)
    report = response.info().getheader('Location')

    json_data = json.loads(response.read())

    if 'ResourceReportResource' in json_data['value']:
        success = False
        logging.error('[ERROR]: Validation failed!!!')

    else:
        success = True
        logging.info('[OK]: Validation passed')

    return {
        'success': success,
        'report': report
        }

#===========================

parser = argparse.ArgumentParser(description = 'Performs metadata validation calling \
                                 the INSPIRE Metadata Validation Service at \
                                 http://inspire-geoportal.ec.europa.eu/validator2/.\
                                 Takes as input a folder where xml metadata are stored.')
parser.add_argument('--infolder', dest = "infolder",
                                 help = "Folder where the metadata are. ")
parser.add_argument('--logfile', dest = "logfile",
                                 help = "Specify log file name. ")
args = parser.parse_args()
INPUT_FOLDER = args.infolder
LOGGER = args.logfile
os.chdir(INPUT_FOLDER)

logging.basicConfig(filename = LOGGER, level = logging.DEBUG)

meta = []
for file in glob.glob("*.xml") :
	meta.append(file.split(".")[0])

for record in meta :
    print("validating.. ", record, ".xml \n")
    logging.debug("validating : ")
    logging.debug(record)
    path_input = INPUT_FOLDER + '/' + record + '.xml'

    with open(path_input) as ff :
        try:
            RESULT = validate_inspire_metadata(ff.read())
            if not RESULT['success'] :
                print('[ERROR]: Validation failed: see {} for report'.format(RESULT['report']))

            else :
                print('[OK]: Validation passed')
        except :
            logging.error('[ERROR]: Wrong file encoding?')
            print('[ERROR]: Wrong file encoding?')

print("Done")
