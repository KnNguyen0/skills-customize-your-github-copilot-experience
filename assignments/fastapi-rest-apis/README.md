# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a REST API using the FastAPI framework, define routes and data models, and validate request data with Pydantic.

## 📝 Tasks

### 🛠️ Create API Endpoints

#### Description
Build a FastAPI app with routes to manage a simple item resource and return JSON responses.

#### Requirements
Completed program should:

- Define a FastAPI application in `starter-code.py`.
- Create at least two routes: `GET /items/{item_id}` and `POST /items`.
- Return JSON responses with item data and appropriate status codes.
- Use path or query parameters for item lookup.

### 🛠️ Add Validation and Documentation

#### Description
Use Pydantic models to validate request data and make sure the API exposes interactive documentation.

#### Requirements
Completed program should:

- Define Pydantic models for item creation and response schemas.
- Validate incoming POST request data and return errors for invalid input.
- Include example request shapes in comments or README notes.
- Confirm the API docs are available at `/docs` when the app is running.
