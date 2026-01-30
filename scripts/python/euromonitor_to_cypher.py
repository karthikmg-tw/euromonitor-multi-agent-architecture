"""
Euromonitor PDF Data Extractor to Cypher Generator

Purpose: Helper utilities to extract data from Euromonitor PDFs and generate
         Neo4j Cypher statements for incremental data loading.

Usage:
    from euromonitor_to_cypher import CypherGenerator

    # Generate country update
    gen = CypherGenerator()
    cypher = gen.update_country('JP', {
        'market_size_2023': 18500,
        'key_insight': 'Trading cards driving growth'
    })
    print(cypher)
"""

from typing import Dict, List, Any, Optional
from datetime import datetime


class CypherGenerator:
    """Generate Cypher statements for Euromonitor data"""

    def __init__(self, data_source: str = "Euromonitor International"):
        self.data_source = data_source
        self.timestamp = datetime.now().isoformat()

    def update_country(self, iso_code: str, properties: Dict[str, Any]) -> str:
        """
        Generate Cypher to update a country with new properties.

        Args:
            iso_code: ISO country code (e.g., 'CN', 'JP')
            properties: Dictionary of properties to add/update

        Returns:
            Cypher statement string
        """
        props_str = self._format_properties(properties)

        return f"""// Update {iso_code} with detailed metrics
MATCH (country:Country {{iso_code: '{iso_code}'}})
SET country += {{
{props_str}
}};
"""

    def create_company(self, name: str, properties: Dict[str, Any]) -> str:
        """Generate Cypher to create/update a company."""
        props_str = self._format_properties(properties)

        cypher = f"""// Create/Update company: {name}
MERGE (comp:Company {{name: '{name}'}})
SET comp += {{
{props_str}
}};
"""

        # Add HQ relationship if country specified
        if 'hq_country' in properties:
            cypher += f"""
// Link to HQ country
MATCH (comp:Company {{name: '{name}'}}),
      (country:Country {{name: '{properties['hq_country']}'}})
MERGE (comp)-[:HEADQUARTERED_IN]->(country);
"""

        return cypher

    def create_product(self, name: str, properties: Dict[str, Any],
                      publisher: Optional[str] = None) -> str:
        """Generate Cypher to create a product and link to publisher."""
        props_str = self._format_properties(properties)

        cypher = f"""// Create product: {name}
MERGE (prod:Product {{name: '{name}'}})
SET prod += {{
{props_str}
}};
"""

        if publisher:
            cypher += f"""
// Link to publisher
MATCH (prod:Product {{name: '{name}'}}),
      (comp:Company {{name: '{publisher}'}})
MERGE (prod)-[:PUBLISHED_BY]->(comp);
"""

        return cypher

    def create_brand(self, name: str, properties: Dict[str, Any],
                    owner: Optional[str] = None) -> str:
        """Generate Cypher to create a brand and link to owner company."""
        props_str = self._format_properties(properties)

        cypher = f"""// Create brand: {name}
MERGE (brand:Brand {{name: '{name}'}})
SET brand += {{
{props_str}
}};
"""

        if owner:
            cypher += f"""
// Link to owner
MATCH (brand:Brand {{name: '{name}'}}),
      (comp:Company {{name: '{owner}'}})
MERGE (brand)-[:OWNED_BY]->(comp);
"""

        return cypher

    def link_trend_to_country(self, trend_name: str, country_code: str,
                            relationship: str = "IMPACTS") -> str:
        """Generate Cypher to link a trend to a country."""
        return f"""// Link trend '{trend_name}' to {country_code}
MATCH (trend:Trend {{name: '{trend_name}'}}),
      (country:Country {{iso_code: '{country_code}'}})
MERGE (trend)-[:{relationship}]->(country);
"""

    def create_market_segment(self, name: str, country: str,
                            category: str, properties: Dict[str, Any]) -> str:
        """Generate Cypher to create a market segment analysis."""
        props = {
            'name': name,
            'country': country,
            'category': category,
            **properties
        }
        props_str = self._format_properties(props)

        return f"""// Create market segment: {name}
MERGE (segment:MarketSegment {{
{props_str}
}});

// Link to country
MATCH (segment:MarketSegment {{name: '{name}'}}),
      (country:Country {{iso_code: '{country}'}})
MERGE (segment)-[:IN_MARKET]->(country);
"""

    def create_forecast(self, country_code: str, properties: Dict[str, Any]) -> str:
        """Generate Cypher to create forecast data."""
        props_str = self._format_properties(properties)

        return f"""// Create forecast for {country_code}
MERGE (forecast:Forecast {{
  country: '{country_code}',
{props_str}
}});

// Link to country
MATCH (forecast:Forecast {{country: '{country_code}'}}),
      (country:Country {{iso_code: '{country_code}'}})
MERGE (forecast)-[:PROJECTS]->(country);
"""

    def batch_update_countries(self, country_data: Dict[str, Dict[str, Any]]) -> str:
        """Generate Cypher for multiple country updates."""
        statements = [
            "// Batch update multiple countries",
            "// Generated: " + self.timestamp,
            ""
        ]

        for iso_code, properties in country_data.items():
            statements.append(self.update_country(iso_code, properties))
            statements.append("")  # blank line

        return "\n".join(statements)

    def _format_properties(self, properties: Dict[str, Any], indent: str = "  ") -> str:
        """Format properties dictionary into Cypher property syntax."""
        lines = []
        for key, value in properties.items():
            formatted_value = self._format_value(value)
            lines.append(f"{indent}{key}: {formatted_value}")

        return ",\n".join(lines)

    def _format_value(self, value: Any) -> str:
        """Format a Python value into Cypher syntax."""
        if value is None:
            return "null"
        elif isinstance(value, bool):
            return "true" if value else "false"
        elif isinstance(value, str):
            # Escape single quotes in strings
            escaped = value.replace("'", "\\'")
            return f"'{escaped}'"
        elif isinstance(value, (int, float)):
            return str(value)
        elif isinstance(value, list):
            formatted_items = [self._format_value(item) for item in value]
            return f"[{', '.join(formatted_items)}]"
        elif isinstance(value, dict):
            # For nested dicts (rare, but handle it)
            formatted_pairs = [f"{k}: {self._format_value(v)}"
                             for k, v in value.items()]
            return f"{{{', '.join(formatted_pairs)}}}"
        else:
            return str(value)


