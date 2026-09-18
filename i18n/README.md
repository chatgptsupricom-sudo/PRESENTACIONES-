# Traducciones ES → EN

El inglés de la presentación vive en el diccionario `const EN={...}` dentro de
`index.html`. Estos scripts permiten editarlo fuera del HTML (por ejemplo, con
DeepL) sin tocar el markup.

## Archivos

| Archivo | Qué es |
|---|---|
| `es.txt` | Solo los textos en español, uno por línea (7 KB). Para pegar en DeepL. |
| `traducciones.tsv` | `español<TAB>inglés`, 105 filas. Es la fuente de verdad editable. |
| `extract.py` | Regenera `es.txt` y `traducciones.tsv` desde `index.html`. |
| `apply.py` | Escribe `traducciones.tsv` de vuelta en `index.html`. |

## Flujo con DeepL

1. `python i18n/extract.py`
2. Abrir `i18n/es.txt` y pegar su contenido en DeepL (español → inglés).
   DeepL respeta los saltos de línea, así que la salida tiene las mismas 105
   líneas en el mismo orden.
3. Pegar la salida en la **segunda columna** de `i18n/traducciones.tsv`
   (las columnas van separadas por un TAB; no cambiar la primera columna: es la
   clave de búsqueda y debe coincidir exactamente con el texto del HTML).
4. `python i18n/apply.py`
5. Abrir `index.html` y verificar con el botón EN.

El límite del DeepL gratuito es de 1.500 caracteres por pegado, así que hará
falta hacerlo por partes (`es.txt` son 7.006 caracteres, unas 5 tandas).

## Advertencias

- **No editar la primera columna.** Si el español del TSV deja de coincidir
  carácter por carácter con el del HTML, esa frase simplemente no se traduce.
- Revisar a mano las frases partidas por `<span>`: en el hero y en la portada de
  marcas, una misma oración está dividida en 2 o 3 filas del TSV. DeepL traduce
  cada fragmento por separado y el resultado puede no encajar al unirlos.
- DeepL tiende a ser literal con el lenguaje comercial. Conviene revisar los
  titulares antes de publicar.
