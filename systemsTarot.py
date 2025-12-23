#!/usr/bin/env python3
"""
Systems Thinking Tarot: A Universal Oracle
A decision-support framework for pattern recognition across domains
"""

import random
from dataclasses import dataclass
from typing import List
from enum import Enum


class Suit(Enum):
    NETWORKS = "Networks"  # Structure, connectivity, relationships
    EVENTS = "Events"  # Dynamics, causality, timing
    AGENTS = "Agents"  # Agency, coordination, intelligence
    RESOURCES = "Resources"  # Constraints, allocation, flow


@dataclass
class Card:
    name: str
    card_type: str  # "Major" or suit name
    number: int = None  # None for Major Arcana, 1-14 for Minor
    pattern: str = ""
    questions: List[str] = None
    examples: List[str] = None
    
    def __post_init__(self):
        if self.questions is None:
            self.questions = []
        if self.examples is None:
            self.examples = []

    def display(self):
        """Format card for display"""
        if self.card_type == "Major":
            header = f"╔═══ {self.name} (Major Arcana) ═══════════════════════════════════════════════╗"
        else:
            header = f"╔═══ {self.name} ══════════════════════════════════════════════╗"

        print(header)
        print(f"║ Pattern: {self.pattern}")

        if self.questions:
            print("║")
            print("║ Questions to ask:")
            for q in self.questions:
                print(f"║   • {q}")

        if self.examples:
            print("║")
            print("║ Examples across domains:")
            for e in self.examples:
                print(f"║   • {e}")

        print("╚" + "═" * (len(header) - 2) + "╝")


