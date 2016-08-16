from IPython.core.display import display, HTML
display(HTML("""<style>

@font-face {
    font-family: 'Cooper Hewit' ;
    src: url(utils/CooperHewitt-Medium.otf);
}

@font-face {
    font-family: 'Cooper Hewit Bold' ;
    src: url(utils/CooperHewitt-Bold.otf);
}

@font-face {
    font-family: 'Cooper Hewit Light' ;
    src: url(utils/CooperHewitt-Light.otf);
}

.container {
    width:96% !important;
    font-family: 'Cooper Hewit','Source Sans Pro', 'Open Sans', 'Helvetica', Sans;
}

.text_cell_render h1 {
    text-align: center;
    font-family: 'Cooper Hewit Light';
    font-size: 52px;
}

h2, h3 {
    font-family: 'Cooper Hewit Bold' ;
}

.text_cell_render p,
.text_cell_render h2,
.text_cell_render h3,
.text_cell_render h4,
.text_cell_render ul,
.text_cell_render ol,
.text_cell_render table {
    max-width: 860px;
    margin: 0 auto;
    line-height: 30px;
}

.text_cell_render p,
.text_cell_render ul,
.text_cell_render ol,
.text_cell_render table {
    font-family: 'Cooper Hewit' ;
    font-size: 20px;
    padding-bottom : 26px;
}

.text_cell_render h4 {
    font-size: 20px;
    text-align: center;
}

.text_cell.rendered .input_prompt {
    display : none !important;
}

.text_cell_render table {
    width: 860px;
    margin: 26px auto;
    text-align: center;
}

.text_cell_render td,
.text_cell_render th {
    padding: 8px;
    text-align: center;
}

.text_cell_render table thead {
    background-color: #333;
    color: white;
    font-family: 'Cooper Hewit Light';
    text-align: center;
}

.CodeMirror {
    padding: 8px 20px;
}
.CodeMirror pre {
    font-size: 20px;
    line-height: 28px;
}

div.output_text pre {
    color: #333;
    font-size: 18px;
    line-height: 26px;
}
.output_png img{
    margin: 0 auto;
    margin-top: 12px;
    display: block;
    min-width: 600px;
}
</style>"""))