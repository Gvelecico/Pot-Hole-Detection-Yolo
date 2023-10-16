import psycopg2


class LocationsSQL:

    def __init__(self):
        self.conection = psycopg2.connect(database = "pieercwz", 
                                user = "pieercwz", 
                                host= 'suleiman.db.elephantsql.com',
                                password = "UVT9KsBlWa9GmCYQ62NwV4lIdk4cN865",
                                port = 5432)
        

    def insertLatLong(self, lat, long):

        cur = self.conection.cursor()

        cur.execute("INSERT INTO location_hole(long, lat) VALUES('{}','{}')".format(long, lat))
        self.conection.commit()
        cur.close()
        self.conection.close()