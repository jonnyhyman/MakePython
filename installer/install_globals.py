"""
    Making a change? Here's the make-change checklist!
        1. Make change as needed
            1.1 make sure zip_nam matches zip_url and dl=1!!!!!!!!!!
            1.2 make sure the folder zipped has same name as zip_nam

        2. pyinstaller __make__.spec
        3. test locally
        4. test remotely / fresh install
"""

zip_nam = 'editor-0-8'
zip_url = "https://www.dropbox.com/s/9465wk6waif3ft9/editor-0-8.zip?dl=1"
pythonorg_root = "https://www.python.org/ftp/python/"
delete_log_after = False
pip_dependencies = {'PyQt5':'pyqt5'} # foldername / pypi name
