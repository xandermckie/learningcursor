## Warm-Up App Architecture

### Data Flow
APScheduler → fetcher.py (API call) → data/cache.json → app.py (route) → index.html

### Key Decisions
- fetcher.py is separate from app.py: routes don't contain business logic
- Scheduler runs on app startup, not on each request
- Cache always exists: app degrades to stale data, never crashes
- Search runs via /search route returning JSON, not full page reload

### What I'm Building
[Fill in your app's specific purpose here]

### Open Questions
[Things you're not sure about yet — add as you go]

#Note: Notepad no longer exists in this version of Cursor and @web is now @browser.