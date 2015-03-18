%rebase('layout.tpl', title=title)
%#template to display list of projects in an HTML table.
<h1>{{title}}</h1>
<table border="1">
%i=0 #i is 0 for the title row
%for row in rows:
  <tr>
  %j=0 #j is 0 if this is the first column.
  %for col in row:
    %if i==0:
      %if j==0: #if first row, discard first column.
        %j+=1
      %else:
        <th>{{col}}</th>
      %end #if j==0:
    %elif j==0:
      <td><a href="/wish/{{col}}">\\
      %j+=1
    %elif j==1:
{{col}}</a></td>
      %j+=1
    %else:
      <td>{{col}}</td>
      %j+=1 #Unnecessary: I'm only interested in the first two columns, but just in case I need a column counter later...
    %end #if
  %end #for col in row
  </tr>
%i+=1
%end #for row in rows
</table>
