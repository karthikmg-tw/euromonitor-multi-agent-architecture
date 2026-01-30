// ============================================
// COMPANIES & BRANDS
// Euromonitor Asia Pacific Knowledge Graph v2
// ============================================
// Author: Winston (Architect Agent) + Karthikmg
// Date: 2026-01-23
// Source: Toys and Games in Asia Pacific (June 2024)
// ============================================

// ============================================
// STEP 1: CREATE COMPANIES
// ============================================

// Tencent - Regional Leader
MERGE (tencent:Company {id: 'comp_tencent'})
SET tencent.name = 'Tencent Holdings Ltd',
    tencent.type = 'GBO',
    tencent.primary_market = 'China',
    tencent.market_position = 'Regional leader',
    tencent.created_at = datetime(),
    tencent.updated_at = datetime();

// NetEase
MERGE (netease:Company {id: 'comp_netease'})
SET netease.name = 'NetEase Inc',
    netease.type = 'GBO',
    netease.primary_market = 'China',
    netease.market_position = 'Top 4 regional',
    netease.created_at = datetime(),
    netease.updated_at = datetime();

// miHoYo
MERGE (mihoyo:Company {id: 'comp_mihoyo'})
SET mihoyo.name = 'miHoYo',
    mihoyo.type = 'Company',
    mihoyo.primary_market = 'China',
    mihoyo.market_position = 'Top 4 regional',
    mihoyo.created_at = datetime(),
    mihoyo.updated_at = datetime();

// LEGO
MERGE (lego:Company {id: 'comp_lego'})
SET lego.name = 'LEGO Group',
    lego.type = 'GBO',
    lego.primary_market = 'Global',
    lego.market_position = 'Traditional toys leader',
    lego.headquarters_country = 'Denmark',
    lego.created_at = datetime(),
    lego.updated_at = datetime();

// Nintendo
MERGE (nintendo:Company {id: 'comp_nintendo'})
SET nintendo.name = 'Nintendo Co Ltd',
    nintendo.type = 'GBO',
    nintendo.primary_market = 'Japan',
    nintendo.market_position = 'Top brand in Asia Pacific',
    nintendo.headquarters_country = 'Japan',
    nintendo.created_at = datetime(),
    nintendo.updated_at = datetime();

// Sony Interactive Entertainment
MERGE (sony:Company {id: 'comp_sony'})
SET sony.name = 'Sony Interactive Entertainment',
    sony.type = 'GBO',
    sony.primary_market = 'Japan',
    sony.market_position = 'Top 3 brand',
    sony.headquarters_country = 'Japan',
    sony.created_at = datetime(),
    sony.updated_at = datetime();

// Pop Mart
MERGE (popmart:Company {id: 'comp_popmart'})
SET popmart.name = 'Pop Mart',
    popmart.type = 'Company',
    popmart.primary_market = 'China',
    popmart.market_position = 'Blind collectables leader',
    popmart.created_at = datetime(),
    popmart.updated_at = datetime();

// Sembo - Local Chinese Brand
MERGE (sembo:Company {id: 'comp_sembo'})
SET sembo.name = 'Sembo',
    sembo.type = 'NBO',
    sembo.primary_market = 'China',
    sembo.headquarters_country = 'China',
    sembo.created_at = datetime(),
    sembo.updated_at = datetime();

// Enlighten (Qman)
MERGE (enlighten:Company {id: 'comp_enlighten'})
SET enlighten.name = 'Enlighten (Qman)',
    enlighten.type = 'NBO',
    enlighten.primary_market = 'China',
    enlighten.headquarters_country = 'China',
    enlighten.created_at = datetime(),
    enlighten.updated_at = datetime();

// Bloks
MERGE (bloks:Company {id: 'comp_bloks'})
SET bloks.name = 'Bloks',
    bloks.type = 'Company',
    bloks.primary_market = 'China',
    bloks.headquarters_country = 'China',
    bloks.created_at = datetime(),
    bloks.updated_at = datetime();

// ============================================
// STEP 2: CREATE BRANDS
// ============================================

// PlayStation
MERGE (playstation:Brand {id: 'brand_playstation'})
SET playstation.name = 'PlayStation',
    playstation.owner_company_id = 'comp_sony',
    playstation.type = 'GBN',
    playstation.created_at = datetime(),
    playstation.updated_at = datetime();

// Nintendo Switch
MERGE (switch:Brand {id: 'brand_nintendo_switch'})
SET switch.name = 'Nintendo Switch',
    switch.owner_company_id = 'comp_nintendo',
    switch.type = 'GBN',
    switch.created_at = datetime(),
    switch.updated_at = datetime();

// Pokémon
MERGE (pokemon:Brand {id: 'brand_pokemon'})
SET pokemon.name = 'Pokémon',
    pokemon.owner_company_id = 'comp_nintendo',
    pokemon.type = 'GBN',
    pokemon.created_at = datetime(),
    pokemon.updated_at = datetime();

