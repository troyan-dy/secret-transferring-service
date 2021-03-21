# secret transferring service
Service for transferring secrets over http on FastAPI

Ready for heroku


## Dependencies
- docker-compose
- python 3.9

## Commands
### Install
- `make install`

### Run tests
- `make test`
### Linting
- `make lint`

### Formatting
- `make format`

### Start in docker
- `make start`
- `make stop`


## Usage
### Create secret
- Curl
```bash
curl -X 'POST' \
  'http://0.0.0.0:5000/create_secret' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "expire": 10000,
  "message": "some message",
  "password": "01234"
}'
```
- Response body
```json
{
  "expire": 10000,
  "token": "116cf556-3d80-4e19-ba2c-5d6dd8008a00"
}
```
### Check secret
- Curl
```bash
curl -X 'POST' \
  'http://0.0.0.0:5000/check_secret/116cf556-3d80-4e19-ba2c-5d6dd8008a00' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "password": "01234"
}'
```

- Response body
```json
{
  "message": "some message",
  "success": true
}
```
