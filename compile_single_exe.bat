pyinstaller --noconsole --onefile .\main.py --name=Desktop_Cat_build --icon=assets\icon.ico --distpath=.\Release
rd /s /q .\build
del *.spec