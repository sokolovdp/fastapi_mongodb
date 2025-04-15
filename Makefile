APPS:=./APPS
TESTS:=./tests

.PHONY: pretty lint # test

pretty:
	black $(APPS)
	isort $(APPS)

lint:
	black $(APPS) --check
	isort $(APPS) --check-only
	ruff check $(APPS)

test:
	pytest $(TESTS) -v -rA