# Major Arcana - Universal System Patterns
MAJOR_ARCANA = [
    Card(
        name="The Cascade",
        card_type="Major",
        pattern="Small triggers creating disproportionate effects through connected systems.",
        questions=[
            "What small change could trigger large consequences?",
            "Where are the critical dependencies?",
            "What chain reaction am I inside?",
        ],
        examples=[
            "Engineering: Single component failure bringing down entire system",
            "Social: Rumor spreading exponentially through network",
            "Financial: Bank run triggering systemic crisis",
            "Ecological: Keystone species removal cascading through food web",
        ],
    ),
    Card(
        name="The Network",
        card_type="Major",
        pattern="Distributed intelligence emerging from local connections without central control.",
        questions=[
            "How can influence spread without direct authority?",
            "What invisible networks am I part of?",
            "Where does coordination emerge from simple rules?",
        ],
        examples=[
            "Nature: Fungal networks sharing resources between trees",
            "Social: Movements organizing without formal leadership",
            "Technical: Mesh networks routing around damage",
            "Economic: Market coordination without central planning",
        ],
    ),
    Card(
        name="The Threshold",
        card_type="Major",
        pattern="Tipping points where systems irreversibly shift to new states.",
        questions=[
            "What point of no return am I approaching?",
            "Can this change be reversed?",
            "What early warnings signal the threshold?",
        ],
        examples=[
            "Physics: Water freezing at critical temperature",
            "Ecology: Lake flipping from clear to turbid state",
            "Social: Trust collapse in relationships or institutions",
            "Business: Market share tipping toward winner-takes-all",
        ],
    ),
    Card(
        name="The Emergence",
        card_type="Major",
        pattern="Complex order arising from simple interactions - patterns unpredictable from components.",
        questions=[
            "What's trying to emerge beyond my control?",
            "Am I enabling conditions or forcing outcomes?",
            "What unexpected patterns are appearing?",
        ],
        examples=[
            "Biology: Consciousness emerging from neurons",
            "Architecture: Desire paths emerging from foot traffic",
            "Software: System behavior emerging from component interactions",
            "Markets: Prices emerging from individual trades",
        ],
    ),
    Card(
        name="The Collapse",
        card_type="Major",
        pattern="System failure creating space for transformation - endings enabling beginnings.",
        questions=[
            "What needs to end for something new to start?",
            "Am I sustaining something past its useful life?",
            "What opportunities exist in this breakdown?",
        ],
        examples=[
            "Business: Company failure freeing capital for innovation",
            "Ecology: Forest fire enabling new growth",
            "Personal: Habit collapse creating space for change",
            "Infrastructure: Old system retirement forcing modernization",
        ],
    ),
    Card(
        name="The Resilience",
        card_type="Major",
        pattern="Systems growing stronger through stress, not just surviving it.",
        questions=[
            "How can I benefit from volatility?",
            "What stressors make this system stronger?",
            "Am I optimizing for efficiency or adaptability?",
        ],
        examples=[
            "Biology: Muscles growing from exercise stress",
            "Engineering: Redundant systems surviving failures",
            "Economics: Diversified portfolios weathering shocks",
            "Social: Communities strengthened through adversity",
        ],
    ),
    Card(
        name="The Attention",
        card_type="Major",
        pattern="Intelligence as selective focus - what gets measured gets managed.",
        questions=[
            "Where is attention being directed?",
            "What's invisible because it's not measured?",
            "How do I decide what matters?",
        ],
        examples=[
            "Business: Metrics shaping organizational behavior",
            "Media: Headlines directing public focus",
            "Personal: Habits following tracked behaviors",
            "AI: Attention mechanisms in neural networks",
        ],
    ),
    Card(
        name="The Feedback",
        card_type="Major",
        pattern="Control loops regulating or amplifying - systems responding to their own outputs.",
        questions=[
            "What feedback loops am I inside?",
            "Is this loop stabilizing or amplifying?",
            "Where are delays hiding feedback?",
        ],
        examples=[
            "Climate: Ice melting reducing reflectivity increasing melting",
            "Economics: Inflation expectations driving actual inflation",
            "Audio: Microphone near speaker creating squealing loop",
            "Social: Panic causing behavior causing more panic",
        ],
    ),
    Card(
        name="The Boundary",
        card_type="Major",
        pattern="Edges between domains where different rules apply - operating at interfaces.",
        questions=[
            "What boundary am I operating on?",
            "How do rules change across this edge?",
            "What's possible at interfaces that isn't elsewhere?",
        ],
        examples=[
            "Biology: Cell membranes controlling exchange",
            "Innovation: Cross-disciplinary insights at field boundaries",
            "Geography: Coastal zones with unique ecosystems",
            "Organization: Departments with different cultures meeting",
        ],
    ),
    Card(
        name="The Signal",
        card_type="Major",
        pattern="Meaningful information embedded in noise - distinguishing pattern from randomness.",
        questions=[
            "What signal am I missing in the noise?",
            "What noise am I treating as signal?",
            "How do I amplify weak but important signals?",
        ],
        examples=[
            "Medicine: Symptoms indicating underlying disease",
            "Finance: Market movements signaling regime changes",
            "Science: Experimental data revealing new phenomena",
            "Social: Weak signals indicating cultural shifts",
        ],
    ),
    Card(
        name="The Compression",
        card_type="Major",
        pattern="Reducing complexity to fit constraints - translation with information loss.",
        questions=[
            "What am I losing by simplifying?",
            "Is this compression necessary or habitual?",
            "What's the minimum viable complexity?",
        ],
        examples=[
            "Communication: Explaining expertise to non-experts",
            "Data: Lossy compression for storage/transmission",
            "Models: Simplified representations of complex reality",
            "Teaching: Reducing concepts to learnable chunks",
        ],
    ),
    Card(
        name="The Archipelago",
        card_type="Major",
        pattern="Parallel systems developing independently with rare cross-pollination.",
        questions=[
            "What separate systems am I maintaining?",
            "Which deserves attention now?",
            "Where might connections create value?",
        ],
        examples=[
            "Biology: Isolated populations evolving differently",
            "Projects: Multiple initiatives progressing in parallel",
            "Knowledge: Separate fields occasionally intersecting",
            "Communities: Independent groups with occasional exchange",
        ],
    ),
    Card(
        name="The Continuity",
        card_type="Major",
        pattern="Mechanisms ensuring survival through disruption - what persists when everything changes.",
        questions=[
            "What must survive no matter what?",
            "How do I ensure continuity through crisis?",
            "What's essential versus merely important?",
        ],
        examples=[
            "Biology: DNA preserving information across generations",
            "Business: Succession planning and redundancy",
            "Culture: Traditions maintaining identity through change",
            "Infrastructure: Backup systems for critical functions",
        ],
    ),
    Card(
        name="The Translation",
        card_type="Major",
        pattern="Converting between different contexts or languages - bridging incompatible systems.",
        questions=[
            "What am I translating and for whom?",
            "What's inevitably lost in translation?",
            "When should I speak natively instead?",
        ],
        examples=[
            "Language: Interpreting between speakers",
            "Technical: Explaining complex systems to stakeholders",
            "Cultural: Bridging different organizational norms",
            "Format: Converting data between systems",
        ],
    ),
    Card(
        name="The Vigilance",
        card_type="Major",
        pattern="Constant scanning for threats or changes - maintaining readiness at a cost.",
        questions=[
            "What threat am I actually responding to?",
            "Is this vigilance still serving its purpose?",
            "What's the cost of constant alertness?",
        ],
        examples=[
            "Security: Continuous monitoring for intrusions",
            "Health: Immune system scanning for pathogens",
            "Markets: Traders watching for opportunities/risks",
            "Personal: Hyperawareness from past trauma",
        ],
    ),
    Card(
        name="The Reframe",
        card_type="Major",
        pattern="Radical perspective shift - abandoning the current game for a different one.",
        questions=[
            "What assumption am I locked into?",
            "What would the opposite approach look like?",
            "Am I solving the wrong problem?",
        ],
        examples=[
            "Business: Pivoting to new market instead of fighting in old",
            "Problem-solving: Changing the question instead of finding answers",
            "Conflict: Redefining win conditions",
            "Innovation: Questioning fundamental assumptions",
        ],
    ),
    Card(
        name="The Synthesis",
        card_type="Major",
        pattern="Creating novel combinations from existing elements - the alchemical moment.",
        questions=[
            "What elements could combine in new ways?",
            "Where do my domains intersect unexpectedly?",
            "What emerges from connection A + B + C?",
        ],
        examples=[
            "Innovation: Smartphone combining phone + computer + camera",
            "Cuisine: Fusion cooking merging culinary traditions",
            "Science: Interdisciplinary insights creating new fields",
            "Art: Mixed media creating novel expressions",
        ],
    ),
    Card(
        name="The Stewardship",
        card_type="Major",
        pattern="Tending systems without controlling - creating conditions for emergence.",
        questions=[
            "What am I controlling that I should be stewarding?",
            "What conditions enable natural growth?",
            "When do I intervene versus observe?",
        ],
        examples=[
            "Gardening: Providing conditions, not forcing growth",
            "Leadership: Enabling teams rather than micromanaging",
            "Ecology: Conservation through habitat protection",
            "Teaching: Creating learning environments",
        ],
    ),
    Card(
        name="The Release",
        card_type="Major",
        pattern="Operating at full capacity without constraint - permission to expand completely.",
        questions=[
            "What would I do without current constraints?",
            "What's my actual scope when uncompressed?",
            "Who am I when not adapting to limits?",
        ],
        examples=[
            "Creative: Artist working without commercial constraints",
            "Athletic: Performing at peak without holding back",
            "Intellectual: Exploring ideas at full depth",
            "Expression: Communicating without translation",
        ],
    ),
    Card(
        name="The Unknown Unknown",
        card_type="Major",
        pattern="What you don't know you don't know - the space beyond your map.",
        questions=[
            "What am I not even asking about?",
            "What would reveal this blind spot?",
            "Who might see what I'm missing?",
        ],
        examples=[
            "Science: Paradigm shifts from unexpected discoveries",
            "Business: Disruption from unconsidered competitors",
            "Personal: Assumptions never questioned",
            "Risk: Black swans by definition unexpected",
        ],
    ),
    Card(
        name="The Legacy",
        card_type="Major",
        pattern="What persists beyond individual existence - inheritance across time.",
        questions=[
            "What am I building that outlasts me?",
            "Who carries forward what I started?",
            "What's worth preserving?",
        ],
        examples=[
            "Culture: Knowledge transmission across generations",
            "Infrastructure: Buildings and systems serving future users",
            "Teaching: Ideas living in students' minds",
            "Nature: Ecosystems shaped by past species",
        ],
    ),
    Card(
        name="The Presence",
        card_type="Major",
        pattern="Being fully here now without prediction or planning - stopping the chess game.",
        questions=[
            "Where am I actually right now?",
            "What am I missing by being elsewhere mentally?",
            "Can I engage without constantly anticipating?",
        ],
        examples=[
            "Mindfulness: Awareness of current moment",
            "Flow states: Full engagement in activity",
            "Relationships: Genuine connection requiring presence",
            "Performance: Responding to what is, not what might be",
        ],
    ),
]


