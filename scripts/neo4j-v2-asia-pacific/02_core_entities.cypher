// ============================================
// CORE ENTITIES - Geography & Categories
// Euromonitor Asia Pacific Knowledge Graph v2
// ============================================
// Author: Winston (Architect Agent) + Karthikmg
// Date: 2026-01-23
// Source: Toys and Games in Asia Pacific (June 2024)
// ============================================

// ============================================
// STEP 1: CREATE REGION
// ============================================

MERGE (apac:Geography:Region {id: 'geo_asia_pacific'})
SET apac.name = 'Asia Pacific',
    apac.type = 'Region',
    apac.level = 0,
    apac.description = 'Asia Pacific region for Toys and Games market',
    apac.market_position = 'Highest video games sales among 7 global regions',
    apac.data_source = 'Euromonitor International',
    apac.report_date = date('2024-06-01'),
    apac.created_at = datetime(),
    apac.updated_at = datetime();

// ============================================
// STEP 2: CREATE COUNTRIES
// ============================================

// China - Market Leader
MERGE (china:Geography:Country {id: 'geo_china'})
SET china.name = 'China',
    china.iso_code = 'CN',
    china.type = 'Country',
    china.level = 1,
    china.region = 'Asia Pacific',
    china.market_rank = 1,
    china.created_at = datetime(),
    china.updated_at = datetime();

// Japan - Second Largest Market
MERGE (japan:Geography:Country {id: 'geo_japan'})
SET japan.name = 'Japan',
    japan.iso_code = 'JP',
    japan.type = 'Country',
    japan.level = 1,
    japan.region = 'Asia Pacific',
    japan.market_rank = 2,
    japan.created_at = datetime(),
    japan.updated_at = datetime();

// South Korea
MERGE (korea:Geography:Country {id: 'geo_south_korea'})
SET korea.name = 'South Korea',
    korea.iso_code = 'KR',
    korea.type = 'Country',
    korea.level = 1,
    korea.region = 'Asia Pacific',
    korea.market_rank = 3,
    korea.created_at = datetime(),
    korea.updated_at = datetime();

// India - High Growth Market
MERGE (india:Geography:Country {id: 'geo_india'})
SET india.name = 'India',
    india.iso_code = 'IN',
    india.type = 'Country',
    india.level = 1,
    india.region = 'Asia Pacific',
    india.growth_potential = 'high',
    india.created_at = datetime(),
    india.updated_at = datetime();

// Indonesia
MERGE (indonesia:Geography:Country {id: 'geo_indonesia'})
SET indonesia.name = 'Indonesia',
    indonesia.iso_code = 'ID',
    indonesia.type = 'Country',
    indonesia.level = 1,
    indonesia.region = 'Asia Pacific',
    indonesia.growth_potential = 'high',
    indonesia.created_at = datetime(),
    indonesia.updated_at = datetime();

// Thailand
MERGE (thailand:Geography:Country {id: 'geo_thailand'})
SET thailand.name = 'Thailand',
    thailand.iso_code = 'TH',
    thailand.type = 'Country',
    thailand.level = 1,
    thailand.region = 'Asia Pacific',
    thailand.created_at = datetime(),
    thailand.updated_at = datetime();

// Malaysia
MERGE (malaysia:Geography:Country {id: 'geo_malaysia'})
SET malaysia.name = 'Malaysia',
    malaysia.iso_code = 'MY',
    malaysia.type = 'Country',
    malaysia.level = 1,
    malaysia.region = 'Asia Pacific',
    malaysia.created_at = datetime(),
    malaysia.updated_at = datetime();

// Philippines
MERGE (philippines:Geography:Country {id: 'geo_philippines'})
SET philippines.name = 'Philippines',
    philippines.iso_code = 'PH',
    philippines.type = 'Country',
    philippines.level = 1,
    philippines.region = 'Asia Pacific',
    philippines.created_at = datetime(),
    philippines.updated_at = datetime();

// Singapore
MERGE (singapore:Geography:Country {id: 'geo_singapore'})
SET singapore.name = 'Singapore',
    singapore.iso_code = 'SG',
    singapore.type = 'Country',
    singapore.level = 1,
    singapore.region = 'Asia Pacific',
    singapore.created_at = datetime(),
    singapore.updated_at = datetime();

