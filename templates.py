# from jinja2 import Template

"""
    ***** Elementos de una plantilla *****
"""

# temp1 = "Hola {{nombre}}"
# print(Template(temp1).render(nombre="Jaime"))

# ----------------------------------------------------------------------------
"""
    ***** Variables en las plantillas *****
"""

# temp2 = '<a href="{{url}}"> {{enlace}} </a>'
# print(Template(temp2).render(url="http://www.flask.com", enlace="Flask"))

# temp3 = '<a href="{{datos[0]}}"> {{datos[1]}} </a>'
# print(Template(temp3).render(datos=["http://www.flask.com", "Flask"]))

# temp4 = '<a href="{{datos["url"]}}"> {{datos.enlace}} </a>'
# print(Template(temp4).render(datos={"url": "http://www.flask.com",
#                                     "enlace": "Flask"}))

# ----------------------------------------------------------------------------
"""
    ***** Filtros de variables *****
    https://jinja.palletsprojects.com/en/3.1.x/templates/#builtin-filters
"""

# temp5 = 'Hola {{ nombre|striptags|title }}'
# print(Template(temp5).render(nombre="    pepe    "))

# temp6 = "Los datos son {{ lista|join(', ') }}"
# print(Template(temp6).render(lista=["amarillo", "verde", "rojo"]))

# temp7 = "El último elemento tiene {{ lista|last|length}} caracteres"
# print(Template(temp7).render(lista=["amarillo", "verde", "rojo"]))

# temp8 = "La siguiente cadena muestra todos los caracteres: {{ info|escape }}"
# print(Template(temp8).render(info="<hola&que&tal> "))

# ----------------------------------------------------------------------------
"""
    ***** Instrucciones en las plantillas (for) *****
"""

# temp9 = '''
# <ul>
# {% for elem in elems -%}
#     <li>{{loop.index}} - {{ elem }}</li>
# {% endfor -%}
# </ul>
# '''
# print(Template(temp9).render(elems=["amarillo", "verde", "rojo"]))

# ----------------------------------------------------------------------------
"""
    ***** Instrucciones en las plantillas (if) *****
"""

# temp10 = '''
# {% if elems is defined %}
#     <ul>
#     {% for elem in elems -%}
#         {% if elem is divisibleby 2 -%}
#             <li>{{elem}} es divisible por 2</li>
#         {% else -%}
#             <li>{{elem}} no es divisible por 2</li>
#         {% endif -%}
#     {% endfor -%}
#     </ul>
# {% endif %}
# '''
# print(Template(temp10).render(elems=[1, 2, 3, 4, 5, 6]))