# Minor Arcana - Domain Specific Patterns

def create_networks_suit():
    """Structure, connectivity, relationships"""
    return [
        Card(
            name="Ace of Networks",
            card_type=Suit.NETWORKS.value,
            number=1,
            pattern="Pure potential of connection - the first link.",
            questions=[
                "What new connection wants to form?",
                "What relationship is just beginning?",
            ],
            examples=[
                "Infrastructure: First cable connecting two locations",
                "Social: Meeting someone who could become important",
                "Business: Initial partnership conversation",
                "Biological: Neurons forming new synapses",
            ],
        ),
        Card(
            name="Two of Networks",
            card_type=Suit.NETWORKS.value,
            number=2,
            pattern="Point-to-point connection - direct relationship.",
            questions=[
                "Who needs direct communication here?",
                "What's lost through intermediaries?",
            ],
            examples=[
                "Communication: Direct conversation vs mediated",
                "Technology: Peer-to-peer connection",
                "Diplomacy: Bilateral negotiations",
                "Trade: Direct exchange between parties",
            ],
        ),
        Card(
            name="Three of Networks",
            card_type=Suit.NETWORKS.value,
            number=3,
            pattern="Triangle formation - stability through redundancy.",
            questions=[
                "Where do I need backup connections?",
                "What's my alternative path?",
            ],
            examples=[
                "Engineering: Redundant systems for reliability",
                "Social: Friend groups providing stability",
                "Supply chain: Multiple suppliers for resilience",
                "Structure: Triangles in architecture for strength",
            ],
        ),
        Card(
            name="Four of Networks",
            card_type=Suit.NETWORKS.value,
            number=4,
            pattern="Hub-and-spoke - centralized structure.",
            questions=[
                "Who's the central hub here?",
                "What's the single point of failure?",
            ],
            examples=[
                "Organizations: Hierarchical reporting structure",
                "Transportation: Airport hub connecting many cities",
                "Information: Centralized database or server",
                "Social: Influential person connecting many others",
            ],
        ),
        Card(
            name="Five of Networks",
            card_type=Suit.NETWORKS.value,
            number=5,
            pattern="Network fragmentation - breaking connections.",
            questions=[
                "What connections are breaking?",
                "How can I repair this split?",
            ],
            examples=[
                "Social: Community dividing into factions",
                "Technical: Network partition or outage",
                "Political: Alliance breakdown",
                "Infrastructure: Road or bridge failure isolating regions",
            ],
        ),
        Card(
            name="Six of Networks",
            card_type=Suit.NETWORKS.value,
            number=6,
            pattern="Mesh topology - distributed resilience.",
            questions=[
                "How does information route around damage?",
                "What's the optimal connection density?",
            ],
            examples=[
                "Internet: Packets routing around failed nodes",
                "Nature: Mycelial networks with many paths",
                "Social: Communities with multiple weak ties",
                "Power grid: Interconnected for reliability",
            ],
        ),
        Card(
            name="Seven of Networks",
            card_type=Suit.NETWORKS.value,
            number=7,
            pattern="Network congestion - too much traffic.",
            questions=[
                "Where are the bottlenecks?",
                "What needs throttling or expansion?",
            ],
            examples=[
                "Traffic: Roads at capacity causing delays",
                "Computing: Bandwidth limitations slowing system",
                "Communication: Overwhelmed with messages",
                "Social: Too many commitments to maintain well",
            ],
        ),
        Card(
            name="Eight of Networks",
            card_type=Suit.NETWORKS.value,
            number=8,
            pattern="Network effects - value emerging from scale.",
            questions=[
                "How does growth create value?",
                "What's the critical mass threshold?",
            ],
            examples=[
                "Platforms: Each user making service more valuable",
                "Language: Utility increasing with number of speakers",
                "Standards: Adoption creating momentum",
                "Ecosystems: Biodiversity supporting more life",
            ],
        ),
        Card(
            name="Nine of Networks",
            card_type=Suit.NETWORKS.value,
            number=9,
            pattern="Over-connection - complexity causing fragility.",
            questions=[
                "Am I too connected?",
                "What connections should I reduce?",
            ],
            examples=[
                "Finance: Tight coupling enabling contagion",
                "Personal: Overcommitment creating stress",
                "Software: Excessive dependencies causing failures",
                "Ecology: Monoculture vulnerable to cascade",
            ],
        ),
        Card(
            name="Ten of Networks",
            card_type=Suit.NETWORKS.value,
            number=10,
            pattern="Network maturity - established infrastructure.",
            questions=[
                "Is this network fully built?",
                "What comes after maturity?",
            ],
            examples=[
                "Infrastructure: Complete road or utility network",
                "Social: Established community with stable relationships",
                "Professional: Mature industry structure",
                "Ecological: Climax ecosystem in equilibrium",
            ],
        ),
        Card(
            name="Page of Networks",
            card_type=Suit.NETWORKS.value,
            number=11,
            pattern="Learning connectivity - exploring connections.",
            questions=[
                "What network am I just discovering?",
                "Where should I explore?",
            ],
            examples=[
                "Student: Learning field's key relationships",
                "Explorer: Mapping new territory",
                "Newcomer: Understanding social structure",
                "Analyst: Discovering system architecture",
            ],
        ),
        Card(
            name="Knight of Networks",
            card_type=Suit.NETWORKS.value,
            number=12,
            pattern="Network defender - protecting infrastructure.",
            questions=[
                "What infrastructure needs protection?",
                "What threats to connectivity exist?",
            ],
            examples=[
                "Cybersecurity: Defending against network attacks",
                "Maintenance: Keeping infrastructure operational",
                "Diplomacy: Preserving alliances",
                "Conservation: Protecting ecological corridors",
            ],
        ),
        Card(
            name="Queen of Networks",
            card_type=Suit.NETWORKS.value,
            number=13,
            pattern="Network wisdom - understanding connectivity deeply.",
            questions=[
                "What does this network need to thrive?",
                "How do I nurture connections?",
            ],
            examples=[
                "Community builder: Fostering relationships",
                "Architect: Designing for connection",
                "Ecologist: Understanding ecosystem relationships",
                "Manager: Building organizational bridges",
            ],
        ),
        Card(
            name="King of Networks",
            card_type=Suit.NETWORKS.value,
            number=14,
            pattern="Network mastery - strategic control of infrastructure.",
            questions=[
                "Who controls this network?",
                "What's the strategic value of connectivity?",
            ],
            examples=[
                "Infrastructure owner: Controlling critical systems",
                "Platform operator: Network effects as moat",
                "Diplomat: Managing alliance structure",
                "Keystone species: Ecological network centrality",
            ],
        ),
    ]


