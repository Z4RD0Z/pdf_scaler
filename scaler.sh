#!/bin/sh
folder_path=`find /home/$USER -type d -name "pdf_scaler"`

cd $folder_path

./pdf_scaler.py