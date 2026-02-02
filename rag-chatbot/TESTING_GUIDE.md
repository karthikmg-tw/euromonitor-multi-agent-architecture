# RAG Chatbot Testing Guide

## Quick Start

### 1. Start the Backend (if not running)

```bash
cd rag-chatbot
source venv/bin/activate
python -m uvicorn app.main:app --reload --port 8000
```

### 2. Choose Your Testing Method

**Option A: Interactive Shell Script (Recommended)**
```bash
./test_chat.sh
```

**Option B: Interactive Python Script**
```bash
python test_chat.py
```

**Option C: Direct cURL (Quick tests)**
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"query": "What are kidults?", "top_k": 5}' | jq -r '.answer'
```

---

## Test Scenarios

### Scenario 1: Factual Queries (Definition/Lookup)

**Best Settings:** `entity_weight=1.5, chunk_weight=0.7, top_k=5`

**Test Questions:**
- "What is LEGO?"
- "What are kidults?"
- "What is digital integration?"
- "What are construction toys?"

**What to Look For:**
- ✅ Clear, concise definition
- ✅ Structured organization (sections/headings)
- ✅ Key attributes mentioned
- ✅ Related concepts referenced

**Example Good Response:**
```
LEGO is a leading global brand and manufacturer of construction toys.

Market Position:
- #1 player in traditional toys in China
- Strong brand recognition

Recent Performance:
- First sales decline in 2023
- Competition from local brands
...
```

---

### Scenario 2: Exploratory Queries (Why/How)

**Best Settings:** `entity_weight=0.7, chunk_weight=1.5, top_k=7`

**Test Questions:**
- "Why are kidults important to the toy market?"
- "How is digital integration changing toys?"
- "Why are mobile games popular in Asia Pacific?"
- "What challenges do traditional toy makers face?"

**What to Look For:**
- ✅ Detailed explanations with reasoning
- ✅ Specific examples and quotes from documents
- ✅ Multiple perspectives (benefits + challenges)
- ✅ Evidence-based claims (statistics, data points)
- ✅ Causal relationships explained

**Example Good Response:**
```
Kidults are important for several key reasons:

1. Declining Birth Rates: With birth rates declining, toy companies are "looking to tap into adult consumers' childhood nostalgia" (Source: Market Research).

2. Greater Spending Power: Kidults have significantly higher purchasing power than children, with average spend 2-3x higher...

3. Market Expansion: This segment allows companies to offset declining children's sales...

However, challenges include...
```

---

### Scenario 3: Comparative Queries

**Best Settings:** `entity_weight=1.0, chunk_weight=1.0, top_k=7` (Balanced)

**Test Questions:**
- "How do mobile games compare to traditional toys in Asia Pacific?"
- "What's the difference between Japan and China toy markets?"
- "Compare LEGO and local Chinese brands"
- "Physical stores vs e-commerce in toy retail?"

**What to Look For:**
- ✅ Side-by-side comparison structure
- ✅ Quantitative comparisons (percentages, ratios)
- ✅ Multiple dimensions compared
- ✅ Nuanced analysis (not just pros/cons)

**Example Good Response:**
```
Mobile Games vs Traditional Toys:

Market Size:
- Mobile games: 2-4x larger than traditional toys
- China: Mobile games account for 70%+ of video games market

Growth Trends:
- Mobile: Strong rebound post-pandemic
- Traditional: Stagnating in mature markets

Challenges:
- Mobile: Regulation, license approval
- Traditional: E-commerce shift, declining birth rates
...
```

---

### Scenario 4: Edge Cases

**Test Questions:**
- "What is quantum computing?" (Out of domain)
- "Tell me about toys in Europe" (Adjacent domain)
- "What will happen in 2025?" (Future prediction)
- "" (Empty query)

**What to Look For:**
- ✅ Graceful handling of out-of-domain queries
- ✅ Honest acknowledgment of missing information
- ✅ Offer of related information when available

---

## Weight Tuning Cheat Sheet

| Query Type | Entity Weight | Chunk Weight | Top K | Use Case |
|------------|---------------|--------------|-------|----------|
| Factual definition | 1.5 | 0.7 | 5 | "What is X?" |
| Exploratory why/how | 0.7 | 1.5 | 7 | "Why does X happen?" |
| Comparative analysis | 1.0 | 1.0 | 7 | "X vs Y?" |
| Quick lookup | 1.5 | 0.5 | 3 | Fast, concise answer |
| Deep research | 0.6 | 1.5 | 10 | Maximum detail |

---

## Quality Checklist

### Good Answer Indicators ✅

- [ ] Directly addresses the question
- [ ] Structured with headings/sections (for complex queries)
- [ ] Includes specific examples or data points
- [ ] Cites entities by name when referencing concepts
- [ ] Discusses both opportunities AND challenges (where relevant)
- [ ] Maintains analytical, professional tone
- [ ] No hallucinated information
- [ ] Appropriate length (not too brief, not verbose)

### Red Flags 🚩

- [ ] Generic, vague statements without specifics
- [ ] No structure (wall of text)
- [ ] Contradictory information
- [ ] Information not in source documents
- [ ] Overly brief for complex questions
- [ ] No evidence or examples provided

---

## Debugging Tips

### Issue: Answers Too Brief

**Fix:**
- Increase `top_k` from 5 to 7-10
- Increase `chunk_weight` to 1.3-1.5
- Check: Are chunks being retrieved? (debug mode)

### Issue: Answers Too Verbose

**Fix:**
- Decrease `top_k` from 7 to 5
- Increase `entity_weight` to 1.5
- Prefer entity-focused queries

### Issue: Missing Expected Information

**Fix:**
- Check: Does the information exist in source document?
- Try different phrasings of the question
- Increase `top_k` to retrieve more results
- Lower `min_similarity` threshold

### Issue: Generic/Vague Answers

**Fix:**
- Increase `chunk_weight` for more detailed excerpts
- Check: Is enhanced prompt active? (should see structured responses)
- Verify dual-source retrieval is working (debug mode)

---

## Sample Test Session

```bash
# Start interactive tester
./test_chat.sh

# Choose option 1 (quick tests) to verify basic functionality
# Then try option 5 (compare weights) with your domain questions
# Finally, option 2-4 for custom queries

# Good test questions from your domain:
- "What trends are driving toys in Asia Pacific?"
- "Why is China important?"
- "What challenges does LEGO face?"
- "How are kidults changing the market?"
```

---

## Performance Benchmarks

**Expected Response Times:**
- Factual query (top_k=5): 2-4 seconds
- Exploratory (top_k=7): 3-5 seconds
- Comparative (top_k=7): 3-6 seconds

**Expected Answer Quality:**
- Word count: 150-300 words (varies by query)
- Structure: 2-4 main sections for complex queries
- Sources: Mix of entities + chunks (check debug output)

---

## Next Steps After Testing

Once you've validated the system:

1. **Document Your Findings**
   - Which weight configurations work best for your use cases?
   - Any domain-specific patterns you noticed?

2. **Consider Presets**
   - Create named presets for common query types
   - Example: `preset="research"` maps to `(0.7, 1.5, 7)`

3. **User Feedback Loop**
   - Track which queries work well vs poorly
   - Iterate on prompts and weights based on real usage

4. **Production Readiness**
   - Add logging for monitoring
   - Set up error handling for edge cases
   - Consider caching for frequent queries

---

**Remember:** The boring technology that works is tested technology. Take time to validate across different scenarios before shipping.
