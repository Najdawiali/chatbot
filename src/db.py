from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from local_settings import postgresql as settings


class MovieQuery:
    def __init__(self):
        self.engine = self._get_engine_from_settings()
        self.session = self._get_session()

    def _get_engine(self, user, passwd, host, port, db):
        url = f"postgresql://{user}:{passwd}@{host}:{port}/{db}"
        engine = create_engine(url, pool_size=50, echo=False)
        return engine

    def _get_engine_from_settings(self):
        required_keys = ['pguser', 'pgpasswd', 'pghost', 'pgport', 'pgdb']
        if not all(key in settings for key in required_keys):
            raise Exception('Bad config file')

        return self._get_engine(
            settings['pguser'],
            settings['pgpasswd'],
            settings['pghost'],
            settings['pgport'],
            settings['pgdb']
        )

    def _get_session(self):
        Session = sessionmaker(bind=self.engine)
        return Session()

    def get_movie_story(self, movie_name):
        query = text("""
        SELECT f.description, c.name AS category, l.name AS language,
               a.first_name, a.last_name
        FROM film f
        JOIN film_category fc ON f.film_id = fc.film_id
        JOIN category c ON fc.category_id = c.category_id
        JOIN language l ON f.language_id = l.language_id
        JOIN film_actor fa ON f.film_id = fa.film_id
        JOIN actor a ON fa.actor_id = a.actor_id
        WHERE LOWER(f.title) = :t
        """)

        result = self.session.execute(query, {"t": movie_name.lower()})
        rows = result.fetchall()
        actor_names = [f'{row.first_name} {row.last_name}' for row in rows]
        actors_str = ", ".join(actor_names)

        if rows:
            Movie_Story = f'Description:{rows[0].description}, Category:{rows[0].category}, movie language: {rows[0].language}, actors:{actors_str}'
            return Movie_Story
        else:
            return "Movie not found."