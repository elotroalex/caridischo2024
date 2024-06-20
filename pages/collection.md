---
layout: page
title: Browse the Collection
gallery: True
permalink: /collection/
---

This site's collection can be browsed below.

{% assign my_array = "ants, bugs, bees, bugs, ants" | split: ", " %}

{{ my_array | uniq | join: ", " }}

{% include gallery.html facet_by='section|language*' collection='caridischo' num_column=4 %}
