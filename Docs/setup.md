# PromptWatch - Development Setup

This document tracks the software, dependencies, and setup process used to build PromptWatch.

---

# Development Environment

## Operating System

- Windows 11
- Git Bash (MINGW64)

## IDE

- Visual Studio Code

## Version Control

- Git

---

# Project Structure

```text
PROMPTWATCH/
│
├── backend/
├── frontend/
├── docs/
├── .gitignore
└── README.md
```

---

# Frontend Setup

## Framework

- React
- TypeScript
- Vite

## Create Project

```bash
npm create vite@latest frontend -- --template react-ts
```

## Install Dependencies

```bash
cd frontend
npm install
```

## Run Development Server

```bash
npm run dev
```

Default URL:

```
http://localhost:5173
```

---

# Backend Setup

## Create Virtual Environment

```bash
cd backend
python -m venv .venv
```

## Activate Virtual Environment

### Git Bash

```bash
source .venv/Scripts/activate
```

### PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

---

## Install Dependencies

```bash
pip install fastapi uvicorn
```

## Save Dependencies

```bash
pip freeze > requirements.txt
```

## Run FastAPI

```bash
uvicorn main:app --reload
```

Default URL

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

# Python Packages

| Package | Purpose                 |
| ------- | ----------------------- |
| FastAPI | REST API Framework      |
| Uvicorn | ASGI Development Server |

---

# Node Packages

| Package    | Purpose        |
| ---------- | -------------- |
| React      | User Interface |
| TypeScript | Type Safety    |
| Vite       | Build Tool     |
| ESLint     | Code Quality   |

---

# Decisions Made

- Chose FastAPI for the backend.
- Chose React + Vite for the frontend.
- Separated frontend and backend into independent applications.
- Using SQLite during development.
- Planning to use a layered detection engine for prompt analysis.

---

# Future Dependencies

## Backend

- SQLAlchemy
- Pydantic
- Alembic
- pytest
- httpx
- python-dotenv

## Frontend

- Tailwind CSS
- Axios
- React Router
- TanStack Query
- Recharts

---

# Setup Checklist

- [x] Create Git repository
- [x] Create frontend
- [x] Create backend
- [x] Install React
- [x] Install FastAPI
- [ ] Connect frontend to backend
- [ ] Build first API endpoint
- [ ] Build prompt analyzer
- [ ] Create dashboard
- [ ] Deploy application

---

Last Updated

2026-07-30
