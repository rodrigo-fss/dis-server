# Bcredi - Bank Statements Info Extraction

## How to Run Properly

This is a Python app for bancary statement info extraction.

[Docker](https://www.docker.com/) is required for all environments.

### Setup instructions:

1. Clone this repository (you need [git](https://git-scm.com/) installed):
  
    `git clone git@github.com:bcredi/bcredi-img-rec.git`

### Running:

1. Run the bash script:
   
   *If running in local or staging:*
    
        docker-compose up

2. Access `http://0.0.0.0:5000/` and use the form to convert a bank statement to a csv

### How it's Architectured:
    
1. Flask handle the web part os the application, manananging routes and functions related to
each one of the pages
2. The user input receives a pdf file and a bank option that is related to a bank templante
3. Bank templates handle each of the steps between the raw pdf and the converted csv passing
information through module functions
4. Specific transformation related to a bank are in the `bank_template` folder, the `common_template`
folder stores the functions that are used in more than one bank
5. The ideia is to make code reusable (modules) and readable (templates) 

### Testing

To trigger the automated tests you should get into the container 
`docker exec -it bcredi-doc-extraction /bin/sh` 
and run pytest inside test folder
`cd test;pytest`

the test folder also holds the `test/acc_test.py` file that could be debbuged if its the case
