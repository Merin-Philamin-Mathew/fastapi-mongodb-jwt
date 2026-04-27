# FastAPI MongoDB Authentication API

A FastAPI-based REST API with JWT authentication, MongoDB integration, and user management.

## Features

- **User Authentication** — Register and login with JWT tokens
- **JWT Security** — RSA-based token generation and validation
- **MongoDB Integration** — User data persistence with MongoDB
- **CORS Support** — Configurable cross-origin requests
- **Password Security** — Bcrypt hashing for secure password storage
- **Email Verification** — User account verification support

## Project Structure

```
fastapi_mongodb/
├── app/
│   ├── routers/
│   │   ├── auth.py          # Authentication endpoints
│   │   └── user.py          # User management endpoints
│   ├── serializers/
│   │   └── userSerializers.py  # MongoDB response serialization
│   ├── __init__.py
│   ├── config.py            # Settings management
│   ├── database.py          # MongoDB connection
│   ├── main.py              # FastAPI application
│   ├── oauth2.py            # JWT configuration & validation
│   ├── schemas.py           # Pydantic models
│   └── utils.py             # Helper functions
├── docker-compose.yml       # MongoDB setup
├── verify_keys.py           # JWT key verification script
├── requirements.txt         # Python dependencies
└── .env                      # Environment variables (not in repo)
```

## Prerequisites

- Python 3.8+
- MongoDB 5.0+
- pip

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd fastapi_mongodb
   ```

2. **Create virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up MongoDB**
   ```bash
   docker-compose up -d
   ```

5. **Configure environment variables**
   Create a `.env` file in the project root:
   ```
   DATABASE_URL=mongodb://username:password@localhost:27017/
   MONGO_INITDB_ROOT_USERNAME=admin
   MONGO_INITDB_ROOT_PASSWORD=password
   MONGO_INITDB_DATABASE=fastapi_db
   JWT_PUBLIC_KEY=<base64-encoded-public-key>
   JWT_PRIVATE_KEY=<base64-encoded-private-key>
   REFRESH_TOKEN_EXPIRES_IN=60
   ACCESS_TOKEN_EXPIRES_IN=900
   JWT_ALGORITHM=RS256
   CLIENT_ORIGIN=http://localhost:3000
   ```

6. **Generate JWT Keys** (first time setup)
   ```bash
   python verify_keys.py
   ```

## Running the Application

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## API Endpoints

### Authentication
- `POST /api/auth/register` — Register a new user
- `POST /api/auth/login` — Login and get JWT tokens
- `POST /api/auth/logout` — Logout

### Users
- `GET /api/users/me` — Get current user profile
- `PUT /api/users/{user_id}` — Update user information

### Health
- `GET /api/healthchecker` — Health check endpoint

## Environment Variables

| Variable | Description |
|----------|-------------|
| `DATABASE_URL` | MongoDB connection string |
| `JWT_PUBLIC_KEY` | Base64-encoded RSA public key |
| `JWT_PRIVATE_KEY` | Base64-encoded RSA private key |
| `ACCESS_TOKEN_EXPIRES_IN` | Access token expiration (seconds) |
| `REFRESH_TOKEN_EXPIRES_IN` | Refresh token expiration (seconds) |
| `CLIENT_ORIGIN` | Allowed frontend URL |

## Key Files

- **config.py** — Loads environment variables
- **database.py** — MongoDB connection setup
- **oauth2.py** — JWT authentication configuration and validation
- **schemas.py** — Pydantic models for request/response validation
- **utils.py** — Password hashing and verification utilities

## Development

### Docker Compose MongoDB Setup

Start MongoDB:
```bash
docker-compose up -d
```

Stop MongoDB:
```bash
docker-compose down
```

View Docker setup documentation: [docker_mongodb_setup.md](notes/docker/docker_mongodb_setup.md)

## License

MIT
