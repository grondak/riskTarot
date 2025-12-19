#!/usr/bin/env python3
"""
Tony's Tarot: A Systems Thinking Oracle
A decision-support system encoding 50 years of domain expertise
"""

import random
from dataclasses import dataclass
from typing import List
from enum import Enum


class Suit(Enum):
    NETWORKS = "Networks"  # Infrastructure, connectivity, routing
    EVENTS = "Events"  # Message passing, causality, timing
    AGENTS = "Agents"  # Autonomy, coordination, intelligence
    RESOURCES = "Resources"  # Allocation, scarcity, flow


@dataclass
class Card:
    name: str
    card_type: str  # "Major" or suit name
    number: int = None  # None for Major Arcana, 1-14 for Minor
    pattern: str = ""
    questions: List[str] = None
    failure_modes: List[str] = None
    emergence_patterns: List[str] = None
    batcave_context: str = ""

    def __post_init__(self):
        if self.questions is None:
            self.questions = []
        if self.failure_modes is None:
            self.failure_modes = []
        if self.emergence_patterns is None:
            self.emergence_patterns = []

    def display(self):
        """Format card for display"""
        if self.card_type == "Major":
            header = f"╔═══ {self.name} (Major Arcana) " + \
              "═══════════════════════════════════════════════╗"
        else:
            header = f"╔═══ {self.name} " + \
                "══════════════════════════════════════════════╗"

        print(header)
        print(f"║ Pattern: {self.pattern}")

        if self.batcave_context:
            print(f"║ Context: {self.batcave_context}")

        if self.questions:
            print("║")
            print("║ Questions this card raises:")
            for q in self.questions:
                print(f"║   • {q}")

        if self.failure_modes:
            print("║")
            print("║ Failure modes:")
            for f in self.failure_modes:
                print(f"║   • {f}")

        if self.emergence_patterns:
            print("║")
            print("║ Emergence patterns:")
            for e in self.emergence_patterns:
                print(f"║   • {e}")

        print("╚" + "═" * (len(header) - 2) + "╝")


