"""
crop_info.py
Display info (latin name, reason, tips) for each crop label the model predicts.
"""

CROP_INFO = {
    "rice":        {"latin": "Oryza sativa",         "reason": "High humidity, warm temperature, and adequate rainfall match rice requirements.",         "tips": ["Maintain flooded conditions during vegetative stage.", "Apply nitrogenous fertilizer in 3 split doses.", "Monitor for brown planthopper and blast disease."]},
    "wheat":       {"latin": "Triticum aestivum",    "reason": "Cool temperatures and moderate rainfall are ideal for wheat cultivation.",                "tips": ["Sow at optimal density (100–125 kg/ha seed rate).", "Irrigate at crown root initiation and heading stages.", "Watch for rust disease in humid conditions."]},
    "maize":       {"latin": "Zea mays",             "reason": "Warm temperatures, moderate humidity, and good rainfall suit maize growth.",              "tips": ["Apply starter fertilizer near the seed at planting.", "Side-dress nitrogen at V6 stage for best yields.", "Ensure good drainage to prevent root rot."]},
    "tomato":      {"latin": "Solanum lycopersicum", "reason": "Moderate temperature and humidity with good potassium levels support tomatoes.",          "tips": ["Stake or cage plants for support as they grow.", "Use drip irrigation to keep foliage dry.", "Apply calcium to prevent blossom-end rot."]},
    "banana":      {"latin": "Musa spp.",            "reason": "High temperature, humidity, and potassium-rich soil create perfect banana conditions.",   "tips": ["Requires high potassium — supplement with potash fertilizer.", "Mulch heavily to retain soil moisture.", "Remove suckers to redirect energy to the main plant."]},
    "chickpea":    {"latin": "Cicer arietinum",      "reason": "Dry conditions and cooler temperatures with low nitrogen match chickpea needs.",          "tips": ["Inoculate seeds with Rhizobium bacteria for nitrogen fixation.", "Avoid waterlogging — chickpea is sensitive to excess moisture.", "Harvest when 90% of pods turn brown."]},
    "cotton":      {"latin": "Gossypium hirsutum",   "reason": "Hot dry climate with moderate rainfall suits cotton cultivation.",                        "tips": ["Thin seedlings to 25–30 cm spacing.", "Apply potassium to improve fibre quality.", "Monitor for bollworm and aphid infestations."]},
    "jute":        {"latin": "Corchorus olitorius",  "reason": "High humidity and warm temperature favour jute fibre production.",                        "tips": ["Sow in well-drained loamy soil.", "Retting in clean water improves fibre quality.", "Harvest before flowering for best yield."]},
    "coffee":      {"latin": "Coffea arabica",       "reason": "Mild temperature, high humidity, and acidic soil create ideal coffee conditions.",        "tips": ["Shade-grow for better flavour development.", "Prune annually to maintain bush shape.", "Mulch heavily to retain soil moisture."]},
    "mango":       {"latin": "Mangifera indica",     "reason": "Tropical heat, dry winters, and deep soil support mango fruiting.",                       "tips": ["Allow a dry period before flowering to stimulate blooms.", "Thin fruit clusters to improve size.", "Apply micronutrient sprays (Zn, B) at flowering."]},
    "grapes":      {"latin": "Vitis vinifera",       "reason": "Warm dry summers and well-drained soil are perfect for grape cultivation.",               "tips": ["Train vines on a trellis system.", "Prune dormant canes each winter.", "Manage irrigation carefully — stressed vines produce better fruit."]},
    "watermelon":  {"latin": "Citrullus lanatus",    "reason": "High heat, moderate moisture, and sandy loam soil suit watermelon growth.",               "tips": ["Plant on raised beds for drainage.", "Use drip irrigation to keep foliage dry.", "Harvest when the tendril nearest the fruit browns."]},
    "papaya":      {"latin": "Carica papaya",        "reason": "Tropical warmth, high humidity, and fertile soil accelerate papaya growth.",              "tips": ["Avoid waterlogging — roots rot easily.", "Apply balanced NPK every 2 weeks.", "Remove male trees once female trees are identified."]},
    "coconut":     {"latin": "Cocos nucifera",       "reason": "Sandy coastal soil, high humidity, and warm temperatures favour coconut.",                "tips": ["Space palms 7–10 m apart.", "Apply potassium and magnesium regularly.", "Irrigate during dry spells for consistent yield."]},
    "lentil":      {"latin": "Lens culinaris",       "reason": "Cool dry climate and low nitrogen soil are ideal for lentils.",                           "tips": ["Inoculate with Rhizobium before sowing.", "Avoid heavy clay soils.", "Harvest when lower pods start to rattle."]},
    "blackgram":   {"latin": "Vigna mungo",          "reason": "Warm humid conditions and moderate rainfall suit blackgram.",                             "tips": ["Sow at the start of the monsoon.", "Apply phosphorus at sowing.", "Use short-duration varieties for double cropping."]},
    "mungbean":    {"latin": "Vigna radiata",        "reason": "Warm weather and well-drained loamy soil support mungbean.",                              "tips": ["Sow at 30 cm row spacing.", "Apply rhizobium inoculant.", "Harvest in the morning to prevent pod shattering."]},
    "mothbeans":   {"latin": "Vigna aconitifolia",   "reason": "Very drought-tolerant — thrives in sandy, arid soils.",                                   "tips": ["Grows well without irrigation.", "Fix atmospheric nitrogen — no N fertilizer needed.", "Harvest pods as they mature to prevent losses."]},
    "pigeonpeas":  {"latin": "Cajanus cajan",        "reason": "Semi-arid climate and well-drained soils suit pigeonpeas.",                               "tips": ["Intercrop with cereals for land efficiency.", "Tolerates drought once established.", "Deep taproot improves soil structure."]},
    "kidneybeans": {"latin": "Phaseolus vulgaris",   "reason": "Moderate temperatures and well-drained fertile soil suit kidney beans.",                  "tips": ["Avoid frost — sow after last frost date.", "Do not over-irrigate; beans are drought-tolerant.", "Harvest when pods are dry and crisp."]},
}


def get_crop_info(crop_name: str) -> dict:
    """Return display info for a crop; falls back gracefully for unknown names."""
    key = crop_name.lower().replace(" ", "")
    info = CROP_INFO.get(key) or next(
        (v for k, v in CROP_INFO.items() if k in key or key in k), None
    )
    return info or {
        "latin": "—",
        "reason": f"The model determined that {crop_name} best matches the given conditions.",
        "tips": [
            "Follow standard agronomic practices for this crop.",
            "Consult a local agricultural extension officer for region-specific advice.",
        ],
    }
