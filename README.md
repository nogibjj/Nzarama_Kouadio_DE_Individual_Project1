[![CI](https://github.com/nogibjj/Nzarama_Kouadio_DE_Individual_Project1/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Nzarama_Kouadio_DE_Individual_Project1/actions/workflows/cicd.yml)
## Individual Project 1: Continuous Integration Using Gitlab Actions of Python Data Science Project

## Structure 

```
Nzarama_Kouadio_DE_Individual_Project1/
├── .devcontainer/
│   ├── devcontainer.json
│   └── Dockerfile
├── .github/
│   └── workflows/
│       └── cicd.yml
├── dataset
│   └── police_killings_csv
├── mylib/
│   ├── __init__.py
│   └── lib.py
├── .gitignore
├── Dockerfile
├── LICENSE
├── main.ipynb
├── main.py
├── Makefile
├── README.md
├── repeat.sh
├── requirements.txt
├── setup.sh
├── test_lib.py
└── test_main.py

```

## Goal of the project

This project analyzes the data on police killings in the United States. It uses Python, Pandas, and Matplotlib to generate summary statistics (mean, median, standard deviation) and visualizations. It also contains a Jupyter Notebook with cells that perform descriptive statistics. Additionally, a CI/CD pipeline is set up using GitHub Actions, and a summary report in Markdown format is generated as part of the pipeline.

## Features
- Load and clean the dataset
- Generate summary statistics (mean, median, standard deviation, minimum, maximum)
- Create visualizations: histogram of killings by age and a pie chart by gender
- CI/CD pipeline with GitHub Actions
- Generate a Markdown summary report

## Set Up Instructions

1. Clone the repository using git clone 
2. Install the required packages through -r requirements.txt
3. Run the main.py script or the main.pipynb script to generate the report

## Video
The demo video linked below will explain how the project works. Click on the link or copy and paste to a browser: https://youtu.be/6PR0x8i2_j0
