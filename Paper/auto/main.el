(TeX-add-style-hook
 "main"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("IEEEtran" "journal")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("biblatex" "style=ieee")))
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (TeX-run-style-hooks
    "latex2e"
    "IEEEtran"
    "IEEEtran10"
    "biblatex"
    "amsmath"
    "url"
    "graphicx"
    "float")
   (LaTeX-add-labels
    "fig:3dplot"
    "fig:3dplot_plane"
    "fig:circles"
    "fig:size1"
    "fig:size3"
    "fig:size7"
    "fig:random"
    "fig:nonoise"
    "fig:2noise"
    "fig:1noise"))
 :latex)