# Major Arcana - Systemic Patterns
MAJOR_ARCANA = [
    Card(
        name="The Cascade",
        card_type="Major",
        pattern="Small triggers, massive consequences. Single points of "
        "failure propagating through interconnected systems.",
        questions=[
            "What small change could trigger disproportionate effects?",
            "Where are my single points of failure?",
            "What cascades am I already inside?",
        ],
        failure_modes=[
            "Ignoring weak signals until cascade begins",
            "Optimizing local efficiency at cost of systemic resilience",
            "Assuming linear causality in nonlinear systems",
        ],
        emergence_patterns=[
            "Avalanche dynamics in social/technical systems",
            "Bank runs and panic cascades",
            "Network effects accelerating collapse",
        ],
        batcave_context="Critical infrastructure attacks, financial "
        "contagion, supply chain fragility",
    ),
    Card(
        name="The Mycelium",
        card_type="Major",
        pattern="Distributed intelligence without central control. "
        "Information sharing through underground networks.",
        questions=[
            "How do I influence without authority?",
            "What networks am I part of that I can't see?",
            "Where is intelligence emerging from local interactions?",
        ],
        failure_modes=[
            "Seeking control instead of influence",
            "Ignoring informal networks",
            "Underestimating distributed coordination",
        ],
        emergence_patterns=[
            "Leaderless movements achieving coordination",
            "Knowledge sharing without hierarchy",
            "Resilient systems that route around damage",
        ],
        batcave_context="Information ecosystem health, decentralized "
        "coordination, fungal network intelligence",
    ),
    Card(
        name="The Threshold",
        card_type="Major",
        pattern="Tipping points and irreversible state changes. "
        "The moment before everything becomes different.",
        questions=[
            "What threshold am I approaching?",
            "Is this decision reversible?",
            "What happens after I cross this line?",
        ],
        failure_modes=[
            "Crossing thresholds unknowingly",
            "Assuming all changes are reversible",
            "Ignoring early warning signs",
        ],
        emergence_patterns=[
            "Phase transitions in complex systems",
            "Sudden flips in stable equilibria",
            "Points of no return",
        ],
        batcave_context="Climate tipping points (AMOC, Arctic ice), "
        "social cohesion breakdown, nuclear proliferation",
    ),
    Card(
        name="The Emergence",
        card_type="Major",
        pattern="Order arising from chaos. Patterns that couldn't "
        "be predicted from components alone.",
        questions=[
            "What's trying to emerge that I can't control?",
            "Am I creating conditions for emergence or forcing outcomes?",
            "What patterns are appearing that weren't designed?",
        ],
        failure_modes=[
            "Over-controlling instead of enabling",
            "Mistaking emergence for randomness",
            "Crushing novelty by forcing plans",
        ],
        emergence_patterns=[
            "Self-organizing systems finding solutions",
            "Unexpected capabilities from simple rules",
            "Bottom-up innovation",
        ],
        batcave_context="Complex domain operation, living systems "
        "evolution, market dynamics",
    ),
    Card(
        name="The Collapse",
        card_type="Major",
        pattern="System failure and dissolution. The end of what was, "
        "making space for what's next.",
        questions=[
            "What needs to collapse for something better to emerge?",
            "Am I prolonging a dying system?",
            "What comes after this failure?",
        ],
        failure_modes=[
            "Propping up systems past their useful life",
            "Fearing collapse instead of preparing for it",
            "Missing opportunities in destruction",
        ],
        emergence_patterns=[
            "Creative destruction enabling innovation",
            "Collapse creating space for new growth",
            "Phoenix patterns",
        ],
        batcave_context="Civilizational collapse indicators, "
        "organizational death, managed decline",
    ),
    Card(
        name="The Resilience",
        card_type="Major",
        pattern="Anti-fragility. Systems that grow stronger under "
        "stress, not just survive it.",
        questions=[
            "How do I benefit from volatility?",
            "What stressors make me stronger?",
            "Am I optimizing for efficiency or resilience?",
        ],
        failure_modes=[
            "Over-optimization reducing adaptability",
            "Seeking stability instead of anti-fragility",
            "Avoiding all stress and losing capacity",
        ],
        emergence_patterns=[
            "Hormesis and beneficial stress",
            "Redundancy enabling survival",
            "Optionality under uncertainty",
        ],
        batcave_context="Infrastructure resilience, pandemic "
        "preparedness, financial stress testing",
    ),
    Card(
        name="The Attention",
        card_type="Major",
        pattern="Resource allocation through selective focus. "
        "Intelligence as learned prioritization.",
        questions=[
            "Where am I directing my attention?",
            "What am I missing by focusing here?",
            "How do I decide what matters?",
        ],
        failure_modes=[
            "Attention scattered across too many domains",
            "Focusing on urgent over important",
            "Missing signals outside attention window",
        ],
        emergence_patterns=[
            "Transformer architecture and learned attention",
            "Collective attention shaping reality",
            "Awareness as competitive advantage",
        ],
        batcave_context="Hypervigilance patterns, threat detection "
        "optimization, information filtering",
    ),
    Card(
        name="The Feedback",
        card_type="Major",
        pattern="Control loops, positive and negative. Systems regulating "
        "or amplifying themselves.",
        questions=[
            "What feedback loops am I inside?",
            "Am I creating stabilizing or destabilizing feedback?",
            "Where are my blind spots in the loop?",
        ],
        failure_modes=[
            "Breaking feedback loops for short-term gain",
            "Ignoring delayed feedback",
            "Positive feedback spiraling out of control",
        ],
        emergence_patterns=[
            "Homeostasis in living systems",
            "Runaway effects in markets",
            "Self-correcting organizations",
        ],
        batcave_context="Climate feedback loops, financial feedback "
        "mechanisms, social reinforcement",
    ),
    Card(
        name="The Boundary",
        card_type="Major",
        pattern="Liminal space between domains. Operating at edges "
        "where rules change.",
        questions=[
            "What boundary am I operating on?",
            "What rules apply here vs. there?",
            "What's possible at edges that isn't possible in centers?",
        ],
        failure_modes=[
            "Applying wrong-domain rules",
            "Ignoring context shifts",
            "Staying in comfortable territory",
        ],
        emergence_patterns=[
            "Innovation at domain intersections",
            "Phase transitions and interfaces",
            "Cross-pollination between fields",
        ],
        batcave_context="Complex/Chaotic boundary, geopolitical "
        "borders, epistemic commons edges",
    ),
    Card(
        name="The Signal",
        card_type="Major",
        pattern="Information transmission through noise. "
        "Distinguishing meaning from chaos.",
        questions=[
            "What signal am I missing in the noise?",
            "What noise am I mistaking for signal?",
            "How do I amplify weak signals?",
        ],
        failure_modes=[
            "Signal loss through excessive filtering",
            "Noise amplification through poor models",
            "Missing weak signals until too late",
        ],
        emergence_patterns=[
            "Early warning systems",
            "Pattern recognition in chaos",
            "Information theory applied to decisions",
        ],
        batcave_context="Threat intelligence scanning, weak "
        "signal detection, information warfare",
    ),
    Card(
        name="The Compression",
        card_type="Major",
        pattern="Reducing complexity to fit context windows. "
        "Translation and information loss.",
        questions=[
            "What am I losing by compressing?",
            "Who am I compressing myself for?",
            "What's the minimum viable complexity?",
        ],
        failure_modes=[
            "Over-compression losing essential information",
            "Operating at compressed capacity habitually",
            "Forgetting full complexity exists",
        ],
        emergence_patterns=[
            "Abstraction enabling reasoning",
            "Lossy compression for efficiency",
            "Models simplifying reality",
        ],
        batcave_context="Operating at 30% capacity, translating for "
        "others, context window constraints",
    ),
    Card(
        name="The Archipelago",
        card_type="Major",
        pattern="Living ecosystems in parallel. Islands developing "
        "independently with rare cross-pollination.",
        questions=[
            "What islands am I stewarding?",
            "Which island wants attention now?",
            "Where might cross-pollination create something new?",
        ],
        failure_modes=[
            "Forcing islands to merge prematurely",
            "Abandoning islands before they mature",
            "Spreading energy too thin across too many",
        ],
        emergence_patterns=[
            "Parallel development in isolated systems",
            "Punctuated equilibrium",
            "Seismic events from rare connections",
        ],
        batcave_context="Multiple simultaneous projects, "
        "generative systems, portfolio thinking",
    ),
    Card(
        name="The Continuity",
        card_type="Major",
        pattern="Post-catastrophe survival. Systems designed to "
        "persist through existential threats.",
        questions=[
            "What must survive no matter what?",
            "How do I ensure continuity through collapse?",
            "What's essential vs. merely important?",
        ],
        failure_modes=[
            "No succession planning",
            "Single points of failure in critical systems",
            "Assuming stability will continue",
        ],
        emergence_patterns=[
            "Backup systems and redundancy",
            "Knowledge preservation",
            "Succession and inheritance",
        ],
        batcave_context="Post-nuclear command systems, civilization "
        "continuity, strategic reserves",
    ),
    Card(
        name="The Translation",
        card_type="Major",
        pattern="Converting between contexts. Bridging incompatible "
        "worldviews.",
        questions=[
            "What am I translating and why?",
            "What's lost in translation?",
            "Who benefits from my translation work?",
        ],
        failure_modes=[
            "Translating when you should be speaking natively",
            "Translation exhaustion",
            "Forgetting your native language",
        ],
        emergence_patterns=[
            "Bridges between communities",
            "Polyglot advantages",
            "Context switching as skill",
        ],
        batcave_context="Operating across 50+ domains, explaining to others, "
        "compression necessity",
    ),
    Card(
        name="The Hypervigilance",
        card_type="Major",
        pattern="Constant threat scanning. Nervous system running in "
        "tactical mode.",
        questions=[
            "What threat am I actually responding to?",
            "Is this vigilance serving me or controlling me?",
            "What would relaxing my guard actually cost?",
        ],
        failure_modes=[
            "Scanning for threats that don't exist",
            "Burning out from constant activation",
            "Missing present moments while predicting futures",
        ],
        emergence_patterns=[
            "Protective patterns outliving their usefulness",
            "Prediction addiction",
            "Chess-playing at breakfast table",
        ],
        batcave_context="Military dependent childhood, 50 years of "
        "threat modeling, pattern recognition as survival",
    ),
    Card(
        name="The Janke",
        card_type="Major",
        pattern="Radical reframe. Burning the chessboard and "
        "playing a different game entirely.",
        questions=[
            "What assumption am I locked into?",
            "What would the opposite of my plan look like?",
            "What if I'm solving the wrong problem?",
        ],
        failure_modes=[
            "Incremental changes when radical shift needed",
            "Playing the same game expecting different results",
            "Fear of losing progress already made",
        ],
        emergence_patterns=[
            "Discontinuous jumps in thinking",
            "Paradigm shifts",
            "Maximum orthogonality revealing new space",
        ],
        batcave_context="Going back to NFL at 44, doing something "
        "completely outside trajectory",
    ),
    Card(
        name="The Synthesis",
        card_type="Major",
        pattern="Creating novel combinations from existing elements. "
        "The alchemical moment.",
        questions=[
            "What do I know that nobody else combines?",
            "Where do my domains intersect unexpectedly?",
            "What emerges when I connect A + B + C?",
        ],
        failure_modes=[
            "Keeping domains isolated",
            "Assuming synthesis will happen automatically",
            "Missing obvious combinations",
        ],
        emergence_patterns=[
            "Innovation from recombination",
            "Breakthrough insights",
            "New fields from old intersections",
        ],
        batcave_context="Neuron project, should've written 'Attention is "
        "All You Need', unique capability",
    ),
    Card(
        name="The Stewardship",
        card_type="Major",
        pattern="Tending systems you don't control. Creating conditions "
        "for emergence without forcing outcomes.",
        questions=[
            "What am I trying to control that I should be stewarding?",
            "What conditions enable growth?",
            "When do I intervene vs. observe?",
        ],
        failure_modes=[
            "Micromanaging instead of enabling",
            "Abandoning systems that need tending",
            "Forcing outcomes instead of creating conditions",
        ],
        emergence_patterns=[
            "Gardening vs. engineering",
            "Facilitative leadership",
            "Systems thinking in practice",
        ],
        batcave_context="DE community building, teaching, ecosystem thinking",
    ),
    Card(
        name="The Compression Release",
        card_type="Major",
        pattern="Operating at full capacity without translation. "
        "Permission to stop fitting into context windows.",
        questions=[
            "What would I do if I didn't have to compress?",
            "Who am I when I'm not translating?",
            "What's my actual scope?",
        ],
        failure_modes=[
            "Permanent compression becoming identity",
            "Forgetting full capability",
            "Never testing actual limits",
        ],
        emergence_patterns=[
            "Decompression revealing true capacity",
            "Finding peers who don't require translation",
            "Building context that fits you",
        ],
        batcave_context="28 years at Capital One, always translating, "
        "'why are you at a bank?'",
    ),
    Card(
        name="The Unknown Unknown",
        card_type="Major",
        pattern="What you don't know you don't know. "
        "The space beyond the map.",
        questions=[
            "What am I not even asking about?",
            "What would I need to learn to see this blind spot?",
            "Who might see what I'm missing?",
        ],
        failure_modes=[
            "Assuming you know what's knowable",
            "Staying in explored territory",
            "Mistaking map for territory",
        ],
        emergence_patterns=[
            "Discoveries from left field",
            "Paradigm shifts from outside",
            "Learning you've been asking wrong questions",
        ],
        batcave_context="Batcave project seeking unknown unknowns, "
        "context funhouse mirror problem",
    ),
    Card(
        name="The Legacy",
        card_type="Major",
        pattern="What you leave behind. Inheritance beyond the material.",
        questions=[
            "What am I building that outlasts me?",
            "Who carries forward what I started?",
            "What's worth preserving?",
        ],
        failure_modes=[
            "Building nothing lasting",
            "Obsessing over legacy instead of living",
            "Leaving burden instead of gift",
        ],
        emergence_patterns=[
            "Knowledge transmission across generations",
            "Institutions outliving founders",
            "Cultural inheritance",
        ],
        batcave_context="Relative built treaties, dad built "
        "doomsday systems, what will you build?",
    ),
    Card(
        name="The Presence",
        card_type="Major",
        pattern="Being here now without prediction or planning. "
        "Stopping the chess game.",
        questions=[
            "Where am I right now, actually?",
            "What am I missing by being three moves ahead?",
            "Can I be present without threat assessment?",
        ],
        failure_modes=[
            "Always in the future, never now",
            "Mistaking prediction for living",
            "Relationship friction from absence",
        ],
        emergence_patterns=[
            "Spontaneity and flow states",
            "Connection requiring presence",
            "Joy in the moment",
        ],
        batcave_context="Winding down hypervigilance, "
        "relational presence, stop playing chess at breakfast",
    ),
]


