from pathlib import Path
p=Path('index.html')
s=p.read_text()
old='<span class="big">Address:</span> 125 Airtex Drive, Houston, TX 77090, United States<br>\n<span class="big">Guests:</span> 4 Adults<br>'
new='<span class="big">Address:</span> 125 Airtex Drive, Houston, TX 77090, United States<br>\n<span class="big">Agoda Booking ID:</span> <b>1069305506</b><br>\n<span class="big">Booking Reference No:</span> <b>22654933</b><br>\n<span class="big">Lead Guest:</span> Steve Treurnich<br>\n<span class="big">Guests:</span> 4 Adults<br>'
if old not in s:
    raise SystemExit('Houston booking insertion point not found')
s=s.replace(old,new,1)
p.write_text(s)
