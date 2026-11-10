"""
crop_predict.py — standalone crop recommendation (no Flask needed)

Models used (same as AgriSense), in ./Rec_Models/:
  crop_recommendation_model.pkl  -> LogisticRegression (predict_proba)
  season_encoder.pkl             -> LabelEncoder for the season column
  scaler.pkl                     -> StandardScaler fitted on all 8 features

Feature order (must match training):
  N, P, K, temperature, humidity, ph, rainfall, season_encoded

Usage as a script:
  python crop_predict.py --n 90 --p 42 --k 43 --temp 26 --humidity 80 \
                         --ph 6.5 --rainfall 200 --season rainy

Usage as a module:
  from crop_predict import CropRecommender
  rec = CropRecommender()
  result = rec.predict(n=90, p=42, k=43, temp=26, humidity=80,
                       ph=6.5, rainfall=200, season="rainy")
"""

import argparse
import json
import os
import pickle

import numpy as np

from crop_info import get_crop_info

MODEL_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Rec_Models")
TOP_N = 3


def _load(path: str):
    """Load a pickle/joblib file with clear errors for the common failure modes."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"Model file not found: {path}")

    # 'invalid load key, v' usually means the file is a Git LFS pointer or a
    # saved web page, not a real pickle. Detect that and say so.
    with open(path, "rb") as f:
        head = f.read(64)
    if head.startswith(b"version https://git-lfs") or head.lstrip().startswith(b"<"):
        raise ValueError(
            f"{path} is not a real model file (looks like a Git LFS pointer or an "
            f"HTML download). Re-download the actual file, or regenerate it with "
            f"train_crop_model.py."
        )

    try:
        with open(path, "rb") as f:
            return pickle.load(f)
    except pickle.UnpicklingError:
        import joblib  # fallback: file may have been saved with joblib.dump
        return joblib.load(path)


class CropRecommender:
    def __init__(self, model_dir: str = MODEL_DIR):
        self.model = _load(os.path.join(model_dir, "crop_recommendation_model.pkl"))
        self.season_encoder = _load(os.path.join(model_dir, "season_encoder.pkl"))
        self.scaler = _load(os.path.join(model_dir, "scaler.pkl"))

    @property
    def seasons(self):
        return list(self.season_encoder.classes_)

    def predict(self, n, p, k, temp, humidity, ph, rainfall, season, top_n=TOP_N) -> dict:
        season = str(season).strip().lower()
        if season not in self.season_encoder.classes_:
            raise ValueError(f"Invalid season '{season}'. Valid: {', '.join(self.seasons)}")

        season_encoded = int(self.season_encoder.transform([season])[0])
        features = np.array([[n, p, k, temp, humidity, ph, rainfall, season_encoded]], dtype=float)
        scaled = self.scaler.transform(features)

        probs = self.model.predict_proba(scaled)[0]
        classes = self.model.classes_
        order = np.argsort(probs)[::-1]

        recommendations = []
        for rank, i in enumerate(order[:top_n], start=1):
            info = get_crop_info(str(classes[i]))
            recommendations.append({
                "rank": rank,
                "crop": str(classes[i]).title(),
                "confidence": round(float(probs[i]) * 100, 2),
                "latin": info["latin"],
                "reason": info["reason"],
                "tips": info["tips"],
            })

        return {
            "top_crop": recommendations[0],
            "recommendations": recommendations,
            "all_scores": [
                {"name": str(classes[i]), "score": round(float(probs[i]) * 100, 2)}
                for i in order
            ],
            "season_used": season,
        }


def main():
    ap = argparse.ArgumentParser(description="AgriSense crop recommendation")
    ap.add_argument("--n", type=float, required=True, help="Nitrogen (mg/kg)")
    ap.add_argument("--p", type=float, required=True, help="Phosphorus (mg/kg)")
    ap.add_argument("--k", type=float, required=True, help="Potassium (mg/kg)")
    ap.add_argument("--temp", type=float, required=True, help="Temperature (°C)")
    ap.add_argument("--humidity", type=float, required=True, help="Humidity (%%)")
    ap.add_argument("--ph", type=float, required=True, help="Soil pH")
    ap.add_argument("--rainfall", type=float, required=True, help="Rainfall (mm)")
    ap.add_argument("--season", type=str, required=True,
                    help="autumn | rainy | spring | summer | winter | zaid")
    ap.add_argument("--json", action="store_true", help="Print full JSON output")
    args = ap.parse_args()

    rec = CropRecommender()
    result = rec.predict(args.n, args.p, args.k, args.temp, args.humidity,
                         args.ph, args.rainfall, args.season)

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return

    top = result["top_crop"]
    print(f"\nSeason: {result['season_used']}")
    print(f"Best match: {top['crop']} ({top['latin']}) — {top['confidence']}%")
    print(f"Why: {top['reason']}\n")
    print("Top recommendations:")
    for r in result["recommendations"]:
        print(f"  {r['rank']}. {r['crop']:<12} {r['confidence']}%")
    print("\nGrowing tips:")
    for i, t in enumerate(top["tips"], 1):
        print(f"  {i}. {t}")


if __name__ == "__main__":
    main()
