FROM python:3.13-rc-slim
WORKDIR /app
RUN pip install uv
COPY . .
CMD ["uv", "run", "app.py"]
EXPOSE 8002
