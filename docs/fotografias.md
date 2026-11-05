# Fotografías e ilustraciones

## Cambio de identidad visual (handover ChatGPT, 5-nov-2026)

Las fotografías personales se sustituyeron por dos **ilustraciones expresionistas originales** (óleo de empaste, azul y crema):

| Uso | Archivo original | Clave en `_data/fotos.yml` | Versiones web |
|---|---|---|---|
| Portada, Sobre mí e imagen para redes (Open Graph) | `oil_paint_impasto_style_portrait_in_thick_express.png` (figura pensativa, saxofón descansando) | `hero` | `assets/img/pintura-contemplativa-*` |
| Música | `a_painted_impasto_oil_style_image_identical_in_com.png` (saxofonista tocando) | `musica` | `assets/img/pintura-saxofonista-*` |
| Música · sección 01 «Mi relación con el jazz» | `a_painterly_impressionist_oil_brushstroke_style_i.png` (saxofonista con sombrero; agregada por Lalo) | `jazz` | `assets/img/pintura-sombrero-*` |

Reglas: **no modificar ni reinterpretar las pinturas** (sin corregir proporciones, colores ni composición, sin recortes).
Solo se cambia el tamaño y el formato. Por eso la portada usa la proporción 4:5 de las pinturas.
Las pinturas miden 1122 px de ancho: el archivo `-1200` es en realidad de 1122 px (el script nunca amplía).
El PNG del saxofonista con sombrero trae esquinas redondeadas con fondo blanco: el CSS (`.jazz-foto img`) las oculta con `border-radius`, sin tocar el archivo.
Las fotografías anteriores (`hero-*`, `musica-*`) se retiraron del sitio pero siguen en el historial de Git.

Para regenerar las versiones web:

```bash
python3 scripts/optimizar_fotos.py fotos-originales/oil_paint_impasto_style_portrait_in_thick_express.png pintura-contemplativa
python3 scripts/optimizar_fotos.py fotos-originales/a_painted_impasto_oil_style_image_identical_in_com.png pintura-saxofonista
```

## Política anterior de fotografías (handover v0.2, se conserva como referencia)

- Solo fotografías **originales y reales** del propietario. Nada de rostros generados o reinterpretados por IA.
- Sin adelgazamiento ni cambios de proporciones. Solo ajustes moderados de luz, contraste, encuadre y color, y solo si se aprueban.
- Las pinceladas y decoraciones van **alrededor** de la foto, nunca sobre el rostro.
- No inventar retratos en lugares o situaciones donde no existe una foto original.

## Privacidad

Las fotos del teléfono guardan coordenadas GPS y datos del aparato. El script las **borra** siempre.
Los originales se guardan en `fotos-originales/`, que está en `.gitignore`: nunca se suben al repositorio público.

## Agregar o cambiar una foto

```bash
python3 -m pip install --upgrade pillow                           # una vez
mkdir -p fotos-originales && cp ~/Desktop/IMG_1216.jpeg fotos-originales/
python3 scripts/optimizar_fotos.py fotos-originales/IMG_1216.jpeg hero
```

Esto crea `assets/img/hero-480|800|1200` en AVIF, WebP y JPEG. Luego, en `_data/fotos.yml`, pon `archivo: "hero"`
y el `alto` que indica el script. El encuadre se ajusta con `posicion` (por ejemplo `center 30%`) sin recortar el archivo.

## Fotos previstas en v0.2 (ya sustituidas)

| Uso | Original | Clave en `_data/fotos.yml` |
|---|---|---|
| Portada (hero) y Sobre mí | `IMG_1216.jpeg` (cafetería, sudadera verde) | `hero` |
| Música | `PhotoShoot-29.jpeg` (sesión con saxofón; la 30 no se recibió) | `musica` |

### Tratamiento aplicado a `IMG_1216.jpeg`

Las personas del fondo (lado izquierdo) y una tarjeta sobre la mesa se difuminaron para no publicar a terceros.
La figura del propietario no se tocó: sin cambios de rostro, proporciones, luz ni color. Solo se cambió el tamaño.

La ilustración del sitio anterior (`assets/eduardo-saxofon*`) sigue en el repositorio pero está excluida de la publicación en `_config.yml`.
