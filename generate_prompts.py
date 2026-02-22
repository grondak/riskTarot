#!/usr/bin/env python3
"""
Prompt generator for Systems Thinking Tarot card imagery.

Reads card data from systemsTarot.py and writes one image-generation prompt
per card into resources/prompts/.

File naming:
  Major Arcana  → major_{nn:02d}_{slug}.txt          (nn = 01–22)
  Minor Arcana  → {suit_lower}_{nn:02d}_{slug}.txt   (nn = 01–14)

Run:
  python generate_prompts.py
"""

import os
import re

from systemsTarot import MAJOR_ARCANA, create_networks_suit, create_events_suit, \
    create_agents_suit, create_resources_suit

# ---------------------------------------------------------------------------
# Output directory
# ---------------------------------------------------------------------------
OUT_DIR = os.path.join(os.path.dirname(__file__), "resources", "prompts")
os.makedirs(OUT_DIR, exist_ok=True)


# ---------------------------------------------------------------------------
# Visual vocabulary per suit / arcana type
# ---------------------------------------------------------------------------

MAJOR_STYLE = (
    "mystical tarot card illustration, intricate Art Nouveau border with celestial motifs, "
    "deep indigo and gold palette, cosmic starfield background, symbolic and archetypal imagery, "
    "richly detailed, dramatic chiaroscuro lighting"
)

SUIT_STYLES = {
    "Networks": (
        "tarot card illustration, ornate geometric border, deep cerulean and cyan palette, "
        "luminous node-and-thread motifs, structural and crystalline aesthetic, "
        "glowing filaments on dark ground, detailed linework"
    ),
    "Events": (
        "tarot card illustration, dynamic Art Deco border with chevron motifs, "
        "amber and vermillion palette, kinetic energy, motion lines and lightning, "
        "dramatic directional lighting, sense of urgency and change"
    ),
    "Agents": (
        "tarot card illustration, organic border of intertwining figures and vines, "
        "emerald and forest-green palette, populated with symbolic figures or creatures, "
        "warm candlelit atmosphere, sense of intelligence and coordination"
    ),
    "Resources": (
        "tarot card illustration, earthy border of roots and mineral veins, "
        "ochre and burnished-gold palette, tactile materials and flowing substances, "
        "rich textures of wood, stone, water, and soil, abundance or scarcity made visible"
    ),
}

# Rank-specific visual cues for Minor Arcana
RANK_CUES = {
    1:  "a single seed, spark, or origin point — pure potential, void about to bloom",
    2:  "two elements in direct dialogue — a bridge, a handshake, or mirrored forms",
    3:  "three points forming a triangle — stability, redundancy, the first structure",
    4:  "a hub at centre with spokes radiating outward — centrality, hierarchy",
    5:  "fracture lines and diverging paths — tension, breakage, conflict",
    6:  "a web or lattice of equal nodes — distributed resilience, many equal paths",
    7:  "congestion, bottleneck, or overflow — too much pressing through too little",
    8:  "a growing spiral or compounding cascade — scale and network effects",
    9:  "over-abundance or entanglement — complexity at its limit",
    10: "a completed ring or full circle — maturity, the cycle closed",
    11: "a youthful or apprentice figure exploring the scene — curiosity, discovery",
    12: "an armoured or swift figure in motion — defender, executor, quick response",
    13: "a wise seated figure tending or guiding — nurture, deep understanding",
    14: "a commanding figure surveying the domain — mastery, strategic overview",
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def slugify(text: str) -> str:
    """Convert card name to a filesystem-safe slug."""
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "_", text)
    return text.strip("_")


def examples_to_visuals(examples: list[str]) -> str:
    """Pull the domain nouns from example strings for visual grounding."""
    # Keep only the bit after the colon (the concrete description)
    visuals = []
    for ex in examples:
        parts = ex.split(":", 1)
        if len(parts) == 2:
            visuals.append(parts[1].strip().lower())
    return "; ".join(visuals[:3])  # cap at 3 to keep prompt focused


# ---------------------------------------------------------------------------
# Prompt builders
# ---------------------------------------------------------------------------

def build_major_prompt(card, index: int) -> str:
    visual_grounding = examples_to_visuals(card.examples)
    questions_flavour = card.questions[0] if card.questions else ""

    lines = [
        f"{MAJOR_STYLE}.",
        f'Card title at bottom: "{card.name}" — Major Arcana.',
        f"Central image: {card.pattern}",
        f"Visual references woven into the scene: {visual_grounding}.",
        f'Philosophical mood: "{questions_flavour}"',
        "Portrait orientation, tarot card proportions (2:3.5), "
        "no text except the card title in an elegant serif at the base.",
    ]
    return "\n".join(lines)


def build_minor_prompt(card) -> str:
    suit = card.card_type        # e.g. "Networks"
    number = card.number         # 1–14
    style = SUIT_STYLES.get(suit, SUIT_STYLES["Networks"])
    rank_cue = RANK_CUES.get(number, "")
    visual_grounding = examples_to_visuals(card.examples)

    lines = [
        f"{style}.",
        f'Card title at bottom: "{card.name}" — {suit}, card {number}.',
        f"Central image: {card.pattern}",
        f"Compositional anchor: {rank_cue}.",
        f"Scene details drawn from: {visual_grounding}.",
        "Portrait orientation, tarot card proportions (2:3.5), "
        "no text except the card title in an elegant serif at the base.",
    ]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main generation loop
# ---------------------------------------------------------------------------

def generate_all():
    generated = []

    # --- Major Arcana ---
    for i, card in enumerate(MAJOR_ARCANA, start=1):
        filename = f"major_{i:02d}_{slugify(card.name)}.txt"
        prompt = build_major_prompt(card, i)
        path = os.path.join(OUT_DIR, filename)
        with open(path, "w") as f:
            f.write(prompt + "\n")
        generated.append((filename, card.name))

    # --- Minor Arcana ---
    suits = [
        ("networks", create_networks_suit()),
        ("events",   create_events_suit()),
        ("agents",   create_agents_suit()),
        ("resources",create_resources_suit()),
    ]

    for suit_prefix, cards in suits:
        for card in cards:
            filename = f"{suit_prefix}_{card.number:02d}_{slugify(card.name)}.txt"
            prompt = build_minor_prompt(card)
            path = os.path.join(OUT_DIR, filename)
            with open(path, "w") as f:
                f.write(prompt + "\n")
            generated.append((filename, card.name))

    # Summary
    print(f"Generated {len(generated)} prompt files → {OUT_DIR}/\n")
    for filename, name in generated:
        print(f"  {filename}  ({name})")


if __name__ == "__main__":
    generate_all()