// LEGO Brand
MERGE (legobrand:Brand {id: 'brand_lego'})
SET legobrand.name = 'LEGO',
    legobrand.owner_company_id = 'comp_lego',
    legobrand.type = 'GBN',
    legobrand.created_at = datetime(),
    legobrand.updated_at = datetime();

// Genshin Impact
MERGE (genshin:Brand {id: 'brand_genshin'})
SET genshin.name = 'Genshin Impact',
    genshin.owner_company_id = 'comp_mihoyo',
    genshin.type = 'GBN',
    genshin.created_at = datetime(),
    genshin.updated_at = datetime();

// Honkai: Star Rail
MERGE (honkai:Brand {id: 'brand_honkai'})
SET honkai.name = 'Honkai: Star Rail',
    honkai.owner_company_id = 'comp_mihoyo',
    honkai.type = 'GBN',
    honkai.launch_year = 2023,
    honkai.created_at = datetime(),
    honkai.updated_at = datetime();

// Yu-Gi-Oh!
MERGE (yugioh:Brand {id: 'brand_yugioh'})
SET yugioh.name = 'Yu-Gi-Oh!',
    yugioh.type = 'GBN',
    yugioh.created_at = datetime(),
    yugioh.updated_at = datetime();

// Duel Masters
MERGE (duel:Brand {id: 'brand_duel_masters'})
SET duel.name = 'Duel Masters',
    duel.type = 'GBN',
    duel.created_at = datetime(),
    duel.updated_at = datetime();

// ============================================
// STEP 3: LINK BRANDS TO COMPANIES
// ============================================

MATCH (b:Brand), (c:Company)
WHERE b.owner_company_id = c.id
MERGE (b)-[:OWNED_BY {created_at: datetime()}]->(c);

// ============================================
// STEP 4: LINK COMPANIES TO CATEGORIES
// ============================================

// Tencent - Video Games, Mobile Games
MATCH (c:Company {id: 'comp_tencent'}),
      (cat1:Category {id: 'cat_video_games'}),
      (cat2:Category {id: 'cat_mobile_games'})
MERGE (c)-[:COMPETES_IN {created_at: datetime()}]->(cat1)
MERGE (c)-[:COMPETES_IN {created_at: datetime()}]->(cat2);

// NetEase - Video Games, Mobile Games
MATCH (c:Company {id: 'comp_netease'}),
      (cat1:Category {id: 'cat_video_games'}),
      (cat2:Category {id: 'cat_mobile_games'})
MERGE (c)-[:COMPETES_IN {created_at: datetime()}]->(cat1)
MERGE (c)-[:COMPETES_IN {created_at: datetime()}]->(cat2);

// miHoYo - Video Games, Mobile Games
MATCH (c:Company {id: 'comp_mihoyo'}),
      (cat1:Category {id: 'cat_video_games'}),
      (cat2:Category {id: 'cat_mobile_games'})
MERGE (c)-[:COMPETES_IN {created_at: datetime()}]->(cat1)
MERGE (c)-[:COMPETES_IN {created_at: datetime()}]->(cat2);

// LEGO - Construction, Traditional Toys
MATCH (c:Company {id: 'comp_lego'}),
      (cat1:Category {id: 'cat_construction'}),
      (cat2:Category {id: 'cat_traditional'})
MERGE (c)-[:COMPETES_IN {created_at: datetime()}]->(cat1)
MERGE (c)-[:COMPETES_IN {created_at: datetime()}]->(cat2);

// Nintendo - Video Games, Hardware
MATCH (c:Company {id: 'comp_nintendo'}),
      (cat1:Category {id: 'cat_video_games'}),
      (cat2:Category {id: 'cat_vg_hardware'})
MERGE (c)-[:COMPETES_IN {created_at: datetime()}]->(cat1)
MERGE (c)-[:COMPETES_IN {created_at: datetime()}]->(cat2);

// Sony - Video Games, Hardware
MATCH (c:Company {id: 'comp_sony'}),
      (cat1:Category {id: 'cat_video_games'}),
      (cat2:Category {id: 'cat_vg_hardware'})
MERGE (c)-[:COMPETES_IN {created_at: datetime()}]->(cat1)
MERGE (c)-[:COMPETES_IN {created_at: datetime()}]->(cat2);

// Sembo - Construction
MATCH (c:Company {id: 'comp_sembo'}),
      (cat:Category {id: 'cat_construction'})
MERGE (c)-[:COMPETES_IN {created_at: datetime()}]->(cat);

// Enlighten - Construction
MATCH (c:Company {id: 'comp_enlighten'}),
      (cat:Category {id: 'cat_construction'})
MERGE (c)-[:COMPETES_IN {created_at: datetime()}]->(cat);

// Bloks - Construction
MATCH (c:Company {id: 'comp_bloks'}),
      (cat:Category {id: 'cat_construction'})
MERGE (c)-[:COMPETES_IN {created_at: datetime()}]->(cat);

