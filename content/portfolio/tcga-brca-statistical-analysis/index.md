---
title: "Advanced Clinical Biostatistics & Survival Modeling in R"
date: 2026-03-26
summary: "An automated, STROBE-compliant biostatistical pipeline querying the GDC API to evaluate the prognostic impact of AJCC Tumor Staging on overall survival in the TCGA-BRCA cohort."
tags:
  - Biostatistics
  - Survival Analysis
  - R
  - Oncology
  - Genomics
links:
  - type: code
    icon: brands/github
    url: https://github.com/Dhafir85/tcga-brca-statistical-analysis
    label: GitHub
featured: true
role: "Lead Bioinformatician"
duration: "1 month"
team_size: 1
highlights:
  - "Automated NCI GDC API data ingestion using TCGAbiolinks"
  - "Publication-grade, STROBE-compliant demographics via gtsummary"
  - "Diagnostic age consistency check across stages via One-Way ANOVA"
  - "Prognostic evaluation of AJCC tumor staging via Kaplan-Meier curves (p < 0.0001)"
---

## Executive Summary

This analysis evaluates the prognostic impact of AJCC Tumor Staging on overall survival within the Breast Invasive Carcinoma (TCGA-BRCA) cohort. By deploying an automated, end-to-end biostatistical pipeline, we extracted and transformed raw hospital registry data into STROBE-compliant clinical insights. 

The primary finding reveals a statistically profound divergence in mortality rates across tumor stages ($p < 0.0001$), while confirming that the age of diagnostic onset remains consistent across all stages, eliminating it as a primary confounding variable.

---

## Methodology & Pipeline Architecture

To guarantee absolute computational reproducibility, this project strictly avoids manual flat-file downloads. Data extraction is fully scripted and automated directly from the National Cancer Institute (NCI) Genomic Data Commons (GDC) API.

The pipeline is structured into five distinct computational phases:

```
┌────────────────────────┐      ┌────────────────────────┐      ┌────────────────────────┐
│  Phase I: Acquisition  │ ───▶ │  Phase II: Cleaning    │ ───▶ │  Phase III: Baseline   │
│  Query NCI GDC API via │      │  Standardize metrics,  │      │  Generate demographic  │
│  TCGAbiolinks package  │      │  collapse tumor stages │      │  tables (gtsummary)    │
└────────────────────────┘      └────────────────────────┘      └────────────────────────┘
                                                                            │
                                                                            ▼
┌────────────────────────┐      ┌────────────────────────┐      ┌────────────────────────┐
│  Phase V: Discussion   │ ◀─── │  Phase V: Time-to-Event│ ◀─── │  Phase IV: ANOVA       │
│  Interpret clinical    │      │  Kaplan-Meier survival │      │  Confirm age variance  │
│  weight of AJCC stages │      │  profiles & Log-Rank   │      │  uniformity (p=0.4902) │
└────────────────────────┘      └────────────────────────┘      └────────────────────────┘
```

---

## Technical Implementation & Computational Phases

### Phase I: Programmatic Data Acquisition
The pipeline query dynamically retrieves the clinical dataset for the Breast Invasive Carcinoma (TCGA-BRCA) cohort using the `TCGAbiolinks` Bioconductor package. It implements local data caching logic to avoid redundant downloads:
```R
# Querying GDC API for clinical datasets
clinical_brca <- GDCquery_clinic(project = "TCGA-BRCA", type = "clinical")
```

### Phase II: Data Preprocessing & Standardization
Clinical registry data contains inconsistent formatting and missing values. The pipeline cleans, transforms, and subsets the matrix by:
- Deriving diagnostic age in years from raw days of age (`Age_at_Diagnosis_Years = age_at_diagnosis / 365.25`).
- Collapsing highly stratified AJCC stages into broader analytical categories (`Stage I`, `Stage II`, `Stage III`, `Stage IV`) for statistical power.
- ordered factoring to ensure models and tables sort stages correctly.

### Phase III: Cohort Demographics (STROBE Guidelines)
Summarized patient population variables using medians and interquartile ranges (IQR) for non-normality, and frequencies/proportions for categorical variables. The pipeline leverages `gtsummary` to build baseline characteristics tables (Table 1) and runs univariable hypothesis testing across the strata (Kruskal-Wallis and Fisher's exact tests).

### Phase IV: Diagnostic Age Variance Verification (ANOVA)
To ensure the survival differences seen in later stages are not confounded by advanced age at diagnosis, we computed a **One-Way Analysis of Variance (ANOVA)**. 
- The ANOVA test reveals no statistically significant variance in age of diagnostic onset across the four tumor stages ($p = 0.4902$).
- The median age remains heavily concentrated near 60 years across all cohorts.

### Phase V: Time-to-Event Survival Modeling (Kaplan-Meier)
Overall survival (OS) time was modeled in months alongside binary encoding for vital status (event of interest vs. right-censoring). We fit a Kaplan-Meier model using the `survival` package and evaluated the divergence of the survival trajectories:
- The log-rank test shows a highly significant difference in overall survival probabilities ($p < 0.0001$).
- Stages I, II, and III display a progressive, gradual decline over a 150-month horizon.
- Stage IV presents a precipitous survival drop, falling below 25% within the first 60 months.

---

## Tech Stack & Packages

- **Language:** R (v4.3+) with Quarto Literate Programming
- **Data Acquisition:** `TCGAbiolinks` (Bioconductor)
- **Cleaning & Visualization:** `dplyr`, `stringr`, `ggplot2` (tidyverse)
- **Clinical Tables:** `gtsummary` (STROBE-compliant formatting), `gt`, `broom`
- **Survival Modeling:** `survival` (KM & Cox models), `survminer` (survival plots)

---

## How to Run the Analysis

The complete codebase, processed data configurations, and Quarto templates are available on GitHub.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Dhafir85/tcga-brca-statistical-analysis.git
   ```
2. **Install R dependencies:**
   ```R
   if (!require("BiocManager", quietly = TRUE))
       install.packages("BiocManager")
   BiocManager::install(c("TCGAbiolinks", "DESeq2", "survival", "survminer", "gtsummary", "gt"))
   ```
3. **Render the Quarto HTML report:**
   ```bash
   quarto render TCGA_analysis.qmd
   ```
