var config = {
  style: 'mapbox://styles/mpotter/ck3ukxqlq0od01cnhven0r0ki',
  accessToken: 'pk.eyJ1IjoibXBvdHRlciIsImEiOiJjajAxZGltM3UwNjF2MzJsczVnN3R2eTNnIn0._Sj0HRLt8VTQGTojMWYFfQ',
  showMarkers: false,
  theme: 'light',
  alignment: 'left',
  title: 'TRIBUNE DEVELOPMENT SITE',
  subtitle: "20 Years of Urbanization in Downtown Chicago",
  footer: 'Source: Riverside Investment & Development',
  chapters: [
    {
      id: 'fultonriver_2',
      title: 'Transformational Development Opportunity',
      image: 'https://dk7h73956znl6.cloudfront.net/fultonriverdistrict.png',
      description: 'At 37-acres, the Tribune property is a unique blank slate development site central to the City’s most desirable 24/7 submarkets: West Loop, River North and Fulton Market. Artificially restricted from development for over 30 years, the property completed a rezoning in 2018 that allows for a multi-phase, mixed-use development of up to 11 million square feet. A natural extension of the river’s Confluence District - downtown Chicago’s original and recently re-established commercial epicenter - this site presents a rare opportunity to create a state of the art “city in the park” bringing over 2/3rd miles of new riverwalk and 15 acres of public open space downtown.',
      location: {
        center: { lon: -87.65125, lat: 41.88814 },
        zoom: 14.16,
        pitch: 0.00,
        bearing: 0.00
      },
      onChapterEnter: [{
          layer: 'large-parcels-3',
          opacity: 1
        },
        {
          layer: '3d-buildings',
          opacity: 0
        },
        {
          layer: 'road-label',
          opacity: 1
        },
      ],
      onChapterExit: [
        {
          layer: 'road-label',
          opacity: 0
        },
      ]
    },
    {
      id: 'past_growth',
      title: 'Two Decades of Urbanization',
      image: 'https://dk7h73956znl6.cloudfront.net/chicago_cbd_table.png',
      description: 'Over the past two decades, the CBD core has experienced a dramatic urban renaissance along with population growth unlike any other major U.S. city according to the Brookings Institute. During this time the conventional Loop/West Loop and River North submarkets have become built out and today few viable development sites remain. In 2014 a new submarket catalyzed by Google in Fulton Market emerged, creating Chicago’s first “neighborhood” office submarket largely defined by a high concentration of world-class restaurants and amenities. Meanwhile highly successful civic projects (such as the riverwalk), office (green) and residential (orange) projects along the river’s edge have solidified Chicago’s “second great waterfront” as the city’s most desirable aesthetic.',
      location: {
        center: [-87.65041, 41.88537],
        zoom: 14.06,
        pitch: 0.00,
        bearing: 0.00
      },
      onChapterEnter: [
        {
          layer: 'cta-l-lines',
          opacity: .55
        },
        {
          layer: 'chicago-cbd-supply-to-date',
          opacity: 1
        },
        {
          layer: 'chicago-cbd-supply-to-date-label',
          opacity: 1
        },
      ],
      onChapterExit: [
        {
          layer: 'chicago-cbd-supply-to-date',
          opacity: 0
        },
        {
          layer: 'chicago-cbd-supply-to-date-label',
          opacity: 0
        },
      ]
    },
    {
      id: 'commuter_lines',
      title: 'Access to a Commuter Population of 5.5 Million',
      description: 'Chicagos downtown core is accessible via mass transit to the top recruitment populations for suburban employees in all directions. As the largest metro transit system in the U.S. outside of the east coast corridor, Amtrak and Metra trains provide efficient connections to Ogilvie Station and Union Station, that latter of which is the #4 busiest rail station in the U.S. by ridership.',
      location: {
        center: [-87.74011, 42.02653],
        zoom: 8.25,
        pitch: 0.00,
        bearing: 0.00
      },
      onChapterEnter: [{
          layer: 'cta-l-lines',
          opacity: 0
        },
        {
          layer: 'metra-lines',
          opacity: 1
        },
        {
          layer: 'metra-stations-updated',
          opacity: 1
        },
      ],
      onChapterExit: [{
          layer: 'metra-lines',
          opacity: .5
        },
        {
          layer: 'metra-stations-updated',
          opacity: .5
        },
      ]
    },
    {
      id: 'suburban',
      image: 'https://dk7h73956znl6.cloudfront.net/income_scale.png',
      title: 'Access to Suburban Talent',
      description: 'Along these commuter rail lines an analysis of 2017 IRS income data indicates the highest suburban concentrations of +$100,000 earners reside in communities north and west of downtown. These suburbs are serviced primarily by the Union Pacific North and Union Pacific Northwest (to Ogilvie Station) and the Burlington North Santa Fe (to Union Station).',
      location: {
        center: [-87.74011, 42.02653],
        zoom: 8.25,
        pitch: 0.00,
        bearing: 0.00
      },
      onChapterEnter: [{
          layer: 'chicago-irs',
          opacity: .60
        },
      ],
      onChapterExit: [{
          layer: 'metra-lines',
          opacity: 0
        },
        {
          layer: 'metra-stations-updated',
          opacity: 0
        }
      ]
    },
    {
      id: 'city',
      image: 'https://dk7h73956znl6.cloudfront.net/income_scale.png',
      title: 'Access to City Talent',
      description: 'In the city the highest concentrations of six-figure earners can be found in neighborhoods north and northwest and increasingly within the CBD core itself. These leading city zip codes contain over 75,000 filers with earnings over $100,000/year across established neighborhoods including Lincoln Park, Bucktown and Wicker Park that are serviced by CTA Blue and Brown lines. Also included are downtown neighborhoods exhibiting some of the best density and demographics in the U.S. where the top CBD income concentrations can be found in River North (48%), Streeterville (46%) and Fulton Market (42%).',
      location: {
        center: { lon: -87.65577, lat: 41.90434 },
        zoom: 13.05,
        pitch: 0.00,
        bearing: 0.00
      },
      onChapterEnter: [
      ],
      onChapterExit: [
        {
          layer: 'cta-l-lines',
          opacity: .55
        },
        {
          layer: 'chicago-irs',
          opacity: 0
        },
      ]
    },
    {
      id: 'dxzoning',
      title: '2016: Expanded "DX" Zoning',
      description: 'In 2016 City Council approved updates to the zoning code governing the downtown "DX" floor area bonus system and an expansion of the downtown zoning district boundaries. Under the moniker "Neighborhood Opportunity Bonus", the changes were introduced to accommodate rapid growth in demand by increasing allowable density in high-demand areas served by transit to the north and west of the conventional downtown core.',
      location: {
        center: { lon: -87.65518, lat: 41.88858 },
        zoom: 13.72,
        pitch: 0.00,
        bearing: 0.00
      },
      onChapterEnter: [{
        layer: 'downtownzoning',
        opacity: .65
      },
      {
        layer: 'road-label',
        opacity: 1
      },
    ],
      onChapterExit: [{
        layer: 'downtownzoning',
        opacity: 0
      }, ]
    },
    {
      id: 'northbranchzoning',
      title: '2017: Removed "PMD" Zoning',
      image: 'https://dk7h73956znl6.cloudfront.net/historical_chicago_ave_bridge.jpg',
      description: 'Shortly thereafter, in 2017 the Department of Planning concluded a two-year long comprehensive re-zoning process encompassing 750-acres of land on the North Branch of the Chicago River. The “modernization” land use and transportation framework effectively eliminated restrictive industrial zoning along the river with a goal to transform large scale underutilized sites into vibrant mixed-use developments each offering new grand-scale open spaces and river access.',
      location: {
        center: [-87.65929, 41.90447],
        zoom: 13.43,
        pitch: 0.00,
        bearing: 0.00
      },
      onChapterEnter: [{
          layer: 'cta-l-lines',
          opacity: 0
        },
        {
          layer: 'large-parcels-3',
          opacity: 0
        },
        {
          layer: 'northbranchzoning',
          opacity: .65
        },
      ],
      onChapterExit: [{
          layer: 'northbranchzoning',
          opacity: 0
        },
        {
          layer: 'large-parcels-3',
          opacity: 1
        },
      ]
    },
    {
      id: 'master_plans',
      title: '2018: Zoned Master Planned Sites',
      description: 'In 2018, the City separately approved rezoning of three major industrial sites to enable city-scale redevelopments resulting from the new framework. Known as the Chicago Tribune (center), The 78 (south) and Lincoln Yards (north), each site is approved for between 11 up to 15 million square feet of high-density development. Each of these sites contemplate roughly 50% office use within the program and plan to seek corporate anchor tenants for an official launch.',
      location: {
        center: { lon: -87.65837, lat: 41.89165 },
        zoom: 12.97,
        pitch: 0.00,
        bearing: 0.00
      },
      onChapterEnter: [
        {
          layer: 'road-label',
          opacity: 0
        },
        {
          layer: 'large-parcels-3',
          opacity: 1
        },
      ],
      onChapterExit: [
      ]
    },
    {
      id: 'transitwayline',
      title: '3-Mile "North Branch Transitway"',
      image: 'https://dk7h73956znl6.cloudfront.net/transitway.jpeg',
      description: 'Within the modernization framework the City identified a number of transportation projects throughout the corridor to improve public transportation. Most significant is the “North Branch Transitway” (green line), which calls for a repurposing of an unused 3-mile freight rail spur into a dedicated pedestrian and Bus Rapid Transit (BRT) corridor anchored by Union Station and Ogilvie Station at the south and the Metra Clybourn and 606 Trail to the north. Legal procedures to commence this project are underway at the north leg of the Transitway and development of the Tribune site will enable the southern end of the corridor.',
      location: {
        center: { lon: -87.66897, lat: 41.89806 },
        zoom: 13.49,
        pitch: 0.00,
        bearing: 0.00
      },
      onChapterEnter: [{
        layer: 'transitway',
        opacity: 1
      },
      {
        layer: 'walkshed-commuter',
        opacity: .25
      },],
      onChapterExit: [{
          layer: 'transitway',
          opacity: 0
        },
        {
          layer: 'walkshed-commuter',
          opacity: 0
        },
      ]
    },
    {
      id: 'riverwalk',
      title: '2015-2017: Main Branch Riverwalk',
      image: 'https://dk7h73956znl6.cloudfront.net/chicagoriverwalk-Season-Celebration.jpg',
      description: 'Completed up to Lake Street in 2017, the Main Branch Riverwalk has quickly become one of the City’s top attractions for residents and tourists alike. As the #3 most visited urban linear park in the U.S., behind only NYC’s High Line and the San Antonio Riverwalk, properties adjacent to the Main Branch are witnessing broad based demand from the City’s leading global corporations, luxury residences, premiere hospitality brands, and upscale retailers and restaurants.',
      location: {
        center: [-87.62922, 41.88744],
        zoom: 16.38,
        pitch: 53.00,
        bearing: -89.39
      },
      onChapterEnter: [{
        layer: '3d-buildings',
        opacity: 1
      }, ],
      onChapterExit: []
    },
    {
      id: 'confluence',
      title: 'Chicago River Confluence - Phase 1 Tower North',
      image: 'https://dk7h73956znl6.cloudfront.net/confluence_north.png',
      description: 'Since 2016 over 3.5 million square feet of Class +A office has been delivered or is leased in new construction around the Confluence. Now home to an array of businesses within diverse industries including William Blair, Salesforce, Hyatt Corporation, Bank of America, McDermott Will & Emery, DLA Piper and Mead Johnson, these tenants reflect an appreciation for the river with its unparalleled light, air, and views, and have solidified the river as the location of choice for Chicago’s leading corporations.',
      location: {
        center: [-87.63837, 41.88675],
        zoom: 16.15,
        pitch: 53.50,
        bearing: -28.80
      },
      onChapterEnter: [],
      onChapterExit: [{
        layer: '3d-buildings',
        opacity: 0
      }, ]
    },
    {
      id: 'infill',
      title: 'Completed Projects - Tribune is the Only Infill Site',
      description: 'Of the three new blank slate sites, Tribune is the only property immediately contiguous to downtown, central to existing development patterns, and which offers an ability to utilize existing mass transit infrastructure. Evidencing demand around the location, within a 20-minute walk from Phase 1 at Grand Avenue, 16,000 luxury residential units (44% of all CBD deliveries) and 15.5 million square feet of Class +A office (74% of all CBD deliveries) have been delivered during the past 10 years.',
      location: {
        center: { lon: -87.65837, lat: 41.89165 },
        zoom: 12.97,
        pitch: 0.00,
        bearing: 0.00
      },
      onChapterEnter: [{
          layer: 'cta-l-lines',
          opacity: .55
        },
        {
          layer: 'chicago-cbd-supply-to-date',
          opacity: 1
        },
        {
          layer: 'chicago-cbd-supply-to-date-label',
          opacity: 1
        },
        {
          layer: 'trib-20min',
          opacity: .25
        },
      ],
      onChapterExit: [{
        layer: 'chicago-cbd-supply-to-date',
        opacity: 0
      },
      {
        layer: 'chicago-cbd-supply-to-date-label',
        opacity: 0
      },
      {
        layer: 'trib-20min',
        opacity: 0
      },
      ]
    },
    {
      id: 'fulton',
      image: 'https://dk7h73956znl6.cloudfront.net/fultonmarketdistrict.jpg',
      title: 'Planned Projects - Tribune is Centrally Located',
      description: 'For all of its success, Fulton Market’s growth depends on a continual push west, whereas the Tribune site is infill to downtown’s highest performing submarkets. Future office product in the CBD is concentrated in Fulton Market (+6 million square feet planned) where investors have purchased nearly all industrial sites of significance in the past 5 years. Major residential projects are being zoned at Greyhound and Moody Bible, just north and east of Tribune, which together total +6,000 new units, and will effectively close out River North’s post-recession development frenzy marching up to and then past Chicago Avenue.',
      location: {
        center: { lon: -87.64699, lat: 41.88622 },
        zoom: 14.29,
        pitch: 0.00,
        bearing: 0.00
      },
      onChapterEnter: [{
          layer: 'planned',
          opacity: 1
        },
        {
          layer: 'planned_labels',
          opacity: 1
        },
      ],
      onChapterExit: [
      ]
    },
    {
      id: 'cta_walksheds',
      title: 'CTA “L” – 5 Minute Walksheds',
      description: 'Tribune is serviced by four CTA stations in under .5 miles that currently handle over 26,000 weekday riders. Phase 1 at Grand Avenue is .25 miles to Grand/Halsted CTA Blue, .45 miles to the CTA Brown at The Mart and .75 miles to CTA Red at Grand/State. Fulton Market is well served by the CTA Green line at Morgan, however for most employees in the submarket utilizing this station entails transferring from other lines in the Loop at State/Lake. In Fulton Market, even the most transit accessible sites along Halsted are inferior to Tribune Phase 1 relative to the CTA Blue, Brown and Red line proximity.',
      location: {
        center: { lon: -87.64699, lat: 41.88622 },
        zoom: 14.29,
        pitch: 0.00,
        bearing: 0.00
      },
      onChapterEnter: [{
          layer: 'cta-5min',
          opacity: .25
        },
      ],
      onChapterExit: [{
            layer: 'cta-5min',
            opacity: 0
        },
      ]
    },
    {
      id: 'commuter_walksheds',
      title: 'Ogilvie and Union Station – 10 Minute Walksheds',
      description: 'Access to commuter rail stations remains essential for office development sites to appeal to the broadest number of end users and employees. System wide, three lines terminate at Ogilvie Station and comprise 30% of all suburban ridership while eight lines terminate at Union Station representing 55% of all suburban ridership. Nearly all planned development in Fulton Market is bound by Halsted, Lake, Kinzie and Ogden. This submarket begins at Halsted Street .4 miles west of Ogilvie, whereas the Tribune property begins .6 miles north at Grand Avenue. Such walking distances are roughly equivalent to 300 N LaSalle in River North or east to Dearborn/State Streets in the Loop. Relative to Union Station, both submarkets are at similar disadvantages compared to the Loop/West Loop, but on par with the majority of office stock in River North.',
      location: {
        center: { lon: -87.64699, lat: 41.88622 },
        zoom: 14.29,
        pitch: 0.00,
        bearing: 0.00
      },
      onChapterEnter: [{
          layer: 'walkshed-commuter',
          opacity: .35
        },
      ],
      onChapterExit: [{
          layer: 'walkshed-commuter',
          opacity: 0
        },
        {
          layer: 'planned',
          opacity: 0
        },
        {
          layer: 'planned_labels',
          opacity: 0
        },
      ]
    },
    {
      id: 'techhubs',
      title: 'Tribune Site – Proven Tech Location',
      image: 'https://dk7h73956znl6.cloudfront.net/600_aerial.jpg',
      description: 'The Tribune property is anchored by Chicago’s most prominent technology and innovation hubs. Since 2015 The Mart (south) has repositioned from furniture showroom to a leading destination for corporate headquarters and is the home of 1871 which ranked as the #1 University affiliated incubator in the world” in 2018. To the north is 600 W. Chicago, home of serial start-up, venture capital and entrepreneurship firm Lightbank. The former Montgomery Ward warehouse contains an ecosystem of both mature and high growth technology companies. Both facilities serve as vibrant hubs, attracting employees in some of the most competitive recruitment fields in the city.',
      location: {
        center: [-87.64409, 41.89739],
        zoom: 15.87,
        pitch: 57.50,
        bearing: 115.97
      },
      onChapterEnter: [
        {
          layer: '3d-buildings',
          opacity: .75
        },
      ],
      onChapterExit: []
    },
    {
      id: 'tribune_montgomery',
      title: 'Tribune Site – Connecting to Montgomery Ward Park',
      image: 'https://dk7h73956znl6.cloudfront.net/montgomery_ward_skyline.jpg',
      description: 'Directly across the river from Tribune Phase 1 is River North’s largest park. The A. Montgomery Ward Park contains 4-acres of green space, playgrounds, a waterfront promenade and year-round programming such as “Movies in the Park”. A future pedestrian bridge will span the river at Erie Street, improving access east between the site and River North’s dense offering of amenities, transportation, offices and residences.',
      location: {
        center: [-87.64452, 41.89533],
        zoom: 16.12,
        pitch: 42.00,
        bearing: 161.29
      },
      onChapterEnter: [],
      onChapterExit: []
    },
    {
      id: 'tribune_eastbankclub',
      title: 'Tribune Site – Adjacent to East Bank Club',
      image: 'https://dk7h73956znl6.cloudfront.net/ebc_exterior_river.jpg',
      description: 'As one of the largest private fitness facilities in the U.S. offering +450,000 square feet of fitness, dining, and resort style amenities, the East Bank Club is Chicago’s premier health club. Covering over two full city blocks, the Club offers an array of constantly evolving amenities, state-of-the-art exercise facilities and serves as the unofficial Town Square for River North office workers and residents.',
      location: {
        center: [-87.64177, 41.89010],
        zoom: 16.30,
        pitch: 48.50,
        bearing: 81.45
      },
      onChapterEnter: [],
      onChapterExit: []
    },
    {
      id: 'tribune_grandavebridge',
      title: 'Tribune Site – Connecting River North, River West & the West Loop',
      image: 'https://dk7h73956znl6.cloudfront.net/kinzie-park.jpg',
      description: 'Phase 1 of the Tribune master plan will commence at Grand Avenue, transforming a currently barren riverfront parking lot from pedestrian barrier to pedestrian magnet. Delivering over 2 million square feet of office and residential development, 850’ of new Riverwalk and 4-acres of open space, Phase 1 will not only be a destination unto itself, but also serve to stitch together the River North and River West neighborhoods and become a new gateway between the West Loop and future development north within the Tribune master plan.',
      location: {
        center: [-87.64116, 41.89144],
        zoom: 16.58,
        pitch: 60.00,
        bearing: 149.29
      },
      onChapterEnter: [],
      onChapterExit: [
        {
          layer: '3d-buildings',
          opacity: 0
        },]
    },
    {
      id: 'sites_planned_all',
      image: 'https://dk7h73956znl6.cloudfront.net/grand_two_towers.png',
      title: 'Tribune Site - Phase 1 Office Towers',
      description: 'Conceptual rendering of Phase 1 office towers totaling 1 million square feet, prominently situated along the river between Grand Avenue and Ohio Street feeder.',
      location: {
        center: [-87.64451, 41.88737],
        zoom: 13.64,
        pitch: 0.50,
        bearing: 0.20
      },
      onChapterEnter: [  {
        layer: 'cta-l-lines',
        opacity: .0
        },
        {
        layer: 'road-label',
        opacity: 1
        },
      ],
      onChapterExit: [
      ]
    },
    //final brackets for
  ]
};
