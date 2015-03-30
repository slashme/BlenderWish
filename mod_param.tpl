%rebase('layout.tpl', title=title)
%#Template to modify a single project parameter.
%#edit_action is the URL that will be called.
%#edit_desc is the description of the parameter to update.
%#edit_type is the type of input field to use.
<h1>{{title}}</h1>
<form action="{{edit_action}}" method="post" enctype='multipart/form-data'>
  {{edit_desc}} <input name="value" type="{{edit_type}}" /><br>
  <input value="Submit change" type="submit" />
</form>
