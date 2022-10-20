Flying Karate Masters: Matthew Yee, Kevin Li, Joseph Wu
SoftDev
K13: Stuylin' & Wylin' & Profilin'
2022-10-19
time spent: 0.2 hours

Inline Styling
<tag></tag>
<tag style = "styling here">

seperate property and value using ';' and just add a ' ' to add more properties
ex:

color - effects color of text
background color - effects color of background
text-align - aligns text to a specified orientation. Use center to center text
font-family - controlling what font the text displays
padding - puts a space inbetween text and its edge. can add -left, -right, -top and -bottom. The values can be __px or __%.
<span> - tag is an inline container used to mark up a part of text, or a document without creating a new element like a <p>
vertical-align: align element vertically relative to the parent element, top, middle, bottom
margin - space between text and edge of element border. -top, -right, -left, -bottom, __px, __%
width - control the width of the element's border, __px, __%
display - sets whether an element is treated as a block or inline element, block, inline, inline-block, flex, inline-flex, grd, inline-grid, flow-root, etc. Ex display: inline-block;

Internal Styling
<h1 class = "class">
    ldskjflaskjfl;
</h1>

In order to style use:

<style>
h1 {
    styling here
}
    or
.class {
    styling here
}
</style>

External Styling
<head> 
    <link 
    rel="stylesheet"
    type="text/css"
    href="FILENAME">
</head>

Note: "FILENAME" must contain the route to the CSS file if the CSS file and HTML file are not in the same directory.
