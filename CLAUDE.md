# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository overview

`dineshlib` is a collection of small Rust CLI utilities. Each tool lives in its own subdirectory with its own `Cargo.toml` (independent crate, not a workspace).

## Commands

All commands are run from inside the tool's subdirectory (e.g., `cd weather`).

```sh
cargo build --release   # build
cargo run --release      # run
cargo test               # run tests
cargo clippy             # lint
cargo fmt                # format
```

## Tools

### `weather`

Prints tomorrow's average temperature (integer °C) to stdout. Pipeline:
1. `get_location` — calls `http://ip-api.com/json/?fields=lat,lon` to geolocate by IP
2. `get_forecast` — calls Open-Meteo `/v1/forecast` with `forecast_days=2`, takes index `[1]` (tomorrow) from the `daily` arrays
3. Prints `(max + min) / 2` as an integer

Both APIs are free and require no key. The binary exits with code 1 on any network or data error, printing to stderr.

Note: the README shows a richer boxed output format; the current `main.rs` only prints the raw average integer — the display layer is not yet implemented.
