---
# Campo Gravitacional
El proyecto presentado es un programa desarrollado en el lenguaje de programación python. El programa calcula el campo gravitacional generado por cierta cantidad de planetas en un punto determinado. Después de haber calculado el campo gravitaciónal para un punto sin masa, se calcula el campo gravitacional suponiendo que el mismo punto tiene una masa de 4 kg.
***
# Tabla de Contenido
1. [Información General](#información-general)
2. [Tecnología](#tecnología)
3. [Detalles a Aclarar](#detalles-a-aclarar)
***


## Información General
El siguiente programa fue creado para la clase de Física del Instituo Tecnológico Autónomo de México.
######
Un campo está compuesto por diferentes vectores que indican hacia donde sería atraída una partícula si estuviera en determinado punto del plano.

Los cuerpos generan un campo gravitacional en el espacio por el simple hecho de tener masa. Estos campos gravitacionales nos indican como son las perturbaciones creadas por los cuerpos en el espacio. Siempre podremos calcular el campo gravitacional en cualquier punto mientras tengamos su masa y su posición.

En la imagen siguiente se puede observar el campo gravitacional generado por el cuerpo m. Después se observa la manera en la que el cuerpo m´ se moverá por estar dentro del campo gravitacional de m.

![Campo Gravitacional](ImagenCampoGravitacional.jpg)

Los magnitudes de los campos gravitacionales pueden ser calculadas con la siguiente fórmula:

![FórmulaCG](FórmulaCG.png)

* g = campo gravitacional
* G = constante de gravitación universal
* M = masa del cuerpo
* r = distancia entre el cuerpo y el punto a analizar

Para más información sobre campos gravitacionales ir a este [sitio](#https://www.uv.es/jmarques/_private/Campogravitatorio.pdf).

## Tecnologías
* Python 3.6.6
* [PyCharm](https://www.youtube.com/watch?v=SZUNUB6nz3g&feature=emb_title)
## Detalles a Aclarar
* El programa sólo calculará el campo gravitacional en los ejes x e y. Calcular los campos gravitacionales en x e y permitirá que después se pueda calcular el vector de dirección del campo gravitacional.

* Después de calcular el campo gravitacional para el punto sin masa el campo gravitacional se multiplica por 4 para obtener un segundo campo gravitacional. El nuevo campo gavitacional será el campo correspondiente a una masa de 4 kg si tal masa se encontrara en el punto a analizar.

* El siguiente bloque de código es un bucle que permitirá sumar tantos campos gravitacionales como planetas hayamos introducido al sistema:

```python
for i in range(numPlanets):
    if(coords[cont] - puntoa[0]) != 0:
        C1 = (masas[i]*(coords[cont] - puntoa[0]))/(coords[cont]-puntoa[0]).__abs__().__pow__(2)
        campox = campox + C1
    cont = cont+1
    if (coords[cont] - puntoa[1]) != 0:
        C2 =(masas[i]*(coords[cont] - puntoa[1]))/(coords[cont]-puntoa[1]).__abs__().__pow__(2)
        campoy = campoy +C2
    cont = cont+1
```
    El código es comprendido mejor con la ayuda del siguiente diagrama:

   ![DiagramaBien](DiagramaBien.png)
