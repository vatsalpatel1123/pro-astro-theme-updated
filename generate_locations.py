"""
Script to generate all location pages for Long Island Home Buyers website
Based on the great-neck.astro template structure
"""

import os

# Location data with neighborhoods and surrounding areas
LOCATIONS = {
    "manhasset": {
        "name": "Manhasset",
        "coords": "40.7979, -73.6993",
        "neighborhoods": [
            {"name": "Munsey Park", "type": "Village", "desc": "Exclusive residential village with tree-lined streets and prestigious homes. Known for excellent schools and family-friendly atmosphere.", "tags": ["Prestigious", "Top Schools", "Family-Friendly"]},
            {"name": "Plandome", "type": "Village", "desc": "Charming village featuring beautiful homes, manicured lawns, and a strong sense of community. Close to shopping and dining.", "tags": ["Village Charm", "Community", "Shopping"]},
            {"name": "Plandome Heights", "type": "Village", "desc": "Small, upscale village with well-maintained properties and quiet streets. Highly desirable residential area.", "tags": ["Upscale", "Quiet", "Residential"]},
            {"name": "Plandome Manor", "type": "Village", "desc": "Affluent village community with luxury estates and waterfront properties. Excellent schools and low crime.", "tags": ["Luxury", "Waterfront", "Safe"]},
            {"name": "Strathmore", "type": "Village", "desc": "Historic village district with stately homes and mature landscaping. Walking distance to downtown Manhasset.", "tags": ["Historic", "Stately Homes", "Walkable"]},
            {"name": "Flower Hill", "type": "Village", "desc": "Scenic village with rolling hills, large lots, and beautiful estates. Peaceful setting with easy highway access.", "tags": ["Scenic", "Large Lots", "Peaceful"]},
            {"name": "North Strathmore", "type": "Area", "desc": "Northern residential section featuring mid-century homes and family-friendly neighborhoods near schools.", "tags": ["Family Homes", "Schools", "Suburban"]},
            {"name": "Spinney Hill", "type": "Area", "desc": "Established neighborhood with diverse housing stock and excellent proximity to the Americana Manhasset.", "tags": ["Established", "Shopping", "Diverse"]},
            {"name": "Shopper's World Area", "type": "Area", "desc": "Central location near Northern Boulevard shopping and dining. Convenient for commuters and families alike.", "tags": ["Central", "Shopping", "Convenient"]}
        ],
        "surrounding": ["Great Neck", "Port Washington", "Roslyn", "Garden City", "New Hyde Park"],
        "intro": "the heart of the Gold Coast, home to our headquarters and the iconic Americana Manhasset"
    },

    "roslyn": {
        "name": "Roslyn",
        "coords": "40.7998, -73.6509",
        "neighborhoods": [
            {"name": "Roslyn Village", "type": "Village", "desc": "Historic waterfront village with charming downtown, antique shops, and Roslyn Pond. Protected historic district.", "tags": ["Historic", "Waterfront", "Downtown"]},
            {"name": "Roslyn Estates", "type": "Village", "desc": "Upscale residential village featuring luxury homes, excellent schools, and prestigious addresses on the North Shore.", "tags": ["Luxury", "Top Schools", "Prestigious"]},
            {"name": "Roslyn Harbor", "type": "Village", "desc": "Exclusive waterfront village along Hempstead Harbor with stunning water views and estate properties.", "tags": ["Waterfront", "Exclusive", "Harbor Views"]},
            {"name": "Roslyn Heights", "type": "Hamlet", "desc": "Diverse residential community with ranch homes, split-levels, and convenient access to shopping and highways.", "tags": ["Diverse", "Convenient", "Suburban"]},
            {"name": "East Hills", "type": "Village", "desc": "Affluent village community with large estates, rolling terrain, and top-rated schools. Very low density.", "tags": ["Estates", "Top Schools", "Low Density"]},
            {"name": "Harbor Hill", "type": "Area", "desc": "Historic estate area, former site of the Mackay Estate. Now features luxury homes with Long Island Sound views.", "tags": ["Historic", "Luxury", "Sound Views"]},
            {"name": "Old Northern Boulevard", "type": "Area", "desc": "Established neighborhood along historic Route 25A with mature trees and classic Long Island architecture.", "tags": ["Established", "Mature Trees", "Historic"]},
            {"name": "Roslyn Country Club Area", "type": "Area", "desc": "Residential neighborhood surrounding the historic Roslyn Country Club. Prestigious location with large properties.", "tags": ["Country Club", "Prestigious", "Large Lots"]}
        ],
        "surrounding": ["Manhasset", "Port Washington", "Greenvale", "East Hills", "Great Neck"],
        "intro": "a historic Gold Coast village known for its charming downtown, waterfront location, and prestigious estates"
    },

    "port-washington": {
        "name": "Port Washington",
        "coords": "40.8257, -73.6982",
        "neighborhoods": [
            {"name": "Sands Point", "type": "Village", "desc": "Ultra-exclusive waterfront village with multi-million dollar estates, private beaches, and stunning Long Island Sound views.", "tags": ["Ultra-Luxury", "Waterfront", "Private Beaches"]},
            {"name": "Port Washington North", "type": "Village", "desc": "Prestigious waterfront village featuring luxury homes, marinas, and direct water access. Highly desirable location.", "tags": ["Waterfront", "Luxury", "Marina Access"]},
            {"name": "Manorhaven", "type": "Village", "desc": "Waterfront village community with diverse housing stock, beach access, and strong sense of community along the harbor.", "tags": ["Waterfront", "Community", "Beach Access"]},
            {"name": "Baxter Estates", "type": "Village", "desc": "Small, exclusive waterfront village with beautiful homes and direct access to Manhasset Bay. Very low density.", "tags": ["Exclusive", "Waterfront", "Low Density"]},
            {"name": "Flower Hill (PW)", "type": "Village", "desc": "Scenic village section in Port Washington with rolling hills, large estates, and excellent school access.", "tags": ["Scenic", "Estates", "Top Schools"]},
            {"name": "Main Street District", "type": "Area", "desc": "Vibrant downtown area with shops, restaurants, and the LIRR station. Walkable urban village atmosphere.", "tags": ["Downtown", "LIRR", "Walkable"]},
            {"name": "Beacon Hill", "type": "Area", "desc": "Established residential neighborhood on elevated terrain offering water views and proximity to town amenities.", "tags": ["Water Views", "Established", "Convenient"]},
            {"name": "Soundview", "type": "Area", "desc": "Waterfront residential area with beach access, marinas, and stunning Long Island Sound views. Active boating community.", "tags": ["Waterfront", "Boating", "Sound Views"]},
            {"name": "Harbor Acres", "type": "Area", "desc": "Family-friendly neighborhood with mid-century homes, good schools, and easy access to beaches and downtown.", "tags": ["Family-Friendly", "Beaches", "Schools"]}
        ],
        "surrounding": ["Manhasset", "Great Neck", "Sands Point", "Roslyn", "Kings Point"],
        "intro": "a vibrant waterfront community on the Manhasset Bay with excellent schools, beaches, and a charming downtown"
    },

    "glen-cove": {
        "name": "Glen Cove",
        "coords": "40.8623, -73.6340",
        "neighborhoods": [
            {"name": "The Village", "type": "Area", "desc": "Historic downtown core with the Gold Coast Arts Center, City Hall, and charming shopping district. Walkable urban center.", "tags": ["Downtown", "Historic", "Walkable"]},
            {"name": "The Landing", "type": "Area", "desc": "Waterfront development featuring condos, townhomes, and amenities along Hempstead Harbor. Modern living with water views.", "tags": ["Waterfront", "Modern", "Harbor Views"]},
            {"name": "Garvies Point", "type": "Area", "desc": "Scenic peninsula location near the Garvies Point Museum and Preserve. Natural beauty with waterfront access.", "tags": ["Waterfront", "Nature", "Scenic"]},
            {"name": "North Shore", "type": "Area", "desc": "Upscale residential section along the Long Island Sound with estate properties and private beaches.", "tags": ["Upscale", "Sound Views", "Estates"]},
            {"name": "Glen Cove Heights", "type": "Area", "desc": "Elevated residential neighborhood offering water views, established homes, and proximity to downtown amenities.", "tags": ["Water Views", "Established", "Convenient"]},
            {"name": "Glen Head Border", "type": "Area", "desc": "Southern residential section bordering Glen Head, featuring suburban homes and excellent school access.", "tags": ["Suburban", "Schools", "Family-Friendly"]},
            {"name": "Dosoris Island", "type": "Area", "desc": "Exclusive peninsula neighborhood with waterfront estates, private beaches, and gated community atmosphere.", "tags": ["Exclusive", "Waterfront", "Gated"]},
            {"name": "Brewster Woods", "type": "Area", "desc": "Established neighborhood with tree-lined streets, mid-century homes, and strong community connections.", "tags": ["Established", "Trees", "Community"]}
        ],
        "surrounding": ["Sea Cliff", "Glen Head", "Locust Valley", "Oyster Bay", "Greenvale"],
        "intro": "a historic Gold Coast city with a revitalized waterfront, charming downtown, and diverse neighborhoods"
    },

    "glen-head": {
        "name": "Glen Head",
        "coords": "40.8392, -73.6218",
        "neighborhoods": [
            {"name": "Village Center", "type": "Area", "desc": "Central hamlet area near the LIRR station with convenient shopping and dining. Easy commuter access to NYC.", "tags": ["LIRR", "Shopping", "Convenient"]},
            {"name": "Duck Pond Road", "type": "Area", "desc": "Established residential section with well-maintained homes, mature landscaping, and family-friendly streets.", "tags": ["Established", "Family-Friendly", "Mature Trees"]},
            {"name": "Glen Head Heights", "type": "Area", "desc": "Elevated neighborhood offering scenic views, larger lots, and proximity to top-rated North Shore schools.", "tags": ["Scenic", "Large Lots", "Top Schools"]},
            {"name": "Cedar Swamp Road", "type": "Area", "desc": "Rural-suburban section with larger properties, country atmosphere, and horse-friendly zoning in some areas.", "tags": ["Rural", "Large Properties", "Country"]},
            {"name": "Old Tappan Road", "type": "Area", "desc": "Quiet residential area with diverse housing stock and excellent connectivity to Glen Cove and Greenvale.", "tags": ["Quiet", "Diverse", "Convenient"]},
            {"name": "North Glen Head", "type": "Area", "desc": "Northern section bordering Glen Cove with suburban homes, good schools, and community amenities.", "tags": ["Suburban", "Schools", "Community"]},
            {"name": "Stony Hill Road", "type": "Area", "desc": "Scenic route through Glen Head featuring estate properties, rolling terrain, and natural beauty.", "tags": ["Scenic", "Estates", "Rolling Hills"]}
        ],
        "surrounding": ["Glen Cove", "Sea Cliff", "Greenvale", "Old Brookville", "Oyster Bay"],
        "intro": "a charming North Shore hamlet known for excellent schools, convenient LIRR access, and suburban tranquility"
    },

    "sands-point": {
        "name": "Sands Point",
        "coords": "40.8501, -73.7174",
        "neighborhoods": [
            {"name": "Sands Point Village", "type": "Village", "desc": "Ultra-exclusive waterfront village with historic Gold Coast estates, private beaches, and stunning Long Island Sound views.", "tags": ["Ultra-Luxury", "Historic", "Waterfront"]},
            {"name": "Port Washington Peninsula", "type": "Area", "desc": "Northern peninsula featuring multi-million dollar waterfront properties with private docks and beach access.", "tags": ["Waterfront", "Private Docks", "Luxury"]},
            {"name": "Beacon Hill Area", "type": "Area", "desc": "Elevated estates with panoramic water views, gated properties, and mature landscaping. Maximum privacy.", "tags": ["Estates", "Water Views", "Gated"]},
            {"name": "Sands Point Preserve", "type": "Area", "desc": "Historic area near the 216-acre preserve, featuring former Gold Coast mansions and nature trails.", "tags": ["Historic", "Nature", "Prestigious"]},
            {"name": "Lighthouse Road", "type": "Area", "desc": "Exclusive waterfront street leading to Sands Point Lighthouse, with spectacular estate properties.", "tags": ["Waterfront", "Exclusive", "Estates"]},
            {"name": "Middle Neck Road Estates", "type": "Area", "desc": "Grand properties along the main thoroughfare, featuring classical architecture and extensive grounds.", "tags": ["Grand Estates", "Architecture", "Large Lots"]},
            {"name": "Sound View Estates", "type": "Area", "desc": "Premium waterfront homes with direct Long Island Sound access, private beaches, and sunset views.", "tags": ["Waterfront", "Sound Access", "Views"]}
        ],
        "surrounding": ["Port Washington", "Manhasset", "Great Neck", "Kings Point", "Manorhaven"],
        "intro": "one of Long Island's most prestigious Gold Coast villages with historic estates, private beaches, and unparalleled waterfront living"
    },

    "old-brookville": {
        "name": "Old Brookville",
        "coords": "40.8198, -73.6009",
        "neighborhoods": [
            {"name": "Whitney Lane Estates", "type": "Area", "desc": "Ultra-exclusive estate area with multi-acre properties, horse farms, and complete privacy. Among LI's most expensive.", "tags": ["Ultra-Luxury", "Horse Farms", "Multi-Acre"]},
            {"name": "Cedar Swamp Area", "type": "Area", "desc": "Rural estate section with rolling terrain, mature forests, and grand properties. Country atmosphere.", "tags": ["Rural Estates", "Rolling Hills", "Privacy"]},
            {"name": "Brookville Road Estates", "type": "Area", "desc": "Historic Gold Coast section with former Gilded Age estates, now private residences with extensive grounds.", "tags": ["Historic", "Gilded Age", "Large Estates"]},
            {"name": "Northern Boulevard Estates", "type": "Area", "desc": "Prestigious properties along historic Route 25A, featuring gated entrances and exceptional privacy.", "tags": ["Prestigious", "Gated", "Private"]},
            {"name": "Piping Rock Area", "type": "Area", "desc": "Elite neighborhood near the historic Piping Rock Club, featuring estate homes and equestrian facilities.", "tags": ["Elite", "Equestrian", "Club Proximity"]},
            {"name": "Old Brookville Center", "type": "Area", "desc": "Village center area with larger estate properties, excellent schools, and serene country setting.", "tags": ["Estate Properties", "Top Schools", "Serene"]},
            {"name": "South Woods", "type": "Area", "desc": "Wooded estate section with maximum privacy, mature trees, and some of the island's finest properties.", "tags": ["Wooded", "Maximum Privacy", "Finest Properties"]}
        ],
        "surrounding": ["Brookville", "Glen Head", "Roslyn", "Old Westbury", "Locust Valley"],
        "intro": "an ultra-exclusive Gold Coast village renowned for sprawling estates, horse country, and unmatched privacy"
    },

    "old-westbury": {
        "name": "Old Westbury",
        "coords": "40.7887, -73.5993",
        "neighborhoods": [
            {"name": "The Village Center", "type": "Village", "desc": "Historic Gold Coast village with Old Westbury Gardens, NYIT campus, and exceptional estate properties.", "tags": ["Historic", "Gardens", "Prestigious"]},
            {"name": "Wheatley Road Estates", "type": "Area", "desc": "Grand boulevard featuring some of Long Island's finest estates, mature trees, and exceptional privacy.", "tags": ["Grand Estates", "Boulevard", "Privacy"]},
            {"name": "Post Road Area", "type": "Area", "desc": "Historic area with Gilded Age pedigree, large properties, and proximity to Old Westbury Gardens.", "tags": ["Gilded Age", "Large Properties", "Historic"]},
            {"name": "SUNY Old Westbury Area", "type": "Area", "desc": "Section near the state university campus, featuring estate homes on former Gold Coast property.", "tags": ["Estates", "Campus Proximity", "Quiet"]},
            {"name": "Jericho Turnpike Estates", "type": "Area", "desc": "Southern section with excellent highway access, estate properties, and top-rated schools.", "tags": ["Highway Access", "Estates", "Top Schools"]},
            {"name": "North Woods", "type": "Area", "desc": "Heavily wooded estate area offering maximum seclusion, mature landscaping, and grand homes.", "tags": ["Wooded", "Seclusion", "Grand Homes"]},
            {"name": "Glen Cove Road Section", "type": "Area", "desc": "Prestigious corridor with gated estates, equestrian facilities, and old-world charm.", "tags": ["Gated", "Equestrian", "Old-World"]}
        ],
        "surrounding": ["Brookville", "Jericho", "Westbury", "Roslyn Heights", "East Hills"],
        "intro": "a prestigious Gold Coast village home to Old Westbury Gardens and some of Long Island's most magnificent estates"
    },

    "brookville": {
        "name": "Brookville",
        "coords": "40.8142, -73.5698",
        "neighborhoods": [
            {"name": "Upper Brookville", "type": "Village", "desc": "Incorporated village section with strict zoning, large minimum lot sizes, and exceptional estate properties.", "tags": ["Strict Zoning", "Large Lots", "Estates"]},
            {"name": "Muttontown Preserve Area", "type": "Area", "desc": "Bordering the 550-acre nature preserve, featuring equestrian estates and natural beauty.", "tags": ["Nature Preserve", "Equestrian", "Natural Beauty"]},
            {"name": "Wolver Hollow Road", "type": "Area", "desc": "Exclusive street with grand estates, mature landscaping, and complete privacy. Horse country atmosphere.", "tags": ["Exclusive", "Estates", "Horse Country"]},
            {"name": "Chicken Valley Road", "type": "Area", "desc": "Prestigious rural road with large estates, rolling hills, and country living. Very private.", "tags": ["Rural", "Rolling Hills", "Private"]},
            {"name": "Cedar Swamp Woods", "type": "Area", "desc": "Wooded estate section with natural beauty, wildlife, and some of the area's finest properties.", "tags": ["Wooded", "Wildlife", "Finest Properties"]},
            {"name": "Northern Boulevard Section", "type": "Area", "desc": "Historic corridor with Gilded Age heritage, gated properties, and exceptional estates.", "tags": ["Historic", "Gated", "Exceptional"]},
            {"name": "Brookville Center", "type": "Area", "desc": "Village center area near the Old Brookville Library and community amenities. Estate homes.", "tags": ["Village Center", "Community", "Estates"]}
        ],
        "surrounding": ["Old Brookville", "Upper Brookville", "Muttontown", "Oyster Bay Cove", "Laurel Hollow"],
        "intro": "an elite Gold Coast community known for sprawling estates, equestrian facilities, and preserved natural beauty"
    },

    # Nassau County Central Locations
    "garden-city": {
        "name": "Garden City",
        "coords": "40.7268, -73.6343",
        "neighborhoods": [
            {"name": "Cathedral Area", "type": "Area", "desc": "Historic village center near the Cathedral of the Incarnation, featuring tree-lined streets and classic architecture.", "tags": ["Historic", "Cathedral", "Tree-Lined"]},
            {"name": "Garden City Park", "type": "Hamlet", "desc": "Northern section with diverse housing, convenient shopping, and excellent school access. Family-friendly community.", "tags": ["Family-Friendly", "Shopping", "Schools"]},
            {"name": "Stewart Manor Border", "type": "Area", "desc": "Western residential section with well-maintained homes, quiet streets, and strong sense of community.", "tags": ["Quiet", "Community", "Well-Maintained"]},
            {"name": "Adelphi University Area", "type": "Area", "desc": "Central location near the university campus, featuring stately homes and beautiful landscaping.", "tags": ["University", "Stately Homes", "Beautiful"]},
            {"name": "Franklin Avenue District", "type": "Area", "desc": "Upscale shopping district with convenient access to restaurants, boutiques, and village amenities.", "tags": ["Shopping", "Upscale", "Convenient"]},
            {"name": "South Garden City", "type": "Area", "desc": "Southern residential section with larger homes, excellent schools, and proximity to Hempstead Turnpike.", "tags": ["Larger Homes", "Schools", "Accessible"]},
            {"name": "Meadow Drive Area", "type": "Area", "desc": "Prestigious section featuring beautiful estates, manicured lawns, and exceptional properties.", "tags": ["Prestigious", "Estates", "Manicured"]},
            {"name": "Nassau Boulevard Section", "type": "Area", "desc": "Eastern corridor with classic Garden City homes, tree-canopied streets, and village charm.", "tags": ["Classic", "Tree-Canopied", "Charming"]},
            {"name": "Clinton Road Area", "type": "Area", "desc": "Quiet residential neighborhood with well-established homes and convenient village access.", "tags": ["Quiet", "Established", "Village Access"]}
        ],
        "surrounding": ["Mineola", "Westbury", "Hempstead", "East Garden City", "Uniondale"],
        "intro": "a prestigious planned village known for tree-lined streets, top-rated schools, and timeless architecture"
    },

    "mineola": {
        "name": "Mineola",
        "coords": "40.7495, -73.6407",
        "neighborhoods": [
            {"name": "Mineola Village", "type": "Village", "desc": "Downtown core with LIRR hub, Nassau County Courthouse, shops, and restaurants. Urban village atmosphere.", "tags": ["LIRR Hub", "Downtown", "Urban Village"]},
            {"name": "Willis Avenue Area", "type": "Area", "desc": "Residential section near Winthrop Hospital with diverse housing and convenient access to amenities.", "tags": ["Hospital Proximity", "Diverse", "Convenient"]},
            {"name": "Herricks Border", "type": "Area", "desc": "Northern section bordering the Herricks school district, featuring suburban homes and family-friendly streets.", "tags": ["Herricks Schools", "Suburban", "Family-Friendly"]},
            {"name": "Jericho Turnpike Corridor", "type": "Area", "desc": "Commercial and residential mix along Route 25, offering shopping, dining, and easy highway access.", "tags": ["Commercial", "Shopping", "Highway Access"]},
            {"name": "East Mineola", "type": "Area", "desc": "Eastern residential section with established neighborhoods, good schools, and community parks.", "tags": ["Established", "Schools", "Parks"]},
            {"name": "Roslyn Road Area", "type": "Area", "desc": "Western section with tree-lined residential streets, proximity to downtown, and walkable amenities.", "tags": ["Tree-Lined", "Walkable", "Downtown Access"]},
            {"name": "Mineola Boulevard", "type": "Area", "desc": "Main thoroughfare featuring diverse housing stock, convenient shopping, and excellent connectivity.", "tags": ["Diverse", "Shopping", "Connected"]}
        ],
        "surrounding": ["Garden City", "Westbury", "Williston Park", "East Williston", "Carle Place"],
        "intro": "a vibrant village and Nassau County seat with excellent LIRR access, diverse neighborhoods, and urban convenience"
    },

    "westbury": {
        "name": "Westbury",
        "coords": "40.7557, -73.5876",
        "neighborhoods": [
            {"name": "Westbury Village", "type": "Village", "desc": "Historic village center with charming downtown, LIRR station, and diverse community. Walkable and convenient.", "tags": ["Historic", "LIRR", "Walkable"]},
            {"name": "New Cassel Border", "type": "Area", "desc": "Northern section with affordable housing options, diverse community, and good school access.", "tags": ["Affordable", "Diverse", "Schools"]},
            {"name": "Salisbury Area", "type": "Area", "desc": "Upscale section near Eisenhower Park featuring larger homes, excellent schools, and family amenities.", "tags": ["Upscale", "Large Homes", "Park Access"]},
            {"name": "Old Westbury Border", "type": "Area", "desc": "Southern section bordering the Gold Coast village, featuring estate-style properties and prestigious addresses.", "tags": ["Estate Properties", "Prestigious", "Border Area"]},
            {"name": "Post Avenue District", "type": "Area", "desc": "Main commercial corridor with shopping, dining, and entertainment including the NYCB Theatre.", "tags": ["Commercial", "Entertainment", "Dining"]},
            {"name": "Carle Place Border", "type": "Area", "desc": "Western residential section with suburban homes, convenient shopping, and highway access.", "tags": ["Suburban", "Shopping", "Highway Access"]},
            {"name": "Westbury South", "type": "Area", "desc": "Southern residential neighborhoods with diverse housing, good schools, and community parks.", "tags": ["Diverse Housing", "Community", "Parks"]},
            {"name": "East Westbury", "type": "Area", "desc": "Eastern section with established neighborhoods, mature trees, and proximity to retail centers.", "tags": ["Established", "Mature Trees", "Retail Access"]}
        ],
        "surrounding": ["Carle Place", "Old Westbury", "New Cassel", "Salisbury", "East Meadow"],
        "intro": "a diverse and vibrant village featuring excellent LIRR access, Eisenhower Park, and the NYCB Theatre at Westbury"
    },

    "hicksville": {
        "name": "Hicksville",
        "coords": "40.7684, -73.5251",
        "neighborhoods": [
            {"name": "Old Country Road Area", "type": "Area", "desc": "Central commercial corridor with shopping, dining, and Broadway Mall. Excellent retail access.", "tags": ["Shopping", "Broadway Mall", "Retail"]},
            {"name": "Hicksville LIRR District", "type": "Area", "desc": "Downtown area near the LIRR station with diverse housing and excellent NYC commuter access.", "tags": ["LIRR", "Downtown", "Commuter Friendly"]},
            {"name": "North Hicksville", "type": "Area", "desc": "Northern residential section with suburban homes, good schools, and family-friendly neighborhoods.", "tags": ["Suburban", "Family-Friendly", "Schools"]},
            {"name": "South Hicksville", "type": "Area", "desc": "Southern section with diverse housing stock, convenient shopping, and community amenities.", "tags": ["Diverse", "Shopping", "Community"]},
            {"name": "West Hicksville", "type": "Area", "desc": "Western neighborhoods bordering Plainview, featuring larger lots and excellent school access.", "tags": ["Larger Lots", "Schools", "Quiet"]},
            {"name": "East Hicksville", "type": "Area", "desc": "Eastern section with established neighborhoods, mature landscaping, and convenient highway access.", "tags": ["Established", "Mature", "Highway Access"]},
            {"name": "Burns Park Area", "type": "Area", "desc": "Residential section near recreational facilities, featuring family homes and active community.", "tags": ["Recreation", "Family Homes", "Active Community"]},
            {"name": "Newbridge Road Corridor", "type": "Area", "desc": "Major thoroughfare with mixed residential and commercial properties, excellent connectivity.", "tags": ["Mixed Use", "Connected", "Convenient"]}
        ],
        "surrounding": ["Plainview", "Jericho", "Levittown", "Bethpage", "Westbury"],
        "intro": "a bustling Long Island hamlet known for Broadway Commons, diverse community, and excellent LIRR connectivity"
    },

    "jericho": {
        "name": "Jericho",
        "coords": "40.7923, -73.5401",
        "neighborhoods": [
            {"name": "North Jericho", "type": "Area", "desc": "Northern section near Syosset border, featuring larger homes, top-rated schools, and low crime.", "tags": ["Top Schools", "Safe", "Larger Homes"]},
            {"name": "Jericho Turnpike Corridor", "type": "Area", "desc": "Historic Route 25 featuring convenient shopping, dining, and excellent highway access.", "tags": ["Shopping", "Historic Route", "Highway Access"]},
            {"name": "Cantiague Park Area", "type": "Area", "desc": "Western section near the 127-acre park, featuring family homes and exceptional recreation.", "tags": ["Park Access", "Recreation", "Family Homes"]},
            {"name": "South Jericho", "type": "Area", "desc": "Southern residential section with excellent schools, suburban homes, and community amenities.", "tags": ["Excellent Schools", "Suburban", "Community"]},
            {"name": "Merry Lane Area", "type": "Area", "desc": "Established neighborhood with well-maintained homes, mature landscaping, and quiet streets.", "tags": ["Established", "Mature Trees", "Quiet"]},
            {"name": "East Jericho", "type": "Area", "desc": "Eastern section bordering Hicksville, featuring diverse housing and convenient shopping access.", "tags": ["Diverse", "Shopping", "Convenient"]},
            {"name": "Broadway Jericho", "type": "Area", "desc": "Western corridor with excellent school access, larger properties, and sought-after addresses.", "tags": ["Excellent Schools", "Larger Properties", "Sought-After"]}
        ],
        "surrounding": ["Syosset", "Woodbury", "Hicksville", "Plainview", "Old Westbury"],
        "intro": "a highly sought-after hamlet renowned for top-rated Jericho schools, safe neighborhoods, and suburban excellence"
    },

    "syosset": {
        "name": "Syosset",
        "coords": "40.8262, -73.5021",
        "neighborhoods": [
            {"name": "Syosset Village", "type": "Hamlet", "desc": "Central area near LIRR station with shopping, dining, and excellent commuter access to NYC.", "tags": ["LIRR", "Shopping", "Commuter Access"]},
            {"name": "Syosset Park Estates", "type": "Village", "desc": "Incorporated village with strict zoning, larger homes, and top-rated Syosset schools. Very desirable.", "tags": ["Incorporated", "Top Schools", "Larger Homes"]},
            {"name": "Muttontown Estates", "type": "Area", "desc": "High-end section bordering Muttontown Preserve, featuring luxury homes and natural beauty.", "tags": ["Luxury", "Nature Preserve", "High-End"]},
            {"name": "Split Rock Golf Area", "type": "Area", "desc": "Prestigious neighborhood near the historic golf club, featuring beautiful estates and mature landscaping.", "tags": ["Golf Club", "Estates", "Prestigious"]},
            {"name": "North Syosset", "type": "Area", "desc": "Northern residential section with excellent schools, safe streets, and family-friendly atmosphere.", "tags": ["Top Schools", "Safe", "Family-Friendly"]},
            {"name": "South Syosset", "type": "Area", "desc": "Southern section with diverse housing, convenient shopping, and excellent school access.", "tags": ["Diverse", "Shopping", "Schools"]},
            {"name": "Woodbury Border", "type": "Area", "desc": "Western section bordering corporate parks, featuring upscale homes and modern amenities.", "tags": ["Upscale", "Corporate Proximity", "Modern"]},
            {"name": "Berry Hill Area", "type": "Area", "desc": "Exclusive section with custom homes, rolling terrain, and maximum privacy. Highly sought-after.", "tags": ["Exclusive", "Custom Homes", "Privacy"]}
        ],
        "surrounding": ["Jericho", "Woodbury", "Plainview", "Cold Spring Harbor", "Oyster Bay"],
        "intro": "an affluent North Shore hamlet celebrated for top-rated schools, beautiful neighborhoods, and convenient LIRR access"
    },

    "plainview": {
        "name": "Plainview",
        "coords": "40.7765, -73.4673",
        "neighborhoods": [
            {"name": "Old Bethpage Border", "type": "Area", "desc": "Western section near the historic village restoration, featuring larger lots and suburban tranquility.", "tags": ["Historic Proximity", "Larger Lots", "Tranquil"]},
            {"name": "Central Plainview", "type": "Area", "desc": "Core residential area with diverse housing, excellent Plainview-Old Bethpage schools, and community parks.", "tags": ["Schools", "Diverse", "Parks"]},
            {"name": "North Plainview", "type": "Area", "desc": "Northern section with well-maintained ranch and split-level homes, quiet streets, and family atmosphere.", "tags": ["Ranch Homes", "Quiet", "Family-Friendly"]},
            {"name": "South Plainview", "type": "Area", "desc": "Southern residential neighborhoods with mature trees, established community, and convenient shopping.", "tags": ["Mature Trees", "Established", "Shopping"]},
            {"name": "Manetto Hill Area", "type": "Area", "desc": "Elevated section with scenic views, excellent schools, and safe, family-oriented neighborhoods.", "tags": ["Scenic", "Top Schools", "Safe"]},
            {"name": "Woodbury Border", "type": "Area", "desc": "Eastern section near corporate parks, featuring convenient highway access and modern amenities.", "tags": ["Highway Access", "Corporate Proximity", "Convenient"]},
            {"name": "Pasadena Drive Area", "type": "Area", "desc": "Established neighborhood with well-kept homes, strong community spirit, and excellent school access.", "tags": ["Established", "Community Spirit", "Schools"]},
            {"name": "Washington Avenue District", "type": "Area", "desc": "Central corridor with shopping, dining, and easy access to all Plainview amenities.", "tags": ["Shopping", "Dining", "Central"]}
        ],
        "surrounding": ["Old Bethpage", "Hicksville", "Jericho", "Syosset", "Woodbury"],
        "intro": "a family-friendly suburban hamlet known for excellent schools, safe neighborhoods, and convenient mid-Island location"
    },

    "woodbury": {
        "name": "Woodbury",
        "coords": "40.8156, -73.4718",
        "neighborhoods": [
            {"name": "Woodbury Village", "type": "Village", "desc": "Incorporated village with strict zoning, estate properties, and excellent schools. Very low density.", "tags": ["Incorporated", "Estate Properties", "Low Density"]},
            {"name": "Corporate Park Area", "type": "Area", "desc": "Business district near major corporate headquarters including Canon and Estée Lauder. Modern development.", "tags": ["Corporate", "Modern", "Business"]},
            {"name": "North Woodbury Estates", "type": "Area", "desc": "Northern section with luxury homes, rolling terrain, and top-rated Syosset schools.", "tags": ["Luxury", "Rolling Hills", "Top Schools"]},
            {"name": "South Woodbury", "type": "Area", "desc": "Southern residential section with upscale homes, excellent schools, and low crime rates.", "tags": ["Upscale", "Schools", "Safe"]},
            {"name": "Syosset-Woodbury Border", "type": "Area", "desc": "Eastern section with access to both Syosset and Jericho schools, featuring diverse upscale housing.", "tags": ["School Choice", "Upscale", "Diverse"]},
            {"name": "Crossways Park Area", "type": "Area", "desc": "Commercial section near the park and office complex, offering convenient shopping and services.", "tags": ["Commercial", "Shopping", "Services"]},
            {"name": "Woodbury Country Club Area", "type": "Area", "desc": "Prestigious neighborhood near the country club, featuring custom estates and golf course living.", "tags": ["Country Club", "Estates", "Prestigious"]}
        ],
        "surrounding": ["Syosset", "Plainview", "Jericho", "Huntington", "Cold Spring Harbor"],
        "intro": "an upscale incorporated village featuring estate homes, top-rated schools, and major corporate headquarters"
    },

    "melville": {
        "name": "Melville",
        "coords": "40.7934, -73.4151",
        "neighborhoods": [
            {"name": "Corporate Center", "type": "Area", "desc": "Major business district home to corporate headquarters, office parks, and commercial development.", "tags": ["Corporate", "Business District", "Commercial"]},
            {"name": "Walt Whitman Shops Area", "type": "Area", "desc": "Upscale shopping district featuring high-end retail, dining, and entertainment venues.", "tags": ["Upscale Shopping", "Dining", "Entertainment"]},
            {"name": "North Melville", "type": "Area", "desc": "Northern residential section with executive homes, excellent schools, and proximity to corporate parks.", "tags": ["Executive Homes", "Schools", "Corporate Proximity"]},
            {"name": "Melville South", "type": "Area", "desc": "Southern section with diverse housing, convenient highway access, and family-friendly neighborhoods.", "tags": ["Diverse", "Highway Access", "Family-Friendly"]},
            {"name": "Sweet Hollow Road Area", "type": "Area", "desc": "Scenic corridor with upscale homes, natural beauty, and excellent Halfhollow Hills schools.", "tags": ["Scenic", "Upscale", "Top Schools"]},
            {"name": "Chichester Area", "type": "Area", "desc": "Established neighborhood with well-maintained homes, convenient shopping, and strong community.", "tags": ["Established", "Shopping", "Community"]},
            {"name": "Northern State Corridor", "type": "Area", "desc": "Easily accessible area near the parkway, featuring modern housing and excellent connectivity.", "tags": ["Highway Access", "Modern", "Connected"]}
        ],
        "surrounding": ["Huntington Station", "Dix Hills", "Farmingdale", "Plainview", "Half Hollow Hills"],
        "intro": "a bustling corporate hub and shopping destination featuring upscale amenities, excellent schools, and modern development"
    },

    # Nassau County Southern Locations
    "levittown": {
        "name": "Levittown",
        "coords": "40.7259, -73.5143",
        "neighborhoods": [
            {"name": "Island Trees", "type": "Hamlet", "desc": "Northern section with excellent Island Trees schools, diverse community, and family-friendly atmosphere.", "tags": ["Island Trees Schools", "Family-Friendly", "Community"]},
            {"name": "Central Levittown", "type": "Area", "desc": "Historic planned community with classic ranch homes, tree-lined streets, and strong community spirit.", "tags": ["Historic", "Ranch Homes", "Community Spirit"]},
            {"name": "Wantagh Parkway Area", "type": "Area", "desc": "Southern section with convenient parkway access, diverse housing, and proximity to beaches.", "tags": ["Parkway Access", "Diverse", "Beach Proximity"]},
            {"name": "Division Avenue District", "type": "Area", "desc": "Commercial corridor with shopping, dining, and services. Convenient for residents.", "tags": ["Shopping", "Dining", "Convenient"]},
            {"name": "North Levittown", "type": "Area", "desc": "Northern residential section with well-maintained homes, excellent schools, and family atmosphere.", "tags": ["Well-Maintained", "Schools", "Family"]},
            {"name": "South Levittown", "type": "Area", "desc": "Southern section with classic Levittown architecture, established community, and convenient amenities.", "tags": ["Classic", "Established", "Amenities"]},
            {"name": "Memorial Park Area", "type": "Area", "desc": "Central section near community park and pool, featuring active recreation and family homes.", "tags": ["Park", "Recreation", "Active Community"]}
        ],
        "surrounding": ["Wantagh", "Bethpage", "Hicksville", "Seaford", "East Meadow"],
        "intro": "America's first planned suburban community, featuring classic ranch homes, strong community spirit, and family-friendly neighborhoods"
    },

    "wantagh": {
        "name": "Wantagh",
        "coords": "40.6837, -73.5101",
        "neighborhoods": [
            {"name": "Wantagh Village", "type": "Hamlet", "desc": "Central hamlet area near LIRR station with convenient shopping, dining, and excellent schools.", "tags": ["LIRR", "Shopping", "Schools"]},
            {"name": "Jones Beach Area", "type": "Area", "desc": "Southern section near the iconic Jones Beach, featuring beach proximity and summer atmosphere.", "tags": ["Beach Proximity", "Jones Beach", "Summer"]},
            {"name": "Wantagh Park Area", "type": "Area", "desc": "Waterfront section near the park and marina, offering boating, fishing, and water activities.", "tags": ["Waterfront", "Marina", "Boating"]},
            {"name": "North Wantagh", "type": "Area", "desc": "Northern residential section with suburban homes, top-rated Wantagh schools, and family community.", "tags": ["Suburban", "Top Schools", "Family"]},
            {"name": "South Wantagh", "type": "Area", "desc": "Southern neighborhoods closer to the water, featuring diverse housing and beach town atmosphere.", "tags": ["Beach Town", "Diverse", "Water Access"]},
            {"name": "Sunrise Highway Corridor", "type": "Area", "desc": "Commercial corridor with shopping centers, dining, and excellent highway connectivity.", "tags": ["Shopping", "Dining", "Highway Access"]},
            {"name": "Twin Lakes Area", "type": "Area", "desc": "Scenic neighborhood near Twin Lakes Preserve, offering nature trails and waterfront access.", "tags": ["Scenic", "Nature", "Waterfront"]}
        ],
        "surrounding": ["Seaford", "Levittown", "Bellmore", "Merrick", "Massapequa"],
        "intro": "a vibrant South Shore hamlet known for Jones Beach proximity, excellent schools, and strong community spirit"
    },

    "massapequa": {
        "name": "Massapequa",
        "coords": "40.6807, -73.4740",
        "neighborhoods": [
            {"name": "Massapequa Park", "type": "Village", "desc": "Incorporated village with charming downtown, LIRR station, and walkable village atmosphere.", "tags": ["Village", "LIRR", "Walkable"]},
            {"name": "North Massapequa", "type": "Hamlet", "desc": "Northern section with excellent schools, suburban homes, and family-friendly neighborhoods.", "tags": ["Schools", "Suburban", "Family-Friendly"]},
            {"name": "South Massapequa", "type": "Area", "desc": "Southern section near the Great South Bay, featuring waterfront access and beach atmosphere.", "tags": ["Waterfront", "Bay Access", "Beach"]},
            {"name": "Harbor Green", "type": "Area", "desc": "Waterfront community with marina access, canal homes, and boating lifestyle.", "tags": ["Marina", "Canal Homes", "Boating"]},
            {"name": "Massapequa Preserve Area", "type": "Area", "desc": "Northern section near the 423-acre preserve, offering nature trails, biking, and outdoor recreation.", "tags": ["Nature Preserve", "Trails", "Recreation"]},
            {"name": "Sunrise Highway Corridor", "type": "Area", "desc": "Central commercial area with shopping, dining, and excellent highway access.", "tags": ["Shopping", "Dining", "Highway"]},
            {"name": "Broadway District", "type": "Area", "desc": "Main commercial street with shops, restaurants, and community character. Heart of Massapequa.", "tags": ["Commercial", "Restaurants", "Community"]},
            {"name": "East Massapequa", "type": "Area", "desc": "Eastern residential section with diverse housing, good schools, and convenient amenities.", "tags": ["Diverse", "Schools", "Convenient"]}
        ],
        "surrounding": ["North Massapequa", "Seaford", "Wantagh", "Amityville", "Farmingdale"],
        "intro": "a thriving South Shore community known for excellent schools, waterfront living, and the scenic Massapequa Preserve"
    },

    "freeport": {
        "name": "Freeport",
        "coords": "40.6576, -73.5832",
        "neighborhoods": [
            {"name": "Freeport Village", "type": "Village", "desc": "Historic nautical village with working waterfront, marina district, and charming downtown. Unique character.", "tags": ["Nautical Village", "Marina", "Historic"]},
            {"name": "Cow Meadow Park Area", "type": "Area", "desc": "Northern section near the expansive park, offering recreation, sports, and family amenities.", "tags": ["Park", "Recreation", "Sports"]},
            {"name": "South Freeport", "type": "Area", "desc": "Southern waterfront section with canal homes, boat access, and maritime atmosphere.", "tags": ["Waterfront", "Canal Homes", "Maritime"]},
            {"name": "Woodcleft Canal District", "type": "Area", "desc": "Iconic fishing village area with restaurants, charter boats, and working waterfront. Tourist destination.", "tags": ["Fishing Village", "Restaurants", "Waterfront"]},
            {"name": "North Freeport", "type": "Area", "desc": "Northern residential section with diverse housing, good schools, and convenient amenities.", "tags": ["Diverse", "Schools", "Convenient"]},
            {"name": "Sunrise Highway Corridor", "type": "Area", "desc": "Commercial area with shopping, dining, and excellent highway connectivity.", "tags": ["Shopping", "Dining", "Highway Access"]},
            {"name": "Freeport LIRR District", "type": "Area", "desc": "Central area near the train station with walkable downtown, shops, and commuter access.", "tags": ["LIRR", "Walkable", "Downtown"]}
        ],
        "surrounding": ["Merrick", "Baldwin", "Oceanside", "Roosevelt", "Bellmore"],
        "intro": "a unique nautical village with working waterfront, famous fishing boats, and vibrant maritime heritage"
    },

    "long-beach": {
        "name": "Long Beach",
        "coords": "40.5884, -73.6579",
        "neighborhoods": [
            {"name": "West End", "type": "Area", "desc": "Western beachfront section with oceanfront condos, beach access, and vibrant summer atmosphere.", "tags": ["Beachfront", "Oceanfront", "Summer"]},
            {"name": "East End", "type": "Area", "desc": "Eastern section with diverse housing, quieter streets, and family-friendly beach town atmosphere.", "tags": ["Family Beach", "Quiet", "Diverse"]},
            {"name": "Downtown Long Beach", "type": "Area", "desc": "Central district along Park Avenue with shops, restaurants, bars, and year-round activity.", "tags": ["Downtown", "Restaurants", "Active"]},
            {"name": "The Boardwalk Area", "type": "Area", "desc": "Iconic 2.2-mile oceanfront boardwalk with beaches, surfing, recreation, and ocean views.", "tags": ["Boardwalk", "Surfing", "Ocean Views"]},
            {"name": "Canal District", "type": "Area", "desc": "Northern waterfront section along the bay with canal homes, boat docks, and water access.", "tags": ["Canal Homes", "Bay Access", "Boating"]},
            {"name": "West Park Area", "type": "Area", "desc": "Western residential section near West End Beach, featuring family homes and beach proximity.", "tags": ["Beach Proximity", "Family Homes", "West End"]},
            {"name": "Lido Beach Border", "type": "Area", "desc": "Eastern section bordering Lido Beach, offering quieter beach atmosphere and residential character.", "tags": ["Quieter Beach", "Residential", "Border"]},
            {"name": "National Boulevard", "type": "Area", "desc": "Main thoroughfare featuring diverse housing, convenient shopping, and central location.", "tags": ["Central", "Shopping", "Diverse"]}
        ],
        "surrounding": ["Lido Beach", "Island Park", "Atlantic Beach", "Point Lookout", "East Atlantic Beach"],
        "intro": "a vibrant barrier island city featuring 2.2 miles of pristine beaches, iconic boardwalk, and year-round coastal living"
    },

    "oceanside": {
        "name": "Oceanside",
        "coords": "40.6387, -73.6401",
        "neighborhoods": [
            {"name": "Oceanside Village", "type": "Hamlet", "desc": "Central hamlet area near LIRR station with shopping, dining, and excellent Oceanside schools.", "tags": ["LIRR", "Shopping", "Schools"]},
            {"name": "South Oceanside", "type": "Area", "desc": "Southern section closer to the water, featuring beach proximity and summer atmosphere.", "tags": ["Beach Proximity", "Water Access", "Summer"]},
            {"name": "North Oceanside", "type": "Area", "desc": "Northern residential section with diverse housing, family neighborhoods, and good schools.", "tags": ["Diverse", "Family", "Schools"]},
            {"name": "Davison Avenue Area", "type": "Area", "desc": "Western section with established homes, convenient shopping, and community amenities.", "tags": ["Established", "Shopping", "Community"]},
            {"name": "Long Beach Road Corridor", "type": "Area", "desc": "Main commercial corridor with retail, dining, and services. Very convenient.", "tags": ["Commercial", "Retail", "Convenient"]},
            {"name": "Oceanside Park Area", "type": "Area", "desc": "Central section near the park and recreation center, featuring family homes and active community.", "tags": ["Park", "Recreation", "Family Homes"]},
            {"name": "East Oceanside", "type": "Area", "desc": "Eastern residential neighborhoods with diverse housing and proximity to Rockville Centre.", "tags": ["Diverse", "Residential", "Convenient"]}
        ],
        "surrounding": ["Baldwin", "Rockville Centre", "East Rockaway", "Lynbrook", "Island Park"],
        "intro": "a thriving South Shore hamlet featuring excellent schools, beach proximity, and strong family-oriented community"
    },

    "east-meadow": {
        "name": "East Meadow",
        "coords": "40.7139, -73.5590",
        "neighborhoods": [
            {"name": "Newbridge Commons Area", "type": "Area", "desc": "Central section near the shopping center, offering convenient retail, dining, and services.", "tags": ["Shopping", "Dining", "Convenient"]},
            {"name": "Eisenhower Park Area", "type": "Area", "desc": "Northern section near Nassau's largest park, offering recreation, sports, and family amenities.", "tags": ["Park Access", "Recreation", "Sports"]},
            {"name": "North East Meadow", "type": "Area", "desc": "Northern residential section with suburban homes, top-rated schools, and family neighborhoods.", "tags": ["Suburban", "Top Schools", "Family"]},
            {"name": "South East Meadow", "type": "Area", "desc": "Southern section with diverse housing, good schools, and convenient highway access.", "tags": ["Diverse", "Schools", "Highway Access"]},
            {"name": "East Meadow HS District", "type": "Area", "desc": "Central residential area with excellent East Meadow schools and strong community spirit.", "tags": ["Schools", "Community", "Residential"]},
            {"name": "Hempstead Turnpike Corridor", "type": "Area", "desc": "Major commercial corridor with shopping centers, restaurants, and services.", "tags": ["Shopping", "Commercial", "Services"]},
            {"name": "Salisbury Park Area", "type": "Area", "desc": "Western section near Salisbury Park, featuring suburban homes and community amenities.", "tags": ["Park", "Suburban", "Community"]},
            {"name": "East East Meadow", "type": "Area", "desc": "Eastern residential neighborhoods with established homes and convenient location.", "tags": ["Established", "Residential", "Convenient"]}
        ],
        "surrounding": ["Westbury", "Uniondale", "Levittown", "Salisbury", "Merrick"],
        "intro": "a family-friendly suburban community known for excellent schools, Eisenhower Park, and convenient mid-Island location"
    },

    # Suffolk County Western Locations
    "huntington": {
        "name": "Huntington",
        "coords": "40.8682, -73.4257",
        "neighborhoods": [
            {"name": "Huntington Village", "type": "Village", "desc": "Vibrant downtown with shops, restaurants, galleries, and LIRR. Walkable urban village atmosphere.", "tags": ["Downtown", "LIRR", "Walkable"]},
            {"name": "Huntington Bay", "type": "Village", "desc": "Exclusive waterfront village along Huntington Harbor, featuring luxury estates and private beaches.", "tags": ["Waterfront", "Luxury", "Private Beaches"]},
            {"name": "Lloyd Harbor", "type": "Village", "desc": "Ultra-exclusive waterfront village with multi-acre estates, beaches, and preserved natural beauty.", "tags": ["Ultra-Exclusive", "Estates", "Waterfront"]},
            {"name": "Huntington Station", "type": "Hamlet", "desc": "Diverse southern section with LIRR hub, affordable housing, and convenient access to amenities.", "tags": ["LIRR Hub", "Diverse", "Affordable"]},
            {"name": "Cold Spring Harbor", "type": "Hamlet", "desc": "Historic North Shore hamlet with charming waterfront village, harbor, and prestigious addresses.", "tags": ["Historic", "Waterfront Village", "Prestigious"]},
            {"name": "Centerport", "type": "Hamlet", "desc": "Waterfront hamlet on Northport Bay, featuring beaches, harbor, and maritime character.", "tags": ["Waterfront", "Harbor", "Maritime"]},
            {"name": "South Huntington", "type": "Area", "desc": "Southern residential section with diverse housing, good schools, and convenient location.", "tags": ["Diverse", "Schools", "Convenient"]},
            {"name": "Greenlawn", "type": "Hamlet", "desc": "Eastern hamlet with suburban character, good schools, and community atmosphere.", "tags": ["Suburban", "Schools", "Community"]}
        ],
        "surrounding": ["Dix Hills", "Melville", "Northport", "East Northport", "Commack"],
        "intro": "a vibrant North Shore town featuring charming Huntington Village, waterfront hamlets, and diverse neighborhoods"
    },

    "dix-hills": {
        "name": "Dix Hills",
        "coords": "40.8048, -73.3387",
        "neighborhoods": [
            {"name": "North Dix Hills", "type": "Area", "desc": "Northern section with luxury estates, larger lots, and top-rated Half Hollow Hills schools.", "tags": ["Luxury Estates", "Large Lots", "Top Schools"]},
            {"name": "South Dix Hills", "type": "Area", "desc": "Southern residential section with upscale homes, excellent schools, and family neighborhoods.", "tags": ["Upscale", "Schools", "Family"]},
            {"name": "East Dix Hills", "type": "Area", "desc": "Eastern section with diverse upscale housing, convenient shopping, and highway access.", "tags": ["Upscale", "Shopping", "Highway Access"]},
            {"name": "West Dix Hills", "type": "Area", "desc": "Western neighborhoods featuring larger properties, rolling terrain, and prestigious addresses.", "tags": ["Larger Properties", "Rolling Hills", "Prestigious"]},
            {"name": "Vanderbilt Motor Parkway Area", "type": "Area", "desc": "Central section along historic parkway, offering convenient access and established homes.", "tags": ["Historic Parkway", "Convenient", "Established"]},
            {"name": "Caledonia Park Area", "type": "Area", "desc": "Northern section near the park, featuring family homes and community recreation.", "tags": ["Park", "Family Homes", "Recreation"]},
            {"name": "Five Towns Area", "type": "Area", "desc": "Southern section with upscale suburban homes, excellent schools, and low density.", "tags": ["Upscale Suburban", "Schools", "Low Density"]}
        ],
        "surrounding": ["Huntington", "Melville", "Commack", "Deer Park", "Half Hollow Hills"],
        "intro": "an affluent Suffolk County hamlet renowned for top-rated schools, luxury estates, and upscale suburban living"
    },

    # Suffolk County North Fork Locations
    "cutchogue": {
        "name": "Cutchogue",
        "coords": "41.0123, -72.4862",
        "neighborhoods": [
            {"name": "Cutchogue Village", "type": "Hamlet", "desc": "Historic village center with charming downtown, wineries, and farmland. North Fork character.", "tags": ["Historic", "Wineries", "Village"]},
            {"name": "Peconic Bay Waterfront", "type": "Area", "desc": "Southern waterfront section along Peconic Bay, featuring beaches, marinas, and water views.", "tags": ["Waterfront", "Bay Views", "Beaches"]},
            {"name": "Long Island Sound Shore", "type": "Area", "desc": "Northern coastline with sound beaches, estates, and spectacular water views.", "tags": ["Sound Views", "Beaches", "Estates"]},
            {"name": "Vineyard Area", "type": "Area", "desc": "Wine country section with vineyards, farm stands, and rural agricultural character.", "tags": ["Wineries", "Agricultural", "Rural"]},
            {"name": "New Suffolk", "type": "Hamlet", "desc": "Waterfront hamlet with maritime heritage, beaches, and quiet residential character.", "tags": ["Maritime", "Waterfront", "Quiet"]},
            {"name": "Nassau Point", "type": "Area", "desc": "Exclusive peninsula with private beaches, waterfront estates, and stunning bay views.", "tags": ["Exclusive", "Peninsula", "Waterfront"]},
            {"name": "Wickham Avenue Area", "type": "Area", "desc": "Central residential section with diverse housing, convenient village access, and community atmosphere.", "tags": ["Residential", "Village Access", "Community"]}
        ],
        "surrounding": ["Mattituck", "Southold", "Greenport", "Peconic", "East Marion"],
        "intro": "a charming North Fork hamlet featuring world-class wineries, farmland, and peaceful waterfront living"
    },

    "greenport": {
        "name": "Greenport",
        "coords": "41.1023, -72.3598",
        "neighborhoods": [
            {"name": "Greenport Village", "type": "Village", "desc": "Historic maritime village with working waterfront, shops, restaurants, and nautical character. Year-round charm.", "tags": ["Maritime Village", "Historic", "Waterfront"]},
            {"name": "Stirling Harbor Area", "type": "Area", "desc": "Northern harbor section with marinas, boat yards, and maritime industry. Active waterfront.", "tags": ["Harbor", "Marina", "Maritime"]},
            {"name": "Mitchell Park Waterfront", "type": "Area", "desc": "Central waterfront area with park, carousel, restaurants, and ferry access to Shelter Island.", "tags": ["Waterfront Park", "Ferry", "Restaurants"]},
            {"name": "Greenport West", "type": "Area", "desc": "Western residential section with village homes, walkable streets, and community character.", "tags": ["Village Homes", "Walkable", "Community"]},
            {"name": "East Greenport", "type": "Area", "desc": "Eastern section with waterfront properties, boat access, and quieter residential atmosphere.", "tags": ["Waterfront", "Boat Access", "Quiet"]},
            {"name": "Front Street District", "type": "Area", "desc": "Main commercial street with boutiques, galleries, restaurants, and vintage village charm.", "tags": ["Shopping", "Dining", "Vintage Charm"]},
            {"name": "Greenport Harbor", "type": "Area", "desc": "Active harbor area with commercial fishing, marinas, and working waterfront character.", "tags": ["Working Harbor", "Fishing", "Marinas"]}
        ],
        "surrounding": ["Southold", "East Marion", "Shelter Island", "Cutchogue", "Orient"],
        "intro": "a vibrant maritime village at the North Fork's eastern tip, featuring working waterfront, wineries, and year-round charm"
    },

    "mattituck": {
        "name": "Mattituck",
        "coords": "40.9923, -72.5362",
        "neighborhoods": [
            {"name": "Mattituck Village", "type": "Hamlet", "desc": "Central hamlet area with shops, restaurants, and community character. Heart of Mattituck.", "tags": ["Village", "Shopping", "Community"]},
            {"name": "Peconic Bay Waterfront", "type": "Area", "desc": "Southern waterfront along Peconic Bay, featuring beaches, marinas, and water access.", "tags": ["Waterfront", "Bay", "Beaches"]},
            {"name": "Sound Avenue Vineyard Area", "type": "Area", "desc": "Northern wine country section with prestigious vineyards, farm stands, and agricultural heritage.", "tags": ["Wineries", "Agricultural", "Farm Stands"]},
            {"name": "Mattituck Inlet", "type": "Area", "desc": "Inlet area with marina, boat access, fishing, and maritime atmosphere.", "tags": ["Inlet", "Marina", "Boating"]},
            {"name": "North Mattituck", "type": "Area", "desc": "Northern residential section with diverse housing, farmland views, and rural character.", "tags": ["Residential", "Farmland", "Rural"]},
            {"name": "Oregon Road Area", "type": "Area", "desc": "Central corridor with convenient access, diverse housing, and community amenities.", "tags": ["Convenient", "Diverse", "Community"]},
            {"name": "Reeves Park Area", "type": "Area", "desc": "Waterfront park section with beach access, recreation, and family amenities.", "tags": ["Park", "Beach", "Recreation"]}
        ],
        "surrounding": ["Cutchogue", "Laurel", "Jamesport", "Southold", "Aquebogue"],
        "intro": "a scenic North Fork hamlet featuring award-winning wineries, pristine beaches, and charming rural character"
    },

    "jamesport": {
        "name": "Jamesport",
        "coords": "40.9523, -72.5837",
        "neighborhoods": [
            {"name": "Jamesport Village", "type": "Hamlet", "desc": "Historic hamlet center with antique shops, farm stands, and rural Long Island character.", "tags": ["Historic", "Antiques", "Rural"]},
            {"name": "Jamesport Vineyard District", "type": "Area", "desc": "Wine country area with multiple vineyards, tasting rooms, and agricultural tourism.", "tags": ["Wineries", "Tasting Rooms", "Tourism"]},
            {"name": "South Jamesport Waterfront", "type": "Area", "desc": "Southern section along Great Peconic Bay with waterfront access and beach atmosphere.", "tags": ["Waterfront", "Bay", "Beaches"]},
            {"name": "Main Road Corridor", "type": "Area", "desc": "Historic Route 25 through Jamesport, featuring shops, restaurants, and farm stands.", "tags": ["Main Road", "Shopping", "Farm Stands"]},
            {"name": "North Jamesport", "type": "Area", "desc": "Northern agricultural section with farmland, vineyards, and open space character.", "tags": ["Agricultural", "Farmland", "Open Space"]},
            {"name": "Manor Lane Area", "type": "Area", "desc": "Residential section with diverse housing, community character, and rural atmosphere.", "tags": ["Residential", "Community", "Rural"]},
            {"name": "Peconic Bay Beach", "type": "Area", "desc": "Waterfront area with beach access, boat launches, and water recreation.", "tags": ["Beach", "Water Access", "Recreation"]}
        ],
        "surrounding": ["Aquebogue", "Riverhead", "Mattituck", "Laurel", "Calverton"],
        "intro": "a pastoral North Fork hamlet known for boutique wineries, antique shops, and preserved agricultural heritage"
    },

    "southold": {
        "name": "Southold",
        "coords": "41.0651, -72.4262",
        "neighborhoods": [
            {"name": "Southold Village", "type": "Hamlet", "desc": "Historic village center with colonial heritage, local shops, and authentic North Fork character.", "tags": ["Historic", "Colonial", "Village"]},
            {"name": "Peconic Bay Shore", "type": "Area", "desc": "Southern waterfront along Peconic Bay, featuring beaches, marinas, and bay views.", "tags": ["Waterfront", "Bay Views", "Beaches"]},
            {"name": "Long Island Sound Shore", "type": "Area", "desc": "Northern coastline with sound beaches, estates, and spectacular water views.", "tags": ["Sound Views", "Beaches", "Estates"]},
            {"name": "Southold Farm Country", "type": "Area", "desc": "Interior agricultural area with working farms, vineyards, and preserved farmland.", "tags": ["Farmland", "Vineyards", "Agricultural"]},
            {"name": "Founders Landing", "type": "Area", "desc": "Waterfront area with historic landing, beach access, and maritime heritage.", "tags": ["Historic", "Waterfront", "Beach"]},
            {"name": "Hortons Point", "type": "Area", "desc": "Eastern point with lighthouse, beaches, and scenic coastal beauty.", "tags": ["Lighthouse", "Coastal", "Scenic"]},
            {"name": "Main Road District", "type": "Area", "desc": "Commercial corridor with shops, restaurants, wineries, and farm stands.", "tags": ["Commercial", "Wineries", "Farm Stands"]}
        ],
        "surrounding": ["Greenport", "Cutchogue", "East Marion", "Peconic", "Mattituck"],
        "intro": "a historic North Fork town featuring colonial heritage, working farms, world-class wineries, and pristine beaches"
    },

    "east-marion": {
        "name": "East Marion",
        "coords": "41.1262, -72.3398",
        "neighborhoods": [
            {"name": "East Marion Village", "type": "Hamlet", "desc": "Small waterfront hamlet with quiet residential character, beaches, and maritime heritage.", "tags": ["Waterfront", "Quiet", "Maritime"]},
            {"name": "Orient Point Border", "type": "Area", "desc": "Eastern section near Orient Point ferry, featuring waterfront access and coastal character.", "tags": ["Ferry Access", "Waterfront", "Coastal"]},
            {"name": "Rocky Point Beach Area", "type": "Area", "desc": "Northern sound shore with rocky beaches, fishing access, and water views.", "tags": ["Sound Shore", "Beaches", "Fishing"]},
            {"name": "Peconic Bay Waterfront", "type": "Area", "desc": "Southern waterfront along Peconic Bay with calm waters, beaches, and boat access.", "tags": ["Bay", "Beaches", "Boating"]},
            {"name": "Main Road Residential", "type": "Area", "desc": "Central residential area with diverse housing, convenient village access, and community character.", "tags": ["Residential", "Village Access", "Community"]},
            {"name": "Marion Lake Area", "type": "Area", "desc": "Interior section near freshwater lake, offering fishing, nature, and tranquility.", "tags": ["Lake", "Nature", "Tranquil"]},
            {"name": "Truman Beach", "type": "Area", "desc": "Waterfront beach area with swimming, fishing, and peaceful waterfront living.", "tags": ["Beach", "Swimming", "Peaceful"]}
        ],
        "surrounding": ["Greenport", "Orient", "Southold", "Shelter Island"],
        "intro": "a tranquil North Fork hamlet at the eastern tip, featuring pristine beaches, quiet waterfront living, and natural beauty"
    },

    # Suffolk County Eastern Locations
    "the-hamptons": {
        "name": "The Hamptons",
        "coords": "40.9629, -72.1929",
        "neighborhoods": [
            {"name": "Southampton Village", "type": "Village", "desc": "Historic village with upscale shopping, dining, pristine beaches, and timeless elegance. Summer destination.", "tags": ["Historic", "Upscale", "Beaches"]},
            {"name": "East Hampton Village", "type": "Village", "desc": "Prestigious village center with Main Street shopping, galleries, restaurants, and cultural amenities.", "tags": ["Prestigious", "Shopping", "Cultural"]},
            {"name": "Bridgehampton", "type": "Hamlet", "desc": "Central hamlet with farms, farm stands, wineries, and convenient access to all Hampton villages.", "tags": ["Farms", "Wineries", "Central"]},
            {"name": "Sag Harbor", "type": "Village", "desc": "Historic whaling village with working waterfront, yacht clubs, galleries, and vibrant summer scene.", "tags": ["Historic Whaling", "Waterfront", "Yacht Clubs"]},
            {"name": "Amagansett", "type": "Hamlet", "desc": "Quiet beach hamlet between East Hampton and Montauk, featuring pristine beaches and artistic community.", "tags": ["Beaches", "Artistic", "Quiet"]},
            {"name": "Westhampton Beach", "type": "Village", "desc": "Western gateway to the Hamptons with beaches, shopping, dining, and summer social scene.", "tags": ["Beaches", "Shopping", "Social"]},
            {"name": "Water Mill", "type": "Hamlet", "desc": "Historic mill hamlet with estates, farms, beaches, and proximity to Southampton.", "tags": ["Historic Mill", "Estates", "Farms"]},
            {"name": "Sagaponack", "type": "Village", "desc": "Ultra-exclusive agricultural village with farm fields, ocean beaches, and multi-million dollar estates.", "tags": ["Ultra-Exclusive", "Estates", "Beaches"]},
            {"name": "Quogue", "type": "Village", "desc": "Quiet village with pristine beaches, low density, and family-friendly summer atmosphere.", "tags": ["Quiet", "Beaches", "Family"]}
        ],
        "surrounding": ["Southampton", "East Hampton", "Bridgehampton", "Sag Harbor", "Montauk"],
        "intro": "world-renowned summer destination featuring pristine beaches, luxury estates, upscale shopping, and sophisticated cultural scene"
    },

    "montauk": {
        "name": "Montauk",
        "coords": "41.0357, -71.9584",
        "neighborhoods": [
            {"name": "Montauk Village", "type": "Hamlet", "desc": "Commercial center with shops, restaurants, hotels, and the working fishing fleet. Heart of Montauk.", "tags": ["Village", "Fishing Fleet", "Commercial"]},
            {"name": "Montauk Point", "type": "Area", "desc": "Eastern tip of Long Island featuring the iconic lighthouse, state park, and dramatic coastal beauty.", "tags": ["Lighthouse", "State Park", "Coastal"]},
            {"name": "Ditch Plains", "type": "Area", "desc": "Legendary surf beach with consistent waves, surf culture, and beachfront homes. Surfer's paradise.", "tags": ["Surfing", "Beach", "Surf Culture"]},
            {"name": "Montauk Harbor", "type": "Area", "desc": "Working fishing harbor with charter boats, seafood restaurants, marinas, and maritime character.", "tags": ["Fishing Harbor", "Marinas", "Maritime"]},
            {"name": "Hither Hills", "type": "Area", "desc": "Western section near the state park, offering camping, hiking, beaches, and natural beauty.", "tags": ["State Park", "Nature", "Beaches"]},
            {"name": "Fort Pond Bay", "type": "Area", "desc": "Northern waterfront along the bay with marinas, water access, and quieter residential character.", "tags": ["Bay", "Marina", "Quiet"]},
            {"name": "Montauk Downs", "type": "Area", "desc": "Inland section near the state park golf course, featuring diverse housing and recreation access.", "tags": ["Golf", "Recreation", "Residential"]},
            {"name": "Old Montauk Highway", "type": "Area", "desc": "Scenic coastal route with oceanfront estates, beaches, and spectacular Atlantic Ocean views.", "tags": ["Oceanfront", "Scenic", "Estates"]}
        ],
        "surrounding": ["Amagansett", "East Hampton", "Hither Hills"],
        "intro": "Long Island's easternmost hamlet featuring world-class surfing, sport fishing, the iconic lighthouse, and laid-back beach town atmosphere"
    },

    # NYC Borough Pages
    "brooklyn": {
        "name": "Brooklyn",
        "coords": "40.6782, -73.9442",
        "neighborhoods": [
            {"name": "Park Slope", "type": "Neighborhood", "desc": "Brownstone-lined streets near Prospect Park, featuring Victorian architecture, dining, and family atmosphere.", "tags": ["Brownstones", "Park", "Family"]},
            {"name": "Williamsburg", "type": "Neighborhood", "desc": "Trendy North Brooklyn neighborhood with arts scene, nightlife, waterfront parks, and L train access.", "tags": ["Trendy", "Arts", "Nightlife"]},
            {"name": "DUMBO", "type": "Neighborhood", "desc": "Down Under Manhattan Bridge Overpass - waterfront neighborhood with cobblestone streets, tech companies, galleries.", "tags": ["Waterfront", "Tech", "Historic"]},
            {"name": "Brooklyn Heights", "type": "Neighborhood", "desc": "Historic neighborhood with elegant brownstones, Brooklyn Promenade, and stunning Manhattan skyline views.", "tags": ["Historic", "Brownstones", "Views"]},
            {"name": "Bay Ridge", "type": "Neighborhood", "desc": "Southern Brooklyn neighborhood with diverse community, waterfront parks, and family-friendly atmosphere.", "tags": ["Diverse", "Waterfront", "Family"]},
            {"name": "Bedford-Stuyvesant", "type": "Neighborhood", "desc": "Historic Central Brooklyn neighborhood with beautiful brownstones, cultural heritage, and community character.", "tags": ["Historic", "Brownstones", "Cultural"]},
            {"name": "Sunset Park", "type": "Neighborhood", "desc": "Diverse neighborhood with immigrant communities, park views, and affordable housing options.", "tags": ["Diverse", "Park Views", "Affordable"]},
            {"name": "Carroll Gardens", "type": "Neighborhood", "desc": "Charming neighborhood with Italian heritage, tree-lined streets, restaurants, and brownstone charm.", "tags": ["Italian Heritage", "Charming", "Restaurants"]},
            {"name": "Greenpoint", "type": "Neighborhood", "desc": "Northern Brooklyn waterfront neighborhood with Polish heritage, trendy cafes, and manufacturing past.", "tags": ["Waterfront", "Polish Heritage", "Trendy"]}
        ],
        "surrounding": ["Queens", "Manhattan", "Long Island"],
        "intro": "NYC's most populous borough featuring diverse neighborhoods, iconic brownstones, vibrant culture, and waterfront parks"
    },

    "queens": {
        "name": "Queens",
        "coords": "40.7282, -73.7949",
        "neighborhoods": [
            {"name": "Astoria", "type": "Neighborhood", "desc": "Diverse neighborhood with Greek heritage, exceptional dining, cultural attractions, and N/W train access.", "tags": ["Diverse", "Dining", "Cultural"]},
            {"name": "Long Island City", "type": "Neighborhood", "desc": "Waterfront neighborhood with high-rise development, art galleries, tech companies, and Manhattan skyline views.", "tags": ["Waterfront", "Development", "Arts"]},
            {"name": "Flushing", "type": "Neighborhood", "desc": "Vibrant Asian-American hub with authentic cuisine, shopping, cultural diversity, and 7 train access.", "tags": ["Asian Hub", "Cuisine", "Diverse"]},
            {"name": "Forest Hills", "type": "Neighborhood", "desc": "Upscale neighborhood with Tudor architecture, Forest Hills Gardens, tennis stadium, and tree-lined streets.", "tags": ["Upscale", "Tudor", "Tennis"]},
            {"name": "Jackson Heights", "type": "Neighborhood", "desc": "Culturally diverse neighborhood with international cuisine, historic districts, and vibrant street life.", "tags": ["Diverse", "International", "Historic"]},
            {"name": "Bayside", "type": "Neighborhood", "desc": "Northeastern Queens neighborhood with suburban feel, waterfront parks, good schools, and family community.", "tags": ["Suburban", "Waterfront", "Family"]},
            {"name": "Rockaway Beach", "type": "Neighborhood", "desc": "Beachfront community on the Rockaway Peninsula with surfing, boardwalk, and beach town atmosphere.", "tags": ["Beach", "Surfing", "Boardwalk"]},
            {"name": "Sunnyside", "type": "Neighborhood", "desc": "Historic neighborhood with garden apartments, diverse community, convenient 7 train access to Manhattan.", "tags": ["Historic", "Gardens", "Convenient"]},
            {"name": "Rego Park", "type": "Neighborhood", "desc": "Central Queens neighborhood with shopping centers, diverse housing, and convenient subway access.", "tags": ["Shopping", "Diverse", "Convenient"]}
        ],
        "surrounding": ["Brooklyn", "Manhattan", "Long Island", "Nassau County"],
        "intro": "NYC's largest and most diverse borough featuring international communities, exceptional dining, beaches, and cultural attractions"
    },
}

