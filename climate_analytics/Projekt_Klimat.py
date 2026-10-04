from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
import requests

API_URL = "https://archive-api.open-meteo.com/v1/archive"
DEFAULT_COORDINATES = {"latitude": 52.4069, "longitude": 16.9299}  # Poznan, Poland


def fetch_weather_data(
    latitude: float,
    longitude: float,
    start_date: str,
    end_date: str,
) -> pd.DataFrame:
    """Fetches daily temperature telemetry from Open-Meteo Historical Archive API."""
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": start_date,
        "end_date": end_date,
        "daily": "temperature_2m_mean",
        "timezone": "auto",
    }

    try:
        response = requests.get(API_URL, params=params, timeout=10)
        response.raise_for_status()
        payload = response.json()
    except requests.RequestException as exc:
        raise RuntimeError(f"Network error while communicating with Open-Meteo: {exc}") from exc

    if "daily" not in payload:
        error_reason = payload.get("reason", "Unknown API error")
        raise ValueError(f"API response missing 'daily' dataset. Reason: {error_reason}")

    df = pd.DataFrame({
        "timestamp": pd.to_datetime(payload["daily"]["time"]),
        "temperature": payload["daily"]["temperature_2m_mean"],
    })
    df.set_index("timestamp", inplace=True)
    return df


def aggregate_monthly(df: pd.DataFrame) -> pd.Series:
    """Computes monthly mean temperatures from daily time-series."""
    return df["temperature"].resample("ME").mean()


def generate_climate_report(
    daily_df: pd.DataFrame,
    monthly_series: pd.Series,
    output_path: str = "poznan_climate_2025.png",
) -> None:
    """Generates and saves a time-series plot comparing daily metrics with monthly averages."""
    plt.figure(figsize=(12, 6))
    plt.plot(
        daily_df.index,
        daily_df["temperature"],
        label="Daily Mean Temperature",
        color="#87CEEB",
        alpha=0.6,
    )
    plt.plot(
        monthly_series.index,
        monthly_series,
        label="Monthly Average Trend",
        color="#D9534F",
        marker="o",
        linewidth=2,
    )

    plt.title("Poznań Climate & Weather Analytics (2025)", fontsize=14, fontweight="bold")
    plt.xlabel("Date", fontsize=11)
    plt.ylabel("Temperature (°C)", fontsize=11)
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.legend(frameon=True)
    plt.tight_layout()

    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"[INFO] Report chart saved to: {Path(output_path).resolve()}")


def run_pipeline() -> None:
    print("[INFO] Starting weather data extraction pipeline...")
    data = fetch_weather_data(
        latitude=DEFAULT_COORDINATES["latitude"],
        longitude=DEFAULT_COORDINATES["longitude"],
        start_date="2025-01-01",
        end_date="2025-12-31",
    )

    print(f"[INFO] Ingested {len(data)} daily records. Resampling monthly averages...")
    monthly_trend = aggregate_monthly(data)

    generate_climate_report(data, monthly_trend)
    print("[INFO] Pipeline completed successfully.")


if __name__ == "__main__":
    run_pipeline()