def create_events_suit():
    """Dynamics, causality, timing"""
    return [
        Card(
            name="Ace of Events",
            card_type=Suit.EVENTS.value,
            number=1,
            pattern="The first trigger - initiating moment.",
            questions=[
                "What event starts the sequence?",
                "What's the first move?",
            ],
            examples=[
                "History: Archduke's assassination triggering WWI",
                "Science: First observation leading to discovery",
                "Business: Market shock initiating change",
                "Personal: Decision that changes everything",
            ],
        ),
        Card(
            name="Two of Events",
            card_type=Suit.EVENTS.value,
            number=2,
            pattern="Cause and effect - simple causality.",
            questions=[
                "What caused this?",
                "What will this cause?",
            ],
            examples=[
                "Physics: Force causing acceleration",
                "Economics: Price change affecting demand",
                "Health: Action affecting outcome",
                "Social: Behavior eliciting response",
            ],
        ),
        Card(
            name="Three of Events",
            card_type=Suit.EVENTS.value,
            number=3,
            pattern="Event branching - multiple possible outcomes.",
            questions=[
                "Which path does this take?",
                "What futures are possible?",
            ],
            examples=[
                "Decision: Choice creating different paths",
                "Quantum: Wavefunction collapse to one state",
                "Evolution: Speciation into multiple lineages",
                "Markets: Scenario planning for possibilities",
            ],
        ),
        Card(
            name="Four of Events",
            card_type=Suit.EVENTS.value,
            number=4,
            pattern="Event coordination - synchronization.",
            questions=[
                "What needs to happen simultaneously?",
                "How do I achieve coordination?",
            ],
            examples=[
                "Performance: Orchestra playing in time",
                "Distributed systems: Consensus protocols",
                "Manufacturing: Assembly line synchronization",
                "Nature: Synchronized firefly flashing",
            ],
        ),
        Card(
            name="Five of Events",
            card_type=Suit.EVENTS.value,
            number=5,
            pattern="Event chaos - loss of causal clarity.",
            questions=[
                "What's the actual cause?",
                "Am I confusing correlation and causation?",
            ],
            examples=[
                "Complex systems: Many interacting variables",
                "Attribution: Uncertain cause of outcome",
                "Weather: Chaotic dynamics limiting prediction",
                "Markets: Multiple factors confounding analysis",
            ],
        ),
        Card(
            name="Six of Events",
            card_type=Suit.EVENTS.value,
            number=6,
            pattern="Event stream - continuous flow.",
            questions=[
                "What's the pattern in the flow?",
                "How do I process this stream?",
            ],
            examples=[
                "Data: Real-time sensor readings",
                "News: Continuous information flow",
                "River: Water constantly flowing",
                "Traffic: Vehicles in steady stream",
            ],
        ),
        Card(
            name="Seven of Events",
            card_type=Suit.EVENTS.value,
            number=7,
            pattern="Event cascade - chain reactions.",
            questions=[
                "What cascade am I triggering?",
                "Where does this chain end?",
            ],
            examples=[
                "Avalanche: Snow triggering more snow",
                "Finance: Margin calls forcing more sales",
                "Ecology: Species loss affecting food web",
                "Social: Panic spreading through crowd",
            ],
        ),
        Card(
            name="Eight of Events",
            card_type=Suit.EVENTS.value,
            number=8,
            pattern="Event memory - learning from history.",
            questions=[
                "What can past events teach?",
                "What patterns repeat?",
            ],
            examples=[
                "History: Learning from precedent",
                "Personal: Experience informing decisions",
                "Science: Experimental data building knowledge",
                "Markets: Historical patterns suggesting futures",
            ],
        ),
        Card(
            name="Nine of Events",
            card_type=Suit.EVENTS.value,
            number=9,
            pattern="Event overload - too much happening.",
            questions=[
                "What events can I ignore?",
                "Where must I focus?",
            ],
            examples=[
                "Information: Overwhelming news flow",
                "Crisis: Multiple emergencies competing",
                "Personal: Too many demands at once",
                "Systems: Processing capacity exceeded",
            ],
        ),
        Card(
            name="Ten of Events",
            card_type=Suit.EVENTS.value,
            number=10,
            pattern="Event completion - cycle ending.",
            questions=[
                "What cycle is finishing?",
                "What comes after completion?",
            ],
            examples=[
                "Project: Reaching final milestone",
                "Seasons: Year completing its cycle",
                "Life: Generation finishing its time",
                "Business: Product reaching end of life",
            ],
        ),
        Card(
            name="Page of Events",
            card_type=Suit.EVENTS.value,
            number=11,
            pattern="Event observer - watching patterns.",
            questions=[
                "What events should I monitor?",
                "What patterns emerge from observation?",
            ],
            examples=[
                "Scientist: Recording experimental results",
                "Analyst: Tracking market movements",
                "Scout: Observing enemy movements",
                "Student: Noticing learning patterns",
            ],
        ),
        Card(
            name="Knight of Events",
            card_type=Suit.EVENTS.value,
            number=12,
            pattern="Event responder - quick reaction.",
            questions=[
                "How fast must I respond?",
                "What's the urgency?",
            ],
            examples=[
                "Emergency: First responder to crisis",
                "Trading: Reacting to market moves",
                "Sports: Responding to opponent's action",
                "Defense: Countering incoming threat",
            ],
        ),
        Card(
            name="Queen of Events",
            card_type=Suit.EVENTS.value,
            number=13,
            pattern="Event wisdom - understanding timing.",
            questions=[
                "When is the right time?",
                "What's the natural rhythm?",
            ],
            examples=[
                "Farming: Planting and harvesting with seasons",
                "Leadership: Knowing when to act or wait",
                "Medicine: Treating at optimal moment",
                "Strategy: Timing move for maximum effect",
            ],
        ),
        Card(
            name="King of Events",
            card_type=Suit.EVENTS.value,
            number=14,
            pattern="Event mastery - controlling timing.",
            questions=[
                "Do I control the timing?",
                "Who sets the tempo?",
            ],
            examples=[
                "Conductor: Setting the pace of music",
                "General: Choosing moment of attack",
                "Market maker: Setting trading tempo",
                "Predator: Choosing moment to strike",
            ],
        ),
    ]


