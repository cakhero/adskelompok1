run-db:
	docker run --name psql -p 5432:5432 -e POSTGRES_PASSWORD=adminpassword -e POSTGRES_DB=project -v ${PWD}/db_data:/var/lib/posgtresql/data -d postgres