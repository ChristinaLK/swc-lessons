HOW TO
------

These slides are built using ipython notebook and a javascript library called reveal.js, also contained in this folder.  

To layout the slide deck, open ipython notebook (at least version ?) and click the arrow next to "Cell Toolbar" and select "Slideshow".  This will change all your cells so they have a little drop down menu in the right hand corner.  Your options are:

* Slide: new slide (reached by paging right)
* Sub-slide: slide that moves upwards to replace the previous slide (reached by paging down)
* Fragment: adds to whatever is already on the screen, but doesn't replace it like sub-slide
* Skip: don't know what this does
* Notes: For you or others, not printed as slides

To put stuff in, change each cell's format to markdown and then put in your text/images.  For some handy tips on text formatting/images in markdown, see [this style guide](link) or [this style guide](link).

Once you've made your slides, you need to compile/convert them into an html file.  To do this, you must run the very specific command:

~~~
$ipython nbconvert my_slides.ipynb --to slides --post serve
~~~

I've chucked this into a bash script named "make_slides.sh" that takes one argument (where "my_slides.ipynb" is listed above) so I don't need to remember it.  

Hopefully this should compile your slides and pop them up in a new tab on your browser.  

Potential issues:

* You need a couple of other tools for the compile to work: at least pandoc, and possibly jekyll.  If it doesn't compile, read the error message - it will probably tell you what you need to install.  
* I've found this works best if ipython notebook is already open when I do the compile step.  
* If you push the converted slides to github on the gh-pages branch, github will render them nicely on a website.  