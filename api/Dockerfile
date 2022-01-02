FROM registry.gitlab.com/qio/standard/python:3.10-alpine

# Installing packages
RUN apk update
RUN pip install --upgrade pip
COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt
# RUN pip install --no-cache-dir Flask
# RUN pip install --no-cache-dir pipenv
# RUN pip install --no-cache-dir redis

# Install API dependencies
# RUN pipenv install

# Defining working directory and adding source code
WORKDIR /usr/src/app
COPY . .

# Start app
EXPOSE 5000
ENTRYPOINT ["/usr/src/app/runner.sh"]
