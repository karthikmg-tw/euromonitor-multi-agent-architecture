// ============================================
// PHASE 1: CORE ENTITIES - Toys & Games Asia Pacific
// Source: Euromonitor International (June 2024)
// ============================================

// 1. CREATE REGION
MERGE (apac:Region {name: 'Asia Pacific'})
SET apac.description = 'Asia Pacific region for Toys and Games market',
    apac.data_source = 'Euromonitor International',
    apac.report_date = date('2024-06-01');

// 2. CREATE INDUSTRY & CATEGORIES
MERGE (toysGames:Industry {name: 'Toys and Games'})
SET toysGames.description = 'Consumer toys and gaming industry';

MERGE (videoGames:Category {name: 'Video Games'})
SET videoGames.parent_industry = 'Toys and Games',
    videoGames.type = 'product_category';

MERGE (traditionalToys:Category {name: 'Traditional Toys and Games'})
SET traditionalToys.parent_industry = 'Toys and Games',
    traditionalToys.type = 'product_category';

// Subcategories
MERGE (mobileGames:Category {name: 'Mobile Games'})
SET mobileGames.parent_category = 'Video Games';

MERGE (consoleGames:Category {name: 'Console Games'})
SET consoleGames.parent_category = 'Video Games';

MERGE (construction:Category {name: 'Construction'})
SET construction.parent_category = 'Traditional Toys and Games';

MERGE (gamesPuzzles:Category {name: 'Games and Puzzles'})
SET gamesPuzzles.parent_category = 'Traditional Toys and Games';

MERGE (dollsAccessories:Category {name: 'Dolls and Accessories'})
SET dollsAccessories.parent_category = 'Traditional Toys and Games';

// Link categories to industry
MATCH (i:Industry {name: 'Toys and Games'}),
      (c:Category)
WHERE c.parent_industry = 'Toys and Games'
CREATE (c)-[:PART_OF]->(i);

// Link subcategories
MATCH (sub:Category), (parent:Category)
WHERE sub.parent_category = parent.name
CREATE (sub)-[:SUBCATEGORY_OF]->(parent);

// 3. CREATE KEY COUNTRIES WITH MARKET DATA
MERGE (china:Country {name: 'China', iso_code: 'CN'})
SET china.market_size_2023 = 60224,  // USD million
    china.market_rank_apac = 1,
    china.key_insight = 'Strong rebound in 2023 after COVID-19 lockdowns';

MERGE (japan:Country {name: 'Japan', iso_code: 'JP'})
SET japan.market_size_2023 = 18500,  // Approximate from charts
    japan.market_rank_apac = 2,
    japan.key_insight = 'Trading card games driving growth';

MERGE (southKorea:Country {name: 'South Korea', iso_code: 'KR'})
SET southKorea.market_size_2023 = 8500,  // Approximate
    southKorea.market_rank_apac = 3,
    southKorea.key_insight = 'Declining market with kidults focus';

MERGE (india:Country {name: 'India', iso_code: 'IN'})
SET india.market_size_2023 = 3000,  // Approximate
    india.growth_potential = 'high',
    india.key_insight = 'Dynamic growth in video games, e-sports popularity';

MERGE (indonesia:Country {name: 'Indonesia', iso_code: 'ID'})
SET indonesia.market_size_2023 = 2200;

MERGE (thailand:Country {name: 'Thailand', iso_code: 'TH'})
SET thailand.market_size_2023 = 1800;

MERGE (taiwan:Country {name: 'Taiwan', iso_code: 'TW'})
SET taiwan.market_size_2023 = 1500;

MERGE (malaysia:Country {name: 'Malaysia', iso_code: 'MY'})
SET malaysia.market_size_2023 = 1200;

MERGE (philippines:Country {name: 'Philippines', iso_code: 'PH'})
SET philippines.market_size_2023 = 900;

MERGE (hongKong:Country {name: 'Hong Kong', iso_code: 'HK'})
SET hongKong.market_size_2023 = 850;

MERGE (singapore:Country {name: 'Singapore', iso_code: 'SG'})
SET singapore.market_size_2023 = 600;

// Link countries to region
MATCH (r:Region {name: 'Asia Pacific'}),
      (c:Country)
WHERE c.iso_code IN ['CN', 'JP', 'KR', 'IN', 'ID', 'TH', 'TW', 'MY', 'PH', 'HK', 'SG']
CREATE (c)-[:LOCATED_IN]->(r);

// 4. CREATE TOP COMPANIES (Top 10 regional players)
MERGE (tencent:Company {name: 'Tencent Holdings Ltd'})
SET tencent.hq_country = 'China',
    tencent.primary_category = 'Video Games',
    tencent.rank_apac = 1;

MERGE (netease:Company {name: 'NetEase Inc'})
SET netease.hq_country = 'China',
    netease.primary_category = 'Video Games',
    netease.rank_apac = 2;

MERGE (nintendo:Company {name: 'Nintendo Co Ltd'})
SET nintendo.hq_country = 'Japan',
    nintendo.primary_category = 'Video Games',
    nintendo.rank_apac = 3;

