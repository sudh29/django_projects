.PHONY: test lint clean help

help:
	@echo "Available commands:"
	@echo "  make test   - Run test suites across all 6 Django projects"
	@echo "  make lint   - Run Ruff linter across the repository"
	@echo "  make clean  - Clean python bytecode and test databases"

test:
	@echo "=== Testing project1 ==="
	cd project1 && uv run python manage.py test
	@echo "=== Testing project2 ==="
	cd project2 && uv run python manage.py test
	@echo "=== Testing project3 ==="
	cd project3 && uv run python manage.py test
	@echo "=== Testing project4 ==="
	cd project4 && uv run python manage.py test
	@echo "=== Testing project5 ==="
	cd project5 && uv run python manage.py test
	@echo "=== Testing project6 ==="
	cd project6 && uv run python manage.py test

lint:
	uv run ruff check .

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.sqlite3" -delete

