FROM python:3

RUN apt -qq -y update \
&& apt -qq -y upgrade

# env variable for the app directory
ENV APP /app

# Create and use the app directory
RUN mkdir $APP
WORKDIR $APP

# copy the reqs
COPY requirements.txt .

# install the dependencies
RUN pip install -r requirements.txt

# copy the code of the app
COPY . .

# run the app
# CMD [ “uwsgi” “app.ini” ]
RUN chmod u+x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]