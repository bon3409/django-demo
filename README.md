# Django demo

It's a python django practice project and it can show Taiwan stock candlestick chart through yfinance library.

## Install and run

1. **Clone project**

   ```bash
   $ git clone https://github.com/bon3409/django-demo.git
   ```

2. **Install dependency libraries**

   ```bash
   $ pip install -r requirements.txt
   ```

3. **Set environment variable**

   ```bash
   $ cp .env.example .env
   ```

4. **Generate django project secret key**

   ```bash
   $ python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
   ```

   Copy output string and paste to .env variable "SECRET_KEY"

5. **Run migration**

   ```bash
   $ python manage.py migrate
   ```

6. **Run server**

   ```bash
   $ python manage.py runserver
   ```

## Demo Screenshot

![](https://i.imgur.com/HEoPYNH.png)

## 使用 uwsgi

- **安裝**

  ```bash
  $ pip3 install uwsgi
  ```

- **新增設定檔**

  ```bash
  $ cd <project_root_path>

  $ touch uwsgi.ini

  $ vim uwsgi.ini
  ```

  ```ini
  # django project 裡的 uwsgi.ini

  ; 這是用 http 方式的設定
  ; [uwsgi]
  ; http = :8001
  ; module = app.wsgi:application
  ; master = True
  ; processes = 1
  ; threads = 1
  ; vacuum = True
  ; pidfile = /tmp/django-demo.pid # 這個是 pid 檔的位置

  ; ------------------

  ; 這是用 socket 的設定
  [uwsgi]
  socket = 127.0.0.1:8000

  ; django 專案目錄
  chdir = /path/project

  module = app.wsgi:application
  master = True

  ; 進程數
  processes = 1
  threads   = 1
  vacuum    = True

  ; 啟動之後，儲存進程的 pid 位置
  pidfile = /tmp/django-demo.pid

  ; 設置 uwsgi 背景執行時，保存的 log
  daemonize=uwsgi.log
  ```

- **在背景執行**

  ```bash
  $ uwsgi -d --ini uwsgi.ini
  ```

- **終止背景執行的特定 uswgi**

  1.  找出 uwsgi 的位置

      ```bash
      $ where uwsgi # zsh command
      # or
      $ which uwsgi # bash command

      /usr/local/bin/uwsgi
      ```

  2.  **停止特定的 uswgi**

      ```bash
      # sudo uwsgi --stop <指定的 pidfile pid 檔的位置>
      $ sudo /usr/local/bin/uwsgi --stop /tmp/django-demo.pid
      ```

- **檢查目前的 uwsgi**

  ```bash
  $ ps ax | grep uwsgi
  ```

## Nginx 的設定

- **設定檔**

  **nginx.conf**

  ```ini
  server {
      listen       443 ssl;
      listen       [::]:443 ssl;
      server_name  django-demo.com;
      location / {
          # 用 http 作為接口
          # 在 uwsgi.ini 的設定檔就要用 http 的方式
          # proxy_pass http://127.0.0.1:8000;

          # 用 uwsgi 作為接口
          # 在 uwsgi.ini 的設定檔就要用 socket 的方式
          uwsgi_pass      127.0.0.1:8000;
          include         /etc/nginx/uwsgi_params;
      }

      ssl_certificate /etc/nginx/ssl/nginx.crt;
      ssl_certificate_key /etc/nginx/ssl/nginx.key;
  }
  ```

- **啟用配置**

  ```bash
  $ nginx -t        # 檢查設定是否正確

  $ nginx -s reload # 重啟 nginx
  ```
