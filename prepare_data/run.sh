#!/bin/bash

echo "Extracting links..."
python extract_links.py

echo "Downloading files..."
python download_files.py

echo "Extracting ZIPs..."
python extract_zips.py

echo "Converting to Markdown..."
python convert_all_to_md.py

