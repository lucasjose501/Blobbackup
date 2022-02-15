cd restic
git checkout v0.12.1
go run build.go
cd ../
cp restic/restic.exe src/blobbackup/bin/blobbackup.exe

src/blobbackup/scripts/generateui.ps1
pip install .
pyinstaller --clean --noconfirm package/blobbackup.spec
rm build -r -fo