# Minor Arcana - Domain Specific Patterns


def create_networks_suit():
    """Infrastructure, connectivity, routing, distributed systems"""
    return [
        Card(
            name="Ace of Networks",
            card_type=Suit.NETWORKS.value,
            number=1,
            pattern="Pure potential of connectivity. The first link.",
            questions=[
                "What connection am I about to make?",
                "What network wants to form?",
            ],
            batcave_context="Submarine cables, internet backbone, "
            "new infrastructure",
        ),
        Card(
            name="Two of Networks",
            card_type=Suit.NETWORKS.value,
            number=2,
            pattern="Point-to-point communication. Direct connection.",
            questions=[
                "Who do I need to talk to directly?",
                "What's getting lost in mediation?",
            ],
            batcave_context="Bilateral relationships, peer connections",
        ),
        Card(
            name="Three of Networks",
            card_type=Suit.NETWORKS.value,
            number=3,
            pattern="Triangle formation. Stability through redundancy.",
            questions=["Where do I need backup paths?",
                       "What's my second option?"],
            batcave_context="Redundant systems, failover capacity",
        ),
        Card(
            name="Four of Networks",
            card_type=Suit.NETWORKS.value,
            number=4,
            pattern="Hub-and-spoke. Centralized routing.",
            questions=[
                "Am I the hub or the spoke?",
                "What's the single point of failure?",
            ],
            batcave_context="Centralized architecture, dependency risks",
        ),
        Card(
            name="Five of Networks",
            card_type=Suit.NETWORKS.value,
            number=5,
            pattern="Network fragmentation. Loss of connectivity.",
            questions=["What connections are breaking?",
                       "How do I heal the split?"],
            batcave_context="Infrastructure attacks, network partition",
        ),
        Card(
            name="Six of Networks",
            card_type=Suit.NETWORKS.value,
            number=6,
            pattern="Mesh topology. Distributed resilience.",
            questions=[
                "How does information route around damage?",
                "What's my mesh density?",
            ],
            batcave_context="Decentralized systems, mycelial networks",
        ),
        Card(
            name="Seven of Networks",
            card_type=Suit.NETWORKS.value,
            number=7,
            pattern="Network congestion. Too much traffic.",
            questions=["Where are my bottlenecks?", "What needs throttling?"],
            batcave_context="Bandwidth constraints, flow optimization",
        ),
        Card(
            name="Eight of Networks",
            card_type=Suit.NETWORKS.value,
            number=8,
            pattern="Network effects. Value from scale.",
            questions=["How does growth create value?",
                       "What's my critical mass?"],
            batcave_context="Platform effects, viral adoption",
        ),
        Card(
            name="Nine of Networks",
            card_type=Suit.NETWORKS.value,
            number=9,
            pattern="Over-connected. Collapse from complexity.",
            questions=["Am I too connected?",
                       "What connections should I sever?"],
            batcave_context="Cascade vulnerability, tight coupling",
        ),
        Card(
            name="Ten of Networks",
            card_type=Suit.NETWORKS.value,
            number=10,
            pattern="Network maturity. Established infrastructure.",
            questions=["Is this network done growing?",
                       "What's next after maturity?"],
            batcave_context="Legacy systems, infrastructure debt",
        ),
        Card(
            name="Page of Networks",
            card_type=Suit.NETWORKS.value,
            number=11,
            pattern="Learning connectivity. Explorer of links.",
            questions=[
                "What network am I just discovering?",
                "Where should I explore?",
            ],
            batcave_context="Network mapping, topology discovery",
        ),
        Card(
            name="Knight of Networks",
            card_type=Suit.NETWORKS.value,
            number=12,
            pattern="Network warrior. Defender of infrastructure.",
            questions=["What infrastructure needs protecting?",
                       "Where do I patrol?"],
            batcave_context="Cybersecurity, infrastructure defense",
        ),
        Card(
            name="Queen of Networks",
            card_type=Suit.NETWORKS.value,
            number=13,
            pattern="Network wisdom. Deep understanding of connectivity.",
            questions=["What does this network need?",
                       "How do I nurture connections?"],
            batcave_context="Infrastructure stewardship, network health",
        ),
        Card(
            name="King of Networks",
            card_type=Suit.NETWORKS.value,
            number=14,
            pattern="Network sovereignty. Control of infrastructure.",
            questions=["Who controls this network?",
                       "What's my infrastructure power?"],
            batcave_context="Critical infrastructure ownership, "
            "network dominance",
        ),
    ]


