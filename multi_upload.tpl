%rebase('layout.tpl', title=title)
%#Template for multiple file upload
<h1>{{title}}</h1>
<form action="{{uploadaction}}" method="post" enctype='multipart/form-data'>
  Select a file: <input name="upload[]" type="file" multiple ><br>
  <input value="Start upload" type="submit" />
</form>
