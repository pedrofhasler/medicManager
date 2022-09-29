# MedicManager

An application to help with physician management.

## Installation

- Clone the repository and install the requirements

  ```Terminal
  git clone https://github.com/corteisjr/MedicSearch
  cd medicManager
  pip install -r requirements.txt
  ```

- Activate your virtual environment on Unix.

```Terminal
    python3 -m venv venv
    source venv/bin/activate
```

- Activate your virtual environment on Windows

```Terminal
    python -m venv venv
    venv/Scripts/activate
```

- Migrate and run the server

```Terminal
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
```