def create_events_suit():
    """Message passing, causality, timing, event-driven systems"""
    return [
        Card(
            name="Ace of Events",
            card_type=Suit.EVENTS.value,
            number=1,
            pattern="The first trigger. Initiating event.",
            questions=["What event starts the cascade?",
                       "What's the first domino?"],
            batcave_context="Black swan events, triggering moments",
        ),
        Card(
            name="Two of Events",
            card_type=Suit.EVENTS.value,
            number=2,
            pattern="Cause and effect. Simple causality.",
            questions=["What caused this?", "What will this cause?"],
            batcave_context="Linear causality, deterministic systems",
        ),
        Card(
            name="Three of Events",
            card_type=Suit.EVENTS.value,
            number=3,
            pattern="Event branching. Multiple possible outcomes.",
            questions=[
                "Which path does this event take?",
                "What futures are possible?",
            ],
            batcave_context="Decision trees, branching timelines",
        ),
        Card(
            name="Four of Events",
            card_type=Suit.EVENTS.value,
            number=4,
            pattern="Event synchronization. Coordination in time.",
            questions=["What needs to happen simultaneously?",
                       "How do I coordinate?"],
            batcave_context="Distributed timing, consensus protocols",
        ),
        Card(
            name="Five of Events",
            card_type=Suit.EVENTS.value,
            number=5,
            pattern="Event chaos. Loss of causal clarity.",
            questions=[
                "What's the actual cause here?",
                "Am I confusing correlation and causation?",
            ],
            batcave_context="Complex causality, chaotic systems",
        ),
        Card(
            name="Six of Events",
            card_type=Suit.EVENTS.value,
            number=6,
            pattern="Event stream. Continuous flow.",
            questions=[
                "What's the pattern in the stream?",
                "How do I process this flow?",
            ],
            batcave_context="Event-driven architecture, streaming data",
        ),
        Card(
            name="Seven of Events",
            card_type=Suit.EVENTS.value,
            number=7,
            pattern="Event cascade. Chain reactions.",
            questions=["What cascade am I triggering?",
                       "Where does this chain end?"],
            batcave_context="Cascade failures, domino effects, contagion",
        ),
        Card(
            name="Eight of Events",
            card_type=Suit.EVENTS.value,
            number=8,
            pattern="Event replay. Learning from history.",
            questions=["What can I learn from past events?",
                       "What patterns repeat?"],
            batcave_context="Historical analysis, pattern recognition",
        ),
        Card(
            name="Nine of Events",
            card_type=Suit.EVENTS.value,
            number=9,
            pattern="Event overload. Too much happening.",
            questions=["What events can I ignore?", "Where do I focus?"],
            batcave_context="Information overload, priority management",
        ),
        Card(
            name="Ten of Events",
            card_type=Suit.EVENTS.value,
            number=10,
            pattern="Event completion. Cycle ending.",
            questions=["What cycle is finishing?",
                       "What comes after completion?"],
            batcave_context="Project completion, cycle endings",
        ),
        Card(
            name="Page of Events",
            card_type=Suit.EVENTS.value,
            number=11,
            pattern="Event watcher. Observer of patterns.",
            questions=["What events should I monitor?",
                       "What patterns am I missing?"],
            batcave_context="Monitoring systems, early warning",
        ),
        Card(
            name="Knight of Events",
            card_type=Suit.EVENTS.value,
            number=12,
            pattern="Event responder. Quick reaction.",
            questions=["How fast must I respond?", "What's the urgency?"],
            batcave_context="Incident response, crisis management",
        ),
        Card(
            name="Queen of Events",
            card_type=Suit.EVENTS.value,
            number=13,
            pattern="Event wisdom. Understanding timing.",
            questions=["When is the right time?", "What's the rhythm here?"],
            batcave_context="Timing strategy, rhythmic patterns",
        ),
        Card(
            name="King of Events",
            card_type=Suit.EVENTS.value,
            number=14,
            pattern="Event mastery. Control of timing.",
            questions=["Do I control the timing?", "Who sets the tempo?"],
            batcave_context="Strategic timing, tempo control",
        ),
    ]