MERGE (mihoyo:Company {name: 'miHoYo Co Ltd'})
SET mihoyo.hq_country = 'China',
    mihoyo.primary_category = 'Mobile Games',
    mihoyo.rank_apac = 4;

MERGE (bandai:Company {name: 'BANDAI NAMCO Group'})
SET bandai.hq_country = 'Japan',
    bandai.primary_category = 'Toys and Games',
    bandai.rank_apac = 5;

MERGE (nexon:Company {name: 'Nexon Co Ltd'})
SET nexon.hq_country = 'South Korea',
    nexon.primary_category = 'Video Games',
    nexon.rank_apac = 6;

MERGE (sony:Company {name: 'Sony Corp'})
SET sony.hq_country = 'Japan',
    sony.primary_category = 'Video Games',
    sony.rank_apac = 7;

MERGE (lego:Company {name: 'LEGO Group'})
SET lego.hq_country = 'Denmark',
    lego.primary_category = 'Traditional Toys and Games',
    lego.rank_apac = 8;

MERGE (wuhu:Company {name: 'Wuhu Shunrong Sanqi Interactive Entertainment Network Technology Group'})
SET wuhu.hq_country = 'China',
    wuhu.primary_category = 'Video Games',
    wuhu.rank_apac = 9;

MERGE (tomy:Company {name: 'Tomy Co Ltd'})
SET tomy.hq_country = 'Japan',
    tomy.primary_category = 'Traditional Toys and Games',
    tomy.rank_apac = 10;

// Link companies to countries and categories
MATCH (comp:Company), (country:Country)
WHERE comp.hq_country = country.name
CREATE (comp)-[:HEADQUARTERED_IN]->(country);

MATCH (comp:Company), (cat:Category)
WHERE comp.primary_category = cat.name OR comp.primary_category = cat.parent_industry
CREATE (comp)-[:COMPETES_IN]->(cat);

// 5. CREATE KEY TRENDS
MERGE (kidults:Trend {name: 'Kidults Segment Growth'})
SET kidults.description = 'Adults becoming key target for toys and games due to declining birth rates',
    kidults.impact = 'high',
    kidults.regions_affected = ['Asia Pacific'];

MERGE (genderNeutral:Trend {name: 'Gender-Neutral Toys'})
SET genderNeutral.description = 'Increasing focus on gender-neutral products to widen target market',
    genderNeutral.impact = 'medium',
    genderNeutral.driver = 'Gender equality awareness';

MERGE (culturalIdentity:Trend {name: 'Cultural Identity Toys'})
SET culturalIdentity.description = 'Growing appreciation for toys that reflect local cultural identity',
    culturalIdentity.impact = 'high',
    culturalIdentity.primary_market = 'China';

MERGE (ecommerce:Trend {name: 'E-commerce Dominance'})
SET ecommerce.description = 'E-commerce expanding share of distribution, especially for video games',
    ecommerce.impact = 'high',
    ecommerce.video_games_share = 0.90;

MERGE (esports:Trend {name: 'E-sports Growth'})
SET esports.description = 'Increasing popularity of e-sports boosting mobile gaming adoption',
    esports.impact = 'high',
    esports.primary_markets = ['India', 'Indonesia'];

MERGE (crossPlatform:Trend {name: 'Cross-Platform Gaming'})
SET crossPlatform.description = 'Games expanding across mobile, computer, and console platforms',
    crossPlatform.impact = 'medium',
    crossPlatform.benefits = 'Additional sales opportunities';

// Link trends to affected entities
MATCH (t:Trend {name: 'Kidults Segment Growth'}),
      (c:Country)
WHERE c.iso_code IN ['JP', 'KR', 'CN']
CREATE (t)-[:IMPACTS]->(c);

MATCH (t:Trend {name: 'Cultural Identity Toys'}),
      (china:Country {iso_code: 'CN'})
CREATE (t)-[:EMERGING_IN]->(china);

MATCH (t:Trend {name: 'E-sports Growth'}),
      (india:Country {name: 'India'})
CREATE (t)-[:DRIVING_GROWTH_IN]->(india);

// 6. CREATE DISTRIBUTION CHANNELS
MERGE (ecomm:DistributionChannel {name: 'Retail E-Commerce'})
SET ecomm.growth_trend = 'increasing',
    ecomm.dominant_in = 'Video Games';

MERGE (leisureGoods:DistributionChannel {name: 'Leisure and Personal Goods Specialists'})
SET leisureGoods.growth_trend = 'stable';

MERGE (appliances:DistributionChannel {name: 'Appliances and Electronics Specialists'})
SET appliances.notable_market = 'Japan',
    appliances.japan_share = 0.14;

MERGE (generalMerch:DistributionChannel {name: 'General Merchandise Stores'})
SET generalMerch.trend = 'potential growth in South Korea';

// Link channels to categories
MATCH (ec:DistributionChannel {name: 'Retail E-Commerce'}),
      (vg:Category {name: 'Video Games'})
CREATE (vg)-[:SOLD_THROUGH]->(ec);

RETURN 'Core entities created successfully' as status;
