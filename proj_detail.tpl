%#template to show project details
<table border="1">
%i=0
%for row in rows:
  <tr>
  %j=0
  %for col in row:
  %if i==0:
    <th>{{col}}</th>
  %elif j==0:
    <td><a href="/wish/{{col}}">{{col}}</a></td>
    %j=1
  %else:
    <td>{{col}}</td>
  %end
  %end
  </tr>
%i=1
%end
</table>
<br/>
<a href="/list">Back to project list</a>
