# Example of using RQ with FastAPI
## Setup
```shell
docker-compose up -d
```

## Usage
Start task:

```shell
curl http://localhost/task/50
["Job ID: 626ff552-3045-409d-ac87-c37801157831"]%
```

Get status of job:

```shell
curl http://localhost/job/626ff552-3045-409d-ac87-c37801157831
{"Status":"started"}% 
```

```shell
curl http://localhost/job/626ff552-3045-409d-ac87-c37801157831
{"Status":"finished"}% 
```

## Clean up
```shell
docker-compose down
```