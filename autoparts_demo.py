name: Build EXE

on:
  workflow_dispatch:

jobs:
  build:
    runs-on: windows-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install PyInstaller
        run: python -m pip install --upgrade pip && pip install pyinstaller

      - name: Build EXE
        run: pyinstaller --onefile --windowed autoparts_demo.py

      - name: Upload EXE artifact
        uses: actions/upload-artifact@v3
        with:
          name: autoparts_software
          path: dist/autoparts_demo.exe
