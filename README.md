# Backend User System (FastAPI)

A simple user management and authentication system built with FastAPI, SQLAlchemy, JWT, and Docker.

## Features

- User registration
- User listing
- Password hashing (bcrypt)
- JWT authentication
- Protected API endpoint
- Dockerized backend service

## Tech Stack

- FastAPI
- SQLAlchemy
- SQLite
- JWT (python-jose)
- Passlib (bcrypt)
- Docker

---

## Run with Docker

### 1. Build image
```bash
docker build -t user-api .
