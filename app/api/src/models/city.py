from src import db
from src import models

class City(models.Table):
    __table__ = 'cities'
    columns = ['id', 'name']

    def __init__(self, **kwargs):
        City.initialize_table(kwargs)
        
    def zipcodes(self, cursor):
        """Return all zip codes in this city."""
        query_str = ('SELECT z.name '
                       'FROM zipcodes z '
                       'JOIN cities_zipcodes cz '
                         'ON cz.zip_id = z.id '
                      'WHERE cz.city_id = %s;'
                    )
        cursor.execute(query_str, (self.id,))
        records = cursor.fetchall()
        return db.build_from_records(models.Zipcode, records)

    def merchants(self, cursor):
        """Return all merchants in this city."""
        query_str = ('SELECT m.* '
                       'FROM merchants m JOIN cities_zipcodes cz '
                         'ON m.cz_id = cz.id '
                      'WHERE cz.city_id = %s;'
                    )
        cursor.execute(query_str, (self.id,))
        records = cursor.fetchall()
        return db.build_from_records(models.Merchant, records)
