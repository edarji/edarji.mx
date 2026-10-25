---
layout: seccion
title: Ideas
seccion: ideas
intro: "Me interesan las ideas que nos obligan a pensar dos veces. Aquí reúno reflexiones sobre filosofía, psicología, incertidumbre, aprendizaje y las preguntas que aparecen entre una lectura y otra. No es una colección de respuestas definitivas, sino un lugar para explorar."
---
{%- assign colecciones_ideas = "" | split: "" %}
{%- for par in site.data.colecciones %}{% if par[1].seccion == page.seccion %}{% assign colecciones_ideas = colecciones_ideas | push: par %}{% endif %}{% endfor %}
{%- if colecciones_ideas.size > 0 %}
<section class="colecciones" aria-labelledby="colecciones-titulo">
  <h2 id="colecciones-titulo" class="bloque-titulo">Colecciones</h2>
  <ul class="colecciones-lista">
    {%- for par in colecciones_ideas %}
    {%- assign total = site.posts | where: "coleccion", par[0] | size %}
    <li><a href="{{ par[1].url | relative_url }}">{{ par[1].titulo }}</a> <span>· {{ total }} {% if total == 1 %}entrada{% else %}entradas{% endif %}</span></li>
    {%- endfor %}
  </ul>
</section>
{%- endif %}
