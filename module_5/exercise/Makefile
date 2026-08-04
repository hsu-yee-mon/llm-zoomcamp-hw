run:
	pipenv run python assistant.py
chat:
	pipenv run streamlit run app.py
network:
	docker network create monitoring
postgres: network
	docker run -it \
		--name course-assistant-pg \
		--network monitoring \
		-e POSTGRES_USER=user \
		-e POSTGRES_PASSWORD=password \
		-e POSTGRES_DB=course_assistant \
		-p 5432:5432 \
		-v pgdata:/var/lib/postgresql/data \
		postgres:17
dashboard:
	pipenv run streamlit run dashboard.py --server.port 8502
synth_data:
	pipenv run python generate_data.py