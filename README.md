api-arg/
│
├── app/
│ ├── **init**.py
│ ├── main.py
│ ├── api/
│ │ ├── **init**.py
│ │ ├── endpoints/
│ │ ├── **init**.py
│ │ │ ├── argentina.py
│ │ │ ├── president.py
│ │ └── dependencies.py
│ └── utils/
│ ├── **init**.py
│ └── json_parser.py
│
├── data/
│ ├── argentina.json
│ └── presidentes.json
│
└── requirements.txt

Fuentes:

Wikipedia
ChatGPT
Censo 2022 https://www.indec.gob.ar/indec/web/Nivel4-Tema-2-41-165
ANAC https://datos.anac.gob.ar/estadisticas/article/720c108f-3f8c-436c-8159-5fd0506b75e6
Departamentos, provincias, municipios https://datos.gob.ar/dataset/jgm_8/archivo/jgm_8.1
Tourism - https://www.indec.gob.ar/indec/web/Nivel4-Tema-3-13-55
--

In this document Google JSON Style Guide (recommendations for building JSON APIs at Google),

It recommends that:

Property names must be camelCased, ASCII strings.

The first character must be a letter, an underscore (\_), or a dollar sign ($).

Example:

{
"thisPropertyIsAnIdentifier": "identifier value"
}
