### Актуализация модулей с помощью [pip-tools](https://pypi.org/project/pip-tools/)
```bash
docker compose -f docker-compose.dev.yml run --rm backend bash
pip-compile -vv requirements.in
pip-compile -vv requirements.dev.in
```

### Обновление модулей (может поломать совместимость)
```bash
docker compose -f docker-compose.dev.yml run --rm backend bash
pip-compile -vv --upgrade requirements.in
pip-compile -vv --upgrade requirements-dev.in
```
