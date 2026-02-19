# AI Architect Lab – Backend Foundations

## About This Project

This repository documents my journey to becoming an AI Solutions Architect.
The focus of this module is backend development fundamentals using Python.

## Objectives

- Understand virtual environments
- Build and execute Python scripts
- Prepare for API development
- Document projects professionally

## Tech Stack

- Python 3.x
- Virtual Environment (venv)
- Windows OS

## How to Run

1. Activate the virtual environment:
   venv\Scripts\activate

2. Run the server:
   uvicorn app.main:app --reload

3. Open in browser:
   http://127.0.0.1:8000

4. Interactive API documentation:
   http://127.0.0.1:8000/docs

## Learning Progress

- [x] Virtual environment created
- [x] First Python script executed
- [ ] API development with FastAPI
- [ ] AI integration

## Milestone 1 - First API Deployment (Local)

- Installed FastAPI and Uvicorn 
- Built first API endopoint 
- Succesfully launched local server 
- Verified automatic documentation at  /docs 

## API Endpoints

### GET /
Returns a confirmation message that the API is running. 

### POST /agent 
Simulates a basic AI agent interaction for client inquiries. 

## Project Structure

backend-basics/
│
├── app/
│   ├── main.py
│   ├── routes/
│   │   └── agent.py
│   └── models/
│       └── schemas.py
│
├── requirements.txt
├── README.md
└── .gitignore