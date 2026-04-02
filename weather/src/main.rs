use serde::Deserialize;

// ── IP geolocation ─────────────────────────────────────────────────────────

#[derive(Deserialize)]
struct GeoLocation {
    lat: f64,
    lon: f64,
    city: String,
    country: String,
}

async fn get_location(client: &reqwest::Client) -> anyhow::Result<GeoLocation> {
    let geo = client
        .get("http://ip-api.com/json/?fields=lat,lon,city,country")
        .send()
        .await?
        .json::<GeoLocation>()
        .await?;
    Ok(geo)
}

// ── Open-Meteo forecast ────────────────────────────────────────────────────

#[derive(Deserialize)]
struct DailyUnits {
    temperature_2m_max: String,
    temperature_2m_min: String,
    precipitation_sum: String,
    windspeed_10m_max: String,
}

#[derive(Deserialize)]
struct Daily {
    time: Vec<String>,
    weathercode: Vec<u32>,
    temperature_2m_max: Vec<f64>,
    temperature_2m_min: Vec<f64>,
    precipitation_sum: Vec<f64>,
    windspeed_10m_max: Vec<f64>,
}

#[derive(Deserialize)]
struct Forecast {
    daily_units: DailyUnits,
    daily: Daily,
}

async fn get_forecast(client: &reqwest::Client, lat: f64, lon: f64) -> anyhow::Result<Forecast> {
    let url = format!(
        "https://api.open-meteo.com/v1/forecast\
         ?latitude={lat}&longitude={lon}\
         &daily=weathercode,temperature_2m_max,temperature_2m_min,\
                precipitation_sum,windspeed_10m_max\
         &forecast_days=2\
         &timezone=auto"
    );
    let forecast = client.get(&url).send().await?.json::<Forecast>().await?;
    Ok(forecast)
}

// ── WMO weather-code → human description ──────────────────────────────────

fn wmo_description(code: u32) -> &'static str {
    match code {
        0 => "Clear sky",
        1 => "Mainly clear",
        2 => "Partly cloudy",
        3 => "Overcast",
        45 | 48 => "Foggy",
        51 | 53 | 55 => "Drizzle",
        61 | 63 | 65 => "Rain",
        71 | 73 | 75 => "Snow",
        77 => "Snow grains",
        80 | 81 | 82 => "Rain showers",
        85 | 86 => "Snow showers",
        95 => "Thunderstorm",
        96 | 99 => "Thunderstorm with hail",
        _ => "Unknown",
    }
}

fn wmo_emoji(code: u32) -> &'static str {
    match code {
        0 | 1 => "☀️ ",
        2 | 3 => "⛅",
        45 | 48 => "🌫️ ",
        51..=55 => "🌦️ ",
        61..=65 | 80..=82 => "🌧️ ",
        71..=77 | 85 | 86 => "❄️ ",
        95..=99 => "⛈️ ",
        _ => "🌡️ ",
    }
}

// ── Entry point ────────────────────────────────────────────────────────────

#[tokio::main]
async fn main() {
    let client = reqwest::Client::new();

    println!("Fetching location...");
    let loc = match get_location(&client).await {
        Ok(l) => l,
        Err(e) => {
            eprintln!("Could not determine location: {e}");
            std::process::exit(1);
        }
    };

    println!("Fetching forecast for {}, {}...\n", loc.city, loc.country);
    let forecast = match get_forecast(&client, loc.lat, loc.lon).await {
        Ok(f) => f,
        Err(e) => {
            eprintln!("Could not fetch forecast: {e}");
            std::process::exit(1);
        }
    };

    // index 1 = tomorrow (index 0 = today)
    let d = &forecast.daily;
    let u = &forecast.daily_units;

    if d.time.len() < 2 {
        eprintln!("Forecast data missing tomorrow's entry.");
        std::process::exit(1);
    }

    let date = &d.time[1];
    let code = d.weathercode[1];
    let max = d.temperature_2m_max[1];
    let min = d.temperature_2m_min[1];
    let precip = d.precipitation_sum[1];
    let wind = d.windspeed_10m_max[1];

    println!("╔══════════════════════════════════════════╗");
    println!("║  Tomorrow's Weather — {date}      ║");
    println!("║  {}, {}{}║", loc.city, loc.country, " ".repeat(40usize.saturating_sub(loc.city.len() + loc.country.len() + 2)));
    println!("╠══════════════════════════════════════════╣");
    println!("║  {} {:<37}║", wmo_emoji(code), wmo_description(code));
    println!("║                                          ║");
    println!("║  High  : {:<10} {:<20}  ║", format!("{max}"), &u.temperature_2m_max);
    println!("║  Low   : {:<10} {:<20}  ║", format!("{min}"), &u.temperature_2m_min);
    println!("║  Rain  : {:<10} {:<20}  ║", format!("{precip}"), &u.precipitation_sum);
    println!("║  Wind  : {:<10} {:<20}  ║", format!("{wind}"), &u.windspeed_10m_max);
    println!("╚══════════════════════════════════════════╝");
}
