usage: hasher.py [-h] [--csvfile [PATH_CSV]] [--directory [PATH_DIRECTORY]]
                 [--original [ORIGINAL_CSV]]
                 [rehash_value]

Welcome to Hasher!

positional arguments:
  rehash_value          Rehashes your directory and compares it to your cvs
                        file

optional arguments:
  -h, --help            show this help message and exit
  --csvfile [PATH_CSV], -o [PATH_CSV]
                        Path to output new CSV to
  --directory [PATH_DIRECTORY], -d [PATH_DIRECTORY]
                        To be hashed directory
  --original [ORIGINAL_CSV], -c [ORIGINAL_CSV]
                        Specify path to original csv file