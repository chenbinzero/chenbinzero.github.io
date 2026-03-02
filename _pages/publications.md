---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if site.author.googlescholar %}
  <div class="wordwrap">You can find a full list of my articles on <a href="{{site.author.googlescholar}}">my Google Scholar profile</a>.</div>
{% endif %}

{% if site.author.webofscience %}
  <div class="wordwrap">I was recognized as a Highly Cited Researcher in the field of Cross-Field - 2023 and 2024 <a href="{{site.author.webofscience}}">by Clarivate</a>.</div>

{% endif %}

<img src="/images/citationGoogle.png" width="300">

## Selected Publications
(† equal contribution, \* corresponding author — full list on Google Scholar)

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
