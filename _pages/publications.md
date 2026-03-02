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
  <div class="wordwrap">I was recognized as a Highly Cited Researcher in the field of Cross-Field — 2023, 2024 &amp; 2025 <a href="{{site.author.webofscience}}">by Clarivate</a>.</div>
{% endif %}

<!-- Citation stats card — data fetched live from OpenAlex API (via ORCID, no auth needed) -->
<div id="scholar-stats" style="display:flex; gap:1.5rem; flex-wrap:wrap; margin:1rem 0 1.5rem;">
  <div class="scholar-stat-card">
    <span class="scholar-stat-number" id="stat-citations">—</span>
    <span class="scholar-stat-label"><i class="fa-solid fa-quote-left fa-xs"></i> Citations</span>
  </div>
  <div class="scholar-stat-card">
    <span class="scholar-stat-number" id="stat-hindex">—</span>
    <span class="scholar-stat-label"><i class="fa-solid fa-chart-line fa-xs"></i> h-index</span>
  </div>
  <div class="scholar-stat-card">
    <span class="scholar-stat-number" id="stat-i10">—</span>
    <span class="scholar-stat-label"><i class="fa-solid fa-file-lines fa-xs"></i> i10-index</span>
  </div>
  <div class="scholar-stat-card">
    <span class="scholar-stat-number" id="stat-works">—</span>
    <span class="scholar-stat-label"><i class="fa-solid fa-book-open fa-xs"></i> Publications</span>
  </div>
</div>
<p style="font-size:0.75rem; color:var(--global-text-color-light); margin-top:-0.75rem;">
  Live data via <a href="https://openalex.org" target="_blank" style="color:inherit;">OpenAlex</a> ·
  Full list on <a href="{{site.author.googlescholar}}" target="_blank" style="color:inherit;">Google Scholar</a>
</p>

<style>
.scholar-stat-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 0.75rem 1.25rem;
  border: 1px solid var(--global-border-color);
  border-radius: 8px;
  background: var(--global-bg-color);
  box-shadow: 0 1px 3px rgba(0,0,0,0.08);
  min-width: 90px;
}
.scholar-stat-number {
  font-size: 1.6rem;
  font-weight: 700;
  color: var(--global-base-color);
  line-height: 1.1;
}
.scholar-stat-label {
  font-size: 0.72rem;
  color: var(--global-text-color-light);
  margin-top: 0.2rem;
  text-align: center;
  text-transform: uppercase;
  letter-spacing: 0.03em;
}
</style>

<script>
(function() {
  var orcid = "{{ site.author.orcid | remove: 'https://orcid.org/' }}";
  fetch("https://api.openalex.org/authors/https://orcid.org/" + orcid + "?select=cited_by_count,works_count,summary_stats")
    .then(function(r) { return r.json(); })
    .then(function(d) {
      var el = function(id, val) {
        var e = document.getElementById(id);
        if (e) e.textContent = val;
      };
      el("stat-citations", d.cited_by_count ? d.cited_by_count.toLocaleString() : "—");
      el("stat-hindex",    d.summary_stats && d.summary_stats.h_index != null ? d.summary_stats.h_index : "—");
      el("stat-i10",       d.summary_stats && d.summary_stats.i10_index != null ? d.summary_stats.i10_index : "—");
      el("stat-works",     d.works_count ? d.works_count : "—");
    })
    .catch(function() {}); // fail silently — dashes remain
})();
</script>

## Selected Publications
(† equal contribution, \* corresponding author — full list on Google Scholar)

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
