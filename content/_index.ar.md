---
title: ''
summary: 'تحليل البيانات الطبية الحيوية والبحث الحاسوبي'
date: 2026-01-05
type: landing

design:
  spacing: '0'

sections:
  - block: dev-hero
    id: hero
    content:
      username: me
      greeting: ""
      tagline: "تحليل البيانات الطبية الحيوية والبحث الحاسوبي"
      bio: "نحوّل البيانات السريرية والجينومية وبيانات الصور والبنى الجزيئية المعقّدة إلى أدلة دقيقة، قابلة لإعادة الإنتاج، وجاهزة للنشر."
      show_status: false
      show_scroll_indicator: false
      typewriter:
        enable: false
      cta_buttons:
        - text: استكشف خدماتنا
          url: "#services"
          icon: arrow-down
        - text: ناقش مشروعك
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

  - block: service-grid
    id: services
    content:
      title: "قدراتنا"
      text: "دعم حاسوبي متخصّص للباحثين في العلوم الطبية الحيوية، من تصميم الدراسات والنمذجة الإحصائية إلى التحليل القابل لإعادة الإنتاج والمخرجات الجاهزة للنشر."
      items:
        - title: "الإحصاء الحيوي"
          text: "تصميم الدراسات، واختبار الفرضيات، والانحدار، وتحليل البقاء، والنماذج الطولية، وإعداد تقارير إحصائية واضحة."
        - title: "المعلوماتية الحيوية"
          text: "مسارات عمل قابلة لإعادة الإنتاج لتحليل البيانات الجينومية وبيانات النسخ الجيني، والتفسير الوظيفي، واستخلاص الرؤى على مستوى المسارات الحيوية."
        - title: "تحليل الصور الحيوية"
          text: "مسارات كمية لتحليل صور المجهر والأنسجة المرضية، تشمل التجزئة القابلة لإعادة الإنتاج، والقياس، وضبط الجودة."
        - title: "الالتحام الجزيئي والديناميكيات الجزيئية"
          text: "تحضير البنى، والفحص الافتراضي، وتقييم أوضاع الارتباط، وإعداد المحاكاة، وتحليل المسارات، وتقديم ملخصات واضحة للاستقرار."
    design:
      background:
        color:
          light: "#ffffff"
      spacing:
        padding: ["5rem", "0", "5rem", "0"]

  - block: portfolio
    id: portfolio
    content:
      title: "أعمال مختارة"
      subtitle: "مجموعة متنامية من دراسات الحالة القابلة لإعادة الإنتاج في تحليل البيانات الطبية الحيوية."
      count: 0
      filters:
        folders:
          - portfolio
      buttons: []
      default_button_index: 0
    design:
      columns: 3
      background:
        color:
          light: "#ffffff"
          dark: "#ffffff"
      spacing:
        padding: ["5rem", "0", "5rem", "0"]

  - block: tech-stack
    id: toolkit
    content:
      title: "أدوات التحليل"
      subtitle: "نختار الأدوات المناسبة للسؤال العلمي، لا العكس."
      categories:
        - name: المعلوماتية الحيوية والإحصاء
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
        - name: تحليل الصور الحيوية
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
        - name: البيولوجيا البنيوية
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
        - name: المنصات السحابية
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

  - block: contact-info
    id: contact
    content:
      title: تواصل معنا
      subtitle: "أخبرنا عن سؤالك البحثي"
      connect_title: "لنتواصل"
      text: |-
        شاركنا هدف البحث، ونوع البيانات، والمرحلة الحالية، والمخرجات المتوقعة.
        سنرد عليك بخطوات عملية مركّزة وأي أسئلة لازمة لتحديد نطاق التحليل.
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
