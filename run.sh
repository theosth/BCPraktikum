#!/bin/sh

# Install required packages
apk add --no-cache python3-dev py3-pip
pip install --no-cache-dir -r /app/repo/requirements.txt

# Run the factorial.py script with a sample input
python /app/repo/factorial.py 20

# Create output directory if it doesn't exist
mkdir -p /app/repo/output

# Move the output.txt to the output directory
mv /app/repo/output.txt /app/repo/output/output.txt
