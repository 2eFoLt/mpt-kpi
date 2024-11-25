# Проект "Система KPI"
Электронная система KPI, проект студентов Московского Политехнического Университета
## Основные ссылки
[Гайд для участников проекта](https://github.com/2eFoLt/mpt-kpi/blob/main/CONTRIBUTING.md)

## Начало работы
### Весь проект 
```bash
docker volume create mpt-kpi-database
docker compose -f docker-compose.dev.yml up
```

### Запуск front-end контейнеров
```bash
rm -r frontend/node_modules/
docker compose -f docker-compose.dev.yml down
git checkout -- frontend/package-lock.json
docker compose -f docker-compose.dev.yml run --rm frontend npm install
docker compose -f docker-compose.dev.yml build frontend
```

### Остановить проект

```bash
docker compose -f docker-compose.dev.yml down
```

### Очистка старых образов Docker

```bash
docker image prune
docker rmi $(docker images -f "dangling=true" -q) --force
docker system prune -f
```

### Windows troubleshooting
```
Enable File-Sharing in Docker Desktop App
```