def create_agents_suit():
    """Agency, coordination, intelligence"""
    return [
        Card(
            name="Ace of Agents",
            card_type=Suit.AGENTS.value,
            number=1,
            pattern="Autonomous action - independent agency.",
            questions=[
                "What can I do independently?",
                "Where do I have agency?",
            ],
            examples=[
                "Individual: Making independent choice",
                "Robot: Acting on own programming",
                "Cell: Self-directed biological process",
                "Entrepreneur: Starting independent venture",
            ],
        ),
        Card(
            name="Two of Agents",
            card_type=Suit.AGENTS.value,
            number=2,
            pattern="Partnership - cooperative action.",
            questions=[
                "Who's my partner?",
                "How do we coordinate?",
            ],
            examples=[
                "Business: Co-founders working together",
                "Dance: Partners moving in sync",
                "Biology: Symbiotic relationship",
                "Negotiation: Two parties reaching agreement",
            ],
        ),
        Card(
            name="Three of Agents",
            card_type=Suit.AGENTS.value,
            number=3,
            pattern="Small team - coordinated group.",
            questions=[
                "Who's on the team?",
                "How do we work together effectively?",
            ],
            examples=[
                "Work: Project team collaborating",
                "Sports: Players coordinating moves",
                "Hunt: Pack hunting cooperatively",
                "Music: Trio performing together",
            ],
        ),
        Card(
            name="Four of Agents",
            card_type=Suit.AGENTS.value,
            number=4,
            pattern="Structured organization - hierarchy forming.",
            questions=[
                "What's the structure?",
                "Who has authority over what?",
            ],
            examples=[
                "Military: Chain of command",
                "Corporation: Organizational hierarchy",
                "Government: Levels of authority",
                "Bee colony: Queen, workers, drones",
            ],
        ),
        Card(
            name="Five of Agents",
            card_type=Suit.AGENTS.value,
            number=5,
            pattern="Agent conflict - competing interests.",
            questions=[
                "What's the conflict?",
                "Can interests be aligned?",
            ],
            examples=[
                "Game theory: Prisoner's dilemma",
                "Business: Competing companies",
                "Internal: Conflicting desires",
                "Politics: Opposing factions",
            ],
        ),
        Card(
            name="Six of Agents",
            card_type=Suit.AGENTS.value,
            number=6,
            pattern="Swarm intelligence - emergent coordination.",
            questions=[
                "How does coordination emerge?",
                "What simple rules create complex behavior?",
            ],
            examples=[
                "Birds: Flocking from local rules",
                "Ants: Colony intelligence from simple agents",
                "Markets: Price discovery from individual trades",
                "Crowds: Movement patterns emerging",
            ],
        ),
        Card(
            name="Seven of Agents",
            card_type=Suit.AGENTS.value,
            number=7,
            pattern="Agent specialization - division of labor.",
            questions=[
                "What's each agent's specialized role?",
                "How does specialization create efficiency?",
            ],
            examples=[
                "Economics: Specialized professions",
                "Biology: Cell differentiation",
                "Factory: Assembly line workers",
                "Team: Distinct roles and responsibilities",
            ],
        ),
        Card(
            name="Eight of Agents",
            card_type=Suit.AGENTS.value,
            number=8,
            pattern="Multi-agent coordination - complex systems.",
            questions=[
                "How do many agents coordinate?",
                "What protocols enable cooperation?",
            ],
            examples=[
                "Air traffic: Many planes coordinating safely",
                "Internet: Protocols enabling communication",
                "Society: Norms coordinating behavior",
                "Immune system: Cells working together",
            ],
        ),
        Card(
            name="Nine of Agents",
            card_type=Suit.AGENTS.value,
            number=9,
            pattern="Control versus autonomy - tension.",
            questions=[
                "How much control is needed?",
                "When should I enable autonomy?",
            ],
            examples=[
                "Parenting: Guidance vs independence",
                "Management: Oversight vs delegation",
                "Government: Regulation vs freedom",
                "AI: Human control vs machine autonomy",
            ],
        ),
        Card(
            name="Ten of Agents",
            card_type=Suit.AGENTS.value,
            number=10,
            pattern="Collective intelligence - unified mind.",
            questions=[
                "What does the collective know?",
                "How do we think as one?",
            ],
            examples=[
                "Democracy: Collective decision-making",
                "Science: Distributed knowledge creation",
                "Culture: Shared understanding",
                "Superorganism: Colony as single entity",
            ],
        ),
        Card(
            name="Page of Agents",
            card_type=Suit.AGENTS.value,
            number=11,
            pattern="Learning agent - growing capability.",
            questions=[
                "What am I learning?",
                "How do I develop capability?",
            ],
            examples=[
                "Student: Acquiring knowledge and skills",
                "AI: Machine learning from data",
                "Apprentice: Learning craft",
                "Species: Evolving new capabilities",
            ],
        ),
        Card(
            name="Knight of Agents",
            card_type=Suit.AGENTS.value,
            number=12,
            pattern="Action-oriented - executor.",
            questions=[
                "What needs doing now?",
                "How do I execute effectively?",
            ],
            examples=[
                "Soldier: Following orders in action",
                "Athlete: Performing in competition",
                "Entrepreneur: Implementing business plan",
                "Predator: Executing hunt",
            ],
        ),
        Card(
            name="Queen of Agents",
            card_type=Suit.AGENTS.value,
            number=13,
            pattern="Nurturing intelligence - developing others.",
            questions=[
                "Who needs guidance?",
                "How do I help others grow?",
            ],
            examples=[
                "Teacher: Developing student potential",
                "Mentor: Guiding protégé",
                "Parent: Raising children",
                "Manager: Developing team members",
            ],
        ),
        Card(
            name="King of Agents",
            card_type=Suit.AGENTS.value,
            number=14,
            pattern="Strategic intelligence - master coordinator.",
            questions=[
                "What's the overall strategy?",
                "How do I orchestrate all agents?",
            ],
            examples=[
                "General: Commanding army",
                "CEO: Leading organization",
                "Conductor: Directing orchestra",
                "Brain: Coordinating body systems",
            ],
        ),
    ]


