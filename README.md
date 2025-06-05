# Cookie Cutter Django Template - With Authentication
A basic Django 5.0 starter project w/ Oauth piece derived from: https://github.com/mdrhmn/dj-social-auth

## Project Setup
1. Go to https://www.python.org/downloads/release/python-3116/ and downloaded Python 3.11.6.
2. Once downloaded and installed, navigate to your projects directory then create a virtual environment. EX:
  ```shell
  python3 -m venv env
  ```
3. In terminal, disable the pycaches.
  ```shell
  export PYTHONDONTWRITEBYTECODE=1
  ```
4. Update your package repos before proceeding.
  - For CentOS, run `sudo yum update`
  - For most other linux, run `sudo apt-get update`
  - For MacOS, run  `brew update`)
5. Install MariaDB.
  - For CentOS, run `sudo yum install mariadb mariadb-server gcc mysql-devel`
  - For most other linux, run `sudo apt-get install mariadb-server`
  - For MacOS, run  `brew install mariadb` (and maybe also `brew install mysql mysql-client`)
6. ENSURE they were installed by checking the versions AND the version is greater than v10.5.
  ```shell
  mysql --version
  #mariadb --version
  ```
  <details>
    <summary><b>Is your maximum version for MariaDB (not mysql) below v10.5?</b><i> (click to expand)</i></summary>
      ```
      curl -LsS -O https://downloads.mariadb.com/MariaDB/mariadb_repo_setupsudo
      bash mariadb_repo_setup --mariadb-server-version=11.4.4

      #Confirm the repository is working by updatingcache.
      sudo yum makecache -y

      #List available repositories:
      sudo yum repolist

      # Now uninstall old version and install new one:
      sudo yum remove mariadb mariadb-server mysql-devel -y
      sudo yum install mariadb mariadb-server mysql-devel -y
      ```
  </details>
7. Launch the mysql services and enable it so it auto-starts on server restarts and network interruptions.
  - For **Linux**:
    ```shell
    sudo systemctl start mariadb
    sudo systemctl status mariadb
    sudo systemctl enable mariadb
    ````
  - For **MacOS**:
    ```shell
    brew services start mariadb
    brew services info mariadb
    # Don't think you want to run it on MAC every startup
    ````
    <details>
      <summary><b>Services or Systemctl command not exist?</b><i> (click to expand)</i></summary>
        Make sure systemctl on Linux (or launchctl on Mac) is installed to be able to run mysql ascynronously with your Django app at all times.
          - Check with `sudo systemctl list` (for Linux) and `brew services list` (for Mac) to check to see if it's installed
          - **If not installed**, for CentOS do `sudo yum install systemd`, for most other Linux, do `sudo apt-get install systemd`, MacOS should have services already installed.
    </details>

