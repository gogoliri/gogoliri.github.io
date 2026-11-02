---
# ================= THE DOI SWITCH =================
# https://khoaphamdinh.com/papers/quality-constrained-coding.html is the stable
# address for this paper and never changes. Today that URL shows this page: the
# arXiv preprint link and the abstract, with no venue yet.
# When the publisher assigns a DOI, change the ONE line directly below:
#   1. Uncomment it, by deleting the "# " at the start of the line.
#   2. Replace XX.XXXX/XXXXX with the real DOI.
# Save, commit, push. The stable URL then redirects straight to the publisher
# page, in every browser, with no JavaScript involved.
# Leave it commented if you would rather keep this landing page, the way
# vcm-segmentation and oxygen-gait do.
# ==================================================
# doi_redirect: https://doi.org/XX.XXXX/XXXXX

number: 4
group: preprint
title: 'You&#8217;ve Seen Enough: Quality-Constrained Image Coding For Machines'
list_title: 'You&rsquo;ve Seen Enough: Quality-Constrained Image Coding For Machines'
og_title: 'You''ve Seen Enough: Quality-Constrained Image Coding For Machines'
description: 'Image coding for machines that caps human-observed quality at a target level and devotes the remaining bits to machine performance, via constrained joint compression-segmentation training. arXiv preprint.'

authors:
  - {name: Khoa Pham-Dinh, me: true}
  - {name: Sanaz Nami}
  - {name: Hamed Rezazadegan Tavakoli}
  - {name: Moncef Gabbouj}
  - {name: Farhad Pakdaman}

# AFFILIATIONS: uncomment when the affiliation list is settled, replace each
# placeholder with the real institution, add the matching `sup:` to each author
# above, then delete this note. Delete the `corresponding:` line if there is none.
# affiliations: '<sup>1</sup>INSTITUTION ONE &nbsp;&middot;&nbsp; <sup>2</sup>INSTITUTION TWO'
# corresponding: '<sup>*</sup>Corresponding author: <a href="mailto:ADDRESS">ADDRESS</a>.'

# VENUE: uncomment once the paper is accepted, replace with the real conference
# or journal, city, country and dates, then delete this note. `list_venue` is the
# shorter line on the homepage, in the style of the other papers.
# venue: '<em>VENUE NAME. CITY, COUNTRY, DD&ndash;DD MONTH YYYY.</em>'
# list_venue: '<em>VENUE NAME</em>, CITY, COUNTRY, DD&ndash;DD MONTH YYYY.'

# DOI: uncomment once the DOI is issued, replace XX.XXXX/XXXXX with the real
# DOI, then delete this note. It adds the DOI line here and a DOI chip on the
# homepage.
# doi: XX.XXXX/XXXXX

links:
  - {label: arXiv, url: "https://arxiv.org/abs/2609.25108"}
actions:
  - {label: Read on arXiv, url: "https://arxiv.org/abs/2609.25108"}
# ACTIONS: when there is finally something else to link to, add it above. Add the
# PDF button only if a copy is hosted next to the other files as
# papers/quality-constrained-coding.pdf; add the DOI button only once the DOI
# exists; then delete this note.
#   - {label: Read the PDF, url: /papers/quality-constrained-coding.pdf}
#   - {label: Read the published version, url: "https://doi.org/XX.XXXX/XXXXX"}

abstract: >-
  Visual data is increasingly consumed by machine-vision systems rather than by human observers. Image Coding for Machines (ICM) compresses images assuming the main observer is a computer vision application and that the human observer needs to inspect or validate the decisions. Inspired by just-noticeable distortion, we cap human-observed quality at a desired level and devote the remaining bits to machine performance. Specifically, joint compression-segmentation training is recast as a constrained optimization problem in which the codec must meet a predefined acceptable target visual quality while a task term consumes the remaining coding capacity. This paper proposes two variants of a penalty function that guides the quality toward the target: an absolute function and a bilinear function, the latter applying a steeper slope once the target visual quality is exceeded. Experimental results show that, under the quality constraint, the proposed method achieves BD-rates of &minus;22.82% and &minus;29.81% relative to an unconstrained joint rate&ndash;distortion&ndash;task optimization and a simple rate&ndash;distortion baseline, respectively, showcasing bitrate reduction with the same task performance. This is achieved while the codec also meets the target visual quality with a reasonable error and without adding any complexity overhead.

# INDEX TERMS: uncomment and replace with the paper's own keyword list, comma
# separated and in the order the paper prints them, then delete this note.
# index_terms: KEYWORD, KEYWORD, KEYWORD

# Once published: change @misc to @inproceedings or @article, add booktitle or
# journal plus address, month, pages, publisher and doi, and drop the arXiv
# fields if the publisher version supersedes the preprint.
bibtex: |-
  @misc{phamdinh2026quality,
    author        = {Pham-Dinh, Khoa and Nami, Sanaz and
                     Rezazadegan Tavakoli, Hamed and Gabbouj, Moncef and
                     Pakdaman, Farhad},
    title         = {You've Seen Enough: Quality-Constrained Image Coding For Machines},
    year          = {2026},
    eprint        = {2609.25108},
    archivePrefix = {arXiv},
    primaryClass  = {cs.CV},
    url           = {https://arxiv.org/abs/2609.25108}
  }

# FOOTER: uncomment once the paper is published and replace the line with the
# publisher's required notice, copying the wording used by the sibling paper for
# that publisher (casr and vcm-segmentation carry the IEEE notice, oxygen-gait
# carries the CC BY notice), then delete this note. It stays commented until then
# because an empty footer still draws its top rule.
# footer:
#   - '&copy; YYYY PUBLISHER. PUBLISHER&#8217;S REQUIRED COPYRIGHT NOTICE.'

# Google Scholar indexing: only the tags that are true today.
citation:
  - [citation_title, 'You''ve Seen Enough: Quality-Constrained Image Coding For Machines']
  - [citation_author, 'Pham-Dinh, Khoa']
  - [citation_author, 'Nami, Sanaz']
  - [citation_author, 'Rezazadegan Tavakoli, Hamed']
  - [citation_author, 'Gabbouj, Moncef']
  - [citation_author, 'Pakdaman, Farhad']
# SCHOLAR PLACEHOLDERS: add each line only once that fact exists, replace the
# capitalised placeholder with the real value, delete the lines that do not apply
# (a conference paper has no journal title, a journal paper has no conference
# title), then delete this note. Never leave a guessed date, venue or PDF URL
# here: Scholar indexes whatever it finds and a wrong citation is hard to undo.
#   - [citation_conference_title, 'VENUE NAME']
#   - [citation_journal_title, 'JOURNAL NAME']
#   - [citation_publisher, 'PUBLISHER']
#   - [citation_publication_date, 'YYYY/MM/DD']
#   - [citation_volume, 'VOLUME']
#   - [citation_issue, 'ISSUE']
#   - [citation_firstpage, 'FIRST']
#   - [citation_lastpage, 'LAST']
#   - [citation_doi, 'XX.XXXX/XXXXX']
#   - [citation_pdf_url, 'https://khoaphamdinh.com/papers/quality-constrained-coding.pdf']
---
