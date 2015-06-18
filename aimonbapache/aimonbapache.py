from app.form import Form


class Aimonbapache(Form):

    def validate(_self, form_data):
        valid = True
        if 'vhost' not in form_data or \
           'docroot' not in form_data or \
           'hostname' not in form_data or \
           'source_repo' not in form_data:
            valid = False
        if valid is False:
            return "Missing info!"
        return True

    def process(_self, form_data):
        nodes = {}
        hostname = form_data['hostname']
        vhost = form_data['vhost']
        nodes[hostname] = {}
        nodes[hostname]['classes'] = ['aimonb_apache']
        nodes[hostname]['aimonb_apache::vhost'] = vhost
        nodes[hostname]['aimonb_apache::docroot'] = form_data['docroot']
        nodes[hostname]['aimonb_apache::source_repo'] = form_data['source_repo']

        return nodes
