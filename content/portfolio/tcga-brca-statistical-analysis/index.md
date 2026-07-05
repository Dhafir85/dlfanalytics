---
title: "TCGA-BRCA Statistical Analysis"
date: 2026-07-05
summary: "Comprehensive statistical analysis, survival profiling, and differential gene expression analysis of The Cancer Genome Atlas Breast Invasive Carcinoma (TCGA-BRCA) dataset."
tags:
  - Bioinformatics
  - Biostatistics
  - Data Analysis
  - R
  - Oncology
links:
  - type: code
    icon: brands/github
    url: https://github.com/Dhafir85/tcga-brca-statistical-analysis
    label: GitHub
featured: true
role: "Lead Bioinformatician"
duration: "3 months"
team_size: 1
highlights:
  - "Differential gene expression profiling using DESeq2"
  - "Survival analysis via Kaplan-Meier curves & Cox Proportional Hazards"
  - "Molecular subtype (PAM50) genomic-clinical correlations"
  - "Functional pathway enrichment using GSEA and GSVA"
---

An end-to-end bioinformatics and biostatistics pipeline to analyze genomic, transcriptomic, and clinical profiles of breast cancer patients from the GDC Data Portal.

## Overview

Breast cancer is a highly heterogeneous disease characterized by distinct molecular subtypes (Luminal A, Luminal B, HER2-enriched, Basal-like, and Normal-like). This project establishes a robust statistical pipeline to analyze **The Cancer Genome Atlas Breast Invasive Carcinoma (TCGA-BRCA)** dataset, identifying key prognostic biomarkers, differential expression patterns, and clinical associations.

## Key Features

### 1. Data Curation & Quality Control
- **Data Retrieval:** Programmatic fetching of RNA-Seq count matrices and clinical metadata using the `TCGAbiolinks` R/Bioconductor package.
- **Preprocessing:** Quality control filtering, low-count filtering, and normalization (TMM/RLE) to ensure robust downstream statistical comparisons.
- **Batch Correction:** Correction for technical covariates and batch effects using `sva` (Surrogate Variable Analysis) and `ComBat`.

### 2. Differential Gene Expression Analysis (DGEA)
- **Contrast Modeling:** Implemented generalized linear models in `DESeq2` and `edgeR` to identify differentially expressed genes (DEGs) across clinical stages, tumor vs. normal tissue, and molecular subtypes.
- **Visualizations:** Custom generation of Volcano plots, PCA plots, and hierarchical clustering heatmaps (`ComplexHeatmap`) to display transcriptomic variations.

### 3. Survival & Prognostic Profiling
- **Kaplan-Meier Estimators:** Modeled overall survival (OS) and disease-free survival (DFS) across molecular subtypes and high/low expression cohorts.
- **Cox Proportional Hazards:** Built multivariate Cox regression models to calculate hazard ratios (HR) and identify independent prognostic indicators while adjusting for age, stage, and treatment.

### 4. Functional Enrichment & Subtyping
- **PAM50 Subtyping:** Correlated expression patterns with PAM50 classification to evaluate subtype-specific gene signatures.
- **Pathway Analysis:** Performed Gene Set Enrichment Analysis (GSEA) and Gene Set Variation Analysis (GSVA) to highlight perturbed KEGG/Reactome pathways and Gene Ontology (GO) terms.

## Bioinformatics Pipeline

```
┌─────────────────┐      ┌───────────────────┐      ┌─────────────────┐
│ TCGAbiolinks R  │ ───▶ │ DESeq2 Modeling   │ ───▶ │ Survival & Cox  │
│ (Data Curation) │      │ (Gene Expression) │      │ (Clinical OS)   │
└─────────────────┘      └───────────────────┘      └─────────────────┘
                                   │                         │
                                   ▼                         ▼
                         ┌───────────────────┐      ┌─────────────────┐
                         │ GSEA Enrichment   │      │ Shiny Dashboard │
                         │ (Pathway Analysis)│      │ (Interactive)   │
                         └───────────────────┘      └─────────────────┘
```

## Technical Implementation

- **Expression Modeling:** Modeled discrete counts using negative binomial distributions (`DESeq2`) to robustly handle overdispersion in transcriptomic data.
- **Multiple Testing Correction:** Applied the Benjamini-Hochberg (BH) false discovery rate correction to adjust p-values and minimize false positives.
- **Clinical Integration:** Integrated clinical phenotypes (ER, PR, HER2 status) to validate gene signature responsiveness.

## Key Results

- 📊 **Prognostic Biomarkers:** Identified a 10-gene transcriptomic signature highly associated with reduced overall survival in triple-negative breast cancer (TNBC) patients.
- 🧬 **Subtype Discrimination:** Demonstrated clear separation of PAM50 subtypes (specifically Basal-like vs Luminal A) in unsupervised PCA plots.
- 📈 **Validation:** Cross-validated Cox regression hazard models showing high performance (C-index > 0.78) in predicting patient outcomes.

## Tech Stack

**Programming & Workflows**
- R (v4.3+)
- Bioconductor
- Quarto / RMarkdown (reporting)

**Bioconductor Packages**
- `TCGAbiolinks` (data acquisition)
- `DESeq2` / `edgeR` (differential expression)
- `ComplexHeatmap` (heatmaps)
- `clusterProfiler` (enrichment analysis)

**Statistical Packages**
- `survival` (Kaplan-Meier & Cox models)
- `survminer` (survival visualization)
- `limma` (linear modeling)

## How to Run the Analysis

All source scripts, RMarkdown notebooks, and statistical outputs are available in the repository.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Dhafir85/tcga-brca-statistical-analysis.git
   ```
2. **Install dependencies:**
   Open R/RStudio and run:
   ```R
   if (!require("BiocManager", quietly = TRUE))
       install.packages("BiocManager")
   BiocManager::install(c("TCGAbiolinks", "DESeq2", "ComplexHeatmap", "survival", "survminer"))
   ```
3. **Execute the pipeline:**
   Run the main analytical script or knit the summary report:
   ```R
   rmarkdown::render("analysis_pipeline.Rmd")
   ```

---
