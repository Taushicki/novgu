#1) start compose: 
$env:DB_HOST="db" 
$env:DB_USER="root"
$env:DB_PASSWORD="rootpassword"
$env:DB_NAME="testdb"
docker-compose up --build