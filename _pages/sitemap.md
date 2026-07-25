---
layout: archive
title: "Sitemap"
permalink: /sitemap/
author_profile: false
---

En lista med alla sidor och poster på den här sidan. Om du är en robot så här har du en lättsmält [XML version]({{ '/sitemap.xml' | relative_url }}) av sidan.

<h2>Sidor</h2>
{% for post in site.pages %}
  {% include archive-single.html %}
{% endfor %}

<h2>Poster</h2>
{% for post in site.posts %}
  {% include archive-single.html %}
{% endfor %}

{% capture written_label %}'None'{% endcapture %}

{% for collection in site.collections %}
{% unless collection.output == false or collection.label == "posts" %}
  {% capture label %}{{ collection.label }}{% endcapture %}
  {% if label != written_label %}
  <h2>{{ label }}</h2>
  {% capture written_label %}{{ label }}{% endcapture %}
  {% endif %}
{% endunless %}
{% for post in collection.docs %}
  {% unless collection.output == false or collection.label == "posts" %}
  {% include archive-single.html %}
  {% endunless %}
{% endfor %}
{% endfor %}