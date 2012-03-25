import requests

requests = requests.session()

class StatHat(object):

        def http_post(self, path, data):
            url = 'http://api.stathat.com' + path
            r = requests.post(url, data=data)
            return r.content

        def post_value(self, user_key, stat_key, value):
            return self.http_post('/v', {'key': stat_key, 'ukey': user_key, 'value': value})

        def post_count(self, user_key, stat_key, count):
            return self.http_post('/c', {'key': stat_key, 'ukey': user_key, 'count': count})

        def ez_post_value(self, email, stat_name, value):
            return self.http_post('/ez', {'email': email, 'stat': stat_name, 'value': value})

        def ez_post_count(self, email, stat_name, count):
            return self.http_post('/ez', {'email': email, 'stat': stat_name, 'count': count})

