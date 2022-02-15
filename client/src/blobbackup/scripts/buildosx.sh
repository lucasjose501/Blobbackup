#!/bin/bash

cd restic
git checkout v0.12.1
go run build.go
cd ../
cp restic/restic src/blobbackup/bin/blobbackup.exe
chmod +x src/blobbackup/bin/blobbackup.exe

src/blobbackup/scripts/generateui.sh
pip install .
pyinstaller --clean --noconfirm package/blobbackup.spec
rm -rf dist/blobbackup build