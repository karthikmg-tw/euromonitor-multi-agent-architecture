// ============================================
// MARKET INSIGHTS & TRENDS
// Euromonitor Asia Pacific Knowledge Graph v2
// ============================================
// Author: Winston (Architect Agent) + Karthikmg
// Date: 2026-01-23
// Source: Toys and Games in Asia Pacific (June 2024)
// ============================================

// ============================================
// STEP 1: CREATE KEY INSIGHTS
// ============================================

// Regional Overview Insights
MERGE (insight1:Insight {id: 'insight_apac_video_games_dominance'})
SET insight1.type = 'Regional Overview',
    insight1.geography = 'Asia Pacific',
    insight1.insight = 'Video games sales more than 3x higher than traditional toys',
    insight1.year = 2023,
    insight1.created_at = datetime();

MERGE (insight2:Insight {id: 'insight_apac_mobile_games_share'})
SET insight2.type = 'Regional Overview',
    insight2.geography = 'Asia Pacific',
    insight2.insight = 'Mobile gaming accounts for close to 3/4 of video games sales',
    insight2.year = 2023,
    insight2.created_at = datetime();

MERGE (insight3:Insight {id: 'insight_apac_global_leader'})
SET insight3.type = 'Regional Performance',
    insight3.geography = 'Asia Pacific',
    insight3.insight = 'Highest video games sales among seven global regions',
    insight3.year = 2023,
    insight3.created_at = datetime();

MERGE (insight4:Insight {id: 'insight_apac_growth_contribution'})
SET insight4.type = 'Regional Growth',
    insight4.geography = 'Asia Pacific',
    insight4.insight = 'Generated just over half of all new value sales globally in 2018-2023',
    insight4.year_range = '2018-2023',
    insight4.created_at = datetime();

// Distribution Insights
MERGE (insight5:Insight {id: 'insight_video_games_ecommerce'})
SET insight5.type = 'Distribution',
    insight5.category = 'Video Games',
    insight5.geography = 'Asia Pacific',
    insight5.insight = 'E-commerce completely dominant with 90% share regionally',
    insight5.year = 2023,
    insight5.created_at = datetime();

MERGE (insight6:Insight {id: 'insight_traditional_distribution'})
SET insight6.type = 'Distribution',
    insight6.category = 'Traditional Toys and Games',
    insight6.geography = 'Asia Pacific',
    insight6.insight = 'E-commerce 35%, offline retail 66% (stores 23%, other retailers 43%)',
    insight6.year = 2023,
    insight6.created_at = datetime();

// Country-Specific Insights - China
MERGE (insight7:Insight {id: 'insight_china_rebound'})
SET insight7.type = 'Country Performance',
    insight7.geography = 'China',
    insight7.insight = 'Strong rebound in 2023 after COVID-19 lockdowns',
    insight7.year = 2023,
    insight7.created_at = datetime();

MERGE (insight8:Insight {id: 'insight_china_cultural_identity'})
SET insight8.type = 'Consumer Trend',
    insight8.geography = 'China',
    insight8.insight = 'Growing appreciation for toys reflecting cultural identity',
    insight8.year = 2023,
    insight8.created_at = datetime();

MERGE (insight9:Insight {id: 'insight_china_mobile_games'})
SET insight9.type = 'Category Performance',
    insight9.geography = 'China',
    insight9.category = 'Mobile Games',
    insight9.insight = 'Mobile games account for over 70% of video games',
    insight9.year = 2023,
    insight9.created_at = datetime();

// Country-Specific Insights - Japan
MERGE (insight10:Insight {id: 'insight_japan_trading_cards'})
SET insight10.type = 'Category Performance',
    insight10.geography = 'Japan',
    insight10.category = 'Games and Puzzles',
    insight10.insight = 'Trading card games (Pokémon) driving dynamic growth',
    insight10.year = 2023,
    insight10.created_at = datetime();

// Country-Specific Insights - South Korea
MERGE (insight11:Insight {id: 'insight_korea_kidults_focus'})
SET insight11.type = 'Consumer Trend',
    insight11.geography = 'South Korea',
    insight11.insight = 'Low birth rate driving focus on kidults segment',
    insight11.year = 2023,
    insight11.created_at = datetime();

MERGE (insight12:Insight {id: 'insight_korea_gender_neutral'})
SET insight12.type = 'Consumer Trend',
    insight12.geography = 'South Korea',
    insight12.insight = 'Gender-neutral toys becoming notable trend',
    insight12.year = 2023,
    insight12.created_at = datetime();