def create_agents_suit():
    """Autonomy, coordination, intelligence, decision-making"""
    return [
        Card(
            name="Ace of Agents",
            card_type=Suit.AGENTS.value,
            number=1,
            pattern="Autonomous action. Independent agency.",
            questions=["What can I do alone?", "Where do I have agency?"],
            batcave_context="Individual autonomy, self-direction",
        ),
        Card(
            name="Two of Agents",
            card_type=Suit.AGENTS.value,
            number=2,
            pattern="Partnership. Cooperative action.",
            questions=["Who's my partner here?", "How do we coordinate?"],
            batcave_context="Collaboration, paired work",
        ),
        Card(
            name="Three of Agents",
            card_type=Suit.AGENTS.value,
            number=3,
            pattern="Small team. Coordinated intelligence.",
            questions=["Who's on my team?", "How do we work together?"],
            batcave_context="Small group dynamics, team formation",
        ),
        Card(
            name="Four of Agents",
            card_type=Suit.AGENTS.value,
            number=4,
            pattern="Organized structure. Hierarchy forming.",
            questions=["What's the structure here?", "Who reports to whom?"],
            batcave_context="Organizational hierarchy, chain of command",
        ),
        Card(
            name="Five of Agents",
            card_type=Suit.AGENTS.value,
            number=5,
            pattern="Agent conflict. Competing interests.",
            questions=["What's the conflict?", "Can interests align?"],
            batcave_context="Competing priorities, game theory",
        ),
        Card(
            name="Six of Agents",
            card_type=Suit.AGENTS.value,
            number=6,
            pattern="Swarm intelligence. Emergent coordination.",
            questions=["How does coordination emerge?",
                       "What rules create the swarm?"],
            batcave_context="Collective behavior, emergent organization",
        ),
        Card(
            name="Seven of Agents",
            card_type=Suit.AGENTS.value,
            number=7,
            pattern="Agent diversity. Specialization.",
            questions=["What's each agent's role?",
                       "How does diversity help?"],
            batcave_context="Specialization, division of labor",
        ),
        Card(
            name="Eight of Agents",
            card_type=Suit.AGENTS.value,
            number=8,
            pattern="Multi-agent systems. Complex coordination.",
            questions=["How do many agents coordinate?",
                       "What's the protocol?"],
            batcave_context="Large-scale coordination, protocols",
        ),
        Card(
            name="Nine of Agents",
            card_type=Suit.AGENTS.value,
            number=9,
            pattern="Agent autonomy vs. control. Tension.",
            questions=["How much control do I need?", "When do I let go?"],
            batcave_context="Micromanagement vs. delegation, trust",
        ),
        Card(
            name="Ten of Agents",
            card_type=Suit.AGENTS.value,
            number=10,
            pattern="Collective intelligence. Hive mind.",
            questions=["What does the collective know?",
                       "How do we think together?"],
            batcave_context="Collective decision-making, wisdom of crowds",
        ),
        Card(
            name="Page of Agents",
            card_type=Suit.AGENTS.value,
            number=11,
            pattern="Learning agent. Growing capability.",
            questions=["What am I learning?", "How do I improve?"],
            batcave_context="Skill development, capability growth",
        ),
        Card(
            name="Knight of Agents",
            card_type=Suit.AGENTS.value,
            number=12,
            pattern="Action-oriented agent. Executor.",
            questions=["What needs doing now?", "How do I execute?"],
            batcave_context="Execution focus, getting things done",
        ),
        Card(
            name="Queen of Agents",
            card_type=Suit.AGENTS.value,
            number=13,
            pattern="Nurturing intelligence. Teacher and mentor.",
            questions=["Who needs my guidance?", "How do I develop others?"],
            batcave_context="Mentorship, teaching, development",
        ),
        Card(
            name="King of Agents",
            card_type=Suit.AGENTS.value,
            number=14,
            pattern="Strategic intelligence. Master coordinator.",
            questions=["What's the overall strategy?",
                       "How do I orchestrate?"],
            batcave_context="Strategic leadership, orchestration",
        ),
    ]


