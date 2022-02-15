cd restic
git checkout v0.12.1
go run build.go
cd ../
cp restic/restic.exe src/blobbackup/bin/blobbackup.exe

src/blobbackup/scripts/generateui.sh
pip install .
python src/blobbackup/__main__.py