// Taiwan
MERGE (taiwan:Geography:Country {id: 'geo_taiwan'})
SET taiwan.name = 'Taiwan',
    taiwan.iso_code = 'TW',
    taiwan.type = 'Country',
    taiwan.level = 1,
    taiwan.region = 'Asia Pacific',
    taiwan.created_at = datetime(),
    taiwan.updated_at = datetime();

// Hong Kong
MERGE (hongkong:Geography:Country {id: 'geo_hong_kong'})
SET hongkong.name = 'Hong Kong',
    hongkong.iso_code = 'HK',
    hongkong.type = 'Country',
    hongkong.level = 1,
    hongkong.region = 'Asia Pacific',
    hongkong.created_at = datetime(),
    hongkong.updated_at = datetime();

// ============================================
// STEP 3: LINK COUNTRIES TO REGION
// ============================================

MATCH (r:Region {id: 'geo_asia_pacific'}),
      (c:Country)
WHERE c.region = 'Asia Pacific'
MERGE (c)-[:LOCATED_IN {created_at: datetime()}]->(r);

// ============================================
// STEP 4: CREATE CATEGORY TAXONOMY
// ============================================

// Level 0 - Industry
MERGE (industry:Category {id: 'cat_toys_games'})
SET industry.name = 'Toys and Games',
    industry.level = 0,
    industry.parent_id = NULL,
    industry.type = 'Industry',
    industry.created_at = datetime(),
    industry.updated_at = datetime();

// Level 1 - Major Categories
MERGE (traditional:Category {id: 'cat_traditional'})
SET traditional.name = 'Traditional Toys and Games',
    traditional.level = 1,
    traditional.parent_id = 'cat_toys_games',
    traditional.created_at = datetime(),
    traditional.updated_at = datetime();

MERGE (video:Category {id: 'cat_video_games'})
SET video.name = 'Video Games',
    video.level = 1,
    video.parent_id = 'cat_toys_games',
    video.created_at = datetime(),
    video.updated_at = datetime();

// Level 2 - Traditional Subcategories
MERGE (baby:Category {id: 'cat_baby_infant'})
SET baby.name = 'Baby and Infant',
    baby.level = 2,
    baby.parent_id = 'cat_traditional',
    baby.created_at = datetime();

MERGE (action:Category {id: 'cat_action_figures'})
SET action.name = 'Action Figures and Accessories',
    action.level = 2,
    action.parent_id = 'cat_traditional',
    action.created_at = datetime();

MERGE (arts:Category {id: 'cat_arts_crafts'})
SET arts.name = 'Arts and Crafts',
    arts.level = 2,
    arts.parent_id = 'cat_traditional',
    arts.created_at = datetime();

MERGE (construction:Category {id: 'cat_construction'})
SET construction.name = 'Construction',
    construction.level = 2,
    construction.parent_id = 'cat_traditional',
    construction.created_at = datetime();

MERGE (dolls:Category {id: 'cat_dolls'})
SET dolls.name = 'Dolls and Accessories',
    dolls.level = 2,
    dolls.parent_id = 'cat_traditional',
    dolls.created_at = datetime();

MERGE (dressup:Category {id: 'cat_dress_up'})
SET dressup.name = 'Dress-Up and Role Play',
    dressup.level = 2,
    dressup.parent_id = 'cat_traditional',
    dressup.created_at = datetime();

MERGE (games:Category {id: 'cat_games_puzzles'})
SET games.name = 'Games and Puzzles',
    games.level = 2,
    games.parent_id = 'cat_traditional',
    games.created_at = datetime();

MERGE (models:Category {id: 'cat_model_vehicles'})
SET models.name = 'Model Vehicles',
    models.level = 2,
    models.parent_id = 'cat_traditional',
    models.created_at = datetime();

MERGE (outdoor:Category {id: 'cat_outdoor_sports'})
SET outdoor.name = 'Outdoor and Sports',
    outdoor.level = 2,
    outdoor.parent_id = 'cat_traditional',
    outdoor.created_at = datetime();

MERGE (plush:Category {id: 'cat_plush'})
SET plush.name = 'Plush',
    plush.level = 2,
    plush.parent_id = 'cat_traditional',
    plush.created_at = datetime();

MERGE (preschool:Category {id: 'cat_preschool'})
SET preschool.name = 'Pre-School',
    preschool.level = 2,
    preschool.parent_id = 'cat_traditional',
    preschool.created_at = datetime();

