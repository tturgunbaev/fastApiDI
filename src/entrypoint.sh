#!/bin/sh

echo "Migrate the Database at startup of project"
alembic upgrade head


echo "Running uvicorn"
uvicorn main:app --host 0.0.0.0 --port 5000
