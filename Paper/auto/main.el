(TeX-add-style-hook
 "main"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("IEEEtran" "journal")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("biblatex" "style=ieee") ("subfig" "caption=false")))
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "url")
   (TeX-run-style-hooks
    "latex2e"
    "IEEEtran"
    "IEEEtran10"
    "biblatex"
    "amsmath"
    "url"
    "graphicx"
    "float"
    "subfig"
    "todonotes")
   (LaTeX-add-labels
    "fig:3dplot_plane"
    "fig:circles"
    "eq:phi_OG"
    "eq:phi_constant"
    "fig:size1"
    "fig:size3"
    "fig:size7"
    "fig:random"
    "fig:2noise"
    "fig:1noise"
    "fig:noiseplots"))
 :latex)