// ============================================
// STEP 5: LINK COMPANIES TO GEOGRAPHIES
// ============================================

// Tencent - China
MATCH (c:Company {id: 'comp_tencent'}),
      (g:Country {id: 'geo_china'})
MERGE (c)-[:OPERATES_IN {since: 1998, created_at: datetime()}]->(g);

// NetEase - China
MATCH (c:Company {id: 'comp_netease'}),
      (g:Country {id: 'geo_china'})
MERGE (c)-[:OPERATES_IN {since: 1997, created_at: datetime()}]->(g);

// miHoYo - China
MATCH (c:Company {id: 'comp_mihoyo'}),
      (g:Country {id: 'geo_china'})
MERGE (c)-[:OPERATES_IN {since: 2012, created_at: datetime()}]->(g);

// LEGO - China (and implicitly Asia Pacific)
MATCH (c:Company {id: 'comp_lego'}),
      (g:Country {id: 'geo_china'})
MERGE (c)-[:OPERATES_IN {created_at: datetime()}]->(g);

// Nintendo - Japan (primary), multiple APAC countries
MATCH (c:Company {id: 'comp_nintendo'}),
      (japan:Country {id: 'geo_japan'})
MERGE (c)-[:OPERATES_IN {since: 1889, created_at: datetime()}]->(japan);

// Sony - Japan, India
MATCH (c:Company {id: 'comp_sony'}),
      (japan:Country {id: 'geo_japan'}),
      (india:Country {id: 'geo_india'})
MERGE (c)-[:OPERATES_IN {created_at: datetime()}]->(japan)
MERGE (c)-[:OPERATES_IN {created_at: datetime()}]->(india);

// Sembo - China
MATCH (c:Company {id: 'comp_sembo'}),
      (g:Country {id: 'geo_china'})
MERGE (c)-[:OPERATES_IN {created_at: datetime()}]->(g);

// Enlighten - China
MATCH (c:Company {id: 'comp_enlighten'}),
      (g:Country {id: 'geo_china'})
MERGE (c)-[:OPERATES_IN {created_at: datetime()}]->(g);

// Bloks - China
MATCH (c:Company {id: 'comp_bloks'}),
      (g:Country {id: 'geo_china'})
MERGE (c)-[:OPERATES_IN {created_at: datetime()}]->(g);

// ============================================
// STEP 6: LINK BRANDS TO CATEGORIES
// ============================================

// PlayStation - Video Games Hardware
MATCH (b:Brand {id: 'brand_playstation'}),
      (cat:Category {id: 'cat_vg_hardware'})
MERGE (b)-[:ASSOCIATED_WITH {created_at: datetime()}]->(cat);

// Nintendo Switch - Video Games Hardware
MATCH (b:Brand {id: 'brand_nintendo_switch'}),
      (cat:Category {id: 'cat_vg_hardware'})
MERGE (b)-[:ASSOCIATED_WITH {created_at: datetime()}]->(cat);

// Pokémon - Games and Puzzles
MATCH (b:Brand {id: 'brand_pokemon'}),
      (cat:Category {id: 'cat_games_puzzles'})
MERGE (b)-[:ASSOCIATED_WITH {created_at: datetime()}]->(cat);

// LEGO - Construction
MATCH (b:Brand {id: 'brand_lego'}),
      (cat:Category {id: 'cat_construction'})
MERGE (b)-[:ASSOCIATED_WITH {created_at: datetime()}]->(cat);

// Genshin Impact - Mobile Games
MATCH (b:Brand {id: 'brand_genshin'}),
      (cat:Category {id: 'cat_mobile_games'})
MERGE (b)-[:ASSOCIATED_WITH {created_at: datetime()}]->(cat);

// Honkai: Star Rail - Mobile Games
MATCH (b:Brand {id: 'brand_honkai'}),
      (cat:Category {id: 'cat_mobile_games'})
MERGE (b)-[:ASSOCIATED_WITH {created_at: datetime()}]->(cat);

// Yu-Gi-Oh! - Games and Puzzles
MATCH (b:Brand {id: 'brand_yugioh'}),
      (cat:Category {id: 'cat_games_puzzles'})
MERGE (b)-[:ASSOCIATED_WITH {created_at: datetime()}]->(cat);

// Duel Masters - Games and Puzzles
MATCH (b:Brand {id: 'brand_duel_masters'}),
      (cat:Category {id: 'cat_games_puzzles'})
MERGE (b)-[:ASSOCIATED_WITH {created_at: datetime()}]->(cat);

// ============================================
// VERIFICATION QUERIES
// ============================================

// Verify all companies:
// MATCH (c:Company) RETURN c.name, c.type, c.primary_market;

// Verify brand ownership:
// MATCH (b:Brand)-[:OWNED_BY]->(c:Company)
// RETURN b.name, c.name;

// Verify company-category relationships:
// MATCH (c:Company)-[:COMPETES_IN]->(cat:Category)
// RETURN c.name, collect(cat.name) as categories;
