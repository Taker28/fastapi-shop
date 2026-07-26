from pathlib import Path
import sys

import uvicorn

BACKEND_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BACKEND_DIR.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

APP_IMPORT = "backend.app.main:app"

if __name__ == "__main__":
    uvicorn.run(APP_IMPORT, host="127.0.0.1", port=8000, reload=True)
