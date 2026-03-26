import os
import dj_database_url
from pathlib import Path

# Certifique-se que o BASE_DIR está no topo
BASE_DIR = Path(__file__).resolve().parent.parent

# --- SUBSTITUA SEU BLOCO DATABASES POR ESTE ---
DATABASES = {
    'default': dj_database_url.config(
        # Se estiver na Render, ele usa a DATABASE_URL. 
        # Se estiver no seu PC e não achar a variável, usa o SQLite.
        default=f"sqlite:///{os.path.join(BASE_DIR, 'db.sqlite3')}",
        conn_max_age=600
    )
}
# ----------------------------------------------