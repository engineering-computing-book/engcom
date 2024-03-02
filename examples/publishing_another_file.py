import sys
sys.path.append("../")
import engcom

pub = engcom.Publication(source_filename="movie_ratings_binned.py")
pub.write(to="md")