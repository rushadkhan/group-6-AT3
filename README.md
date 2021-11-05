This project involved creating an app in streamlit which enables a user to upload any csv file and access key information around the data it contains. It is designed to be run in a docker container so that it can be used on any operating system without needing to download Python or any specific pacakges.

To use the app download the contents of the repo and build the docker image using the command 'docker build -t data_explorer_app .’ in your command line, once built you can run the container using ‘docker run -it --rm --name data_explorer -p 8501:8501 -v “${PWD}”/App data_explorer_app’. The streamlit app can then be launched via your browser.

An overview of the file structure for the app is shown below.

![image](https://user-images.githubusercontent.com/72027589/140463997-1b2b250d-de92-4d12-8a01-eec670fdc264.png)
