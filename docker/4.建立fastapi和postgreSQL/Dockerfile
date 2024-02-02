FROM cicirello/pyaction:4.14.0

#set the working directory
WORKDIR /code

COPY ./requirements.txt ./
RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN git config --global user.name "roberthHsu"
RUN git config --global user.email "roberthsu2003@gmail.com"
RUN git config --global init.defaultBranch main
RUN git init

COPY . .

EXPOSE 80
EXPOSE 8501

CMD ["tail","-f","/dev/null"]

