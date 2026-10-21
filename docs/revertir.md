# Cómo revertir

## Antes de publicar

Todo el trabajo está en una rama. Producción (`main`) no cambia. Revertir = cerrar el PR o borrar la rama.

## Después de publicar

El sitio anterior (Ed ArJi Jazz) queda guardado en la rama `archivo-ed-arji-jazz`, que apunta al último `main` antes de v0.2.

**Desde GitHub (recomendado):** abre el PR fusionado y pulsa **Revert**. Se crea un PR que deshace el cambio; fusiónalo.
GitHub Pages vuelve a publicar la versión anterior en uno o dos minutos.

**Desde la terminal:**

```bash
git checkout main && git pull
git revert -m 1 <commit-de-fusion>   # -m 1: conserva el lado de main antes de la fusión
git push
```

## Si la construcción falla

GitHub Pages mantiene en línea la última versión que sí se construyó. Revisa el error en la pestaña **Actions** del repositorio
("pages build and deployment"). El dominio no se ve afectado mientras `CNAME` no cambie.
