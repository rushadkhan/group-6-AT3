# group-6-AT3

Repo File structure
rushadkhan/group-6-AT3│
│
├── app/
│   └── streamlit_app.py         <- main script for displaying the application in Docker
│
│
├── src/
│   ├── test
│   │   ├── test_data.py         <- this is a python script for testing code from data.py
│   │   ├── test_numeric.py      <- this is a python script for testing code from numeric.py
│   │   └── test_text.py         <- this is a python script for testing code from text.py
│   │
│   ├── __init__.py              <- this turns ‘src folder’ into a package for importing in main script
│   ├── data.py                  <- this contains the code for displaying the Overall information section
│   ├── numeric.py               <- this contains the code for displaying the Information of numeric columns section
│   └── text.py                  <- this contains the code for displaying the Information of text columns section
│   
├── Dockerfile                   <- this is a file that is used to build the Docker image
├── docker-compose.yml           <- 
├── requirements.txt             <- this lists the packages imported by the python scripts
└── README.md                    <- a markdown file 
