%rebase('layout.tpl', title=title)
%#template to generate an HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<h1>Make a Blender Wish</h1>
<form action="/makewish" method="post">
  Project name:           <input name="wish_name" type="text" /><br>
  Render engine:          <select name="en">
                            %for en in enginelist:
                              <option value="{{en[0]}}">{{en[1]}}</option>
                            %end #for
                          </select><br>
  Frame type:             <select name="ft">
                            %for ft in frametypelist:
                              <option value="{{ft[0]}}">{{ft[1]}}</option>
                            %end #for
                          </select><br>
  Blender major version:  <input name="maj_ver" type="number" value="2"><br>
  Blender minor version:  <input name="min_ver" type="number" value="73"><br>
  Blender version suffix: <input name="ver_suf" type="text"><br>
  First frame to render:  <input name="fr1" type="number" value="1"><br>
  Last frame to render:   <input name="frn" type="number"><br>
  <input value="MakeWish" type="submit" />
</form>
