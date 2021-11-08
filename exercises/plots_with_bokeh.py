from bokeh.plotting import figure,show,output_file

output_file("plot.html")

x_categories=["a","b","c","d","e","f","g"]
x= ["a","f","g"]
y=[4,5,6]

f= figure(x_range=x_categories)

f.vbar(x=x,top=y,width=0.5)

show(f)