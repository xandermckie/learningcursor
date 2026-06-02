## Warm-Up App Architecture

### Data Flow
APScheduler → fetcher.py (API call) → data/cache.json → app.py (route) → index.html

### Key Decisions
- fetcher.py is separate from app.py: routes don't contain business logic
- Scheduler runs on app startup, not on each request
- Cache always exists: app degrades to stale data, never crashes
- Search runs via /search route returning JSON, not full page reload

### What I'm Building
I am building an API based website that shows current crypto values, a ticker, and crypto related news

### Open Questions
how can i sort through the news api to only show crypto news?

how can i make sure that the api isn't being overcalled and both can work together?

#Note: Notepad no longer exists in this version of Cursor and @web is now @browser.
