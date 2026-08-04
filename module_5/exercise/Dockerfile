FROM python:3.10-slim

WORKDIR /app

COPY Pipfile Pipfile.lock ./

RUN pip install --no-cache-dir pipenv \
    && pipenv install --system --deploy

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

# FROM python:3.12-slim

# # COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# WORKDIR /app
# ENV PATH="/app/.venv/bin:$PATH"

# # COPY pyproject.toml uv.lock .python-version ./
# # RUN uv sync --locked

# COPY Pipfile Pipfile.lock ./
# RUN pip install pipenv \
#     && pipenv install --system --deploy

# COPY . .

# CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]