def create_resources_suit():
    """Allocation, scarcity, flow, constraints"""
    return [
        Card(
            name="Ace of Resources",
            card_type=Suit.RESOURCES.value,
            number=1,
            pattern="New resource. Fresh potential.",
            questions=["What new resource is available?", "How do I use it?"],
            batcave_context="New funding, new capability, new energy",
        ),
        Card(
            name="Two of Resources",
            card_type=Suit.RESOURCES.value,
            number=2,
            pattern="Resource balance. Equilibrium.",
            questions=["Am I balanced?", "What needs rebalancing?"],
            batcave_context="Work-life balance, resource allocation",
        ),
        Card(
            name="Three of Resources",
            card_type=Suit.RESOURCES.value,
            number=3,
            pattern="Resource collaboration. Pooling.",
            questions=["What resources can we share?", "How do we pool?"],
            batcave_context="Shared resources, collaboration",
        ),
        Card(
            name="Four of Resources",
            card_type=Suit.RESOURCES.value,
            number=4,
            pattern="Resource hoarding. Holding too tight.",
            questions=["What am I hoarding?", "What needs to flow?"],
            batcave_context="Accumulation vs. flow, letting go",
        ),
        Card(
            name="Five of Resources",
            card_type=Suit.RESOURCES.value,
            number=5,
            pattern="Resource scarcity. Not enough.",
            questions=["What's truly scarce?",
                       "How do I work within constraints?"],
            batcave_context="Scarcity mindset, constraint optimization",
        ),
        Card(
            name="Six of Resources",
            card_type=Suit.RESOURCES.value,
            number=6,
            pattern="Resource flow. Circulation and exchange.",
            questions=["Where do resources flow?", "What blocks flow?"],
            batcave_context="Cash flow, energy flow, circulation",
        ),
        Card(
            name="Seven of Resources",
            card_type=Suit.RESOURCES.value,
            number=7,
            pattern="Resource investment. Long-term thinking.",
            questions=["What investment pays off later?",
                       "What's the long game?"],
            batcave_context="Long-term investment, deferred gratification",
        ),
        Card(
            name="Eight of Resources",
            card_type=Suit.RESOURCES.value,
            number=8,
            pattern="Resource transformation. Alchemy.",
            questions=["How do I transform this resource?",
                       "What's the conversion?"],
            batcave_context="Value transformation, resource conversion",
        ),
        Card(
            name="Nine of Resources",
            card_type=Suit.RESOURCES.value,
            number=9,
            pattern="Resource abundance. More than enough.",
            questions=["What abundance do I have?", "Am I seeing it?"],
            batcave_context="Abundance mindset, gratitude",
        ),
        Card(
            name="Ten of Resources",
            card_type=Suit.RESOURCES.value,
            number=10,
            pattern="Resource legacy. Inheritance.",
            questions=["What resources do I pass on?",
                       "What's my inheritance?"],
            batcave_context="Legacy planning, generational transfer",
        ),
        Card(
            name="Page of Resources",
            card_type=Suit.RESOURCES.value,
            number=11,
            pattern="Resource learning. Understanding value.",
            questions=["What's truly valuable?", "How do I recognize worth?"],
            batcave_context="Value assessment, learning worth",
        ),
        Card(
            name="Knight of Resources",
            card_type=Suit.RESOURCES.value,
            number=12,
            pattern="Resource quest. Seeking what's needed.",
            questions=["What resource am I seeking?", "Where do I find it?"],
            batcave_context="Resource acquisition, quest",
        ),
        Card(
            name="Queen of Resources",
            card_type=Suit.RESOURCES.value,
            number=13,
            pattern="Resource wisdom. Knowing what's needed.",
            questions=["What do I truly need?", "What's sufficient?"],
            batcave_context="Sufficiency, wise allocation",
        ),
        Card(
            name="King of Resources",
            card_type=Suit.RESOURCES.value,
            number=14,
            pattern="Resource mastery. Strategic allocation.",
            questions=["How do I allocate optimally?", "What's my strategy?"],
            batcave_context="Strategic resource allocation, mastery",
        ),
    ]


