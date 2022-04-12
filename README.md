# Example of using RQ with FastAPI
## Setup
```shell
docker-compose up -d
```

## Usage
Start task:

```shell
curl http://localhost/task/50
```
```json
{"job_id": "790c20fa-773c-4e89-9e3d-b5527fb90494"}
```

Get status of job:

```shell
curl http://localhost/job/626ff552-3045-409d-ac87-c37801157831
```
```json
{"status": "started"}
```

```shell
curl http://localhost/job/626ff552-3045-409d-ac87-c37801157831
```
```json
{"status": "finished"}
```

## Clean up
```shell
docker-compose down
```
