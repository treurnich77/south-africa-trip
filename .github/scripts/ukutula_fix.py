from pathlib import Path
p=Path('index.html')
s=p.read_text()
start=s.index('<section class="section">\n<div class="title">Sat Jan 16–Sun Jan 17 — Ukutula Conservation Center (1 Night)</div>')
end=s.index('</section>',start)+len('</section>')
new='''<section class="section">
<div class="title">Sat Jan 16–Sun Jan 17 — Ukutula Lion Lodge & Research Centre (1 Night)</div>
<div class="badges"><span class="badge green">R6,000 PAID</span><span class="badge green">SLOTS RESERVED</span><span class="badge blue">PREDATOR TOUR + LION WALK</span></div>
<span class="big">Accommodation:</span> Family 4 Sleep Chalet — 4 Adults<br>
<span class="big">Date:</span> Jan 16–17, 2027<br>
<span class="big">Invoice Number:</span> <b>56771</b><br>
<span class="big">Accommodation Price:</span> R4,550<br>
<span class="big">Predator Tour:</span> Included with accommodation — Sat Jan 16 at <b>14:00</b><br>
<span class="big">Bush Walk with Lions:</span> Sun Jan 17 at <b>08:00</b> — 4 adults<br>
<span class="big">Lion Walk Price:</span> R900 pp × 4 = R3,600<br><br>
<span class="big">Invoice Total:</span> <b>R8,150.01</b><br>
<span class="big">Paid:</span> <b>R6,000</b> on Oct 6, 2026<br>
<span class="big">Balance Remaining:</span> <b>R2,150.01</b><br>
<span class="big">Payment Method:</span> Visa via Yoco<br>
<span class="big">Yoco Sale:</span> 2026/10/042251<br>
<span class="big">Authorization:</span> 974659<br>
<span class="big">Yoco Reference:</span> y0G9dDJTrwea<br>
<span class="big">Payment Receipt:</span> <a href="https://www.yoco.co.za/receipts/y0G9dDJTrwea" target="_blank">Open Ukutula Yoco Receipt</a><br><br>
<span class="big">Booking Status:</span><br>
Ukutula confirmed availability for all four guests on Jan 16 and 17. The requested and reserved programme is the 14:00 Predator Tour on Jan 16 and the 08:00 Bush Walk with Lions on Jan 17. Yoco confirms the R6,000 payment. Final post-payment acknowledgment from Ukutula is still pending.<br><br>
<span class="big">Refundable Key Deposit:</span> R500 cash on arrival — not counted as trip spend.<br>
<span class="big">Cancellation:</span> less than 2 weeks before arrival forfeits the full deposit; refundable cancellations carry a 10% administration fee.<br><br>
<span class="big">Optional Meals:</span><br>
Breakfast R200 pp — 09:00<br>
Lunch R185 pp — 13:00<br>
Dinner R385 pp — 19:00 in summer<br>
Meals must be booked at least 1 day before arrival.<br><br>
<span class="big">Sunday Departure:</span><br>
Lion Walk at 08:00, then leave Ukutula for OR Tambo with plenty of margin.<br>
Ukutula → OR Tambo: about 165 km; allow roughly 2½–3 hours.<br>
CarFlexi return booking shows 17:30, but plan an earlier return for the 19:45 LH573 departure.
<div class="info">Final-trip sequence: Predator Tour Saturday afternoon, overnight at Ukutula, Lion Walk Sunday morning, then OR Tambo for the evening flight.</div>
</section>'''
s=s[:start]+new+s[end:]
for a,b in [
('Ukutula planned total: ~$455 USD','Ukutula remaining balance: R2,150.01 — R6,000 already paid'),
('Known Paid Total:</span> <span class="big">~$7,211.64 USD','Known Paid Total:</span> <span class="big">~$7,572 USD'),
('Includes the current CFD1FD74 payment of $388.80. The old $440.74 payment has been refunded and is not counted.','Includes the current CFD1FD74 payment of $388.80 and the Ukutula R6,000 payment. The old $440.74 CarFlexi payment was refunded and is not counted.'),
('Known Fixed / Booked Future Commitments:</span> <span class="big">~$7,026 USD','Known Fixed / Booked Future Commitments:</span> <span class="big">~$6,700 USD'),
('Known fixed / booked future commitments: ~$7,026 USD','Known fixed / booked future commitments: ~$6,700 USD'),
('Projected Additional Spend From Now:</span> <span class="big">~$13,570–$16,490 USD','Projected Additional Spend From Now:</span> <span class="big">~$13,244–$16,164 USD'),
('Already paid: ~$7,211.64 USD','Already paid: ~$7,572 USD'),
('Plus projected future spend: ~$13,570–$16,490 USD','Plus projected future spend: ~$13,244–$16,164 USD'),
('Projected Total Holiday Cost:</span> <span class="big">~$20,782–$23,702 USD','Projected Total Holiday Cost:</span> <span class="big">~$20,816–$23,736 USD')
]: s=s.replace(a,b)
p.write_text(s)
