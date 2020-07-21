import dash
import dash_html_components as html
import dash_bootstrap_components as dbc

from components.encabezado import ENCABEZADO
from components.formulario import FORMULARIO


#Hace la app
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

#Se declara el contenido de la app
app.layout = html.Div([ENCABEZADO, FORMULARIO])

#Lo que se ejecuta cuando llamamos app.py
if __name__ == '__main__':
    
    app.run_server(debug=True)