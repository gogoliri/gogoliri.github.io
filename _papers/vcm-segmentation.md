---
# ================= THE DOI SWITCH =================
# The CV links this paper by its DOI. This page is the stable khoaphamdinh.com
# landing page for it, linked from the homepage publication list. Today that URL
# shows this page: abstract, BibTeX, and a link out to the published paper.
# The real DOI is already filled in on the ONE line directly below. Uncommenting
# it - by deleting the "# " at the start of the line - turns this stable URL into
# an instant redirect to the publisher page on IEEE Xplore, in every browser,
# with no JavaScript involved. Save, commit, push.
# It is left commented on purpose: this page carries the standardization-adoption
# note and the award note, which the publisher page does not, and it keeps the
# abstract and BibTeX readable without a publisher paywall or cookie wall.
# ==================================================
# doi_redirect: https://doi.org/10.1109/ISM66958.2025.00038

number: 2
group: peer-reviewed
title: 'Evaluating the Emerging MPEG Video Coding for Machines in Semantic Segmentation'
description: 'An evaluation methodology for MPEG Video Coding for Machines on semantic segmentation with the PandaSet dataset, benchmarked against VVC and HEVC. IEEE ISM 2025.'

authors:
  - {name: Khoa Pham-Dinh, me: true, sup: "1,2"}
  - {name: Farhad Pakdaman, sup: "1,2"}
  - {name: Honglei Zhang, sup: "2"}
  - {name: Hamed Rezazadegan Tavakoli, sup: "2"}
  - {name: Nam Le, sup: "1,2"}
  - {name: Jukka Ahonen, sup: "1,2"}
  - {name: Moncef Gabbouj, sup: "1"}
affiliations: '<sup>1</sup>Dept. of Computing Sciences, Tampere University &nbsp;&middot;&nbsp; <sup>2</sup>Nokia Technologies'

venue: '<em>2025 IEEE International Symposium on Multimedia (ISM). Naples, Italy, 8&ndash;10 December 2025, pp. 141&ndash;148.</em>'
list_venue: '<em>IEEE International Symposium on Multimedia (ISM)</em>, 2025.'
# A candidacy is not an award won: it stays a note, not a badge.
list_note: Candidate for Best Paper Award.
page_note: Candidate for the Best Paper Award.
doi: 10.1109/ISM66958.2025.00038

links:
  - {label: Contribution m67677, url: "/#std-1"}
actions:
  - {label: Read on IEEE Xplore, url: "https://doi.org/10.1109/ISM66958.2025.00038"}

abstract: >-
  Emerging MPEG Video Coding for Machines (MPEG VCM) standardization activities address the growing demand for machine-to-machine visual applications, including video surveillance, autonomous driving, etc. This paper proposes an evaluation methodology tailored to MPEG VCM, with an emphasis on semantic segmentation tasks using the Pandaset dataset. This is a challenging target as standardization works must follow several limitations, such as dataset&#8217;s licensing, fixed tools and software, and compliance with existing common test conditions (CTC) for the standard&#8217;s development. The proposed evaluation methodology includes a step to align Pandaset and COCO labels. Two task networks, Detectron2 and Mask2Former, are used to evaluate the Rate-Performance behavior for semantic segmentation under various coding configurations. The performance of MPEG VCM is benchmarked against traditional codecs (VVC and HEVC), with a detailed analysis of MPEG VCM&#8217;s coding tools. The extensive evaluations reveal interesting observations. (1) Although VCM achieved reasonably good segmentation performance, some of its developed tools, such as temporal resampling and region-of-interest coding, were not well suited for segmentation task. (2) The Hybrid NNVVC Inner Codec outperformed the VVC Inner Codec. (3) VCM&#8217;s performance varies significantly for segmented classes. (4) Despite significant differences in human vision performance, VVC and HEVC exhibit relatively similar performance in machine vision. The main contributions of this work are to (1) enable evaluation of MPEG VCM in a real-world semantic segmentation use case, which is one of VCM&#8217;s targeted tasks, and (2) to provide a detailed assessment of VCM&#8217;s performance in semantic segmentation.
index_terms: 'video compression, video coding for machines, semantic segmentation, autonomous driving, computer vision'

bibtex: |-
  @inproceedings{phamdinh2025vcm,
    author    = {Pham-Dinh, Khoa and Pakdaman, Farhad and Zhang, Honglei and
                 Rezazadegan Tavakoli, Hamed and Le, Nam and Ahonen, Jukka and
                 Gabbouj, Moncef},
    title     = {Evaluating the Emerging {MPEG} Video Coding for Machines in
                 Semantic Segmentation},
    booktitle = {2025 IEEE International Symposium on Multimedia (ISM)},
    address   = {Naples, Italy},
    year      = {2025},
    month     = dec,
    pages     = {141--148},
    publisher = {IEEE},
    doi       = {10.1109/ISM66958.2025.00038}
  }

footer:
  - 'This page is a stable landing page for the paper. The definitive version of record is published by IEEE and is available on IEEE Xplore through the DOI above; no copy of the PDF is hosted here.'
  - '&copy; 2025 IEEE. Personal use of this material is permitted. Permission from IEEE must be obtained for all other uses, in any current or future media, including reprinting/republishing this material for advertising or promotional purposes, creating new collective works, for resale or redistribution to servers or lists, or reuse of any copyrighted component of this work in other works.'

# Google Scholar indexing
citation:
  - [citation_title, 'Evaluating the Emerging MPEG Video Coding for Machines in Semantic Segmentation']
  - [citation_author, 'Pham-Dinh, Khoa']
  - [citation_author, 'Pakdaman, Farhad']
  - [citation_author, 'Zhang, Honglei']
  - [citation_author, 'Rezazadegan Tavakoli, Hamed']
  - [citation_author, 'Le, Nam']
  - [citation_author, 'Ahonen, Jukka']
  - [citation_author, 'Gabbouj, Moncef']
  - [citation_conference_title, '2025 IEEE International Symposium on Multimedia (ISM)']
  - [citation_publisher, 'IEEE']
  - [citation_publication_date, '2025/12/08']
  - [citation_firstpage, '141']
  - [citation_lastpage, '148']
  - [citation_doi, '10.1109/ISM66958.2025.00038']
---
## Standardization impact

The evaluation methodology from this work was adopted into the MPEG Common Test Conditions used to develop the Video Coding for Machines standard (MPEG contribution [m67677](/#std-1), ISO/IEC JTC 1/SC 29/WG 4, April 2024).
