%rebase('layout.tpl', title=title)
%#Template to modify a single project parameter.
%#edit_action is the URL that will be called.
%#edit_desc is the description of the parameter to update.
%#edit_type is the type of input field to use.
%#edit_value is the current value (if a single value) or the list of permitted values (if a foreign key)
<h1>{{title}}</h1>
<form action="{{edit_action}}" method="post" enctype='multipart/form-data'>
%if edit_type == "select":
  {{edit_desc}} <select name="returnvalue">
                  %for item in edit_value:
                    <option value="{{item[0]}}">{{item[0]}}</option>
                  %end #for
                </select><br>
%else: 
  {{edit_desc}}: <input name="returnvalue" type="{{edit_type}}" /><br>
%end #if
  <input value="Submit change" type="submit" />
</form>
