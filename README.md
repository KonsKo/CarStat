<h3> Statistic app</h3>
<p>Grab vehicle data from avito.ru :</p>
<ul>
<li>by script</li>
<li>selery + redis scheduling task</li>
  <ul>
    <li>install redis</li>
    <li>install all dependencies</li>
    <li>celery -A car_stat worker -l info</li>
    <li>celery -A car_stat worker --beat -l info -S django</li>
  </ul>
</ul>
<p>Show statistic information about cars</p>
