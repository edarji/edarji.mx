# Arquitectura técnica

**Decisión:** Jekyll nativo de GitHub Pages + Markdown, en el mismo repositorio (auditoría del 19‑oct‑2026 y plan v0.2 del 20‑oct‑2026).
Sin servidor, sin base de datos, sin GitHub Actions, sin dependencias de JavaScript.

## Cómo se construye

1. Haces push a `main`.
2. GitHub Pages ejecuta Jekyll 3.10 (gema `github-pages` 232) y publica el resultado en edarji.mx.
3. Si la construcción falla, Pages **mantiene la versión anterior en línea** y avisa en la pestaña *Actions* del repo.

## Carpetas

| Carpeta / archivo | Qué es |
|---|---|
| `_config.yml` | Nombre del sitio, URL, plugins (`jekyll-seo-tag`, `jekyll-sitemap`, `jekyll-feed`) y archivos excluidos |
| `_layouts/` | Plantillas: `base` (estructura común), `inicio`, `seccion`, `articulo`, `pagina` |
| `_includes/` | Piezas reutilizables: encabezado, pie, figura (fotos), Spotify, YouTube, lista de entradas, pinceladas |
| `_data/navegacion.yml` | El menú principal |
| `_data/areas.yml` | Tarjetas "Áreas del cuaderno" de la portada |
| `_data/fotos.yml` | Fotografías del sitio y su texto alternativo |
| `_posts/` | Artículos publicados |
| `_drafts/` | Borradores: **nunca se publican** |
| `ideas/`, `musica/`, `laboratorio/`, `biblioteca/`, `sobre-mi/`, `exploracion/` | Páginas de sección |
| `assets/css/main.css` | Todos los estilos. Paleta en `:root` |
| `assets/fonts/` | Fraunces, Source Sans 3 y Caveat, alojadas aquí (licencia OFL) |
| `assets/js/menu.js` | Solo el menú móvil. Sin JS el menú se ve completo |
| `scripts/optimizar_fotos.py` | Genera tamaños de foto y borra metadatos (no se publica) |
| `docs/` | Esta documentación (no se publica) |

## Secciones y categorías

- Cada artículo declara `category:` (`ideas`, `musica`, `laboratorio` o `biblioteca`). La URL queda `/ideas/titulo-del-articulo/`.
- La página de sección lista los artículos de su categoría. Si no hay ninguno, muestra un aviso honesto.
- **Exploración** no es sección del menú: es la etiqueta `exploracion`. Un artículo con `tags: [exploracion]` aparece también en `/exploracion/`.
- Para crear una sección nueva: una carpeta con `index.md` (copiar `ideas/index.md`), una línea en `_data/navegacion.yml` y, si se quiere, una tarjeta en `_data/areas.yml`.

## Principios

- El contenido nunca depende de JavaScript.
- Animaciones discretas en CSS, desactivadas con "reducir movimiento".
- Contraste mínimo 4,5:1 en texto normal y 3:1 en títulos grandes. El ocre (`#E7AE30`) no se usa para texto sobre crema (1,72:1). Para texto pequeño en terracota se usa `#A3462F` (5,2:1).
- Solo fotografías reales del propietario, sin metadatos. Ver [fotografias.md](fotografias.md).
- Multimedia pesada (audio, video) fuera del repositorio: YouTube, Spotify, Bandcamp, etc.

## Por qué no Hugo o Astro

Jekyll viene integrado en GitHub Pages: no requiere instalar nada para publicar ni añadir un flujo de GitHub Actions. Si un día se necesita optimización automática de imágenes o un sitio muy grande, Hugo es la salida natural; el contenido en Markdown se conserva casi igual.
