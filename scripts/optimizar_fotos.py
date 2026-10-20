"""Prepara fotografías originales para edarji.mx.

Uso (desde la raíz del repositorio):
    python3 scripts/optimizar_fotos.py fotos-originales/IMG_1216.jpeg hero

Genera assets/img/hero-480|800|1200.avif|webp|jpg y:
  - corrige la orientación según el EXIF,
  - BORRA todos los metadatos (GPS, modelo del teléfono, fecha),
  - NO recorta, no deforma y no retoca: solo cambia el tamaño.

El original nunca se modifica ni se sube al repositorio (fotos-originales/ está en .gitignore).
Requiere Pillow 11.3 o posterior para AVIF:  python3 -m pip install --upgrade pillow
"""

import sys
from pathlib import Path

from PIL import Image, ImageOps, features

ANCHOS = (480, 800, 1200)
DESTINO = Path("assets/img")
CALIDAD = {"avif": 55, "webp": 78, "jpg": 82}


def optimizar(original: Path, nombre: str) -> None:
    with Image.open(original) as foto:
        foto = ImageOps.exif_transpose(foto).convert("RGB")
        ancho, alto = foto.size
        print(f"Original: {original.name} · {ancho}×{alto}px")

        formatos = ["webp", "jpg"]
        if features.check("avif"):
            formatos.insert(0, "avif")
        else:
            print("Aviso: esta versión de Pillow no soporta AVIF; se omite.")

        DESTINO.mkdir(parents=True, exist_ok=True)
        for w in ANCHOS:
            # Nunca se amplía una foto más allá de su tamaño original.
            w_real = min(w, ancho)
            copia = foto.resize((w_real, round(alto * w_real / ancho)), Image.LANCZOS)
            for formato in formatos:
                salida = DESTINO / f"{nombre}-{w}.{formato}"
                tipo = "JPEG" if formato == "jpg" else formato.upper()
                # Al guardar sin el parámetro exif=, Pillow no copia ningún metadato.
                copia.save(salida, tipo, quality=CALIDAD[formato], optimize=True)
                print(f"  {salida} · {salida.stat().st_size // 1024} KB")

    print(f"\nEn _data/fotos.yml pon:  archivo: \"{nombre}\"  ancho: {ANCHOS[-1]}  alto: {round(alto * ANCHOS[-1] / ancho)}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    optimizar(Path(sys.argv[1]), sys.argv[2])
