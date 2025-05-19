.PHONY: help
help:
	@echo "Available commands: "
	@echo "make dev       Run FastAPI in development mode"

.PHONY: dev
dev:
	 fastapi dev app/main.py