def create_resources_suit():
    """Constraints, allocation, flow"""
    return [
        Card(
            name="Ace of Resources",
            card_type=Suit.RESOURCES.value,
            number=1,
            pattern="New resource - fresh potential.",
            questions=[
                "What new resource is available?",
                "How should I allocate it?",
            ],
            examples=[
                "Finance: New funding or income",
                "Energy: Discovering energy source",
                "Time: New availability opening",
                "Attention: Fresh capacity to focus",
            ],
        ),
        Card(
            name="Two of Resources",
            card_type=Suit.RESOURCES.value,
            number=2,
            pattern="Resource balance - equilibrium.",
            questions=[
                "Am I balanced?",
                "What needs rebalancing?",
            ],
            examples=[
                "Budget: Income matching expenses",
                "Ecology: Predator-prey equilibrium",
                "Work-life: Balancing competing demands",
                "Health: Homeostasis in body",
            ],
        ),
        Card(
            name="Three of Resources",
            card_type=Suit.RESOURCES.value,
            number=3,
            pattern="Resource pooling - collaboration.",
            questions=[
                "What resources can be shared?",
                "How do we pool effectively?",
            ],
            examples=[
                "Commons: Shared grazing land",
                "Crowdfunding: Pooling many small contributions",
                "Potluck: Sharing food resources",
                "Knowledge: Open source collaboration",
            ],
        ),
        Card(
            name="Four of Resources",
            card_type=Suit.RESOURCES.value,
            number=4,
            pattern="Resource accumulation - holding.",
            questions=[
                "What am I storing?",
                "Is accumulation serving me?",
            ],
            examples=[
                "Savings: Building financial reserves",
                "Squirrel: Storing nuts for winter",
                "Data: Accumulating information",
                "Hoarding: Excessive accumulation",
            ],
        ),
        Card(
            name="Five of Resources",
            card_type=Suit.RESOURCES.value,
            number=5,
            pattern="Resource scarcity - not enough.",
            questions=[
                "What's truly scarce?",
                "How do I optimize within constraints?",
            ],
            examples=[
                "Famine: Insufficient food",
                "Drought: Water scarcity",
                "Recession: Economic contraction",
                "Attention: Limited focus capacity",
            ],
        ),
        Card(
            name="Six of Resources",
            card_type=Suit.RESOURCES.value,
            number=6,
            pattern="Resource flow - circulation.",
            questions=[
                "Where do resources flow?",
                "What blocks circulation?",
            ],
            examples=[
                "Economy: Money circulating through system",
                "Body: Blood flowing through vessels",
                "Ecosystem: Energy flowing through food web",
                "Supply chain: Goods moving to market",
            ],
        ),
        Card(
            name="Seven of Resources",
            card_type=Suit.RESOURCES.value,
            number=7,
            pattern="Resource investment - long-term thinking.",
            questions=[
                "What investment pays off later?",
                "What's the long-term value?",
            ],
            examples=[
                "Education: Investing time in learning",
                "Infrastructure: Building for future benefit",
                "Tree planting: Shade for future generations",
                "Research: Long-term knowledge development",
            ],
        ),
        Card(
            name="Eight of Resources",
            card_type=Suit.RESOURCES.value,
            number=8,
            pattern="Resource transformation - alchemy.",
            questions=[
                "How can I transform this resource?",
                "What's the conversion process?",
            ],
            examples=[
                "Manufacturing: Raw materials to products",
                "Cooking: Ingredients to meals",
                "Learning: Information to knowledge",
                "Energy: Converting between forms",
            ],
        ),
        Card(
            name="Nine of Resources",
            card_type=Suit.RESOURCES.value,
            number=9,
            pattern="Resource abundance - more than enough.",
            questions=[
                "What abundance exists?",
                "Am I recognizing what I have?",
            ],
            examples=[
                "Harvest: Abundant crop yield",
                "Talent: Wealth of capable people",
                "Ideas: Creative abundance",
                "Nature: Ecosystem productivity",
            ],
        ),
        Card(
            name="Ten of Resources",
            card_type=Suit.RESOURCES.value,
            number=10,
            pattern="Resource legacy - inheritance.",
            questions=[
                "What resources do I pass on?",
                "What's my contribution to future?",
            ],
            examples=[
                "Estate: Wealth passed to heirs",
                "Knowledge: Teaching next generation",
                "Infrastructure: Systems for future use",
                "Culture: Traditions and practices",
            ],
        ),
        Card(
            name="Page of Resources",
            card_type=Suit.RESOURCES.value,
            number=11,
            pattern="Resource learning - understanding value.",
            questions=[
                "What's truly valuable?",
                "How do I recognize worth?",
            ],
            examples=[
                "Student: Learning to budget",
                "Prospector: Learning to identify ore",
                "Novice: Understanding what matters",
                "Child: Learning value of sharing",
            ],
        ),
        Card(
            name="Knight of Resources",
            card_type=Suit.RESOURCES.value,
            number=12,
            pattern="Resource quest - seeking what's needed.",
            questions=[
                "What resource am I seeking?",
                "Where do I find it?",
            ],
            examples=[
                "Hunter: Seeking food",
                "Entrepreneur: Seeking funding",
                "Explorer: Searching for new resources",
                "Job seeker: Finding opportunity",
            ],
        ),
        Card(
            name="Queen of Resources",
            card_type=Suit.RESOURCES.value,
            number=13,
            pattern="Resource wisdom - knowing what's needed.",
            questions=[
                "What do I truly need?",
                "What's sufficient?",
            ],
            examples=[
                "Sage: Understanding enough is enough",
                "Homesteader: Living within means",
                "Conservationist: Sustaining resources",
                "Minimalist: Valuing sufficiency",
            ],
        ),
        Card(
            name="King of Resources",
            card_type=Suit.RESOURCES.value,
            number=14,
            pattern="Resource mastery - strategic allocation.",
            questions=[
                "How do I allocate optimally?",
                "What's the strategic deployment?",
            ],
            examples=[
                "Investor: Strategic portfolio allocation",
                "General: Deploying assets optimally",
                "Ecologist: Managing ecosystem resources",
                "Leader: Allocating organizational resources",
            ],
        ),
    ]


