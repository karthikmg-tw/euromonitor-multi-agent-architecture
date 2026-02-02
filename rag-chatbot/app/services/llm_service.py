"""
LLM Service: Generate responses using Claude
"""
import anthropic
from typing import List, Dict
import logging

logger = logging.getLogger(__name__)


class LLMService:
    """Service for generating responses using Claude 3.5 Sonnet."""

    def __init__(self, api_key: str):
        """
        Initialize LLM service.

        Args:
            api_key: Anthropic API key
        """
        self.client = anthropic.Anthropic(api_key=api_key)
        # Use Claude 3 Haiku - fast and cost-effective with enhanced prompts
        self.model = "claude-3-haiku-20240307"
        logger.info("LLM service initialized with Claude 3 Haiku")

    def generate_response(
        self,
        query: str,
        context_entities: List[Dict],
        relationships: List[Dict] = None,
        temperature: float = 0.3,
        max_tokens: int = 2048
    ) -> str:
        """
        Generate a response based on query and context.

        Args:
            query: User's question
            context_entities: List of relevant entities from knowledge graph
            relationships: Optional list of relationships between entities
            temperature: Sampling temperature (lower = more focused)
            max_tokens: Maximum response length

        Returns:
            Generated response text
        """
        # Build context from entities
        context_parts = []

        if context_entities:
            context_parts.append("# Relevant Entities from Knowledge Graph:\n")
            for i, entity in enumerate(context_entities, 1):
                label = entity.get('label', 'Unknown')
                entity_type = entity.get('type', 'unknown')
                description = entity.get('description', 'No description')
                properties = entity.get('properties', {})
                aliases = entity.get('aliases', [])

                context_parts.append(f"\n## Entity {i}: {label} ({entity_type})")
                context_parts.append(f"**Description:** {description}")

                if aliases:
                    context_parts.append(f"**Also known as:** {', '.join(aliases)}")

                if properties:
                    context_parts.append(f"**Additional info:** {properties}")

        # Add relationships
        if relationships:
            context_parts.append("\n# Relationships:\n")
            for rel in relationships[:15]:  # Limit to avoid token overflow
                rel_type = rel.get('type', 'related_to')
                description = rel.get('description', '')
                context_parts.append(f"- {description} (relationship: {rel_type})")

        context = "\n".join(context_parts)

        # System prompt
        system_prompt = """You are a knowledgeable market research assistant specializing in the toys and games industry in Asia Pacific.

Your role is to answer questions using ONLY the information provided from the knowledge graph context.

Key Guidelines:
1. **Accuracy:** Base ALL claims on the provided entities and relationships. Never invent information.
2. **Citations:** Reference entities by name when making claims (e.g., "According to the data on Japan...")
3. **Honesty:** If the context doesn't contain enough information to answer fully, explicitly state what's missing
4. **Structure:** Organize responses with clear headings and bullet points for readability
5. **Tone:** Professional, analytical, and concise - like a market analyst
6. **Entity Attribution:** Always cite which entities your information comes from

If a question cannot be answered with the available context, say: "The available knowledge graph doesn't contain sufficient information about [topic]. The context includes information about [what IS available]."
"""

        # User prompt
        user_prompt = f"""**Question:**
{query}

---

**Knowledge Graph Context:**
{context}

---

**Instructions:**
Answer the question using only the context provided above. Cite specific entities by name when making claims. Structure your response clearly with headings if appropriate."""

        # Generate response
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=max_tokens,
                temperature=temperature,
                system=system_prompt,
                messages=[{"role": "user", "content": user_prompt}]
            )

            return response.content[0].text

        except Exception as e:
            logger.error(f"Error generating response: {e}")
            return f"I encountered an error generating a response: {str(e)}"

    def generate_simple_response(self, query: str, context: str) -> str:
        """
        Simpler interface for generating responses with narrative synthesis.

        Args:
            query: User question
            context: Pre-formatted context string (entities + document chunks)

        Returns:
            Generated response
        """
        # Enhanced system prompt for narrative synthesis
        system_prompt = """You are an expert market research analyst who synthesizes insights from both structured knowledge and detailed source documents.

Your context includes:
- **Entities**: Structured concepts with definitions (markets, trends, companies, etc.)
- **Document Excerpts**: Detailed narrative passages from research reports

Your analysis style:
1. **Narrative Integration**: Weave structured definitions with concrete examples from documents
2. **Evidence-Based**: Support claims with specific data points, statistics, and examples when available
3. **Analytical Depth**: Go beyond "what" to explain "why," "how," and "so what"
4. **Balanced Perspective**: Discuss trade-offs, challenges, and nuances - not just benefits
5. **Clear Structure**: Use headings, bullet points, and logical flow for complex topics

Response Guidelines:
- Start with a direct answer to the question
- Support with specific examples and data from document excerpts
- Reference entities by name when introducing concepts
- Include quantitative evidence when present (percentages, dollar amounts, growth rates)
- Discuss both opportunities AND challenges when relevant
- Maintain professional, analytical tone
- If information is insufficient, clearly state what's missing

Base everything strictly on the provided context. Never invent information."""

        # Enhanced user prompt with explicit instructions
        user_prompt = f"""**Question:**
{query}

---

**Context (Retrieved Information):**
{context}

---

**Instructions:**
Using the entities and document excerpts above, provide a comprehensive, well-structured answer that:
- Integrates both structured concepts and detailed examples
- Includes specific data and evidence from the excerpts
- Explains the reasoning and implications
- Discusses relevant trade-offs or challenges

Your answer:"""

        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=2048,
                temperature=0.3,
                system=system_prompt,
                messages=[{
                    "role": "user",
                    "content": user_prompt
                }]
            )

            return response.content[0].text

        except Exception as e:
            logger.error(f"Error generating response: {e}")
            return f"Error: {str(e)}"
