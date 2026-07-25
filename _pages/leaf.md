---
title: "Leaflet"
permalink: /leaf/
date: 2024-02-16T18:39:14+00:00
---
Test av leaflet map

{% leaflet_map {"zoom" : 5,
                "center" : [39.080957, 17.136717],
                "providerBasemap": "OpenStreetMap.HOT"} %}
    {%- for post in site.posts -%}
        {% if post.location.geojson %}
            {% leaflet_geojson {{post.location.geojson}} %}
        {% elsif post.location.latitude and post.location.longitude %}
            {% leaflet_marker { "latitude" : {{post.location.latitude}},
                                "longitude" : {{post.location.longitude}} } %}
        {% endif %}
    {% endfor %}
{% endleaflet_map %}