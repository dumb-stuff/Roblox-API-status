FROM python:3.11-rc-slim

WORKDIR /app

COPY . .

EXPOSE 80

RUN pip install .

CMD ["roblox-server-checker start localhost 80"]