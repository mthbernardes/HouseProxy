from jinja2 import FileSystemLoader, Environment

template_engine = Environment(loader=FileSystemLoader("html"))

def get_template(name):
    return template_engine.get_template(name)