// Country-Specific Insights - India
MERGE (insight13:Insight {id: 'insight_india_video_games_growth'})
SET insight13.type = 'Forecast',
    insight13.geography = 'India',
    insight13.category = 'Video Games',
    insight13.insight = 'Dynamic growth expected in video games over forecast period',
    insight13.year_range = '2024-2029',
    insight13.created_at = datetime();

MERGE (insight14:Insight {id: 'insight_india_esports'})
SET insight14.type = 'Consumer Trend',
    insight14.geography = 'India',
    insight14.category = 'Video Games',
    insight14.insight = 'Rising popularity of e-sports boosting mobile gaming',
    insight14.year = 2023,
    insight14.created_at = datetime();

// ============================================
// STEP 2: LINK INSIGHTS TO GEOGRAPHIES
// ============================================

MATCH (i:Insight), (g:Geography)
WHERE i.geography = g.name
MERGE (i)-[:ABOUT_GEOGRAPHY {created_at: datetime()}]->(g);

// ============================================
// STEP 3: LINK INSIGHTS TO CATEGORIES
// ============================================

MATCH (i:Insight), (c:Category)
WHERE i.category = c.name
MERGE (i)-[:ABOUT_CATEGORY {created_at: datetime()}]->(c);

// ============================================
// STEP 4: CREATE TRENDS
// ============================================

// Trend 1: Kidults
MERGE (trend1:Trend {id: 'trend_kidults'})
SET trend1.trend_name = 'Kidults',
    trend1.description = 'Adult consumers becoming key target for toys and games',
    trend1.impact = 'high',
    trend1.geography = ['Asia Pacific', 'Japan', 'South Korea'],
    trend1.drivers = ['Declining birth rates in major markets', 'Adults have greater spending power', 'Players tapping into childhood nostalgia'],
    trend1.created_at = datetime();

// Trend 2: Cultural Identity
MERGE (trend2:Trend {id: 'trend_cultural_identity'})
SET trend2.trend_name = 'Cultural Identity',
    trend2.description = 'Growing appreciation for locally-themed toys',
    trend2.impact = 'high',
    trend2.geography = ['China'],
    trend2.drivers = ['Chinese consumers showing preference for cultural identity', 'Local players developing culturally-themed products'],
    trend2.created_at = datetime();

// Trend 3: Gender-Neutral Toys
MERGE (trend3:Trend {id: 'trend_gender_neutral'})
SET trend3.trend_name = 'Gender-Neutral Toys',
    trend3.description = 'Blurring distinction between boys and girls toys',
    trend3.impact = 'medium',
    trend3.geography = ['South Korea', 'Asia Pacific'],
    trend3.drivers = ['Awareness of gender equality increasing', 'Widening target market'],
    trend3.created_at = datetime();

// Trend 4: Experiential Retail
MERGE (trend4:Trend {id: 'trend_experiential_retail'})
SET trend4.trend_name = 'Experiential Retail',
    trend4.description = 'Offline stores creating experiential visits',
    trend4.impact = 'high',
    trend4.geography = ['Asia Pacific', 'Japan'],
    trend4.drivers = ['E-commerce threat', 'Need to differentiate from online', 'Making visits fun and engaging'],
    trend4.created_at = datetime();

// Trend 5: Cross-Platform Gaming
MERGE (trend5:Trend {id: 'trend_cross_platform'})
SET trend5.trend_name = 'Cross-Platform Gaming',
    trend5.description = 'Games expanding across multiple platforms',
    trend5.impact = 'high',
    trend5.geography = ['Asia Pacific', 'China'],
    trend5.category = 'Video Games',
    trend5.drivers = ['Mobile games expanding to console/computer', 'Providing additional sales opportunities'],
    trend5.created_at = datetime();

// Trend 6: E-Sports
MERGE (trend6:Trend {id: 'trend_esports'})
SET trend6.trend_name = 'E-Sports',
    trend6.description = 'Rising popularity of competitive gaming',
    trend6.impact = 'high',
    trend6.geography = ['India'],
    trend6.category = 'Video Games',
    trend6.drivers = ['Mobile gaming growth', 'Smartphone penetration'],
    trend6.created_at = datetime();

// ============================================
// STEP 5: LINK TRENDS TO GEOGRAPHIES
// ============================================

// Kidults - Asia Pacific, Japan, South Korea
MATCH (t:Trend {id: 'trend_kidults'}),
      (apac:Region {id: 'geo_asia_pacific'}),
      (japan:Country {id: 'geo_japan'}),
      (korea:Country {id: 'geo_south_korea'})
MERGE (t)-[:IMPACTS_GEOGRAPHY {created_at: datetime()}]->(apac)
MERGE (t)-[:IMPACTS_GEOGRAPHY {created_at: datetime()}]->(japan)
MERGE (t)-[:IMPACTS_GEOGRAPHY {created_at: datetime()}]->(korea);

