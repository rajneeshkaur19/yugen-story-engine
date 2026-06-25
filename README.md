# 🌸 Yūgen Story Engine

**Engineered horror through subtle pacing and restraint.**

An AI-powered story generator that deliberately controls tension curves to create that specific "quiet dread" feeling inspired by Japanese horror aesthetics (yūgen - 幽玄).

---

## 📖 Table of Contents

1. [What is Yūgen?](#what-is-yūgen)
2. [Features](#features)
3. [Quick Start](#quick-start)
4. [Installation](#installation)
5. [Running the Project](#running-the-project)
6. [Project Structure](#project-structure)
7. [Architecture](#architecture)
8. [API Documentation](#api-documentation)
9. [Technologies Used](#technologies-used)
10. [Development Roadmap](#development-roadmap)
11. [Contributing](#contributing)
12. [License](#license)

---

## What is Yūgen?

**Yūgen** (幽玄) is a Japanese aesthetic concept meaning **"subtle, mysterious profundity"** — beauty that's *felt* rather than explained. Think of Japanese horror films like **Ringu** or **Ju-on**. Dread builds through:

- What's **suggested**, not shown
- **Silence**, not screams  
- What's **left unsaid**

This engine generates horror stories that way — not through explicit gore or jump-scares, but through **engineered restraint** and deliberate pacing.

### How It's Different

| Feature | Standard AI Story Generator | Yūgen Story Engine |
|---------|---|---|
| **Pacing** | All at once or randomized | Engineered tension curve |
| **Violence** | Often explicit | Zero gore via restraint filter |
| **Endings** | Usually resolved | Deliberately ambiguous |
| **User Control** | Limited | Full beat navigation & regeneration |
| **Visuals** | Text only | Text + atmospheric images |
| **Atmosphere** | Static text | Ambient animation + sound |

---

## Features

### ✅ Core Features

- **Beat-by-Beat Generation** — Stories generated in controlled beats, not one giant prompt
- **Tension Curve Control** — Choose from presets (Slow Burn, Spike, Gradual, etc.) or create custom curves
- **Restraint Filtering** — Automatically removes explicit content and regenerates if needed
- **Ambiguous Endings** — Stories end unsettled, true to J-horror style
- **Split-View Experience** — Story text on left, atmospheric visuals on right
- **Beat Navigation** — Jump to any beat, regenerate specific ones
- **Story Library** — Persist and browse all generated stories
- **Ambient Atmosphere** — Falling petals animation, sound effects, mood control

### 🎨 UI Features

- **Multi-Page Interface** — Home (Generator) | Library (Gallery) | Settings | About
- **Sakura-Dark Theme** — Japanese aesthetic with pink accents fading to black
- **Real-Time Tension Meter** — Visual graph showing engineered pacing
- **Beat Progress Chain** — See emotional arc of entire story at a glance
- **Quick Actions** — Regenerate beat, save story, export as TXT
- **Whisper Hints** — Subtle hints in Japanese/English for each beat
- **Theme Toggle** — Switch between Sakura Dark and Light mode

### 🔧 Technical Features

- **FastAPI Backend** — Clean, modular REST API
- **Claude Sonnet Integration** — Each beat generated via Claude API
- **Custom Filtering Logic** — Your own restraint classifier (not just prompting)
- **SQLite Persistence** — Stories saved locally with full metadata
- **Type-Safe** — Pydantic models throughout
- **Well-Tested** — Unit + integration tests included
- **Documented** — Comprehensive API docs and architecture guides

---

## Quick Start

### Minimum Requirements

- Python 3.9+
- Anthropic API key (get one at [console.anthropic.com](https://console.anthropic.com))
- ~10 minutes

### 30-Second Setup

```bash
# 1. Clone and enter project
git clone <repo-url>
cd yugen-story-engine

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY

# 5. Run backend (Terminal 1)
python backend/main.py

# 6. Run frontend (Terminal 2)
streamlit run frontend/app.py
```

That's it! Visit `http://localhost:8501` 🎉

---

## Installation

### Prerequisites

Before you start, ensure you have:

- **Python 3.9 or higher** (check with `python --version`)
- **pip** (should come with Python)
- **git** (optional, for cloning)
- **Anthropic API Key** — Get one for free at [https://console.anthropic.com](https://console.anthropic.com)

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/yugen-story-engine.git
cd yugen-story-engine
```

Or manually download and extract the ZIP file.

### Step 2: Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

You should see `(venv)` in your terminal prompt.

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- `fastapi` & `uvicorn` — Backend API
- `streamlit` — Frontend UI
- `anthropic` — Claude API client
- `sqlalchemy` — Database ORM
- `pydantic` — Data validation
- Plus testing and dev tools

### Step 4: Configure Environment

```bash
# Copy example config
cp .env.example .env

# Edit .env file and add:
# ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxx
```

Get your API key:
1. Go to [console.anthropic.com](https://console.anthropic.com)
2. Sign up or log in
3. Create an API key
4. Copy it into `.env`

---

## Running the Project

### Start Backend Server

In **Terminal 1**:

```bash
# Make sure venv is activated
source venv/bin/activate

# Start FastAPI server
python backend/main.py
```

Expected output:
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

Test it: Visit `http://127.0.0.1:8000/health` — should return `{"status": "ok"}`

### Start Frontend (in separate terminal)

In **Terminal 2**:

```bash
# Make sure venv is activated
source venv/bin/activate

# Start Streamlit app
streamlit run frontend/app.py
```

Expected output:
```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
```

Visit `http://localhost:8501` — you're in! 🌸

### First Story Generation

1. **Configure settings** (left sidebar):
   - Setting: "Abandoned Shrine"
   - Mood: "Dread"
   - Tension Curve: "Slow Burn"
   - No. of Beats: 10

2. **Click "✨ Generate Story"**

3. **Watch the magic happen**:
   - Each beat generates from Claude API
   - Real-time tension meter updates
   - Story reveals beat-by-beat
   - Visual and whisper hints appear

---

## Project Structure

```
yugen-story-engine/
│
├── 📁 backend/                          # FastAPI backend
│   ├── main.py                          # Entry point
│   ├── config.py                        # Configuration & presets
│   ├── 📁 models/                       # Data models (Pydantic)
│   │   ├── tension_model.py
│   │   ├── story_model.py
│   │   └── whisper_model.py
│   ├── 📁 services/                     # Business logic
│   │   ├── claude_service.py            # Claude API calls
│   │   ├── restraint_filter.py          # Content filtering
│   │   ├── story_engine.py              # Main generation logic
│   │   ├── visual_service.py            # Image handling
│   │   └── whisper_service.py           # Hint generation
│   ├── 📁 routes/                       # API endpoints
│   │   └── story_routes.py              # /generate, /list, etc
│   ├── 📁 database/                     # Database
│   │   ├── db.py                        # SQLite operations
│   │   └── models.py                    # SQLAlchemy models
│   └── 📁 utils/                        # Helpers
│       ├── tension_curves.py            # Predefined curves
│       ├── prompts.py                   # Claude prompts
│       └── constants.py                 # Magic strings
│
├── 📁 frontend/                         # Streamlit UI
│   ├── app.py                           # Main entry point
│   ├── config.py                        # Frontend config
│   ├── 📁 pages/                        # Multi-page views
│   │   ├── 00_🏠_home.py                # Story generator
│   │   ├── 01_📚_library.py             # Story gallery
│   │   ├── 02_⚙️_settings.py            # User settings
│   │   └── 03_❓_about.py               # About page
│   ├── 📁 components/                   # Reusable UI
│   │   ├── theme.py                     # Theming & CSS
│   │   ├── story_settings.py            # Settings panel
│   │   ├── story_display.py             # Story view
│   │   ├── tension_meter.py             # Tension graph
│   │   ├── beat_progress.py             # Beat chain
│   │   ├── quick_actions.py             # Action buttons
│   │   ├── atmosphere.py                # Ambient effects
│   │   ├── story_library.py             # Library widget
│   │   └── [more components]
│   ├── 📁 assets/                       # Images, CSS, sounds
│   │   ├── images/                      # Story visuals
│   │   ├── styles/                      # CSS files
│   │   ├── icons/                       # SVG icons
│   │   └── sounds/                      # Audio files
│   ├── 📁 utils/                        # Frontend helpers
│   │   ├── api_client.py                # API calls
│   │   ├── cache.py                     # Caching
│   │   └── validators.py                # Input validation
│   └── 📁 hooks/                        # State management
│       ├── story_state.py
│       └── ui_state.py
│
├── 📁 tests/                            # Unit & integration tests
│   ├── 📁 unit/
│   │   ├── test_restraint_filter.py
│   │   ├── test_tension_curves.py
│   │   └── test_story_engine.py
│   ├── 📁 integration/
│   │   └── test_api_generate.py
│   └── 📁 e2e/
│       └── test_full_flow.py
│
├── 📁 data/                             # Local data storage
│   ├── stories.db                       # SQLite database
│   ├── cache/                           # Caching
│   └── logs/                            # Logs
│
├── 📁 docs/                             # Documentation
│   ├── API.md                           # API docs
│   ├── ARCHITECTURE.md                  # System design
│   └── SETUP.md                         # Setup guide
│
├── .env                                 # Environment variables (local)
├── .env.example                         # Template
├── .gitignore                           # Git ignore rules
├── requirements.txt                     # Python dependencies
├── requirements-dev.txt                 # Dev dependencies
├── README.md                            # This file
└── LICENSE                              # MIT License
```

**Total:** ~60 Python files, 20 folders, 1500+ lines of code

---

## Architecture

### System Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    STREAMLIT FRONTEND                       │
│  (User Interface: Pages, Components, Theme)                 │
│                                                              │
│  Pages: Home | Library | Settings | About                   │
│  Components: Settings | Display | Meter | Progress | etc    │
└────────────────────┬────────────────────────────────────────┘
                     │ HTTP Requests
                     ↓
┌─────────────────────────────────────────────────────────────┐
│                    FASTAPI BACKEND                          │
│  (API: Routes, Logic, Database)                             │
│                                                              │
│  Routes: /generate, /list, /story/{id}, /regenerate         │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ STORY ENGINE (Core Logic)                            │  │
│  │                                                      │  │
│  │ 1. Get tension curve (preset or custom)             │  │
│  │ 2. Loop through each beat:                          │  │
│  │    a. Call Claude API (generate_beat)              │  │
│  │    b. Check restraint filter                        │  │
│  │    c. If explicit, regenerate (max 2 attempts)     │  │
│  │    d. Get visual (image) for beat                   │  │
│  │    e. Generate whisper hint (subtle message)        │  │
│  │ 3. Save story to SQLite                             │  │
│  │ 4. Return StoryResponse                             │  │
│  └──────────────────────────────────────────────────────┘  │
│                         │                                   │
│        ┌────────────────┼────────────────┐                  │
│        ↓                ↓                ↓                   │
│  ┌──────────┐    ┌──────────────┐   ┌──────────┐           │
│  │  Claude  │    │  Restraint   │   │ Database │           │
│  │  API     │    │  Filter      │   │ (SQLite) │           │
│  │          │    │              │   │          │           │
│  │ (generate│    │ (check for   │   │ (save    │           │
│  │  beat    │    │  explicit    │   │  story)  │           │
│  │  text)   │    │  content)    │   │          │           │
│  └──────────┘    └──────────────┘   └──────────┘           │
└─────────────────────────────────────────────────────────────┘
```

### Data Flow

```
User Interaction
    ↓
Streamlit UI (frontend/app.py)
    ↓
API Request → FastAPI (backend/main.py)
    ↓
Story Engine (backend/services/story_engine.py)
    ├─ Get Tension Curve (backend/utils/tension_curves.py)
    └─ For each beat:
        ├─ Generate Beat (Claude API via claude_service.py)
        ├─ Check Restraint (restraint_filter.py)
        ├─ Regenerate if needed (claude_service.py again)
        ├─ Get Visual (visual_service.py)
        └─ Generate Whisper (whisper_service.py)
    ↓
Save to Database (backend/database/db.py)
    ↓
Return StoryResponse
    ↓
Streamlit displays:
    ├─ Beat-by-beat reveal (components/story_display.py)
    ├─ Tension meter updates (components/tension_meter.py)
    ├─ Beat progress (components/beat_progress.py)
    └─ Story library (components/story_library.py)
```

### Key Components

#### 1. **Tension Curve** (backend/utils/tension_curves.py)
- Defines emotional arc: [1, 2, 3, 5, 8, 9, 3]
- Each number = target tension (0-10) for that beat
- Presets: Slow Burn, Spike, Gradual, Double Spike, Psychological

#### 2. **Beat Generation** (backend/services/claude_service.py)
- One API call per beat (not one giant prompt)
- Input: tension target + previous context
- Output: ~150 words of story text

#### 3. **Restraint Filter** (backend/services/restraint_filter.py)
- Flags explicit content (gore, jump-scares, clichés)
- Regenerates if necessary
- Enforces yūgen philosophy (subtlety over explicitness)

#### 4. **Story Engine** (backend/services/story_engine.py)
- Orchestrates the whole process
- Loops through each beat
- Handles API calls, filtering, database saves

#### 5. **Frontend Components** (frontend/components/)
- Modular, reusable UI pieces
- Split view (text + image)
- Tension meter, beat navigation, library
- Ambient animations

---

## API Documentation

### Base URL
```
http://localhost:8000
```

### Endpoints

#### 1. **POST /api/generate**
Generate a new story.

**Request:**
```bash
curl -X POST "http://localhost:8000/api/generate" \
  -H "Content-Type: application/json" \
  -d '{
    "setting": "Abandoned Shrine",
    "mood": "Dread",
    "curve_preset": "slow_burn",
    "include_visuals": true,
    "include_whispers": true,
    "language": "english"
  }'
```

**Response (200):**
```json
{
  "id": "abc12345",
  "title": "Abandoned Shrine — Dread",
  "beats": [
    {
      "index": 0,
      "tension_target": 1,
      "text": "The shrine door creaked open...",
      "whisper_hint": "Something is watching.",
      "visual_url": "./frontend/assets/images/shrine/shrine_01.jpg",
      "regeneration_attempts": 0
    },
    ...
  ],
  "setting": "Abandoned Shrine",
  "mood": "Dread",
  "generated_at": 1703123456.789,
  "total_beats": 10,
  "completion_time_seconds": 45.3,
  "tension_curve": [1, 2, 3, 4, 5, 6, 7, 8, 7, 3]
}
```

#### 2. **GET /api/story/{story_id}**
Retrieve a specific story.

**Request:**
```bash
curl "http://localhost:8000/api/story/abc12345"
```

**Response (200):**
```json
{
  "id": "abc12345",
  "title": "Abandoned Shrine — Dread",
  "beats": [...],
  "setting": "Abandoned Shrine",
  "mood": "Dread",
  ...
}
```

#### 3. **GET /api/stories**
List all stories with pagination.

**Request:**
```bash
curl "http://localhost:8000/api/stories?limit=10&offset=0"
```

**Response (200):**
```json
{
  "stories": [...],
  "count": 10
}
```

#### 4. **GET /health**
Health check.

**Response (200):**
```json
{"status": "ok"}
```

---

## Technologies Used

### Backend
| Technology | Purpose | Version |
|-----------|---------|---------|
| **FastAPI** | Web framework | 0.104.1 |
| **Uvicorn** | ASGI server | 0.24.0 |
| **Anthropic Claude** | LLM for story generation | Latest |
| **SQLAlchemy** | ORM | 2.0.23 |
| **Pydantic** | Data validation | 2.5.0 |
| **SQLite** | Database | Built-in |

### Frontend
| Technology | Purpose | Version |
|-----------|---------|---------|
| **Streamlit** | UI framework | 1.28.1 |
| **Matplotlib** | Charting | 3.8.2 |
| **Pillow** | Image handling | 10.1.0 |
| **Requests** | HTTP client | 2.31.0 |

### Development
| Tool | Purpose |
|-----|---------|
| **pytest** | Testing |
| **black** | Code formatting |
| **flake8** | Linting |
| **mypy** | Type checking |

---

## Development Roadmap

### Phase 1 ✅ (Current)
- [x] Backend structure (FastAPI)
- [x] Claude API integration
- [x] Restraint filter
- [x] Story engine (beat generation)
- [x] SQLite database
- [x] Basic Streamlit UI
- [x] Components framework

### Phase 2 (In Progress)
- [ ] Complete all UI components
- [ ] Beat navigation
- [ ] Story library with filters
- [ ] Multi-page support
- [ ] Theme toggle

### Phase 3 (Planned)
- [ ] Visual assets (images per beat)
- [ ] Ambient animation & sounds
- [ ] Advanced settings (custom curves)
- [ ] Batch story generation
- [ ] Export to PDF/EPUB

### Phase 4 (Future)
- [ ] Multiplayer story sharing
- [ ] Community story voting
- [ ] Fine-tuning with custom models
- [ ] Mobile app (React Native)
- [ ] Cloud deployment (Heroku, AWS)

---

## Contributing

Contributions are welcome! Here's how to help:

### 1. Fork the repo
```bash
git clone https://github.com/yourusername/yugen-story-engine.git
cd yugen-story-engine
```

### 2. Create a feature branch
```bash
git checkout -b feature/your-feature-name
```

### 3. Make changes & test
```bash
pytest tests/
black .
flake8 .
```

### 4. Commit & push
```bash
git commit -m "Add feature: brief description"
git push origin feature/your-feature-name
```

### 5. Open a Pull Request
Describe what you changed and why.

### Code Style
- Use **Black** for formatting: `black .`
- Use **type hints**: `def generate_beat(index: int) -> str:`
- Write **docstrings** for functions
- Add **tests** for new features

---

## Testing

Run tests with pytest:

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/unit/test_restraint_filter.py

# Run with coverage
pytest --cov=backend tests/

# Run only integration tests
pytest tests/integration/
```

---

## Troubleshooting

### Issue: Backend won't start
```
Error: Address already in use
```
**Solution:** Change port in `.env`:
```env
FASTAPI_PORT=8001
```

### Issue: API key not working
```
Error: Invalid API key
```
**Solution:** 
1. Check your `.env` file has correct key
2. Get new key from [console.anthropic.com](https://console.anthropic.com)
3. Make sure there are no extra spaces: `ANTHROPIC_API_KEY=sk-ant-xxxxx`

### Issue: Streamlit can't connect to backend
```
ConnectionError: http://127.0.0.1:8000
```
**Solution:**
1. Make sure backend is running (`python backend/main.py`)
2. Check backend is on correct port (default 8000)
3. Try accessing `http://127.0.0.1:8000/health` in browser

### Issue: Database file permission error
```
PermissionError: [Errno 13] Permission denied: 'data/stories.db'
```
**Solution:**
```bash
# Fix permissions
chmod 755 data/
chmod 644 data/stories.db
```

### Issue: Slow story generation
**Explanation:** Claude API calls take 3-15 seconds per beat depending on load.

**Optimization:**
- Use smaller beat counts (start with 5)
- Use faster model (Claude Haiku instead of Sonnet)
- Cache results: stories are saved, no need to regenerate

---

## Performance Tips

### Speed Up Generation
1. **Fewer beats:** 5-8 beats generates faster than 15+
2. **Simpler curves:** Gradual curve often faster than Psychological
3. **Batch generation:** Generate multiple stories at once

### Optimize Database
```bash
# Vacuum database (compress)
sqlite3 data/stories.db "VACUUM;"

# Check database stats
sqlite3 data/stories.db ".tables"
```

---

## Security

### Sensitive Data
- **Never commit `.env`** — it's in `.gitignore`
- **API keys are secrets** — use `.env` file only
- **Database is local** — not exposed to internet

### Safe Deployment
When deploying:
1. Use environment variables for secrets
2. Enable HTTPS
3. Rate-limit API endpoints
4. Add authentication if needed

---

## License

This project is licensed under the **MIT License** — see `LICENSE` file for details.

Feel free to use, modify, and distribute. Attribution appreciated! 🌸

---

## Credits

### Built With
- **Claude** (Anthropic) — Story generation AI
- **FastAPI** — Modern Python web framework
- **Streamlit** — Rapid UI development
- **SQLite** — Lightweight database

### Inspired By
- Japanese horror (Ringu, Ju-on, Kaidan tales)
- Yūgen aesthetic philosophy
- Subtle storytelling techniques

---

## Contact & Support

### Questions?
- Check `docs/` folder for detailed guides
- Open an issue on GitHub
- Check the wireframe for UI reference

### Found a Bug?
1. Describe the issue
2. Include error message & steps to reproduce
3. Open a GitHub issue

### Have Ideas?
1. Check roadmap (might already be planned)
2. Open a discussion on GitHub
3. Fork and create a PR!

---

## Acknowledgments

Built with ❤️ for the placement interview process and because subtle horror is underrated.

Special thanks to:
- Anthropic for Claude API
- FastAPI team for excellent framework
- Streamlit for making UI development accessible
- All contributors and testers

---

## Version History

### v1.0.0 (Current)
- ✅ Core story generation
- ✅ Restraint filtering
- ✅ Tension curve control
- ✅ SQLite persistence
- ✅ Streamlit UI

---

**Happy story generating! 🌸**

*Remember: In yūgen, what's unsaid is more powerful than what's said.*

---

Last Updated: June 2024  
Maintained with ❤️