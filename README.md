![Vue.js](https://img.shields.io/badge/vuejs-%2335495e.svg?style=for-the-badge&logo=vuedotjs&logoColor=%234FC08D)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![MySQL](https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
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