8. Check that you can launch mariaDB: (if it asks for your password, you are using your computer/box's password, NOT the database password)
  ```
  sudo mysql
  ```
  then do `exit` to leave it
9. Add MAYBE add mysql flags (forget if it's needed for python package install of the mysql package next step)
  - For **Linux**:
    ```shell
    export MYSQLCLIENT_CFLAGS='pkg-config mysqlclient --cflags'
    export MYSQLCLIENT_LDFLAGS='pkg-config mysqlclient --libs'
    ```
  - For **MacOS**
    ```shell
    export LDFLAGS="-L/usr/local/lib -L/usr/local/opt/openssl/lib"
    export CPPFLAGS="-I/usr/local/include -I/usr/local/opt/openssl/include"
    ```
10. Install required packages by doing the following:
```shell
 source env/bin/activate
 pip3 install -r requirements.txt
```

11. Create the initial database then log in to it using the **database password**:
  ```mysql
  sudo mysql
  CREATE DATABASE djangodb CHARACTER SET UTF8;
  use djangodb;
  CREATE USER admin2@localhost IDENTIFIED BY 'password1234';
  GRANT ALL PRIVILEGES ON djangodb.* TO admin2@localhost;
  exit
  ```

12. Create Superuser when developing.
```shell
cd app
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
```

## Routine
### for Dev
1. Runserver by doing the following.
```shell
 cd app  #if not already in that directory
 python3 manage.py makemigrations
 #python3 manage.py makemigrations --name changed_my_model backend
 python3 manage.py migrate
 python3 manage.py runserver
```
2. Navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000) to test

### for PROD
1. SSH to Product:
```shell
ssh -i ~/Documents/certificates/aws-cert.pem ec2-user@ec2-12-345-12-34.compute-1.amazonaws.com
```
2. Pull latest
```
cd /{PROJECT_DIRECTORY}
git pull
```
3. Runserver by doing the following.
```shell
 sudo systemctl start mariadb # If you haven't enabled it yet
 cd app
 python3 manage.py makemigrations
 #python3 manage.py makemigrations --name changed_my_model backend
 python3 manage.py migrate
 gunicorn --bind 0.0.0.0:8000 config.wsgi:application
 # Once you confirm it all looks good then do:
 nohup gunicorn --bind 0.0.0.0:8000 config.wsgi:application &
```

## Prod Setup
Must do everything found in "Project Setup" then the following as well.

### Setup a Cert for authenticating with Github (If Github project is Private)
1. Find your "noreply" [email on Github](https://github.com/settings/emails). It should look like: ex. `7654321+tomfried@users.noreply.github.com`
2. On your terminal/PuTTy window on your EC2 instance, create new public/private key pair USING your noreply like so:
```shell
cd ~/.ssh
ssh-keygen -t rsa -b 4096 -C "7654321+tomfried@users.noreply.github.com"
```
3. For a name enter ex: `git_rsa` then enter password when it prompts you.
4. Once command finishes, open up the public (`.pub`) file by doing the following:
```
less git_rsa.pub
```
5. Copy the text from that file and paste it in a new [Github SSH key](https://github.com/settings/keys). Git clone should now work because your box's private key matches the public on Github.

**IF git clones don't work,**, try:
```shell
eval `ssh-agent -s`
ssh-add ~/.ssh/git_rsa
# Enter password
```

### Setup Project on AWS EC2 with HTTP
1. Install and setup Git (to pull in the project)
```shell
sudo yum update
sudo yum install git -y
git version
mkdir git-repos
cd git-repos
git init
```
2. Clone and pull the project (example but pull your project)
```shell
git clone git@{PROJECT_URL}
sudo yum install python-pip -y
pip install -r requirements.txt
cd app
gunicorn --bind 0.0.0.0:8000 config.wsgi:application
```
3. Add Inbounding rule on AWS for port 8000 to enable HTTP. ([pictures explaining how to do it](https://stackoverflow.com/questions/34577076/access-django-app-on-aws-ec2-host))
4. Visit your public IP Address at port 8000, ex: `http://34.123.45.67:8000/`

### Setup for HTTPS
Ultimate Cert Guide: [Digital Ocean - OpenSSL Essentials](https://www.digitalocean.com/community/tutorials/openssl-essentials-working-with-ssl-certificates-private-keys-and-csrs).
1. Setup NGINX and httpd.
```shell
sudo yum install httpd nginx -y
sudo systemctl start httpd
sudo systemctl enable httpd
sudo mkdir /etc/pki/nginx
sudo chmod 755 /etc/pki/nginx
sudo cp ~/git-repos/cookie-cutter-django/app/nginx.conf /etc/nginx
sudo systemctl status nginx
```
2. Generate a KEY and CSR for HTTPS.
```shell
sudo openssl req -newkey rsa:2048 -nodes -keyout /etc/pki/tls/private/examplecompany.key -out /etc/pki/tls/certs/examplecompany.csr
```
Enter the following (example):
```text
Country Name (2 letter code) [XX]:US
State or Province Name (full name) []:Tennessee
Locality Name (eg, city) [Default City]:Knoxville
Organization Name (eg, company) [Default Company Ltd]:Example Company, Inc.
Organizational Unit Name (eg, section) []:.
Common Name (eg, your name or your server's hostname) []:examplecompany.org
Email Address []:examplecompany@gmail.com

Enter Challenge Password (20 characters max): ************
Enter Company Name again: Example Comnpany, Inc.
```
3. Generated a temporary signed CERT from that KEY AND CSR (Needed for CA to validate)
```shell
sudo openssl x509 -signkey /etc/pki/tls/private/examplecompany.key -in /etc/pki/tls/certs/examplecompany.csr -req -days 365 -out /etc/pki/tls/certs/examplecompany.crt
```
4. Copy certs to Nginx file
```shell
sudo cp /etc/pki/tls/certs/examplecompany.crt /etc/pki/nginx/server.crt
sudo cp /etc/pki/tls/private/examplecompany.key /etc/pki/nginx/server.key
```
5. Replace self-signed cert with an officially signed cert.
```shell
sudo yum install certbot python3-certbot-nginx -y
sudo certbot --nginx -d examplecompany.org
```
https://letsencrypt.org/how-it-works/

https://docs.aws.amazon.com/cloudhsm/latest/userguide/ssl-offload-configure-web-server.html

gunicorn -c gunicorn.py config.wsgi

https://localhost:8443
