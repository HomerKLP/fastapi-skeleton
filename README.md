# FastAPI Skeleton

> Base template for FastAPI projects

## Project Requirements:

| Requirement | Description |
| --- | ----------- |
| PROD | |
| Gunicorn | Production deployment |
| Uvicorn | Local development |
| Tortoise-orm | Async ORM |
| Aerich | Migration tool |
| Python-dotenv | Environment vars |
| DEV | |
| Pytest-asyncio | Testing Framework |
| Flake8 | Static Linter |
| Invoke | Command execution tool |
| Black | Code formatter |

### Local deploy:

```bash
 $ docker-compose up -d
 ```

### Run tests:

```bash
$ docker-compose exec fastapi bash
$ inv test

-- or --
 
$ docker-compose exec fastapi inv test


-- to run certain test --

$ pytest -vsk test_example
```
