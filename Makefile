RUN_TEST_COMMAND=PYTHONPATH=".:tests:${PYTHONPATH}" django-admin test --settings=settings
RUN_SERVER_COMMAND=PYTHONPATH=".:tests:${PYTHONPATH}" python tests/manage.py runserver

.DEFAULT_GOAL := help

help:
	@grep '^[a-zA-Z]' $(MAKEFILE_LIST) | sort | awk -F ':.*?## ' 'NF==2 {printf "\033[36m  %-25s\033[0m %s\n", $$1, $$2}'

test: ## run tests quickly with the default Python
	$(RUN_TEST_COMMAND)

run: ## run test server with the default Python
	$(RUN_SERVER_COMMAND)