from enum import Enum
import reflex as rx

# Constantes
MAX_WIDTH = "600px"


# Sizes (Las definimos dentro de una enumeración. Para referirnos a los valores utilizamos la propiedad value.)
class Size(Enum):
    SMALL= "0.5em"
    MEDIUM="0.8em"
    DEFAULT = "1em"
    BIG = "2em"

#Styles (Utilizamos un diccionario en Python (dict) para que todos los componentes de un tipo determinando tengan unos estilos concretos.)
BASE_STYLE = {
    rx.button: {
        "width" : "100%",
        "height" : "100%",
        "display" : "block",
        "padding" : Size.SMALL.value,
        "border_radius" : Size.DEFAULT.value
    },
    rx.link : {
        "text_decoration" : "none",
        "_hover" : {}
    },
}

#Definimos un diccionario de estilos para poder aplicar directamente al componente que queramos, como un estilo en CSS. Se hace en forma de diccionario.
#Se puede generar el diccionario como en el ejemplo anterior o con este nuevo formato con la función dict()


button_title_style = dict(
    font_size=Size.DEFAULT.value
    )

button_body_style = dict(
    font_size=Size.MEDIUM.value
)

icon_centered = {
    "align_self" : "center"
}

title_style = dict(
    width="100%",
    padding_top=Size.DEFAULT.value
)