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
  # Developer Hero - Gradient background with name, role, social, and CTAs
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
        - text: View My Work
          url: "#portfolio"
          icon: arrow-down
        - text: Get In Touch
          url: "#contact"
          icon: envelope
    design:
      style: centered
      avatar_shape: circle
      animations: true
      background:
        color:
          light: "#fafafa"
          dark: "#0a0a0f"
      spacing:
        padding: ["6rem", "0", "4rem", "0"]
  
  # Filterable Portfolio - Alpine.js powered project filtering
  - block: portfolio
    id: portfolio
    content:
      title: "Portfolio"
      subtitle: ""
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
          dark: "#0d0d12"
      spacing:
        padding: ["4rem", "0", "4rem", "0"]
  
  # Visual Tech Stack - Icons organized by category
  - block: tech-stack
    id: toolkit
    content:
      title: "Analytical Toolkit"
      subtitle: "The industry-standard tools driving our robust and reproducible biomedical data analysis and structural biology services."
      categories:
        - name: Bioinformatics & Statistics
          items:
            - name: R
              icon: custom/r
            - name: Python
              icon: custom/python
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
          light: "#f5f5f5"
          dark: "#08080c"
      spacing:
        padding: ["4rem", "0", "4rem", "0"]
  

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
  #         dark: "#08080c"
  #     spacing:
  #       padding: ["4rem", "0", "4rem", "0"]
  
  # Contact Section
  - block: contact-info
    id: contact
    content:
      title: Get In Touch
      subtitle: "Let's build something amazing together"
      text: |-
        I'm always interested in hearing about new projects and opportunities.
        Whether you're looking to hire, collaborate, or just want to say hi, feel free to reach out!
      email: analyticsdlf@gmail.com
      autolink: true
    design:
      columns: '1'
      background:
        color:
          light: "#ffffff"
          dark: "#0d0d12"
      spacing:
        padding: ["4rem", "0", "4rem", "0"]
---
