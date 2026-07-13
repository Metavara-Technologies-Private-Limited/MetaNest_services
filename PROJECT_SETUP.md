# Meta Nest Backend - Project Setup

## Prerequisites

- Python 3.14+
- PostgreSQL
- Git
- VS Code (Recommended)

---

## Clone the Repository

```bash
git clone <repository-url>
cd MetaNest_services
```

---

## Create Virtual Environment

```bash
python -m venv env
```

Activate:

### Windows

```bash
.\env\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Create .env

Create a `.env` file in the project root.

Example:

```env
SECRET_KEY=your-secret-key
DEBUG=True

DB_NAME=metanest_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

---

## Run Migrations

```bash
python manage.py migrate
```

---

## Create Superuser

```bash
python manage.py createsuperuser
```

---

## Run the Project

```bash
python manage.py runserver
```

Open:

http://127.0.0.1:8000/admin

---

## Git Workflow

Create a feature branch:

```bash
git checkout -b feature/branch_name
```

Push:

```bash
git push origin feature/branch_name
```

Raise a Pull Request to the `dev` branch.