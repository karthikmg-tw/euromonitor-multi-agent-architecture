// ============================================
// PHASE 2: DETAILED METRICS FRAMEWORK
// Purpose: Structure for adding granular market data incrementally
// ============================================

// This file demonstrates the pattern for adding detailed data
// Can be executed incrementally as more data is processed

// 1. COUNTRY DETAILED METRICS (Example: China)
// -------------------------------------------------
MATCH (china:Country {iso_code: 'CN'})
SET china += {
  // Market Size & Growth
  market_size_2018: 49900,
  market_size_2023: 60224,
  cagr_2018_2023: 4.2,
  forecast_size_2028: 65700,
  forecast_cagr_2023_2028: 1.8,

  // Category Breakdown (2023)
  video_games_size: 45500,
  traditional_toys_size: 14724,
  video_games_share: 0.756,
  traditional_toys_share: 0.244,

  // Video Games Subcategories
  mobile_games_share: 0.71,
  console_games_share: 0.15,
  computer_games_share: 0.14,

  // Distribution Channels
  ecommerce_share: 0.83,
  offline_share: 0.17,

  // Key Insights
  insight_2023: 'Strong rebound after COVID-19 lockdowns',
  growth_driver_2023: 'Normalization of work/life routines',
  consumer_trend: 'Stress relief and emotional spending',

  // Competitive Landscape
  market_concentration: 'moderate',
  top5_companies_share: 0.42,

  // Source metadata
  last_updated: datetime(),
  data_year: 2023
};

// 2. COMPANY PERFORMANCE METRICS (Example: Tencent)
// -------------------------------------------------
MATCH (tencent:Company {name: 'Tencent Holdings Ltd'})
SET tencent += {
  // Market Position
  regional_market_share: 0.18,
  china_market_share: 0.30,
  growth_2018_2023: 4.5,

  // Product Portfolio
  flagship_products: ['Honor of Kings', 'Fun Party', 'Peacekeeper Elite'],
  category_focus: 'Mobile Games',

  // Strategic Initiatives
  strategy_2023: 'Integration with other platforms (QQ Music, Tencent Video)',
  competitive_advantage: 'Ecosystem integration',

  // Performance
  performance_2023: 'Lost market share despite positive growth',
  challenge: 'Increasing competition from NetEase and miHoYo'
};

// Create product nodes for key games
MERGE (honorKings:Product {name: 'Honor of Kings'})
SET honorKings.type = 'Mobile Game',
    honorKings.genre = 'MOBA';

MATCH (tencent:Company {name: 'Tencent Holdings Ltd'}),
      (honorKings:Product {name: 'Honor of Kings'})
CREATE (honorKings)-[:PUBLISHED_BY]->(tencent);

// 3. TREND DETAILED METRICS
// -------------------------------------------------
MATCH (kidults:Trend {name: 'Kidults Segment Growth'})
SET kidults += {
  // Scope
  affected_countries: ['China', 'Japan', 'South Korea'],
  primary_categories: ['Construction', 'Collectibles', 'Trading Cards'],

  // Drivers
  driver_1: 'Declining birth rates in major markets',
  driver_2: 'Adult consumers have greater spending power',
  driver_3: 'Childhood nostalgia appeal',

  // Impact
  impact_on_strategy: 'Companies shifting from children to adults',
  product_examples: ['LEGO adult sets', 'Pop Mart blind boxes', 'Pokémon cards'],

  // Forecast
  growth_outlook: 'Increasing importance through 2028'
};

// 4. COMPETITIVE DYNAMICS (Example: Construction category)
// -------------------------------------------------
MERGE (constructionMarket:MarketSegment {
  name: 'Construction Toys - China',
  country: 'CN',
  category: 'Construction'
})
SET constructionMarket += {
  leader: 'LEGO',
  leader_challenge_2023: 'First sales decline in many years',

  // Competitive Changes
  competition_intensity: 'increasing',
  local_players_gaining: true,

  // Challengers
  challenger_1: 'Bloks',
  challenger_2: 'Enlighten (Qman)',
  challenger_3: 'Sembo',

  // Differentiation
  local_advantage: 'Chinese naval vessels and aerospace themed toys',
  cultural_resonance: 'Products reflecting national culture'
};

MATCH (lego:Company {name: 'LEGO Group'}),
      (segment:MarketSegment {name: 'Construction Toys - China'})
CREATE (lego)-[:COMPETES_IN]->(segment);

// 5. CHANNEL PERFORMANCE METRICS (Example: E-commerce in China)
// -------------------------------------------------
MERGE (chinaEcomm:ChannelPerformance {
  country: 'CN',
  channel: 'E-commerce',
  year: 2023
})
SET chinaEcomm += {
  // Share Data
  overall_share: 0.83,
  video_games_share: 0.94,
  traditional_toys_share: 0.35,

  // Growth
  trend: 'Declined in traditional toys, grew in specific platforms',
  growing_platform: 'Douyin (TikTok)',
  growth_driver: 'Live streaming e-commerce',

  // Offline Rebound
  offline_trend_2023: 'Resurgence in traditional toys',
  offline_driver: 'Post-pandemic store visits for experiential shopping'
};

MATCH (china:Country {iso_code: 'CN'}),
      (perf:ChannelPerformance {country: 'CN'})
CREATE (perf)-[:MEASURES]->(china);

// 6. FORECAST DATA STRUCTURE
// -------------------------------------------------
MERGE (chinaForecast:Forecast {
  country: 'CN',
  forecast_period: '2023-2028'
})
SET chinaForecast += {
  expected_cagr: 1.8,
  expected_size_2028: 65700,

  // Growth Drivers
  driver_video_games: 'Mobile games and cross-platform expansion',
  driver_traditional: 'Kidults and cultural identity products',

  // Challenges
  challenge_1: 'Slowing user growth in video games',
  challenge_2: 'Declining birth rates',

  // Opportunities
  opportunity_1: 'Licensed toys growing',
  opportunity_2: 'Trendy collectibles',
  opportunity_3: 'Adult consumer segment'
};

MATCH (china:Country {iso_code: 'CN'}),
      (forecast:Forecast {country: 'CN'})
CREATE (forecast)-[:PROJECTS]->(china);

// ============================================
// PATTERN TEMPLATES FOR INCREMENTAL LOADING
// ============================================

// Template 1: Add new country detail
// MATCH (country:Country {iso_code: 'XX'})
// SET country += { /* detailed metrics */ };

// Template 2: Add company performance in specific country
// CREATE (perf:CompanyPerformance {
//   company: 'Company Name',
//   country: 'XX',
//   year: 2023
// })
// SET perf += { /* metrics */ };

// Template 3: Add brand information
// MERGE (brand:Brand {name: 'Brand Name'})
// SET brand += { /* properties */ };
// MATCH (brand:Brand {name: 'Brand Name'}),
//       (company:Company {name: 'Owner'})
// CREATE (brand)-[:OWNED_BY]->(company);

RETURN 'Detailed metrics framework created' as status;
