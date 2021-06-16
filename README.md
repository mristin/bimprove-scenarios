# bimprove-scenarios

These scenarios were written within the [BIMprove Project] to specify the software requirements after the finished elicitation phase.

[BIMprove Project]: https://www.bimprove-h2020.eu/

The text was written across all the teams participating in the project. 

If you want to cite these scenarios, please cite the corresponding publication:

*Ristin, Marko and Edvardsen, Dag Fjeld and van de Venn, Hans Wernher: "RASAECO: Requirements Analysis of Software for the AECO Industry", 29th IEEE International Requirements Engineering Conference, 2021.*

## Installation

You need to have a Python 3.8+ installed on your system.

Create a virtual environment:

```
python -m venv venv
```

Activate it.
In Windows:

```
venv\Scripts\activate
```

or in Linux:

```
source venv/bin/activate
```

(In the activated virtual environment) install the necessary requirements:

```
pip3 install -r requirements.txt 
```

## Rendering

In your virtual environment (see above), run:

```
python render_once.py --output_path rendering
```

The scenarios are rendered to the `rendering/` directory.
