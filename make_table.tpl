%rebase layout title=title
%#template to generate an HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<p>List of projects:</p>
<table border="1">
%i=0 #i is 0 for the title row
%for row in rows:
  <tr>
  %j=0 #j is 0 if this is the first column.
  %for col in row:
    %if i==0:
      <th>{{col}}</th>
    %elif j==0:
      <td><a href="/wish/{{col}}">
      %j+=1
    %elif j==1:
      {{col}}</a></td>
      %j+=1
    %else:
      <td>{{col}}</td>
      %j+=1
    %end #if
  %end #for col in row
  </tr>
%i+=1
%end #for row in rows
</table>
