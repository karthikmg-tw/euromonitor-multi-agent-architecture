#!/usr/bin/env python3
"""
Knowledge Graph Ontology Visualizer
Generates an interactive HTML visualization of the Passport AI ontology.

Requirements:
    pip install pyvis networkx

Usage:
    python visualize_ontology.py
    # Opens ontology_visualization.html in browser
"""

from pyvis.network import Network
import networkx as nx
import webbrowser
import os

def create_ontology_graph():
    """Create the ontology structure as a NetworkX graph."""
    G = nx.DiGraph()

    # ========================================================================
    # NODES
    # ========================================================================

    # Geography nodes
    G.add_node("Asia Pacific", type="Geography", level=0, color="#01579b", shape="box")
    G.add_node("India", type="Geography", level=1, color="#0277bd", shape="box")

    # Category nodes (hierarchy)
    G.add_node("Toys and Games", type="Category", level=0, color="#f57f17", shape="ellipse")
    G.add_node("Traditional Toys", type="Category", level=1, color="#f9a825", shape="ellipse")
    G.add_node("Video Games", type="Category", level=1, color="#f9a825", shape="ellipse")
    G.add_node("Action Figures", type="Category", level=2, color="#fbc02d", shape="ellipse")
    G.add_node("Dolls", type="Category", level=2, color="#fbc02d", shape="ellipse")
    G.add_node("VG Software", type="Category", level=2, color="#fbc02d", shape="ellipse")
    G.add_node("Hand-Held Consoles", type="Category", level=3, color="#fdd835", shape="ellipse")
    G.add_node("Static Consoles", type="Category", level=3, color="#fdd835", shape="ellipse")

    # Company nodes
    G.add_node("Sony Corporation", type="Company", subtype="GBO", color="#4a148c", shape="star")
    G.add_node("Sony India", type="Company", subtype="NBO", color="#6a1b9a", shape="star")
    G.add_node("Mattel India", type="Company", subtype="NBO", color="#7b1fa2", shape="star")
    G.add_node("Hasbro India", type="Company", subtype="NBO", color="#8e24aa", shape="star")

    # Brand nodes
    G.add_node("PlayStation", type="Brand", color="#880e4f", shape="diamond")
    G.add_node("Barbie", type="Brand", color="#ad1457", shape="diamond")
    G.add_node("Hot Wheels", type="Brand", color="#c2185b", shape="diamond")

    # Market Data nodes
    G.add_node("MarketSize\nIndia Toys\n2795M CHF (2024)", type="MarketSize", color="#1b5e20", shape="box", size=30)
    G.add_node("MarketShare\nSony 22.6%", type="MarketShare", color="#2e7d32", shape="box", size=20)
    G.add_node("MarketShare\nMattel 8.1%", type="MarketShare", color="#388e3c", shape="box", size=20)

    # Source nodes
    G.add_node("Euromonitor\nPassport", type="Source", color="#e65100", shape="triangle")
    G.add_node("NCAER", type="Source", color="#ef6c00", shape="triangle")
    G.add_node("Prowess DB", type="Source", color="#f57c00", shape="triangle")

    # Report node (Phase 3)
    G.add_node("Report:\nToys in India\n2025", type="Report", color="#33691e", shape="box")

    # ========================================================================
    # EDGES (Relationships)
    # ========================================================================

    # Geography hierarchy
    G.add_edge("India", "Asia Pacific", label="LOCATED_IN", color="blue", width=2)

    # Category hierarchy
    G.add_edge("Traditional Toys", "Toys and Games", label="BELONGS_TO", color="orange", width=2)
    G.add_edge("Video Games", "Toys and Games", label="BELONGS_TO", color="orange", width=2)
    G.add_edge("Action Figures", "Traditional Toys", label="BELONGS_TO", color="orange", width=1.5)
    G.add_edge("Dolls", "Traditional Toys", label="BELONGS_TO", color="orange", width=1.5)
    G.add_edge("VG Software", "Video Games", label="BELONGS_TO", color="orange", width=1.5)
    G.add_edge("Hand-Held Consoles", "Video Games", label="BELONGS_TO", color="orange", width=1.5)
    G.add_edge("Static Consoles", "Video Games", label="BELONGS_TO", color="orange", width=1.5)

    # Company relationships
    G.add_edge("Sony India", "Sony Corporation", label="PARENT_COMPANY", color="purple", width=2)
    G.add_edge("Sony India", "India", label="OPERATES_IN", color="purple", width=1.5)
    G.add_edge("Mattel India", "India", label="OPERATES_IN", color="purple", width=1.5)
    G.add_edge("Hasbro India", "India", label="OPERATES_IN", color="purple", width=1.5)
    G.add_edge("Sony India", "Video Games", label="COMPETES_IN", color="purple", width=1.5)
    G.add_edge("Mattel India", "Toys and Games", label="COMPETES_IN", color="purple", width=1.5)

    # Brand relationships
    G.add_edge("PlayStation", "Sony India", label="OWNED_BY", color="pink", width=2)
    G.add_edge("Barbie", "Mattel India", label="OWNED_BY", color="pink", width=2)
    G.add_edge("Hot Wheels", "Mattel India", label="OWNED_BY", color="pink", width=2)

    # Market data relationships
    G.add_edge("India", "MarketSize\nIndia Toys\n2795M CHF (2024)", label="HAS_MARKET_SIZE", color="green", width=2)
    G.add_edge("MarketSize\nIndia Toys\n2795M CHF (2024)", "Toys and Games", label="FOR_CATEGORY", color="green", width=2)
    G.add_edge("Sony India", "MarketShare\nSony 22.6%", label="HAS_SHARE", color="green", width=2)
    G.add_edge("Mattel India", "MarketShare\nMattel 8.1%", label="HAS_SHARE", color="green", width=2)

    # Citation relationships
    G.add_edge("MarketSize\nIndia Toys\n2795M CHF (2024)", "Euromonitor\nPassport", label="SOURCED_FROM", color="red", width=2)
    G.add_edge("MarketSize\nIndia Toys\n2795M CHF (2024)", "NCAER", label="SOURCED_FROM", color="red", width=1.5)
    G.add_edge("MarketShare\nSony 22.6%", "Euromonitor\nPassport", label="SOURCED_FROM", color="red", width=1.5)
    G.add_edge("MarketShare\nMattel 8.1%", "Euromonitor\nPassport", label="SOURCED_FROM", color="red", width=1.5)

    # Report relationships (Phase 3)
    G.add_edge("Report:\nToys in India\n2025", "Sony India", label="MENTIONS", color="darkgreen", width=1.5)
    G.add_edge("Report:\nToys in India\n2025", "Video Games", label="MENTIONS", color="darkgreen", width=1.5)
    G.add_edge("Report:\nToys in India\n2025", "PlayStation", label="MENTIONS", color="darkgreen", width=1.5)
    G.add_edge("Report:\nToys in India\n2025", "Euromonitor\nPassport", label="CITES", color="red", width=1.5)

    return G

