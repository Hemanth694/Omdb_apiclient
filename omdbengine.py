from omdb_details import omdb
omdb=omdb("96478b1d")
movie_name=input("Enter a movie name for getting its details")
omdb.set_param(movie_name)
omdbresponse=omdb.send_request()
print(omdbresponse.content)
