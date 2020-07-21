import dash_html_components as html
from components.selector import crear_selector
from helpers.lectura_datos import leer_datos

datos = leer_datos('./data/airbnb.csv', 'host_name', 'neighbourhood')

# Host names
host_names = datos.host_name.unique()

options = [{'label': name, 'value': name } for name in host_names if type(name) == str]

selector = crear_selector(options, "selector-host")

# Delegaciones

delegaciones = datos.neighbourhood.unique()

options_delegaciones = [{'label': delegacion, 'value': delegacion} 
                            for delegacion in delegaciones if type(delegacion) == str]

selector_delegaciones = crear_selector(options_delegaciones, "selector-delegaciones")

FORMULARIO = html.Div(
    html.Div(
        [html.Div(
            selector,
            className="col-lg-6 col-md-6 col-sm-12"),
         html.Div(
             selector_delegaciones,
             className="col-lg-6 col-md-6 col-sm-12")],
        className="row"
    ),
    className="container"
)