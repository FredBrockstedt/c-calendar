#!/usr/bin/env python

"""
convert .css files stored in config variable cssFiles into a single, small file called minify.css
"""
#imports
import cssmin as mini # not maintained, but does the job

### config
# files that are going to be combined
cssFiles = [  
    ["../cv6/", "styles.css"],
    ["fullcalendar-3.5.1/", "fullcalendar.css"],
    ["lib/css/", "jquery-ui.min.css"],
    ["", "custom.css"],
    ["", "c-base.css"]
]

removeComments = True # remove comments in css files: yes/no?

css = "" # string that stores the content of all css files

### helper functions
def extend_url(css, path):
    "look through css, replace any 'url(' occurance to fit path"
    # with quotes
    css = css.replace('url("', "url(\"%s" % path)
    # without quotes
    #css = css.replace('url(', "url(%s" % path)
    return css

### main
# read all files into one large buffer
for path, cssFile in cssFiles:
    with open(path+cssFile, 'r') as f:
        css += extend_url(f.read(), path)

# minify all the css
minified = mini.cssmin(css)
compressionrate = 1-(len(minified)/len(css))
print(" compressed: %.1f%%" % (100*compressionrate))

# write out the new css file
with open("minify.css", 'w') as f:
    f.write(minified)
