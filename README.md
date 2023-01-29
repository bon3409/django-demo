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
