rmdir /s /q .\build
rmdir /s /q .\dist
pause
.\venv\Scripts\python setup.py build_exe
.\venv\Scripts\python setup.py bdist_msi
%SystemRoot%\explorer.exe .\build\exe.win-amd64-3.8