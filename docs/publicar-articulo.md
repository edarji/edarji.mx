# Cómo publicar un artículo

## Opción A: desde el navegador (sin instalar nada)

1. En GitHub, abre la carpeta `_posts/` y pulsa **Add file → Create new file**.
2. Nómbralo `AAAA-MM-DD-titulo-corto.md`, por ejemplo `2026-11-02-la-incertidumbre-como-ventaja.md`.
   La fecha del nombre es la fecha de publicación.
3. Copia el contenido de `_drafts/plantilla-articulo.md` y cambia el título, la categoría y el texto.
4. Pulsa **Commit changes**. En uno o dos minutos el artículo aparece en la portada y en su sección.

## Opción B: desde la Mac

```bash
cd edarji.mx
cp _drafts/plantilla-articulo.md _posts/2026-11-02-la-incertidumbre-como-ventaja.md
# edita el archivo…
bundle exec jekyll serve          # revisa en http://localhost:4000
git add _posts/2026-11-02-la-incertidumbre-como-ventaja.md
git commit -m "Publicar: La incertidumbre como ventaja"
git push
```

## Encabezado del artículo

```yaml
---
title: "La incertidumbre como ventaja"
category: ideas            # ideas | musica | laboratorio | biblioteca
tags: [exploracion, taleb] # opcional
resumen: Una o dos líneas para la portada y la lista de la sección.
---
```

## Dentro del texto

- Markdown normal: `## Subtítulo`, `**negritas**`, `*cursivas*`, `[enlace](https://…)`, `> cita`.
- Disco de Spotify: `{% include spotify.html album="ID_DEL_ALBUM" titulo="Nombre del disco" %}`
  (el ID es la parte final del enlace `open.spotify.com/album/ID`).
- Video de YouTube: `{% include youtube.html id="ID_DEL_VIDEO" titulo="Nombre del video" %}`

## Borradores

Lo que está en `_drafts/` nunca se publica. Para verlo en tu Mac: `bundle exec jekyll serve --drafts`.
