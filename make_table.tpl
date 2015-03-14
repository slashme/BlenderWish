%#template to generate an HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<p>List of projects:</p>
<table border="1">
%i=0
%for row in rows:
    <tr>
  %for col in row:
  %if i==0:
    <th>{{col}}</th>
  %else:
    <td>{{col}}</td>
  %end
  %end
  </tr>
%i+=1
%end
</table>