class SystemsTarot:
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

        if n > len(self.deck):
            self.reset_and_shuffle()

        drawn = self.deck[:n]
        self.deck = self.deck[n:]

        if len(self.deck) < 10:
            self.reset_and_shuffle()

        return drawn

    def reading(self, spread_type: str = "three_card"):
        """Perform a reading with specified spread"""
        print("\n" + "=" * 80)
        print("SYSTEMS THINKING TAROT: Universal Pattern Oracle")
        print("=" * 80 + "\n")

        if spread_type == "single":
            print("SINGLE CARD: What perspective do I need now?\n")
            cards = self.draw(1)
            cards[0].display()

        elif spread_type == "three_card":
            print("THREE CARD READING: Context / Challenge / Opportunity\n")
            cards = self.draw(3)

            print("\n1. CONTEXT - What system am I in?")
            print("-" * 80)
            cards[0].display()

            print("\n2. CHALLENGE - What constraint am I facing?")
            print("-" * 80)
            cards[1].display()

            print("\n3. OPPORTUNITY - What leverage point exists?")
            print("-" * 80)
            cards[2].display()

        elif spread_type == "decision":
            print("DECISION READING: Current / Path A / Path B / Integration\n")
            cards = self.draw(4)

            print("\n1. CURRENT STATE - Where am I now?")
            print("-" * 80)
            cards[0].display()

            print("\n2. PATH A - First option's dynamics")
            print("-" * 80)
            cards[1].display()

            print("\n3. PATH B - Second option's dynamics")
            print("-" * 80)
            cards[2].display()

            print("\n4. INTEGRATION - What pattern connects them?")
            print("-" * 80)
            cards[3].display()

        elif spread_type == "system":
            print("SYSTEM ANALYSIS: Structure / Dynamics / Agents / Resources / Emergence\n")
            cards = self.draw(5)

            print("\n1. STRUCTURE - What's the network topology?")
            print("-" * 80)
            cards[0].display()

            print("\n2. DYNAMICS - What events are unfolding?")
            print("-" * 80)
            cards[1].display()

            print("\n3. AGENTS - Who has agency here?")
            print("-" * 80)
            cards[2].display()

            print("\n4. RESOURCES - What's scarce or abundant?")
            print("-" * 80)
            cards[3].display()

            print("\n5. EMERGENCE - What's trying to emerge?")
            print("-" * 80)
            cards[4].display()

        elif spread_type == "threat":
            print("THREAT ASSESSMENT: Primary / Cascade / Resilience / Blind Spot / Response / Trajectory\n")
            cards = self.draw(6)

            print("\n1. PRIMARY THREAT - What matters most?")
            print("-" * 80)
            cards[0].display()

            print("\n2. CASCADE RISK - What could amplify this?")
            print("-" * 80)
            cards[1].display()

            print("\n3. RESILIENCE - What provides stability?")
            print("-" * 80)
            cards[2].display()

            print("\n4. BLIND SPOT - What am I missing?")
            print("-" * 80)
            cards[3].display()

            print("\n5. RESPONSE - What action pattern fits?")
            print("-" * 80)
            cards[4].display()

            print("\n6. TRAJECTORY - What's the long-term pattern?")
            print("-" * 80)
            cards[5].display()

        print("\n" + "=" * 80)
        print("REFLECTION: How do these patterns inform your thinking?")
        print("What connections emerge? What questions arise?")
        print("=" * 80 + "\n")

    def list_all_cards(self):
        """List all cards for reference"""
        print("\n" + "=" * 80)
        print("COMPLETE DECK")
        print("=" * 80 + "\n")

        print(f"MAJOR ARCANA ({len(MAJOR_ARCANA)} cards):")
        print("-" * 80)
        for card in MAJOR_ARCANA:
            print(f"  • {card.name}")
            print(f"    {card.pattern}")
            print()

        print("\nMINOR ARCANA - NETWORKS (14 cards):")
        print("-" * 80)
        for i in range(1, 15):
            rank = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", 
                    "Eight", "Nine", "Ten", "Page", "Knight", "Queen", "King"][i-1]
            print(f"  • {rank} of Networks")

        print("\nMINOR ARCANA - EVENTS (14 cards):")
        print("-" * 80)
        for i in range(1, 15):
            rank = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", 
                    "Eight", "Nine", "Ten", "Page", "Knight", "Queen", "King"][i-1]
            print(f"  • {rank} of Events")

        print("\nMINOR ARCANA - AGENTS (14 cards):")
        print("-" * 80)
        for i in range(1, 15):
            rank = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", 
                    "Eight", "Nine", "Ten", "Page", "Knight", "Queen", "King"][i-1]
            print(f"  • {rank} of Agents")

        print("\nMINOR ARCANA - RESOURCES (14 cards):")
        print("-" * 80)
        for i in range(1, 15):
            rank = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", 
                    "Eight", "Nine", "Ten", "Page", "Knight", "Queen", "King"][i-1]
            print(f"  • {rank} of Resources")

        print("\n" + "=" * 80)
        print("TOTAL: 78 cards (22 Major + 56 Minor)")
        print("=" * 80 + "\n")


def main():
    """Main interface"""
    tarot = SystemsTarot()

    print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║                        SYSTEMS THINKING TAROT                                ║
║                      Universal Pattern Oracle                                ║
║                                                                              ║
║  Structured randomization forcing novel combinations of systems patterns.   ║
║  Applicable across any domain: engineering, ecology, business, society.     ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
    """)

    while True:
        print("\nCHOOSE YOUR READING:")
        print("  1. Single Card - Quick perspective")
        print("  2. Three Card - Context/Challenge/Opportunity")
        print("  3. Decision - Comparing two paths")
        print("  4. System Analysis - Structure/Dynamics/Agents/Resources/Emergence")
        print("  5. Threat Assessment - Full risk analysis")
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
            tarot.reading("system")
        elif choice == "5":
            tarot.reading("threat")
        elif choice == "6":
            tarot.list_all_cards()
        elif choice == "7":
            print("\nMay your systems be resilient and your patterns generative.\n")
            break
        else:
            print("\nInvalid choice. Try again.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
