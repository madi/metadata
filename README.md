# Another wrapper to the INSPIRE Metadata Validation Service

This is written on top of the nice function developed by Tom Kralidis, see
https://gist.github.com/tomkralidis/275a5f1bc70d21dbda12#file-readme-md
for more info.

This function calls the INSPIRE validation web service at
http://inspire-geoportal.ec.europa.eu/validator2/ and validates in bulk your
metadata. It takes in input the folder name were the metadata are, and the
path and name of the log file.

## Usage

Example of usage:

 python validator.py --help

will print the usage.

 python validator.py --infolder /path/to/metadata/folder --logfile /path/to/log.log

will perform the validation in bulk of your metadata records.