// Cultural Identity - China
MATCH (t:Trend {id: 'trend_cultural_identity'}),
      (china:Country {id: 'geo_china'})
MERGE (t)-[:IMPACTS_GEOGRAPHY {created_at: datetime()}]->(china);

// Gender-Neutral - South Korea, Asia Pacific
MATCH (t:Trend {id: 'trend_gender_neutral'}),
      (korea:Country {id: 'geo_south_korea'}),
      (apac:Region {id: 'geo_asia_pacific'})
MERGE (t)-[:IMPACTS_GEOGRAPHY {created_at: datetime()}]->(korea)
MERGE (t)-[:IMPACTS_GEOGRAPHY {created_at: datetime()}]->(apac);

// Experiential Retail - Asia Pacific, Japan
MATCH (t:Trend {id: 'trend_experiential_retail'}),
      (apac:Region {id: 'geo_asia_pacific'}),
      (japan:Country {id: 'geo_japan'})
MERGE (t)-[:IMPACTS_GEOGRAPHY {created_at: datetime()}]->(apac)
MERGE (t)-[:IMPACTS_GEOGRAPHY {created_at: datetime()}]->(japan);

// Cross-Platform Gaming - Asia Pacific, China
MATCH (t:Trend {id: 'trend_cross_platform'}),
      (apac:Region {id: 'geo_asia_pacific'}),
      (china:Country {id: 'geo_china'})
MERGE (t)-[:IMPACTS_GEOGRAPHY {created_at: datetime()}]->(apac)
MERGE (t)-[:IMPACTS_GEOGRAPHY {created_at: datetime()}]->(china);

// E-Sports - India
MATCH (t:Trend {id: 'trend_esports'}),
      (india:Country {id: 'geo_india'})
MERGE (t)-[:IMPACTS_GEOGRAPHY {created_at: datetime()}]->(india);

// ============================================
// STEP 6: LINK TRENDS TO CATEGORIES
// ============================================

// Cross-Platform Gaming - Video Games
MATCH (t:Trend {id: 'trend_cross_platform'}),
      (cat:Category {id: 'cat_video_games'})
MERGE (t)-[:IMPACTS_CATEGORY {created_at: datetime()}]->(cat);

// E-Sports - Video Games
MATCH (t:Trend {id: 'trend_esports'}),
      (cat:Category {id: 'cat_video_games'})
MERGE (t)-[:IMPACTS_CATEGORY {created_at: datetime()}]->(cat);

// ============================================
// STEP 7: LINK TRENDS TO COMPANIES
// ============================================

// Cultural Identity impacts local Chinese companies
MATCH (t:Trend {id: 'trend_cultural_identity'}),
      (sembo:Company {id: 'comp_sembo'}),
      (enlighten:Company {id: 'comp_enlighten'}),
      (bloks:Company {id: 'comp_bloks'})
MERGE (t)-[:BENEFITS_COMPANY {type: 'positive', created_at: datetime()}]->(sembo)
MERGE (t)-[:BENEFITS_COMPANY {type: 'positive', created_at: datetime()}]->(enlighten)
MERGE (t)-[:BENEFITS_COMPANY {type: 'positive', created_at: datetime()}]->(bloks);

// Cultural Identity challenges LEGO
MATCH (t:Trend {id: 'trend_cultural_identity'}),
      (lego:Company {id: 'comp_lego'})
MERGE (t)-[:BENEFITS_COMPANY {type: 'negative', created_at: datetime()}]->(lego);

// E-Sports benefits gaming companies in India
MATCH (t:Trend {id: 'trend_esports'}),
      (sony:Company {id: 'comp_sony'})
MERGE (t)-[:BENEFITS_COMPANY {type: 'positive', created_at: datetime()}]->(sony);

// ============================================
// VERIFICATION QUERIES
// ============================================

// View all insights by geography:
// MATCH (i:Insight)-[:ABOUT_GEOGRAPHY]->(g:Geography)
// RETURN g.name, count(i) as insight_count, collect(i.insight)[0..3] as sample_insights;

// View all trends:
// MATCH (t:Trend) RETURN t.trend_name, t.description, t.impact, t.geography;

// View trends impacting specific geography:
// MATCH (t:Trend)-[:IMPACTS_GEOGRAPHY]->(g:Country {name: 'China'})
// RETURN t.trend_name, t.description;

// View company-trend relationships:
// MATCH (t:Trend)-[r:BENEFITS_COMPANY]->(c:Company)
// RETURN t.trend_name, c.name, r.type;
