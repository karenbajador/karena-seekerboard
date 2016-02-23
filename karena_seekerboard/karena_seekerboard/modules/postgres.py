class PostgresPipeline(object):

    def __init__(self):
        import psycopg2
        self.conn = psycopg2.connect(user="pi",
                                     dbname="cg_scraping",
                                     host='/var/run/postgresql/')

    def process_item(self, item, spider):
        cur = self.conn.cursor()

        cur.execute('''
                insert into raw_data ( title, url, price, bedrooms, maplink,
                   longitude, latitude, updated_on, content, image_links,
                   attributes, size, parsed_on )
                values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                ''', [
                item['title'],
                item['url'],
                item['price'],
                item.get('bedrooms', None),
                item['maplink'],
                item['longitude'],
                item['latitude'],
                item['time'],
                item['content'],
                item['image_links'],
                item['attributes'],
                item['size'],
                datetime.datetime.now()])
        self.conn.commit()
        return item