MERGE (rc:Category {id: 'cat_remote_control'})
SET rc.name = 'Remote Control Toys',
    rc.level = 2,
    rc.parent_id = 'cat_traditional',
    rc.created_at = datetime();

MERGE (rideon:Category {id: 'cat_ride_on'})
SET rideon.name = 'Ride-On Vehicles',
    rideon.level = 2,
    rideon.parent_id = 'cat_traditional',
    rideon.created_at = datetime();

MERGE (scientific:Category {id: 'cat_scientific'})
SET scientific.name = 'Scientific / Educational',
    scientific.level = 2,
    scientific.parent_id = 'cat_traditional',
    scientific.created_at = datetime();

MERGE (other:Category {id: 'cat_other_traditional'})
SET other.name = 'Other Traditional Toys and Games',
    other.level = 2,
    other.parent_id = 'cat_traditional',
    other.created_at = datetime();

// Level 2 - Video Games Categories
MERGE (hardware:Category {id: 'cat_vg_hardware'})
SET hardware.name = 'Video Games Hardware',
    hardware.level = 2,
    hardware.parent_id = 'cat_video_games',
    hardware.created_at = datetime();

MERGE (software:Category {id: 'cat_vg_software'})
SET software.name = 'Video Games Software',
    software.level = 2,
    software.parent_id = 'cat_video_games',
    software.created_at = datetime();

// Level 3 - Hardware Subcategories
MERGE (handheld:Category {id: 'cat_handheld_consoles'})
SET handheld.name = 'Hand-Held Consoles',
    handheld.level = 3,
    handheld.parent_id = 'cat_vg_hardware',
    handheld.created_at = datetime();

MERGE (static:Category {id: 'cat_static_consoles'})
SET static.name = 'Static Consoles',
    static.level = 3,
    static.parent_id = 'cat_vg_hardware',
    static.created_at = datetime();

MERGE (headsets:Category {id: 'cat_gaming_headsets'})
SET headsets.name = 'Gaming Headsets',
    headsets.level = 3,
    headsets.parent_id = 'cat_vg_hardware',
    headsets.created_at = datetime();

// Level 3 - Software Subcategories
MERGE (mobile:Category {id: 'cat_mobile_games'})
SET mobile.name = 'Mobile Games',
    mobile.level = 3,
    mobile.parent_id = 'cat_vg_software',
    mobile.created_at = datetime();

MERGE (console:Category {id: 'cat_console_games'})
SET console.name = 'Console Games',
    console.level = 3,
    console.parent_id = 'cat_vg_software',
    console.created_at = datetime();

MERGE (computer:Category {id: 'cat_computer_games'})
SET computer.name = 'Computer Games',
    computer.level = 3,
    computer.parent_id = 'cat_vg_software',
    computer.created_at = datetime();

MERGE (online:Category {id: 'cat_online_games'})
SET online.name = 'Online Games and Subscriptions',
    online.level = 3,
    online.parent_id = 'cat_vg_software',
    online.created_at = datetime();

// ============================================
// STEP 5: CREATE CATEGORY HIERARCHY RELATIONSHIPS
// ============================================

// Link Level 1 to Level 0
MATCH (child:Category), (parent:Category)
WHERE child.parent_id = parent.id AND child.level = 1
MERGE (child)-[:BELONGS_TO {created_at: datetime()}]->(parent);

// Link Level 2 to Level 1
MATCH (child:Category), (parent:Category)
WHERE child.parent_id = parent.id AND child.level = 2
MERGE (child)-[:BELONGS_TO {created_at: datetime()}]->(parent);

// Link Level 3 to Level 2
MATCH (child:Category), (parent:Category)
WHERE child.parent_id = parent.id AND child.level = 3
MERGE (child)-[:BELONGS_TO {created_at: datetime()}]->(parent);

// ============================================
// VERIFICATION QUERIES
// ============================================

// Verify all countries created:
// MATCH (c:Country) RETURN c.name, c.iso_code ORDER BY c.market_rank;

// Verify category hierarchy:
// MATCH (c:Category {level: 0})-[:BELONGS_TO*]->(child:Category)
// RETURN c.name, child.name, child.level;

// Verify region relationships:
// MATCH (c:Country)-[:LOCATED_IN]->(r:Region)
// RETURN r.name, count(c) as country_count;
