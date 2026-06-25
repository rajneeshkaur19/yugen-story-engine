CREATE TABLE IF NOT EXISTS stories (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    beats TEXT,
    tension_curve TEXT,
    hints TEXT
);
