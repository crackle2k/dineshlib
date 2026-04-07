# dineshlib

A collection of small CLI utilities (Rust and Ruby).

## Tools

### `weather`

Prints tomorrow's weather forecast in your terminal. It auto-detects your location via IP geolocation, then pulls a forecast from the Open-Meteo API — no API key required.

**Example output**

```
╔══════════════════════════════════════════╗
║  Tomorrow's Weather — 2026-04-03      ║
║  London, United Kingdom               ║
╠══════════════════════════════════════════╣
║  🌧️  Rain                               ║
║                                          ║
║  High  : 14.2       °C                  ║
║  Low   : 8.1        °C                  ║
║  Rain  : 4.5        mm                  ║
║  Wind  : 22.3       km/h                ║
╚══════════════════════════════════════════╝
```

**Build & run**

```sh
cd weather
cargo run --release
```

**Dependencies**

| Crate | Purpose |
|-------|---------|
| `reqwest` | HTTP client |
| `serde` / `serde_json` | JSON deserialization |
| `tokio` | Async runtime |
| `anyhow` | Error handling |

**APIs used** (both free, no key needed)

- [ip-api.com](http://ip-api.com) — IP geolocation
- [Open-Meteo](https://open-meteo.com) — weather forecast

---

### `capitals`

A quiz that prompts you with a capital city; you type the country.

**Example output**

```
Capitals Quiz — name the country. Type 'quit' to stop.

Tokyo: Japan
Correct!
Paris: Germany
Wrong — France
Ottawa: Canada
Correct!

2/3
```

**Build & run**

```sh
cd capitals
cargo run --release
```

No external crates required — stdlib only.
