#Import CSV library foropening and reading from a csv file
import csv

from cs50 import SQL #We are going to use this file to execute SQL Queries

open("tuesday.db", "w").close()

db = SQL("sqlite:///tuesday.db")

db.execute("CREATE TABLE movies (id INTEGER, title TEXT, PRIMARY KEY (id)) ")

db.execute("CREATE TABLE movie_genre (movies_id INTEGER, genre_id INTEGER, PRIMARY KEY(genre_id), FOREIGN KEY(movies_id) REFERENCES movies(id)) ")

db.execute("CREATE TABLE genre (movie_id INTEGER, genre TEXT, FOREIGN KEY (movie_id) REFERENCES movies(id))")

with open("gross movies.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        title = row["Film"].strip().capitalize()
        movieId = db.execute("INSERT INTO movies (title) VALUES(?)",  title)
        
        for genre in row ["Genre"].split(","):
            genre = row["Genre"].strip().capitalize()
            genre_Id = db.execute("INSERT INTO movie_genre (movies_id) VALUES ((SELECT id FROM movies WHERE title=?))", title)
            db.execute("INSERT INTO genre (movie_id, genre) VALUES (?,?) ", movieId, genre)
            