# ============================================
# Example Usage and Templates
# ============================================

def example_usage():
    """Demonstrate how to use the CypherGenerator."""

    gen = CypherGenerator()

    # Example 1: Update Japan with detailed metrics
    print("=" * 50)
    print("Example 1: Update Country")
    print("=" * 50)
    japan_data = {
        'market_size_2018': 16100,
        'market_size_2023': 18500,
        'cagr_2018_2023': 2.8,
        'forecast_size_2028': 18000,
        'key_insight': 'Trading card games boom, especially Pokémon',
        'games_puzzles_growth': 'very high',
        'ecommerce_share': 0.59,
        'appliances_specialists_share': 0.14
    }
    print(gen.update_country('JP', japan_data))

    # Example 2: Create a new company
    print("\n" + "=" * 50)
    print("Example 2: Create Company")
    print("=" * 50)
    company_data = {
        'hq_country': 'China',
        'primary_category': 'Mobile Games',
        'founded_year': 2012,
        'flagship_products': ['Genshin Impact', 'Honkai: Star Rail'],
        'market_position': 'Rising star in global gaming',
        'strategy_2023': 'Generous benefits and free content to attract players'
    }
    print(gen.create_company('miHoYo Co Ltd', company_data))

    # Example 3: Create product
    print("\n" + "=" * 50)
    print("Example 3: Create Product")
    print("=" * 50)
    product_data = {
        'type': 'Mobile Game',
        'genre': 'Action RPG',
        'release_year': 2020,
        'platforms': ['Mobile', 'PC', 'PlayStation', 'Xbox'],
        'business_model': 'Free-to-play with gacha',
        'global_success': True
    }
    print(gen.create_product('Genshin Impact', product_data, publisher='miHoYo Co Ltd'))

    # Example 4: Batch update multiple countries
    print("\n" + "=" * 50)
    print("Example 4: Batch Update")
    print("=" * 50)
    countries = {
        'IN': {
            'video_games_growth_outlook': 'Dynamic',
            'esports_impact': 'Major driver',
            'smartphone_penetration': 'Increasing',
            'key_opportunity': 'Rising middle class and cheap data plans'
        },
        'ID': {
            'growth_outlook': 'Positive',
            'urbanization_impact': 'Supporting growth',
            'youth_population': 'High'
        }
    }
    print(gen.batch_update_countries(countries))


if __name__ == '__main__':
    print("Euromonitor to Cypher Generator")
    print("=" * 50)
    print()
    example_usage()
    print("\n" + "=" * 50)
    print("Copy any of the above Cypher statements into Neo4j Browser")
    print("or save to a .cypher file for batch execution")
    print("=" * 50)
