# clo835-project-app

Some test scripts

## Test Docker Images Locally
### Login to ECR 
```
export ECR=[youracounturl]/project-ecr
```
```
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin [youraccounturl]
```
### Build Images
```
docker build -t $ECR:db-v1 -f Dockerfile_mysql .
```
```
docker build -t $ECR:app-v1 -f Dockerfile .
```
### Export Variables
```
export DBPORT=3306 && export DBHOST=172.17.0.2 && export DBUSER=root && export DBPWD=something && export DATABASE=employees && export DBNAME=employees
```
### Run Containers
```
docker run -d --name db -e MYSQL_ROOT_PASSWORD=something $ECR:db-v1
```
```
docker run -d --name app -p 81:81 -e DBHOST=$DBHOST -e DBPORT=$DBPORT -e DBUSER=$DBUSER -e DBPWD=$DBPWD $ECR:app-v1
```
```
docker logs app
```
### Check connectivity
```
curl localhost:81
```
### Push Images to Repo (Optional for testing)
```
docker push $ECR:db-v1
```
```
docker push $ECR:app-v1
```
### Remove Images and Containers
```
docker rm -vf $(docker ps -aq) && docker rmi -f $(docker images -aq)
```
