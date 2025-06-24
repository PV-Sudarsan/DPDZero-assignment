FROM python:3.13-rc-slim
WORKDIR /app
RUN pip install uv
COPY . .
EXPOSE 8002
CMD ["uv", "run", "app.py"]