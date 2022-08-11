export $(cat .env | xargs) && docker-compose -f docker-compose.yml build
docker-compose up
docker exec -it first-app_api_1 bash
alembic revision --autogenerate -m "some message"
alembic upgrade head