# Fotografías

## Política (aprobada en el handover v0.2)

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

## Fotos previstas

| Uso | Original | Clave en `_data/fotos.yml` |
|---|---|---|
| Portada (hero) y Sobre mí | `IMG_1216.jpeg` (cafetería, sudadera verde) | `hero` |
| Música | `PhotoShoot-30.jpeg` (sesión con saxofón) | `musica` |

La ilustración del sitio anterior (`assets/eduardo-saxofon*`) sigue en el repositorio pero está excluida de la publicación en `_config.yml`.
