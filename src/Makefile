run-db:
	docker run --name db-focorecs -p 5432:5432 -e POSTGRES_PASSWORD=adminpassword -e POSTGRES_DB=project -v ${PWD}/db_data:/var/lib/posgtresql/data -d postgres

reset-db:
	docker stop db-focorecs
	docker rm db-focorecs
	sudo rm -rf db_data
	mkdir db_data
	rm -rf alembic/versions/*
	docker run --name db-focorecs -p 5432:5432 -e POSTGRES_PASSWORD=adminpassword -e POSTGRES_DB=project -v ${PWD}/db_data:/var/lib/posgtresql/data -d postgres

start-db:
	docker start db-focorecs

stop-db:
	docker stop db-focorecs