# Template for location pages
def generate_location_page(location_key, location_data):
    name = location_data["name"]
    coords = location_data["coords"]
    lat, lon = coords.split(", ")
    neighborhoods = location_data["neighborhoods"]
    surrounding = location_data["surrounding"]
    intro = location_data["intro"]

    # Build neighborhoods HTML
    neighborhoods_html = ""
    for idx, hood in enumerate(neighborhoods):
        # Alternate badge colors
        badge_color = "blue-600" if hood["type"] in ["Village", "Area"] else "green-600" if hood["type"] == "Hamlet" else "purple-600"

        neighborhoods_html += f'''
                <!-- {hood["name"]} -->
                <div class="feature-card bg-gradient-to-br from-slate-800 to-slate-700 rounded-2xl p-8 shadow-xl border border-slate-600">
                    <div class="flex items-start justify-between mb-4">
                        <div class="icon-container w-14 h-14 bg-blue-600 rounded-xl flex items-center justify-center">
                            <svg class="w-7 h-7 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/>
                            </svg>
                        </div>
                        <span class="bg-{badge_color} text-white text-xs font-semibold px-3 py-1 rounded-full">{hood["type"]}</span>
                    </div>
                    <h3 class="text-2xl font-bold text-white mb-3">{hood["name"]}</h3>
                    <p class="text-slate-300 leading-relaxed mb-4">
                        {hood["desc"]}
                    </p>
                    <div class="flex flex-wrap gap-2 text-xs">'''

        for tag in hood["tags"]:
            neighborhoods_html += f'''
                        <span class="bg-slate-600 text-slate-200 px-3 py-1 rounded-full">{tag}</span>'''

        neighborhoods_html += '''
                    </div>
                </div>
'''

    # Build surrounding areas list
    surrounding_list = ", ".join(surrounding[:-1]) + ", and " + surrounding[-1] if len(surrounding) > 1 else surrounding[0]

    # SEO keywords
    keywords = f"sell house fast {name} NY, cash home buyers {name}, we buy houses {name} NY, sell inherited property {name}, off-market buyers Long Island"

    # Generate the complete page
    content = f'''---
// src/pages/{location_key}.astro
// Location Page: {name}, NY
import Navigation from '../../components/Navigation.astro';
import Footer from '../../components/Footer.astro';
import LocationForm from '../../components/locationForm.astro';
import GoogleAnalytics from '../../components/GoogleAnalytics.astro';
---

<!DOCTYPE html>
<html lang="en">
<head>
    <GoogleAnalytics />
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- SEO Meta Tags -->
    <title>Sell Your House Fast in {name} NY | Long Island Home Buyers</title>
    <meta name="description" content="Long Island Home Buyers offers fast, fair, and private cash offers for homes in {name}, NY. No repairs, no commissions, close on your timeline.">
    <meta name="keywords" content="{keywords}">

    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website">
    <meta property="og:title" content="Sell Your House Fast in {name} NY | Long Island Home Buyers">
    <meta property="og:description" content="Long Island Home Buyers offers fast, fair, and private cash offers for homes in {name}, NY. No repairs, no commissions, close on your timeline.">

    <!-- Geo Tags -->
    <meta name="geo.region" content="US-NY">
    <meta name="geo.placename" content="{name}, New York">
    <meta name="geo.position" content="{lat};{lon}">
    <meta name="ICBM" content="{lat}, {lon}">

    <!-- Schema.org Markup -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "RealEstateAgent",
      "name": "Long Island Home Buyers",
      "description": "Cash home buyers in {name}, NY",
      "url": "https://prohomebuyers.com/{location_key}",
      "telephone": "+1-718-288-7300",
      "address": {{
        "@type": "PostalAddress",
        "addressLocality": "Manhasset",
        "addressRegion": "NY",
        "addressCountry": "US"
      }},
      "areaServed": {{
        "@type": "City",
        "name": "{name}",
        "containedIn": {{
          "@type": "State",
          "name": "New York"
        }}
      }},
      "priceRange": "$$"
    }}
    </script>

    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

        * {{
            font-family: 'Inter', sans-serif;
        }}

        .gradient-text {{
            background: linear-gradient(135deg, #1e40af 0%, #3b82f6 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}

        .hero-pattern {{
            background-image:
                linear-gradient(to right, #f1f5f9 1px, transparent 1px),
                linear-gradient(to bottom, #f1f5f9 1px, transparent 1px);
            background-size: 40px 40px;
        }}

        .glass-effect {{
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
        }}

        .feature-card {{
            transition: all 0.3s ease;
        }}

        .feature-card:hover {{
            transform: translateY(-8px);
        }}

        .icon-container {{
            transition: all 0.3s ease;
        }}

        .feature-card:hover .icon-container {{
            transform: scale(1.1);
        }}

        .pulse-button {{
            animation: pulse 2s infinite;
        }}

        @keyframes pulse {{
            0%, 100% {{
                box-shadow: 0 0 0 0 rgba(59, 130, 246, 0.7);
            }}
            50% {{
                box-shadow: 0 0 0 10px rgba(59, 130, 246, 0);
            }}
        }}
    </style>
</head>
<body class="bg-slate-50">
    <!-- Navigation -->
    <Navigation />

    <!-- Hero Section -->
    <section class="relative bg-gradient-to-br from-slate-50 via-blue-50 to-slate-100 hero-pattern py-20 md:py-32">
        <div class="max-w-7xl mx-auto px-6">
            <div class="text-center max-w-4xl mx-auto">
                <!-- Location Badge -->
                <div class="inline-flex items-center mb-6 bg-white px-5 py-2 rounded-full shadow-md">
                    <svg class="w-5 h-5 text-blue-600 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/>
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/>
                    </svg>
                    <span class="text-blue-800 font-semibold text-sm">Serving {name}, NY</span>
                </div>

                <h1 class="text-4xl md:text-6xl font-bold text-slate-900 mb-6 leading-tight">
                    Sell Your {name} Home <br/>
                    <span class="gradient-text">Privately and On Your Terms</span>
                </h1>

                <p class="text-xl text-slate-600 mb-10 leading-relaxed max-w-3xl mx-auto">
                    We're your local {name} cash home buyers — helping homeowners sell quickly,
                    privately, and without realtor fees.
                </p>

                <div class="flex flex-col sm:flex-row gap-4 justify-center mb-8">
                    <a href="#contact-form" class="bg-blue-600 text-white px-10 py-4 rounded-full hover:bg-blue-700 transition font-semibold text-lg shadow-lg hover:shadow-xl pulse-button">
                        Get My Offer Now
                    </a>
                    <a href="tel:7182887300" class="bg-white text-slate-900 px-10 py-4 rounded-full hover:bg-slate-50 transition font-semibold text-lg border-2 border-slate-200 hover:border-blue-600 shadow-lg">
                        Call (718) 288-7300
                    </a>
                </div>

                <div class="flex flex-wrap gap-6 justify-center text-sm text-slate-600">
                    <div class="flex items-center">
                        <svg class="w-5 h-5 text-green-600 mr-2" fill="currentColor" viewBox="0 0 20 20">
                            <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
                        </svg>
                        <span class="font-medium">No Repairs Needed</span>
                    </div>
                    <div class="flex items-center">
                        <svg class="w-5 h-5 text-green-600 mr-2" fill="currentColor" viewBox="0 0 20 20">
                            <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
                        </svg>
                        <span class="font-medium">Zero Commissions</span>
                    </div>
                    <div class="flex items-center">
                        <svg class="w-5 h-5 text-green-600 mr-2" fill="currentColor" viewBox="0 0 20 20">
                            <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
                        </svg>
                        <span class="font-medium">Close on Your Timeline</span>
                    </div>
                    <div class="flex items-center">
                        <svg class="w-5 h-5 text-green-600 mr-2" fill="currentColor" viewBox="0 0 20 20">
                            <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
                        </svg>
                        <span class="font-medium">100% Confidential</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Local Introduction Section -->
    <section class="py-20 bg-white">
        <div class="max-w-7xl mx-auto px-6">
            <div class="grid lg:grid-cols-2 gap-12 items-center">
                <div>
                    <div class="inline-block mb-6">
                        <span class="bg-blue-100 text-blue-800 px-4 py-2 rounded-full text-sm font-semibold">
                            Local & Trusted Since 1983
                        </span>
                    </div>
                    <h2 class="text-4xl font-bold text-slate-900 mb-6">
                        Your Trusted Local Home Buyer in <span class="gradient-text">{name}, NY</span>
                    </h2>
                    <p class="text-lg text-slate-600 leading-relaxed mb-6">
                        Long Island Home Buyers is a Manhasset-based company purchasing homes directly from {name}
                        homeowners who value privacy, speed, and convenience. With over 40 years of combined
                        real estate and development experience across Long Island, we provide fair,
                        development-based offers without commissions, repairs, or delays.
                    </p>
                    <p class="text-lg text-slate-600 leading-relaxed mb-8">
                        Whether you're facing foreclosure, dealing with an inherited property, or simply want
                        a private sale without the hassle of traditional listings, we're here to help {name}
                        homeowners navigate their unique situations with compassion and professionalism.
                    </p>
                    <div class="flex flex-wrap gap-4">
                        <div class="flex items-center text-slate-700">
                            <svg class="w-6 h-6 text-blue-600 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
                            </svg>
                            <span class="font-medium">40+ Years Experience</span>
                        </div>
                        <div class="flex items-center text-slate-700">
                            <svg class="w-6 h-6 text-blue-600 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
                            </svg>
                            <span class="font-medium">500+ Homes Purchased</span>
                        </div>
                    </div>
                </div>

                <div class="relative">
                    <div class="bg-gradient-to-br from-blue-100 to-slate-100 rounded-3xl p-8 shadow-2xl border border-slate-200">
                        <div class="bg-white rounded-2xl p-8 shadow-lg">
                            <div class="flex items-center justify-center mb-6">
                                <svg class="w-32 h-32 text-blue-600 opacity-20" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/>
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/>
                                </svg>
                            </div>
                            <div class="text-center">
                                <h3 class="text-2xl font-bold text-slate-900 mb-2">{name}, NY</h3>
                                <p class="text-slate-600 mb-4">Proudly serving your community</p>
                                <div class="space-y-2 text-sm text-slate-600">
                                    <p>📍 Based in Manhasset, NY</p>
                                    <p>🏡 Serving all {name} neighborhoods</p>
                                    <p>⚡ 24-hour offer response time</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- How It Works Section -->
    <section class="py-20 bg-slate-50">
        <div class="max-w-7xl mx-auto px-6">
            <div class="text-center mb-16">
                <h2 class="text-4xl font-bold text-slate-900 mb-4">
                    How to Sell Your {name} Home Fast
                </h2>
                <p class="text-xl text-slate-600 max-w-2xl mx-auto">
                    Our simple 3-step process makes selling your home quick, easy, and stress-free
                </p>
            </div>

            <div class="grid md:grid-cols-3 gap-8">
                <!-- Step 1 -->
                <div class="relative">
                    <div class="feature-card bg-white rounded-2xl p-8 shadow-lg border-2 border-blue-200">
                        <div class="absolute -top-4 -left-4 w-12 h-12 bg-blue-600 text-white rounded-full flex items-center justify-center font-bold text-xl shadow-lg">
                            1
                        </div>
                        <div class="icon-container w-16 h-16 bg-blue-100 rounded-2xl flex items-center justify-center mb-6 mt-2">
                            <svg class="w-8 h-8 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
                            </svg>
                        </div>
                        <h3 class="text-2xl font-bold text-slate-900 mb-3">Submit Your Info</h3>
                        <p class="text-slate-600 leading-relaxed">
                            Tell us about your {name} property through our simple online form.
                            It takes less than 2 minutes — no obligation required.
                        </p>
                    </div>
                </div>

                <!-- Step 2 -->
                <div class="relative">
                    <div class="feature-card bg-white rounded-2xl p-8 shadow-lg border-2 border-blue-200">
                        <div class="absolute -top-4 -left-4 w-12 h-12 bg-blue-600 text-white rounded-full flex items-center justify-center font-bold text-xl shadow-lg">
                            2
                        </div>
                        <div class="icon-container w-16 h-16 bg-blue-100 rounded-2xl flex items-center justify-center mb-6 mt-2">
                            <svg class="w-8 h-8 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
                            </svg>
                        </div>
                        <h3 class="text-2xl font-bold text-slate-900 mb-3">5-Minute Call</h3>
                        <p class="text-slate-600 leading-relaxed">
                            One of our local team members will give you a quick call to confirm
                            details and understand your timeline. No pressure, just a friendly conversation.
                        </p>
                    </div>
                </div>

                <!-- Step 3 -->
                <div class="relative">
                    <div class="feature-card bg-white rounded-2xl p-8 shadow-lg border-2 border-blue-200">
                        <div class="absolute -top-4 -left-4 w-12 h-12 bg-blue-600 text-white rounded-full flex items-center justify-center font-bold text-xl shadow-lg">
                            3
                        </div>
                        <div class="icon-container w-16 h-16 bg-blue-100 rounded-2xl flex items-center justify-center mb-6 mt-2">
                            <svg class="w-8 h-8 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
                            </svg>
                        </div>
                        <h3 class="text-2xl font-bold text-slate-900 mb-3">Get Your Offer</h3>
                        <p class="text-slate-600 leading-relaxed">
                            Receive your fair cash offer within 24 hours. Accept it and close on your
                            timeline — as fast as 7 days or when you're ready.
                        </p>
                    </div>
                </div>
            </div>

            <div class="text-center mt-12">
                <a href="#contact-form" class="inline-flex items-center px-10 py-4 bg-blue-600 text-white rounded-full hover:bg-blue-700 transition font-semibold text-lg shadow-lg">
                    Request Your {name} Offer Now
                    <svg class="w-5 h-5 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
                    </svg>
                </a>
            </div>
        </div>
    </section>

    <!-- Why {name} Homeowners Choose Us -->
    <section class="py-20 bg-white">
        <div class="max-w-7xl mx-auto px-6">
            <div class="text-center mb-16">
                <h2 class="text-4xl font-bold text-slate-900 mb-4">
                    Why {name} Homeowners Choose Us
                </h2>
                <p class="text-xl text-slate-600 max-w-2xl mx-auto">
                    We're not your typical "we buy houses" company — here's what makes us different
                </p>
            </div>

            <div class="grid md:grid-cols-3 gap-8">
                <!-- Feature 1 -->
                <div class="feature-card bg-gradient-to-br from-blue-50 to-slate-50 rounded-2xl p-8 shadow-lg border border-blue-100">
                    <div class="icon-container w-16 h-16 bg-blue-600 rounded-2xl flex items-center justify-center mb-6">
                        <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/>
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/>
                        </svg>
                    </div>
                    <h3 class="text-2xl font-bold text-slate-900 mb-4">Local Expertise</h3>
                    <p class="text-slate-600 leading-relaxed mb-6">
                        Born and based in Manhasset, we've been serving {name} homeowners for decades.
                        We understand your neighborhood, property values, and local market dynamics.
                    </p>
                    <ul class="space-y-2 text-sm text-slate-600">
                        <li class="flex items-start">
                            <svg class="w-5 h-5 text-green-600 mr-2 flex-shrink-0 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
                            </svg>
                            <span>Deep knowledge of {name} real estate</span>
                        </li>
                        <li class="flex items-start">
                            <svg class="w-5 h-5 text-green-600 mr-2 flex-shrink-0 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
                            </svg>
                            <span>Family-owned Long Island company</span>
                        </li>
                        <li class="flex items-start">
                            <svg class="w-5 h-5 text-green-600 mr-2 flex-shrink-0 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
                            </svg>
                            <span>Personal service from local experts</span>
                        </li>
                    </ul>
                </div>

                <!-- Feature 2 -->
                <div class="feature-card bg-gradient-to-br from-blue-50 to-slate-50 rounded-2xl p-8 shadow-lg border border-blue-100">
                    <div class="icon-container w-16 h-16 bg-blue-600 rounded-2xl flex items-center justify-center mb-6">
                        <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/>
                        </svg>
                    </div>
                    <h3 class="text-2xl font-bold text-slate-900 mb-4">Fair, Transparent Offers</h3>
                    <p class="text-slate-600 leading-relaxed mb-6">
                        Our offers are based on true development potential and market value — not lowball tactics.
                        We explain our numbers clearly and answer all your questions.
                    </p>
                    <ul class="space-y-2 text-sm text-slate-600">
                        <li class="flex items-start">
                            <svg class="w-5 h-5 text-green-600 mr-2 flex-shrink-0 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
                            </svg>
                            <span>Development-based valuations</span>
                        </li>
                        <li class="flex items-start">
                            <svg class="w-5 h-5 text-green-600 mr-2 flex-shrink-0 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
                            </svg>
                            <span>No hidden fees or surprises</span>
                        </li>
                        <li class="flex items-start">
                            <svg class="w-5 h-5 text-green-600 mr-2 flex-shrink-0 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
                            </svg>
                            <span>Clear explanation of our process</span>
                        </li>
                    </ul>
                </div>

                <!-- Feature 3 -->
                <div class="feature-card bg-gradient-to-br from-blue-50 to-slate-50 rounded-2xl p-8 shadow-lg border border-blue-100">
                    <div class="icon-container w-16 h-16 bg-blue-600 rounded-2xl flex items-center justify-center mb-6">
                        <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/>
                        </svg>
                    </div>
                    <h3 class="text-2xl font-bold text-slate-900 mb-4">Private, Stress-Free Process</h3>
                    <p class="text-slate-600 leading-relaxed mb-6">
                        No listings, no repairs, no showings. Your sale remains completely private,
                        and we handle all the paperwork and closing details.
                    </p>
                    <ul class="space-y-2 text-sm text-slate-600">
                        <li class="flex items-start">
                            <svg class="w-5 h-5 text-green-600 mr-2 flex-shrink-0 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
                            </svg>
                            <span>100% confidential transactions</span>
                        </li>
                        <li class="flex items-start">
                            <svg class="w-5 h-5 text-green-600 mr-2 flex-shrink-0 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
                            </svg>
                            <span>Sell as-is in any condition</span>
                        </li>
                        <li class="flex items-start">
                            <svg class="w-5 h-5 text-green-600 mr-2 flex-shrink-0 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
                            </svg>
                            <span>Close on your preferred timeline</span>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- {name} Neighborhoods Section -->
    <section class="py-20 bg-gradient-to-br from-slate-900 to-slate-800 relative overflow-hidden">
        <div class="absolute inset-0 hero-pattern opacity-5"></div>
        <div class="max-w-7xl mx-auto px-6 relative z-10">
            <div class="text-center mb-16">
                <div class="inline-block mb-6">
                    <span class="bg-blue-600 text-white px-4 py-2 rounded-full text-sm font-semibold">
                        📍 Neighborhoods We Serve
                    </span>
                </div>
                <h2 class="text-4xl font-bold text-white mb-4">
                    We Buy Homes Throughout {name}
                </h2>
                <p class="text-xl text-slate-300 max-w-3xl mx-auto">
                    From {neighborhoods[0]["name"]} to {neighborhoods[1]["name"]}, we serve every neighborhood in {intro}
                    with fast, fair cash offers
                </p>
            </div>

            <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
{neighborhoods_html}
            </div>

            <!-- Bottom CTA for Neighborhoods -->
            <div class="mt-16 text-center">
                <div class="bg-gradient-to-br from-blue-600 to-blue-700 rounded-2xl p-10 shadow-2xl border border-blue-500">
                    <h3 class="text-3xl font-bold text-white mb-4">
                        Don't See Your {name} Neighborhood Listed?
                    </h3>
                    <p class="text-blue-100 text-lg mb-6 max-w-2xl mx-auto">
                        We buy homes throughout all of {name} — including every section and street.
                        Contact us today for a fair cash offer on your property.
                    </p>
                    <div class="flex flex-col sm:flex-row gap-4 justify-center">
                        <a href="#contact-form" class="inline-flex items-center px-8 py-4 bg-white text-blue-600 rounded-full hover:bg-blue-50 transition font-bold text-lg shadow-xl">
                            <svg class="w-6 h-6 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
                            </svg>
                            Get Your Offer Now
                        </a>
                        <a href="tel:7182887300" class="inline-flex items-center px-8 py-4 bg-blue-500 text-white rounded-full hover:bg-blue-400 transition font-bold text-lg border-2 border-blue-400">
                            <svg class="w-6 h-6 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
                            </svg>
                            Call (718) 288-7300
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Situations We Help With -->
    <section class="py-20 bg-slate-50">
        <div class="max-w-7xl mx-auto px-6">
            <div class="text-center mb-16">
                <h2 class="text-4xl font-bold text-slate-900 mb-4">
                    Situations We Help {name} Homeowners With
                </h2>
                <p class="text-xl text-slate-600 max-w-3xl mx-auto">
                    No matter your situation, Long Island Home Buyers provides fair, fast, and private offers
                    across {name} and Nassau County
                </p>
            </div>

            <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
                <!-- Situation 1 -->
                <div class="feature-card bg-white rounded-2xl p-8 shadow-lg border border-slate-100">
                    <div class="icon-container w-16 h-16 bg-red-100 rounded-2xl flex items-center justify-center mb-6">
                        <svg class="w-8 h-8 text-red-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/>
                        </svg>
                    </div>
                    <h3 class="text-xl font-bold text-slate-900 mb-3">Foreclosure or Financial Stress</h3>
                    <p class="text-slate-600 leading-relaxed">
                        Behind on mortgage payments? We can help you avoid foreclosure and protect your credit
                        with a quick sale before the bank takes action.
                    </p>
                </div>

                <!-- Situation 2 -->
                <div class="feature-card bg-white rounded-2xl p-8 shadow-lg border border-slate-100">
                    <div class="icon-container w-16 h-16 bg-purple-100 rounded-2xl flex items-center justify-center mb-6">
                        <svg class="w-8 h-8 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"/>
                        </svg>
                    </div>
                    <h3 class="text-xl font-bold text-slate-900 mb-3">Inherited or Probate Property</h3>
                    <p class="text-slate-600 leading-relaxed">
                        Dealing with a loved one's estate? We simplify the process by buying inherited homes
                        as-is, handling all probate complications with compassion.
                    </p>
                </div>

                <!-- Situation 3 -->
                <div class="feature-card bg-white rounded-2xl p-8 shadow-lg border border-slate-100">
                    <div class="icon-container w-16 h-16 bg-orange-100 rounded-2xl flex items-center justify-center mb-6">
                        <svg class="w-8 h-8 text-orange-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 14l6-6m-5.5.5h.01m4.99 5h.01M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16l3.5-2 3.5 2 3.5-2 3.5 2zM10 8.5a.5.5 0 11-1 0 .5.5 0 011 0zm5 5a.5.5 0 11-1 0 .5.5 0 011 0z"/>
                        </svg>
                    </div>
                    <h3 class="text-xl font-bold text-slate-900 mb-3">Tax Liens or Code Violations</h3>
                    <p class="text-slate-600 leading-relaxed">
                        Facing delinquent property taxes or costly code violations? We'll buy your property
                        quickly, helping you resolve these issues and move forward.
                    </p>
                </div>

                <!-- Situation 4 -->
                <div class="feature-card bg-white rounded-2xl p-8 shadow-lg border border-slate-100">
                    <div class="icon-container w-16 h-16 bg-blue-100 rounded-2xl flex items-center justify-center mb-6">
                        <svg class="w-8 h-8 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
                        </svg>
                    </div>
                    <h3 class="text-xl font-bold text-slate-900 mb-3">Downsizing or Relocation</h3>
                    <p class="text-slate-600 leading-relaxed">
                        Need to relocate quickly for work or downsize to a smaller space? We offer flexible
                        closing dates that work with your timeline.
                    </p>
                </div>

                <!-- Situation 5 -->
                <div class="feature-card bg-white rounded-2xl p-8 shadow-lg border border-slate-100">
                    <div class="icon-container w-16 h-16 bg-teal-100 rounded-2xl flex items-center justify-center mb-6">
                        <svg class="w-8 h-8 text-teal-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/>
                        </svg>
                    </div>
                    <h3 class="text-xl font-bold text-slate-900 mb-3">Vacant or Outdated Homes</h3>
                    <p class="text-slate-600 leading-relaxed">
                        Tired of maintaining an outdated or vacant property? We buy homes in any condition —
                        no repairs, cleaning, or updates required.
                    </p>
                </div>

                <!-- Situation 6 -->
                <div class="feature-card bg-white rounded-2xl p-8 shadow-lg border border-slate-100">
                    <div class="icon-container w-16 h-16 bg-green-100 rounded-2xl flex items-center justify-center mb-6">
                        <svg class="w-8 h-8 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 5a1 1 0 011-1h14a1 1 0 011 1v2a1 1 0 01-1 1H5a1 1 0 01-1-1V5zM4 13a1 1 0 011-1h6a1 1 0 011 1v6a1 1 0 01-1 1H5a1 1 0 01-1-1v-6zM16 13a1 1 0 011-1h2a1 1 0 011 1v6a1 1 0 01-1 1h-2a1 1 0 01-1-1v-6z"/>
                        </svg>
                    </div>
                    <h3 class="text-xl font-bold text-slate-900 mb-3">Land or Development Sale</h3>
                    <p class="text-slate-600 leading-relaxed">
                        Have a teardown, vacant lot, or development opportunity in {name}?
                        We specialize in land acquisitions and redevelopment projects.
                    </p>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact Form Section -->
    <section id="contact-form" class="py-20 bg-white">
        <div class="max-w-4xl mx-auto px-6">
            <div class="text-center mb-12">
                <h2 class="text-4xl font-bold text-slate-900 mb-4">
                    Get Your {name} Cash Offer Today
                </h2>
                <p class="text-xl text-slate-600">
                    Fill out the form below and receive your no-obligation offer within 24 hours
                </p>
            </div>

            <div class="bg-gradient-to-br from-slate-50 to-blue-50 rounded-2xl shadow-xl p-8 md:p-12 border border-slate-200">
                <LocationForm />
            </div>
        </div>
    </section>

    <!-- CTA Section -->
    <section class="py-24 bg-gradient-to-br from-blue-600 to-blue-800 relative overflow-hidden">
        <div class="absolute inset-0 hero-pattern opacity-10"></div>
        <div class="max-w-4xl mx-auto px-6 text-center relative z-10">
            <h2 class="text-4xl md:text-5xl font-bold text-white mb-6">
                Ready to Sell Your {name} Property Privately?
            </h2>
            <p class="text-xl text-blue-100 mb-10 max-w-2xl mx-auto">
                Get your no-obligation cash offer today. No pressure, no games—just a fair offer
                from {name}'s most trusted home buyers.
            </p>
            <div class="flex flex-col sm:flex-row gap-4 justify-center mb-8">
                <a href="#contact-form" class="bg-white text-blue-600 px-10 py-4 rounded-full hover:bg-blue-50 transition font-bold text-lg shadow-2xl inline-flex items-center justify-center">
                    <svg class="w-6 h-6 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
                    </svg>
                    Get My Offer Now
                </a>
                <a href="tel:7182887300" class="bg-blue-700 text-white px-10 py-4 rounded-full hover:bg-blue-800 transition font-bold text-lg border-2 border-blue-500 inline-flex items-center justify-center">
                    <svg class="w-6 h-6 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
                    </svg>
                    Call or Text (718) 288-7300
                </a>
            </div>
            <p class="text-blue-200 flex items-center justify-center flex-wrap gap-4">
                <span class="inline-flex items-center">
                    <svg class="w-5 h-5 mr-2" fill="currentColor" viewBox="0 0 20 20">
                        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
                    </svg>
                    No Obligations
                </span>
                <span class="inline-flex items-center">
                    <svg class="w-5 h-5 mr-2" fill="currentColor" viewBox="0 0 20 20">
                        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
                    </svg>
                    Fair Cash Offers
                </span>
                <span class="inline-flex items-center">
                    <svg class="w-5 h-5 mr-2" fill="currentColor" viewBox="0 0 20 20">
                        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
                    </svg>
                    Close on Your Timeline
                </span>
            </p>
        </div>
    </section>

    <!-- SEO Footer Section -->
    <section class="py-16 bg-slate-900 text-slate-300">
        <div class="max-w-7xl mx-auto px-6">
            <div class="max-w-4xl">
                <h2 class="text-2xl font-bold text-white mb-4">
                    Cash Home Buyers Serving {name} and Long Island
                </h2>
                <p class="text-lg leading-relaxed mb-6">
                    Long Island Home Buyers purchases homes in {name} and across Long Island — including {surrounding_list},
                    and throughout Nassau County.
                    We buy houses as-is, pay cash, and close on your timeline. Whether you're facing foreclosure,
                    dealing with an inherited property, or simply need a private sale, we're here to help.
                </p>
                <p class="text-lg leading-relaxed mb-6">
                    With over 40 years of combined real estate and development experience, our locally-based team
                    understands the unique challenges {name} homeowners face. We provide fair, development-based
                    offers without the hassle of traditional real estate sales — no repairs, no commissions,
                    no waiting for buyers.
                </p>

                <div class="border-t border-slate-700 pt-6 mt-8">
                    <h3 class="text-lg font-semibold text-white mb-3">Keywords & Services:</h3>
                    <div class="flex flex-wrap gap-3">
                        <span class="px-3 py-1 bg-slate-800 rounded-full text-sm">Sell house fast {name} NY</span>
                        <span class="px-3 py-1 bg-slate-800 rounded-full text-sm">Cash home buyers {name}</span>
                        <span class="px-3 py-1 bg-slate-800 rounded-full text-sm">We buy houses {name} NY</span>
                        <span class="px-3 py-1 bg-slate-800 rounded-full text-sm">Sell inherited property {name}</span>
                        <span class="px-3 py-1 bg-slate-800 rounded-full text-sm">Off-market buyers Long Island</span>
                        <span class="px-3 py-1 bg-slate-800 rounded-full text-sm">{name} real estate investors</span>
                        <span class="px-3 py-1 bg-slate-800 rounded-full text-sm">Sell home privately Nassau County</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <Footer />

    <!-- Scroll to Top Button -->
    <button id="scrollToTop"
            class="fixed bottom-8 right-8 bg-blue-600 text-white w-12 h-12 rounded-full shadow-lg hover:bg-blue-700 transition opacity-0 pointer-events-none z-50"
            onclick="window.scrollTo({{top: 0, behavior: 'smooth'}})">
        <svg class="w-6 h-6 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 10l7-7m0 0l7 7m-7-7v18"/>
        </svg>
    </button>

    <script is:inline>
        // Scroll to top button visibility
        const scrollBtn = document.getElementById('scrollToTop');
        window.addEventListener('scroll', () => {{
            if (window.scrollY > 300) {{
                scrollBtn.classList.remove('opacity-0', 'pointer-events-none');
                scrollBtn.classList.add('opacity-100');
            }} else {{
                scrollBtn.classList.add('opacity-0', 'pointer-events-none');
                scrollBtn.classList.remove('opacity-100');
            }}
        }});

        // Smooth scroll for anchor links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {{
            anchor.addEventListener('click', function (e) {{
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {{
                    target.scrollIntoView({{ behavior: 'smooth' }});
                }}
            }});
        }});
    </script>
</body>
</html>
'''

    return content


# Main execution
def main():
    locations_dir = "d:/AxonFlash/Sites/pro-astro-theme-updated/src/pages/locations"

    for location_key, location_data in LOCATIONS.items():
        output_path = os.path.join(locations_dir, f"{location_key}.astro")
        content = generate_location_page(location_key, location_data)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"Generated: {output_path}")

if __name__ == "__main__":
    main()
