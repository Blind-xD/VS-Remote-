# Hello Python + Docker

Mini ukázka pro začátek s VS Code, Git, Python a Dockerem.

## 1) Spuštění v Pythonu (lokálně)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Pak otevři: http://localhost:8000

Health check: http://localhost:8000/health

## 2) Spuštění v Dockeru

```bash
docker build -t hello-python-docker .
docker run --rm -p 8000:8000 hello-python-docker
```

Pak otevři: http://localhost:8000

## 3) Git základy

```bash
git init
git add .
git commit -m "Prvni verze hello app"
```

## 4) Spuštění přes Docker Compose

```bash
docker compose up --build
```

Pak otevři: http://localhost:8000

Zastavení:

```bash
docker compose down
```

## 5) Jak pokračovat po každé změně

```bash
git add .
git commit -m "Popis zmeny"
git push
```

Rychlá kontrola stavu:

```bash
git status
```
