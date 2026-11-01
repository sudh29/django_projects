# AGENTS.md — Universal Agent Operating Standard: django_projects

> **Repository:** `/home/liberprimus/code/django_projects`  
> **Workspace Authority:** `sudh29` (`liberprimus`)  
> **Tier:** Tier C (Enterprise Relational Backend Architectures & REST Framework)  
> **Active Branch:** `main`  
> **Applicable Agents:** Antigravity, Claude Code, Cursor, Gemini, Codex


---

## 1. Repository Purpose & Architecture

- **Overview:** `django_projects` houses robust enterprise backend architectures implemented with Django 5.2 and Django REST Framework (DRF 3.16). It includes relational data modeling, migrations, SimpleJWT token authentication, CORS configuration, Celery task queues, and REST API endpoints.
- **Key Directory Map:**
  - Django project apps containing `models.py`, `views.py`, `serializers.py`, `urls.py`, and `migrations/`.
  - `manage.py`: Django management runner.
  - `pyproject.toml`: Environment and dependency configurations via `uv`.
- **Architectural Invariants:**
  - **Migration Integrity:** Every modification to `models.py` must be accompanied by generated migrations (`python manage.py makemigrations`). Never edit existing applied migrations in destructive ways.
  - **Serialization Strictness:** DRF serializers must explicitly declare fields (`fields = [...]`); avoid unrestricted `fields = '__all__'`.
  - **Security Baseline:** Ensure `DEBUG = False` and proper `ALLOWED_HOSTS` in production configurations.

### Key Architecture & Entry Points

- **Management Runner:** [`manage.py`](file:///home/liberprimus/code/django_projects/manage.py)
- **Manifest:** [`pyproject.toml`](file:///home/liberprimus/code/django_projects/pyproject.toml)
- **Django Apps:** Contains models, views, serializers, URLs

---

## 2. Coding Style & Engineering Conventions

- Follow Django conventions (Model-View-Template / Serializer-View-Router).
- Explicit `fields = [...]` in DRF serializers.
- Ensure all model mutations produce migrations before committing.

---

## 3. Toolchain & Environment Matrix

- **Runtime:** Python 3.12+
- **Framework:** Django 5.2, DRF 3.16
- **Package Manager:** **`uv`** (`/home/liberprimus/.local/bin/uv` or subproject `.venv`)

### Canonical Commands
All commands run from `/home/liberprimus/code/django_projects`:

| Action | Command | Purpose |
|:---|:---|:---|
| **Dev Server** | `uv run python manage.py runserver` | Start local Django development server |
| **System Check** | `uv run python manage.py check` | Run Django system consistency checks |
| **Run Tests** | `uv run python manage.py test` | Execute Django test suite |
| **Make Migrations** | `uv run python manage.py makemigrations` | Generate model migration scripts |
| **Apply Migrations**| `uv run python manage.py migrate` | Apply database migrations |
| **Lint Code** | `uv run ruff check .` | Fast static analysis via Ruff |
| **Format Code** | `uv run ruff format .` | Auto-format Python code |

### Quick-Start Workflow

```bash
# Server & Migrations
uv run python manage.py runserver       # Run local development server
uv run python manage.py check           # Validate Django setup
uv run python manage.py makemigrations  # Generate migrations
uv run python manage.py migrate         # Apply migrations

# Testing & Quality
uv run python manage.py test            # Run Django test suite
uv run ruff check .                     # Lint check
uv run ruff format .                    # Format code
```

---

## 4. Operational Safety & Agent Boundaries

1. **Blast Radius Containment:** Confine all changes strictly to `/home/liberprimus/code/django_projects`.
2. **Verification Mandate:** Always run `uv run python manage.py check && uv run python manage.py test` before concluding tasks.
3. **Branch Discipline:** Active working branch is `main`.
4. **Secret Hygiene:** Never commit `SECRET_KEY`, database credentials, or `.env` files.

---

## 5. Definition of Done
- [ ] Django system checks pass (`manage.py check`).
- [ ] All unit and view tests pass (`manage.py test`).
- [ ] Model changes have clean migrations.
- [ ] Working tree is clean.