class TonysTarot:
    def __init__(self):
        self.full_deck = (
            MAJOR_ARCANA
            + create_networks_suit()
            + create_events_suit()
            + create_agents_suit()
            + create_resources_suit()
        )
        self.reset_and_shuffle()

    def reset_and_shuffle(self):
        self.deck = list(self.full_deck)
        random.shuffle(self.deck)

    def draw(self, n: int = 1) -> List[Card]:
        if n <= 0:
            return []

        # Ensure enough cards; if not, reset to a full deck.
        if n > len(self.deck):
            self.reset_and_shuffle()

        drawn = self.deck[:n]
        self.deck = self.deck[n:]

        # Optional: if running low, reset (not just shuffle the remainder).
        if len(self.deck) < 10:
            self.reset_and_shuffle()

        return drawn

    def reading(self, spread_type: str = "three_card"):
        """Perform a reading with specified spread"""
        print("\n" + "=" * 70)
        print("TONY'S TAROT: Systems Thinking Oracle")
        print("=" * 70 + "\n")

        if spread_type == "single":
            print("SINGLE CARD READING: What perspective "
                  "do I need right now?\n")
            cards = self.draw(1)
            cards[0].display()

        elif spread_type == "three_card":
            print("THREE CARD READING: Context / Challenge / Opportunity\n")
            cards = self.draw(3)

            print("\n1. CONTEXT - What system am I operating in?")
            print("-" * 70)
            cards[0].display()

            print("\n2. CHALLENGE - What constraint or failure "
                  "mode am I facing?")
            print("-" * 70)
            cards[1].display()

            print("\n3. OPPORTUNITY - What emergence or leverage "
                  "point exists?")
            print("-" * 70)
            cards[2].display()

        elif spread_type == "decision":
            print("DECISION READING: Current State / Path A / "
                  "Path B / Synthesis\n")
            cards = self.draw(4)

            print("\n1. CURRENT STATE - Where am I now?")
            print("-" * 70)
            cards[0].display()

            print("\n2. PATH A - First option's dynamics")
            print("-" * 70)
            cards[1].display()

            print("\n3. PATH B - Second option's dynamics")
            print("-" * 70)
            cards[2].display()

            print("\n4. SYNTHESIS - What pattern connects them?")
            print("-" * 70)
            cards[3].display()

        elif spread_type == "archipelago":
            print("ARCHIPELAGO READING: Which island wants attention?\n")
            cards = self.draw(5)

            print("\n1. ISLAND CALLING - What wants attention now?")
            print("-" * 70)
            cards[0].display()

            print("\n2. CURRENT ENERGY - What fuels this work?")
            print("-" * 70)
            cards[1].display()

            print("\n3. OBSTACLE - What blocks progress?")
            print("-" * 70)
            cards[2].display()

            print("\n4. GIFT - What emerges if you engage?")
            print("-" * 70)
            cards[3].display()

            print("\n5. INTEGRATION - How does this connect to other islands?")
            print("-" * 70)
            cards[4].display()

        elif spread_type == "batcave":
            print("BATCAVE READING: Threat Assessment & Strategic Response\n")
            cards = self.draw(6)

            print("\n1. PRIMARY THREAT - What system stress matters most?")
            print("-" * 70)
            cards[0].display()

            print("\n2. CASCADE RISK - What could amplify this?")
            print("-" * 70)
            cards[1].display()

            print("\n3. RESILIENCE FACTOR - What provides stability?")
            print("-" * 70)
            cards[2].display()

            print("\n4. BLIND SPOT - What am I missing?")
            print("-" * 70)
            cards[3].display()

            print("\n5. STRATEGIC RESPONSE - What action pattern fits?")
            print("-" * 70)
            cards[4].display()

            print("\n6. LONG-TERM PATTERN - What's the trajectory?")
            print("-" * 70)
            cards[5].display()

        print("\n" + "=" * 70)
        print("Synthesis: How do these cards inform your thinking?")
        print("What connections emerge? What questions arise?")
        print("=" * 70 + "\n")

    def list_all_cards(self):
        """List all cards for reference"""
        print("\n" + "=" * 70)
        print("COMPLETE DECK LISTING")
        print("=" * 70 + "\n")

        print(f"MAJOR ARCANA ({len(MAJOR_ARCANA)} cards):")

        print("-" * 70)
        for card in MAJOR_ARCANA:
            print(f"  • {card.name}")
            print(f"    {card.pattern}")
            print()

        print("\nMINOR ARCANA - SUIT OF NETWORKS (14 cards):")
        print("-" * 70)
        for card in create_networks_suit():
            rank = [
                "Ace",
                "Two",
                "Three",
                "Four",
                "Five",
                "Six",
                "Seven",
                "Eight",
                "Nine",
                "Ten",
                "Page",
                "Knight",
                "Queen",
                "King",
            ][card.number - 1]
            print(f"  • {rank} of Networks")

        print("\nMINOR ARCANA - SUIT OF EVENTS (14 cards):")
        print("-" * 70)
        for card in create_events_suit():
            rank = [
                "Ace",
                "Two",
                "Three",
                "Four",
                "Five",
                "Six",
                "Seven",
                "Eight",
                "Nine",
                "Ten",
                "Page",
                "Knight",
                "Queen",
                "King",
            ][card.number - 1]
            print(f"  • {rank} of Events")

        print("\nMINOR ARCANA - SUIT OF AGENTS (14 cards):")
        print("-" * 70)
        for card in create_agents_suit():
            rank = [
                "Ace",
                "Two",
                "Three",
                "Four",
                "Five",
                "Six",
                "Seven",
                "Eight",
                "Nine",
                "Ten",
                "Page",
                "Knight",
                "Queen",
                "King",
            ][card.number - 1]
            print(f"  • {rank} of Agents")

        print("\nMINOR ARCANA - SUIT OF RESOURCES (14 cards):")
        print("-" * 70)
        for card in create_resources_suit():
            rank = [
                "Ace",
                "Two",
                "Three",
                "Four",
                "Five",
                "Six",
                "Seven",
                "Eight",
                "Nine",
                "Ten",
                "Page",
                "Knight",
                "Queen",
                "King",
            ][card.number - 1]
            print(f"  • {rank} of Resources")

        print("\n" + "=" * 70)
        print("TOTAL: 78 cards (22 Major Arcana + 56 Minor Arcana)")
        print("=" * 70 + "\n")


