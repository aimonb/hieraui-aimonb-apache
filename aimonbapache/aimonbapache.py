from app.form import Form


class Aimonbapache(Form):

    def validate(_self, form_data):
        valid = True
        if 'vhost' not in form_data or \
           'docroot' not in form_data or \
           'source_repo' not in form_data:
            valid = False
        if valid is False:
            return "Missing info!"
        return True

    def process(_self, form_data):
        nodes = {}
        vhost = form_data['vhost']
        nodes[vhost]['classes'] = ['aimonb-apache']
        nodes[vhost]['aimonb-apache::vhost'] = vhost
        nodes[vhost]['aimonb-apache::docroot'] = form_data['docroot']
        nodes[vhost]['aimonb-apache::source'] = form_data['source_repo']

        return nodes
