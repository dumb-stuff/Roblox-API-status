FROM python:3.12-rc-slim

WORKDIR /app

COPY . .

EXPOSE 80

RUN pip install .

CMD ["roblox-server-checker start localhost 80"]