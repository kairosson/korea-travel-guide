# ridge & tide — Gangneung & Sokcho Travel Guide (content pilot)

A Flask MVP for the first region of a wider "independent Korea travel guide for
foreigners" project. Scope: Gangneung + Sokcho, chosen as the pilot region
(coastal + mountain + two distinct historical threads — Joseon-era Confucian
scholar heritage at Ojukheon, and Korean War refugee history at Abai Village).

## Run it locally

```bash
python3 -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
python3 app.py
```

Then open http://localhost:5000

## What's here

- `app.py` — Flask routes, one per page
- `templates/` — Jinja2 templates (`base.html` = shared nav/footer,
  `_macros.html` = the reusable "ridge-to-tide" section divider)
- `static/css/style.css` — full design token system (colors, type, layout)
- 10 content pages per the original content plan:
  1. `/` — landing / positioning
  2. `/day-trip` — Seoul → Gangneung day trip
  3. `/gangneung-2d1n` — Gangneung 2-day itinerary
  4. `/sokcho-2d1n` — Sokcho + Seoraksan 2-day itinerary
  5. `/3-days` — combined 3-day route
  6. `/culture/abai-village` — refugee-village history deep dive
  7. `/culture/ojukheon` — Joseon scholar house deep dive
  8. `/food` — food guide, local vs. tourist-facing
  9. `/seoraksan` — hiking/cable car guide by time & difficulty
  10. `/stories` — traveler stories (UGC), seeded with 2 sample entries

## What's intentionally NOT built yet

This is a content-validation MVP, per the "content first, build later" plan:

- No database — story submissions aren't a live form yet, just seed content
  and a callout. Wire up a submission form + DB (SQLite is plenty to start)
  once the content itself gets traction.
- No multilingual routing (i18n) — content is English-only for now. Add
  Flask-Babel or per-locale templates once there's a second language to add.
- No affiliate/booking links — intentionally left out until the content is
  validated; the food/course pages have natural spots to add them later
  (accommodation, tour, and activity partners).
- No search/filtering on the stories page — fine at 2 entries, will need it
  once submissions grow (filter by trip length, style, nationality).

## Extending to a new region

Each region can follow this same template: one `templates/<region>/` folder,
duplicate route pattern in `app.py`, and its own "why here" landing section.
The `_macros.html` divider and `style.css` tokens are meant to carry over
as the shared visual identity across regions.