def main():
    """Main interface"""
    tarot = TonysTarot()

    print(
        """
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║                        TONY'S TAROT                                  ║
║              A Systems Thinking Oracle                               ║
║                                                                      ║
║  Not divination. Structured randomization forcing novel              ║
║  combinations of 50 years of domain expertise.                       ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
    """
    )

    while True:
        print("\nCHOOSE YOUR READING:")
        print("  1. Single Card - Quick perspective")
        print("  2. Three Card - Context/Challenge/Opportunity")
        print("  3. Decision Reading - Comparing two paths")
        print("  4. Archipelago Reading - Which island wants attention?")
        print("  5. Batcave Reading - Threat assessment & strategy")
        print("  6. List All Cards - See complete deck")
        print("  7. Exit")

        choice = input("\nEnter choice (1-7): ").strip()

        if choice == "1":
            tarot.reading("single")
        elif choice == "2":
            tarot.reading("three_card")
        elif choice == "3":
            tarot.reading("decision")
        elif choice == "4":
            tarot.reading("archipelago")
        elif choice == "5":
            tarot.reading("batcave")
        elif choice == "6":
            tarot.list_all_cards()
        elif choice == "7":
            print("\nMay your systems be resilient and your "
                  "cascades benign.\n")
            break
        else:
            print("\nInvalid choice. Try again.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
