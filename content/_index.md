---
# Leave the homepage title empty to use the site title
title: ''
summary: ''
date: 2026-01-05
type: landing

design:
  # Default section spacing
  spacing: '0'

sections:
  # Primary introduction
  - block: dev-hero
    id: hero
    content:
      username: me
      greeting: ""
      show_status: false
      show_scroll_indicator: false
      typewriter:
        enable: false
        prefix: "I build"
        strings:
          - "full-stack web apps"
          - "scalable APIs"
          - "beautiful UIs"
          - "open source tools"
        type_speed: 70
        delete_speed: 40
        pause_time: 2500
      cta_buttons:
        - text: Explore Our Services
          url: "#services"
          icon: arrow-down
        - text: Discuss a Project
          url: "#contact"
          icon: envelope
    design:
      style: centered
      avatar_shape: circle
      animations: true
      background:
        color:
          light: "#ffffff"
          dark: "#ffffff"
      spacing:
        padding: ["7rem", "0", "5rem", "0"]

  # Services
  - block: service-grid
    id: services
    content:
      title: "Capabilities"
      text: "Focused computational support for biomedical researchers—from study design and statistical modeling to reproducible analysis and publication-ready outputs."
      items:
        - title: "Biostatistics"
          text: "Study design, hypothesis testing, regression, survival analysis, longitudinal models, and clear statistical reporting."
        - title: "Bioinformatics"
          text: "Reproducible workflows for genomic and transcriptomic data, functional interpretation, and pathway-level insight."
        - title: "Bioimage Analysis"
          text: "Quantitative workflows for microscopy and pathology images using reproducible segmentation, measurement, and quality control."
        - title: "Molecular Docking & Dynamics"
          text: "Structure preparation, virtual screening, binding-pose assessment, simulation setup, trajectory analysis, and transparent stability summaries."
    design:
      background:
        color:
          light: "#ffffff"
      spacing:
        padding: ["5rem", "0", "5rem", "0"]
  
  # Project portfolio
  - block: portfolio
    id: portfolio
    content:
      title: "Selected Work"
      subtitle: "A growing collection of reproducible biomedical analysis case studies."
      count: 0
      filters:
        folders:
          - portfolio
      buttons: []
      default_button_index: 0
      # Archive link auto-shown if more projects exist than 'count' above
      # archive:
      #   enable: false  # Set to false to explicitly hide
      #   text: "Browse All"  # Customize text
      #   link: "/work/"  # Custom URL
    design:
      columns: 3
      background:
        color:
          light: "#ffffff"
          dark: "#ffffff"
      spacing:
        padding: ["5rem", "0", "5rem", "0"]
  
  # Visual Tech Stack - Icons organized by category
  - block: tech-stack
    id: toolkit
    content:
      title: "Analytical Toolkit"
      subtitle: "Established tools selected to match the scientific question—not the other way around."
      categories:
        - name: Bioinformatics & Statistics
          items:
            - name: R
              icon: custom/r
            - name: Python
              icon: custom/python_color
            - name: GraphPad Prism
              icon: custom/prism
            - name: KNIME
              icon: custom/knime
            - name: Bash
              icon: custom/bash
            - name: Cytoscape
              icon: custom/cytoscape
        - name: Bioimage Analysis
          items:
            - name: QuPath
              icon: custom/qupath
            - name: CellProfiler
              icon: custom/cellprofiler
            - name: CellProfiler Analyst
              icon: custom/cellprofiler_analyst
            - name: Ilastik
              icon: custom/ilastik
            - name: ImageJ
              icon: custom/imagej
        - name: Structural Biology
          items:
            - name: GROMACS
              icon: custom/gromacs
            - name: AutoDock Vina
              icon: custom/vina
            - name: PyMOL
              icon: custom/pymol
            - name: UCSF Chimera
              icon: custom/chimera
            - name: Avogadro
              icon: custom/avogadro
        - name: Cloud Platforms
          items:
            - name: AWS
              icon: custom/aws
            - name: Google Cloud
              icon: custom/google_cloud
            - name: Microsoft Azure
              icon: custom/microsoft_azure
    design:
      style: grid
      show_levels: false
      background:
        color:
          light: "#ffffff"
          dark: "#ffffff"
      spacing:
        padding: ["5rem", "0", "5rem", "0"]
  

  # Recent Blog Posts
  # - block: collection
  #   id: blog
  #   active: false
  #   content:
  #     title: Recent Posts
  #     subtitle: 'Thoughts on web development, tech, and more'
  #     text: ''
  #     filters:
  #       folders:
  #         - blog
  #       exclude_featured: false
  #     count: 3
  #     order: desc
  #   design:
  #     view: card
  #     columns: 3
  #     background:
  #       color:
  #         light: "#f5f5f5"
  #         dark: "#ffffff"
  #     spacing:
  #       padding: ["4rem", "0", "4rem", "0"]
  
  # Contact Section
  - block: contact-info
    id: contact
    content:
      title: Get In Touch
      subtitle: "Tell us about your research question"
      text: |-
        Share your research objective, data type, current stage, and expected output.
        We will respond with focused next steps and any questions needed to define the analytical scope.
      email: analyticsdlf@gmail.com
      autolink: true
    design:
      columns: '1'
      background:
        color:
          light: "#ffffff"
          dark: "#ffffff"
      spacing:
        padding: ["5rem", "0", "5rem", "0"]
---
