#!/bin/bash

alembic revision --autogenerate
alembic upgrade head

uvicorn src.main:app --host 0.0.0.0 --port 9000