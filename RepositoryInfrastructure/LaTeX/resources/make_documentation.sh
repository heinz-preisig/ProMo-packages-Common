cd $1

latex -interaction=nonstopmode main.tex ;\
latex -interaction=nonstopmode main.tex ;\
dvips main.dvi ;\
ps2pdf main.ps ;\
evince main.pdf &


if [ $? -eq 0 ]
 then
   rm *.dvi ;\
   rm *.ps ;\
   rm *.bbl ;\
   rm *.aux ;
   rm *.blg ;
fi


