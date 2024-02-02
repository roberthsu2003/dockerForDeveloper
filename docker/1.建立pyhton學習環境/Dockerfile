FROM python:3.10-slim

# set the working directory
WORKDIR /code

# install dependencies
COPY ./requirements.txt ./
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# 安裝git
# RUN apt-get update && \
#    apt-get upgrade -y && \
#    apt-get install -y git
#
# RUN git config --global user.name "robertHsu"
# RUN git config --global user.email "roberthsu2003@gmail.com"
# RUN git config --global init.defaultBranch main
# RUN git init


# start the server
CMD ["tail", "-f", "/dev/null"]