def visualize_with_pyvis(G, output_file="ontology_visualization.html"):
    """Create an interactive HTML visualization using PyVis."""

    # Create PyVis network
    net = Network(
        height="900px",
        width="100%",
        bgcolor="#ffffff",
        font_color="black",
        directed=True,
        notebook=False
    )

    # Physics settings for better layout
    net.set_options("""
    {
        "physics": {
            "enabled": true,
            "barnesHut": {
                "gravitationalConstant": -30000,
                "centralGravity": 0.3,
                "springLength": 150,
                "springConstant": 0.04,
                "damping": 0.09,
                "avoidOverlap": 0.5
            },
            "minVelocity": 0.75
        },
        "nodes": {
            "font": {
                "size": 14,
                "face": "arial"
            }
        },
        "edges": {
            "arrows": {
                "to": {
                    "enabled": true,
                    "scaleFactor": 0.5
                }
            },
            "smooth": {
                "type": "continuous"
            },
            "font": {
                "size": 10,
                "align": "middle"
            }
        }
    }
    """)

    # Add nodes with attributes
    for node, attrs in G.nodes(data=True):
        title = f"<b>{node}</b><br>"
        title += f"Type: {attrs.get('type', 'Unknown')}<br>"
        if 'subtype' in attrs:
            title += f"Subtype: {attrs['subtype']}<br>"
        if 'level' in attrs:
            title += f"Level: {attrs['level']}"

        net.add_node(
            node,
            label=node,
            color=attrs.get('color', '#97c2fc'),
            shape=attrs.get('shape', 'dot'),
            size=attrs.get('size', 25),
            title=title
        )

    # Add edges with labels
    for source, target, attrs in G.edges(data=True):
        net.add_edge(
            source,
            target,
            label=attrs.get('label', ''),
            color=attrs.get('color', 'gray'),
            width=attrs.get('width', 1)
        )

    # Save and show
    net.show(output_file)
    print(f"✅ Visualization saved to: {output_file}")
    print(f"📊 Opening in browser...")

    # Open in default browser
    webbrowser.open('file://' + os.path.realpath(output_file))

def print_statistics(G):
    """Print graph statistics."""
    print("\n" + "="*70)
    print("PASSPORT AI KNOWLEDGE GRAPH ONTOLOGY - STATISTICS")
    print("="*70)

    # Node statistics
    node_types = {}
    for node, attrs in G.nodes(data=True):
        node_type = attrs.get('type', 'Unknown')
        node_types[node_type] = node_types.get(node_type, 0) + 1

    print("\nNODE COUNTS:")
    for node_type, count in sorted(node_types.items()):
        print(f"  {node_type:20s}: {count:3d}")
    print(f"  {'TOTAL':20s}: {G.number_of_nodes():3d}")

    # Edge statistics
    edge_types = {}
    for source, target, attrs in G.edges(data=True):
        edge_type = attrs.get('label', 'Unknown')
        edge_types[edge_type] = edge_types.get(edge_type, 0) + 1

    print("\nRELATIONSHIP COUNTS:")
    for edge_type, count in sorted(edge_types.items()):
        print(f"  {edge_type:20s}: {count:3d}")
    print(f"  {'TOTAL':20s}: {G.number_of_edges():3d}")

    print("\n" + "="*70)

def main():
    """Main execution."""
    print("🏗️  Building Passport AI Knowledge Graph Ontology...")

    # Create graph
    G = create_ontology_graph()

    # Print statistics
    print_statistics(G)

    # Visualize
    print("\n📊 Generating interactive visualization...")
    visualize_with_pyvis(G)

    print("\n✨ Done! Explore the graph by:")
    print("   - Dragging nodes to rearrange")
    print("   - Hovering over nodes for details")
    print("   - Clicking and dragging the canvas to pan")
    print("   - Scrolling to zoom in/out")

if __name__ == "__main__":
    main()
