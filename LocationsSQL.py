import psycopg2


class LocationsSQL:

    def __init__(self):
        self.conection = psycopg2.connect(database = "pieercwz", 
                                user = "pieercwz", 
                                host= 'suleiman.db.elephantsql.com',
                                password = "UVT9KsBlWa9GmCYQ62NwV4lIdk4cN865",
                                port = 5432)
        self.cur = self.conection.cursor()

    def insertLatLong(self, lat, long):
        self.cur.execute("INSERT INTO location_hole(long, lat) VALUES({},{})".format(long, lat))
        self.conection.commit()
        
    def searchByRaio(self, lat, long):
        # Raio em Km
        raio = 0.005
        self.cur.execute("SELECT * FROM location_hole where (6371 * acos(cos(radians(" + str(lat) + ")) * cos(radians(lat)) * cos(radians(" + str(long) + ") - radians(long)) + sin(radians(" + str(lat) + ")) * sin(radians(lat)))) <= " + str(raio))
        # Recupere os resultados
        return self.cur.fetchall()
        
    def close(self):
        self.cur.close()
        self.conection.close()