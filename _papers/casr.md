---
# ================= THE DOI SWITCH =================
# This page is the stable khoaphamdinh.com landing page for the paper, linked
# from the homepage publication list. The CV prints the permanent link
# https://khoaphamdinh.com/p/casr, which forwards here. Today this URL shows
# the accepted manuscript.
#
# When the publisher assigns a DOI, the ONE line directly below can turn this
# page into a redirect:
#   1. Uncomment it, by deleting the "# " at the start of the line.
#   2. Replace XX.XXXX/XXXXX with the real DOI.
# Save, commit, push. This URL then redirects straight to the publisher page,
# in every browser, with no JavaScript involved.
#
# Think twice before switching: this page carries the Best Student Paper Award
# note, which the publisher page does not. Pointing /p/casr at the DOI instead
# sends CV readers to the publisher and leaves this page as it is.
# ==================================================
# doi_redirect: https://doi.org/XX.XXXX/XXXXX

number: 3
group: peer-reviewed
title: 'CASR: Content-Adaptive Neural Super-Resolution Post-Filter for Versatile Video Coding via Low-Rank Overfitting'
description: 'A content-adaptive super-resolution post-filter for Versatile Video Coding, based on encoder-side overfitting with Low-Rank Adaptation (LoRA). Best Student Paper Award, IEEE MMSP 2026, Istanbul.'

authors:
  - {name: Khoa Pham-Dinh, me: true, sup: "*,1,2,3"}
  - {name: Francesco Cricri, sup: "1"}
  - {name: Maria Santamaria, sup: "1"}
  - {name: Honglei Zhang, sup: "1"}
  - {name: Hamed R. Tavakoli, list_name: Hamed Rezazadegan Tavakoli, sup: "1,2"}
  - {name: Moncef Gabbouj, sup: "3"}
  - {name: Juho Kannala, sup: "2"}
  - {name: Miska M. Hannuksela, sup: "1"}
affiliations: '<sup>1</sup>Nokia &nbsp;&middot;&nbsp; <sup>2</sup>Aalto University &nbsp;&middot;&nbsp; <sup>3</sup>Tampere University'
corresponding: '<sup>*</sup>Corresponding author: <a href="mailto:khoa.phamdinh@aalto.fi">khoa.phamdinh@aalto.fi</a>. Khoa Pham-Dinh was a student at Tampere University during part of the work.'

venue: '<em>IEEE International Workshop on Multimedia Signal Processing (MMSP). Istanbul, Turkey, 22&ndash;24 September 2026.</em>'
list_venue: '<em>IEEE International Workshop on Multimedia Signal Processing (MMSP)</em>, 2026.'
award: mmsp2026-best-student-paper

links:
  - {label: arXiv, url: "https://arxiv.org/abs/2609.37328"}
actions:
  - {label: Read the PDF, url: /papers/casr.pdf}
  - {label: Read on arXiv, url: "https://arxiv.org/abs/2609.37328"}

abstract: >-
  The use of super-resolution as a post-processing step following a video codec allows videos to be encoded at reduced spatial resolution at the encoder side and to be reconstructed and upsampled to the original resolution at the decoder side. In this way, the required bitrate is reduced and the quality of the reconstructed frames is improved without modifying the core coding architecture. However, generic SR models are typically trained offline and lack sufficient adaptability to the diverse content characteristics and compression artifacts produced by video codecs, which limits their effectiveness during test time. To address the limitation, this paper proposes CASR (Content-Adaptive Super-Resolution), a content-adaptive SR post-filter framework for Versatile Video Coding (VVC), based on encoder-side overfitting on each input sequence. In order to limit the bitrate overhead required for signalling the content adaptation signal, i.e., the weight-update, Low-Rank Adaptation (LoRA) is leveraged. The method freezes the convolution kernels of a pretrained SR network and fine-tunes only lightweight rank-<em>r</em> matrices attached to selected convolution layers, using VVC decoded frames and quantization-parameter (QP) maps of test sequences as supervision. The resulting low-rank update is compressed with the MPEG Neural Network Compression and Representation (NNR) standard. Experiments on the JVET common test conditions (CTC) class A1 and A2 sequences indicate that LoRA-based content adaptation provides bitrate savings over a non-adapted SR post-filter at a small signalling cost. Compared with the VVC Test Model (VTM 21.0), the proposed method achieves BD-rate savings of &minus;10.93% (Y), &minus;15.39% (U), &minus;24.41% (V) under random access and &minus;13.43% (Y), &minus;5.75% (U), &minus;22.94% (V) under all-intra. An ablation of the LoRA rank <em>r</em> further shows that <em>r</em>=4 provides the best trade-off between coding gain and signalling cost.
index_terms: 'video coding, post filtering, super resolution, content adaptation, low-rank adaptation, VVC, VSEI, NNR'

# When the DOI is issued: add doi = {10.1109/XXXXXXX.2026.XXXXXXX},
# with the real DOI.
bibtex: |-
  @inproceedings{phamdinh2026casr,
    author    = {Pham-Dinh, Khoa and Cricri, Francesco and Santamaria, Maria and
                 Zhang, Honglei and Tavakoli, Hamed R. and Gabbouj, Moncef and
                 Kannala, Juho and Hannuksela, Miska M.},
    title     = {{CASR}: Content-Adaptive Neural Super-Resolution Post-Filter for
                 Versatile Video Coding via Low-Rank Overfitting},
    booktitle = {2026 IEEE International Workshop on Multimedia Signal Processing (MMSP)},
    address   = {Istanbul, Turkey},
    month     = sep,
    year      = {2026},
    publisher = {IEEE}
  }

footer:
  - 'This page hosts the author&#8217;s accepted version of the manuscript. The final published version will be available from the publisher once it appears.'
  - '&copy; 2026 IEEE. Personal use of this material is permitted. Permission from IEEE must be obtained for all other uses, in any current or future media, including reprinting/republishing this material for advertising or promotional purposes, creating new collective works, for resale or redistribution to servers or lists, or reuse of any copyrighted component of this work in other works.'

# Google Scholar indexing
citation:
  - [citation_title, 'CASR: Content-Adaptive Neural Super-Resolution Post-Filter for Versatile Video Coding via Low-Rank Overfitting']
  - [citation_author, 'Pham-Dinh, Khoa']
  - [citation_author, 'Cricri, Francesco']
  - [citation_author, 'Santamaria, Maria']
  - [citation_author, 'Zhang, Honglei']
  - [citation_author, 'Tavakoli, Hamed R.']
  - [citation_author, 'Gabbouj, Moncef']
  - [citation_author, 'Kannala, Juho']
  - [citation_author, 'Hannuksela, Miska M.']
  - [citation_conference_title, 'IEEE International Workshop on Multimedia Signal Processing (MMSP)']
  - [citation_publication_date, '2026/09/22']
  - [citation_pdf_url, 'https://khoaphamdinh.com/papers/casr.pdf']
---
