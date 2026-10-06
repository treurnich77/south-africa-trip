from pathlib import Path
p=Path('index.html')
s=p.read_text()

nav_old='<a href="#budget">Budget</a>\n</nav>'
nav_new='<a href="#budget">Budget</a>\n<a href="#driving">Daily Driving</a>\n</nav>'
if nav_old in s:
    s=s.replace(nav_old,nav_new,1)

section='''
<section class="section" id="driving">
<div class="title">Daily Driving Plan — Projected Kilometres</div>
<div class="badges"><span class="badge blue">DAY-BY-DAY</span><span class="badge">DRIVING LOAD</span></div>
<div class="info">These are planning distances, not promises. Transfer legs use the itinerary distances where available; game-drive, sightseeing and local days include practical projected mileage. Use ~10,000 km as the safe fuel-budget ceiling for the whole South Africa road trip.</div><br>
<span class="big">Saturday Dec 5</span> — Managua / Houston travel day — <b>0 km</b><br>
<span class="big">Sunday Dec 6</span> — Houston / Newark / Johannesburg flight day — <b>0 km</b><br>
<span class="big">Monday Dec 7</span> — OR Tambo → Airport Inn after rental pickup — <b>~8 km</b><br>
<span class="big">Tuesday Dec 8</span> — Airport Inn → Benoni Home Affairs → Sabie — <b>~355 km</b><br>
<span class="big">Wednesday Dec 9</span> — Panorama / Moholoholo sightseeing circuit — <b>~284 km</b><br>
<span class="big">Thursday Dec 10</span> — Graskop / God's Window / waterfalls circuit — <b>~50 km</b><br>
<span class="big">Friday Dec 11</span> — Sabie → Phabeni Gate → Skukuza + game viewing — <b>~160 km</b><br>
<span class="big">Saturday Dec 12</span> — Skukuza → Satara + safari driving — <b>~150 km</b><br>
<span class="big">Sunday Dec 13</span> — Satara full self-drive safari day — <b>~140 km</b><br>
<span class="big">Monday Dec 14</span> — Satara → Orpen + safari loops — <b>~120 km</b><br>
<span class="big">Tuesday Dec 15</span> — Orpen → Ermelo — <b>~395 km</b><br>
<span class="big">Wednesday Dec 16</span> — Ermelo → Spion Kop — <b>~290 km</b><br>
<span class="big">Thursday Dec 17</span> — Spion Kop → Drakensberg Gardens — <b>~280 km</b><br>
<span class="big">Friday Dec 18</span> — Drakensberg local / resort day — <b>~20 km</b><br>
<span class="big">Saturday Dec 19</span> — Drakensberg local exploring — <b>~40 km</b><br>
<span class="big">Sunday Dec 20</span> — Drakensberg / meeting / local movement — <b>~20 km</b><br>
<span class="big">Monday Dec 21</span> — Drakensberg → Empangeni — <b>~400 km</b><br>
<span class="big">Tuesday Dec 22</span> — Hluhluwe-iMfolozi return trip + game driving — <b>~250 km</b><br>
<span class="big">Wednesday Dec 23</span> — Empangeni → St Lucia + local movement — <b>~230 km</b><br>
<span class="big">Thursday Dec 24</span> — Richards Bay / local Zululand day — <b>~80 km</b><br>
<span class="big">Friday Dec 25</span> — Family / light local driving — <b>~40 km</b><br>
<span class="big">Saturday Dec 26</span> — Empangeni → Kokstad — <b>~385 km</b><br>
<span class="big">Sunday Dec 27</span> — Kokstad → East London / Beacon Bay — <b>~430 km</b><br>
<span class="big">Monday Dec 28</span> — East London → Kenton-on-Sea — <b>~175 km</b><br>
<span class="big">Tuesday Dec 29</span> — Kenton local / beach / family — <b>~50 km</b><br>
<span class="big">Wednesday Dec 30</span> — Kenton → Addo / sightseeing → Storms River — <b>~420 km</b><br>
<span class="big">Thursday Dec 31</span> — Storms River / Tsitsikamma → Knysna — <b>~130 km</b><br>
<span class="big">Friday Jan 1</span> — Knysna → Robberg / Heads / local sightseeing — <b>~100 km</b><br>
<span class="big">Saturday Jan 2</span> — Knysna → Cape Town / Constantia — <b>~500 km</b><br>
<span class="big">Sunday Jan 3</span> — Cape Peninsula / Cape Point / Boulders — <b>~160 km</b><br>
<span class="big">Monday Jan 4</span> — Table Mountain / central Cape Town — <b>~50 km</b><br>
<span class="big">Tuesday Jan 5</span> — Winelands day — <b>~130 km</b><br>
<span class="big">Wednesday Jan 6</span> — Simon's Town / peninsula local day — <b>~100 km</b><br>
<span class="big">Thursday Jan 7</span> — Cape Town local / shopping / rest — <b>~50 km</b><br>
<span class="big">Friday Jan 8</span> — Cape Town → Oudtshoorn — <b>~435 km</b><br>
<span class="big">Saturday Jan 9</span> — Oudtshoorn / Cango Caves / local attractions — <b>~80 km</b><br>
<span class="big">Sunday Jan 10</span> — Oudtshoorn → Beaufort West + stops — <b>~220 km</b><br>
<span class="big">Monday Jan 11</span> — Beaufort West → Bloemfontein — <b>~540 km</b><br>
<span class="big">Tuesday Jan 12</span> — Bloemfontein → Benoni — <b>~439 km</b><br>
<span class="big">Wednesday Jan 13</span> — Benoni / Johannesburg local visits — <b>~50 km</b><br>
<span class="big">Thursday Jan 14</span> — Benoni → Sun City → Mogwase — <b>~230 km</b><br>
<span class="big">Friday Jan 15</span> — Full Pilanesberg self-drive day — <b>~200 km</b><br>
<span class="big">Saturday Jan 16</span> — Pilanesberg morning + Mogwase → Ukutula — <b>~230 km</b><br>
<span class="big">Sunday Jan 17</span> — Ukutula → OR Tambo — <b>~170 km</b><br>
<span class="big">Monday Jan 18</span> — Frankfurt / Houston travel day — <b>0 km</b><br>
<span class="big">Tuesday Jan 19</span> — Houston → Managua — <b>0 km</b><br><br>
<span class="big">Current day-by-day working total:</span> <b>~8,586 km</b><br>
<span class="big">Expected real-world total:</span> <b>~9,000–9,500 km</b><br>
<span class="big">Safe fuel-budget ceiling:</span> <b>10,000 km</b><br><br>
<span class="big">Heaviest driving days:</span> Dec 15, Dec 21, Dec 26, Dec 27, Dec 30, Jan 2, Jan 8, Jan 11 and Jan 12.<br>
<div class="info">For those heavier days: leave with a full tank, water and snacks in the vehicle, and do not depend on finding lunch at a specific time.</div>
</section>
'''

marker='\n</div>\n</body>\n</html>'
if 'id="driving"' not in s:
    s=s.replace(marker,section+marker,1)
p.write_text(s)
