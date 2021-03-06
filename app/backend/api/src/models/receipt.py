import api.src.models as models


class Receipt(models.Table):
    __table__ = 'receipts'
    columns = ['id',
               'merchant_id',
               'month',
               'liquor_sales',
               'beer_sales',
               'wine_sales',
               'cover_sales',
               'total_sales',
               ]

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise Exception(f'{key} not in {self.columns}')
            setattr(self, key, kwargs[key])

    def merchant(self, cursor):
        """Return the merchant for this receipt."""
        query_str = ('SELECT m.* '
                       'FROM merchants m '
                      'WHERE m.id = %s;'
                     )
        cursor.execute(query_str, (self.cz_id,))
        record = cursor.fetchone()
        return orm.build_from_record(models.Merchant, record)
