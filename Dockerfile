# Use an official Python runtime as a base image
FROM python:3.8-slim

# Install any needed packages specified in requirements.txt
RUN apt-get update
RUN apt-get install -y ffmpeg
RUN pip3 install spotify_dl --upgrade

# Define environment variable
ENV SPOTIPY_CLIENT_ID=
ENV SPOTIPY_CLIENT_SECRET=
