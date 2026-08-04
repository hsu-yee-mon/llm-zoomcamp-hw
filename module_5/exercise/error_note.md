- docker file fix ==> as I am not using uv and use pipenv instead , need to change it in docker file
- docker compose work with `docker compose up`
- db initiation error after docker compose 
    ```
    pipenv run python db_init.py
Using timezone: +07
Traceback (most recent call last):
  File "/home/hsu/Documents/Learning/llm-zoomcamp-hw/module_5/db_init.py", line 69, in <module>
    init_db()
  File "/home/hsu/Documents/Learning/llm-zoomcamp-hw/module_5/db_init.py", line 20, in init_db
    conn = get_db_connection()
  File "/home/hsu/Documents/Learning/llm-zoomcamp-hw/module_5/db_init.py", line 12, in get_db_connection
    return psycopg.connect(
  File "/home/hsu/.local/share/virtualenvs/module_5-K8z_S0bj/lib/python3.10/site-packages/psycopg/connection.py", line 100, in connect
    attempts = conninfo_attempts(params)
  File "/home/hsu/.local/share/virtualenvs/module_5-K8z_S0bj/lib/python3.10/site-packages/psycopg/_conninfo_attempts.py", line 55, in conninfo_attempts
    raise last_exc
    ```
    - Solution `docker compose exec streamlit python db_init.p`
        - we need to run it inside docker

        