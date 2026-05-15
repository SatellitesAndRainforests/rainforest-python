.PHONY: install test test-report docker-build docker-run docker-health docker-stop clean

APP_NAME=rainforest-python-front
IMAGE_NAME=rainforest-python-front:local
CONTAINER_NAME=rainforest-python-front-local
HOST_PORT=5001

install:
	python3 -m venv .venv
	. .venv/bin/activate && pip install -r requirements-test.txt

test:
	. .venv/bin/activate && pytest

test-report:
	mkdir -p build/test-results
	. .venv/bin/activate && pytest --junitxml=build/test-results/pytest.xml

docker-build:
	docker build -t $(IMAGE_NAME) .

docker-run:
	docker rm -f $(CONTAINER_NAME) || true
	docker run -d --name $(CONTAINER_NAME) -p $(HOST_PORT):5000 \
		-e GEOSERVER_PASSWORD=$$GEOSERVER_PASSWORD \
		$(IMAGE_NAME)

docker-health:
	curl --fail http://localhost:$(HOST_PORT)/health

docker-stop:
	docker rm -f $(CONTAINER_NAME) || true

clean:
	rm -rf .venv build .pytest_cache
	find . -type d -name "__pycache__" -prune -exec rm -rf {} +
	find . -name "*.pyc" -delete
