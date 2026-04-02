use serde::Deserialize;

#[derive(Deserialize)]
struct GeoLocation {
    lat: f64,
    lon: f64,
}

async fn get_location(client: &reqwest::Client) -> anyhow::Result<GeoLocation> {
    let geo = client
        .get("http://ip-api.com/json/?fields=lat,lon")
        .send()
        .await?
        .json::<GeoLocation>()
        .await?;
    Ok(geo)
}

#[derive(Deserialize)]
struct Daily {
    temperature_2m_max: Vec<f64>,
    temperature_2m_min: Vec<f64>,
}

#[derive(Deserialize)]
struct Forecast {
    daily: Daily,
}

async fn get_forecast(client: &reqwest::Client, lat: f64, lon: f64) -> anyhow::Result<Forecast> {
    let url = format!(
        "https://api.open-meteo.com/v1/forecast\
         ?latitude={lat}&longitude={lon}\
         &daily=temperature_2m_max,temperature_2m_min\
         &forecast_days=2\
         &timezone=auto"
    );
    let forecast = client.get(&url).send().await?.json::<Forecast>().await?;
    Ok(forecast)
}

#[tokio::main]
async fn main() {
    let client = reqwest::Client::new();

    let loc = match get_location(&client).await {
        Ok(l) => l,
        Err(e) => {
            eprintln!("Could not determine location: {e}");
            std::process::exit(1);
        }
    };

    let forecast = match get_forecast(&client, loc.lat, loc.lon).await {
        Ok(f) => f,
        Err(e) => {
            eprintln!("Could not fetch forecast: {e}");
            std::process::exit(1);
        }
    };

    let d = &forecast.daily;
    if d.temperature_2m_max.len() < 2 {
        eprintln!("Forecast data missing tomorrow's entry.");
        std::process::exit(1);
    }

    let avg = ((d.temperature_2m_max[1] + d.temperature_2m_min[1]) / 2.0) as i32;
    println!("{avg}");
}
