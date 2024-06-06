#  what python
FROM python:3.12
#  what port
EXPOSE 5000
# what work directory, will move into /app folder
WORKDIR /app
RUN pip install flask
# will copy files from our file system ( . ) -entire folder
# of the project to image's file system /app
# . . because we're already in /app folder
COPY . .
# what commands to run when the image starts up in the container
CMD ["flask", "run", "--host", "0.0.0.0"]