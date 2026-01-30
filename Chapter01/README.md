
# Chapter 01 – Command Reference

This file contains **all command-line commands used in Chapter 01** of the book.  
It is designed for **reviewers and readers** to easily **copy, paste, and test** each step independently.

---

## System Update & Core Dependencies

```bash
sudo apt-get update
sudo apt-get install openssh-server fail2ban python3-pip python3-dev libxml2-dev libxslt1-dev zlib1g-dev libsasl2-dev libldap2-dev build-essential libssl-dev python2-dev libffi-dev libmysqlclient-dev libpq-dev libjpeg8-dev liblcms2-dev libblas-dev libatlas-base-dev git curl -y
```

---

## Install wkhtmltopdf

```bash
wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-2/wkhtmltox_0.12.6.1-2.jammy_amd64.deb
sudo dpkg -i wkhtmltox_0.12.6.1-2.jammy_amd64.deb
sudo apt-get install -f
```

---

## PostgreSQL Installation & Configuration

```bash
sudo apt install postgresql -y
sudo -u postgres createuser --superuser $(whoami)
sudo su postgres
psql
alter user user_name with password 'your_password';
\q
exit
```

---

## Git Configuration

```bash
git config --global user.name "Your Name"
git config --global user.email youremail@example.com
```

---

## Clone Odoo Source Code

```bash
mkdir ~/odoo-dev
cd ~/odoo-dev
git clone -b 19.0 --single-branch --depth 1 https://github.com/odoo/odoo.git
```

---

## Python Virtual Environment

```bash
python3 -m venv ~/venv-odoo-19.0
source ~/venv-odoo-19.0/bin/activate
```

---

## Install Python Requirements

```bash
cd ~/odoo-dev/odoo/
pip3 install -r requirements.txt
```

---

## Create Database & Start Odoo

```bash
createdb odoo-test
python3 odoo-bin -d odoo-test -i base --addons-path=addons --db-filter=odoo-test$
```

Alternative start:

```bash
./odoo-bin -d odoo-test -i base --addons-path=addons --db-filter=odoo-test$
```

---

## Optional: Node.js & RTL Support

```bash
sudo apt-get install nodejs npm -y
sudo npm install -g rtlcss
```

---

## Nginx Installation (Load Balancing)

```bash
sudo apt update
sudo apt install nginx
sudo systemctl enable nginx
sudo systemctl start nginx
```

Test and reload configuration:

```bash
sudo nginx -t
sudo systemctl reload nginx
```

---

## PostgreSQL Performance Tuning

```bash
sudo nano /etc/postgresql/*/main/postgresql.conf
sudo systemctl reload postgresql
sudo systemctl restart postgresql
sudo -u postgres psql
SHOW shared_buffers;
SHOW effective_cache_size;
SHOW work_mem;
```

---

## Odoo Configuration File

```bash
sudo nano /etc/odoo/odoo.conf
```

Generate config automatically:

```bash
./odoo-bin --save --config myodoo.cfg --stop-after-init
./odoo-bin --help | less
./odoo-bin -c myodoo.cfg
```

---

## Database Management via CLI

```bash
createdb testdb && odoo-bin -d testdb
createdb -T dbname newdbname
dropdb dbname
rm -rf ~/.local/share/Odoo/filestore/dbname
```

Backup & restore:

```bash
pg_dump -Fc -f dbname.dump dbname
tar cjf dbname.tgz dbname.dump ~/.local/share/Odoo/filestore/dbname
tar xf dbname.tgz
pg_restore -C -d dbname dbname.dump
```

---

## Debugging & Development

```bash
python3 odoo-bin --log-handler=odoo.addons.my_module:DEBUG
```

Python breakpoint:

```python
import pdb; pdb.set_trace()
```

