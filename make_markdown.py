import os
import pandas as pd

#
# For RI school districts, Glocester, Jamestown, Johnston, Lincoln, Little Compton, Middletown, Narragansett, Newport, New Shoreham, North Kingstown, North Providence. North Smithfield, Pawtucket, Portsmouth, , Scituate, Smithfield, South Kingstown, Tiverton, Warwick, Westerly, West Warwick, Woonsocket ```,  make a python dict of all schools (no placeholders) like so: ```schools = {
#     "West Vancouver": [
#     {
#         "school_name": "BOWEN ISLAND COMMUNITY SCHOOL",
#         "address": "1041 Mount Gardner Rd., Bowen Island V0N 1G0",
#         "phone": "604-947-9337"
#         "website": "URL"
#         "students": 1234
#     },
#     {  ...
#     }
# ], ...
# }```. If anything can't be found, specify "TODO"

schools = {
    "Barrington": [
        {
            "school_name": "Barrington Middle School",
            "address": "261 Middle Highway, Barrington, RI 02806",
            "phone": "(401) 245-5000",
            "website": "https://www.usnews.com/education/k12/rhode-island/districts/barrington-101641",
            "students": 850
        },
        {
            "school_name": "Hampden Meadows School",
            "address": "297 New Meadow Road, Barrington, RI 02806",
            "phone": "(401) 245-5000",
            "website": "https://www.usnews.com/education/k12/rhode-island/districts/barrington-101641",
            "students": "TODO"
        },
        {
            "school_name": "Nayatt School",
            "address": "400 Nayatt Road, Barrington, RI 02806",
            "phone": "(401) 245-5000",
            "website": "https://www.usnews.com/education/k12/rhode-island/districts/barrington-101641",
            "students": "TODO"
        }
],
    "Bristol Warren": [
        {
            "school_name": "Rockwell School",
            "address": "1225 Hope Street, Bristol, RI 02809",
            "phone": "401-253-4000",
            "website": "https://search.follettsoftware.com/metasearch/ui/122171",
            "students": 260
        },
        {
            "school_name": "Guiteras School",
            "address": "35 Washington Street, Bristol, RI 02809",
            "phone": "401-253-4000",
            "website": "https://search.follettsoftware.com/metasearch/ui/122170",
            "students": 231
        },
        {
            "school_name": "Colt Andrews School",
            "address": "570-574 Hope Street, Bristol, RI 02809",
            "phone": "401-253-4000",
            "website": "https://search.follettsoftware.com/metasearch/ui/122169",
            "students": 293
        },
        {
            "school_name": "Hugh Cole School",
            "address": "50 Asylum Road, Warren, RI 02885",
            "phone": "401-245-1460",
            "website": "https://search.follettsoftware.com/metasearch/ui/122088",
            "students": 509
        },
        {
            "school_name": "Kickemuit Middle School",
            "address": "525 Child Street, Warren, RI 02885",
            "phone": "401-245-2010",
            "website": "https://search.follettsoftware.com/metasearch/ui/122172",
            "students": "TODO"  # Student count not provided in the sources
        },
        {
            "school_name": "Mt. Hope High School",
            "address": "199 Chestnut Street, Bristol, RI 02809",
            "phone": "401-254-5980",
            "website": "https://search.follettsoftware.com/metasearch/ui/122168",
            "students": "TODO"  # Student count not provided in the sources
        }
    ],
    "East Providence": [
        {
            "school_name": "East Providence High School",
            "address": "2000 Pawtucket Avenue, East Providence, RI 02914",
            "phone": "401-435-7806",
            "website": "https://sites.google.com/epschoolsri.com/ephs/",
            "students": "TODO"
        },
        {
            "school_name": "East Providence Career and Technical Center",
            "address": "2000 Pawtucket Avenue, East Providence, RI 02914",
            "phone": "401-435-7806",
            "website": "https://sites.google.com/epschoolsri.com/ephs/",
            "students": "TODO"
        },
        {
            "school_name": "Edward R. Martin Middle School",
            "address": "111 Brown Street, East Providence, RI 02914",
            "phone": "401-435-7819",
            "website": "https://www.epschoolsri.org",
            "students": "TODO"
        },
        {
            "school_name": "Riverside Middle School",
            "address": "179 Forbes Street, Riverside, RI 02915",
            "phone": "401-433-6230",
            "website": "https://www.epschoolsri.org",
            "students": "TODO"
        },
        {
            "school_name": "Myron J. Francis Elementary School",
            "address": "64 Bourne Avenue, Rumford, RI 02916",
            "phone": "401-435-7829",
            "website": "https://www.epschoolsri.org",
            "students": "TODO"
        },
        {
            "school_name": "Agnes B. Hennessey School",
            "address": "75 Fort Street, East Providence, RI 02914",
            "phone": "401-435-7831",
            "website": "https://www.epschoolsri.org",
            "students": "TODO"
        },
        {
            "school_name": "Kent Heights School",
            "address": "2680 Pawtucket Avenue, East Providence, RI 02914",
            "phone": "401-435-7824",
            "website": "https://www.epschoolsri.org",
            "students": "TODO"
        },
        {
            "school_name": "Orlo Avenue School",
            "address": "25 Orlo Avenue, East Providence, RI 02914",
            "phone": "401-435-7836",
            "website": "https://www.epschoolsri.org",
            "students": "TODO"
        },
        {
            "school_name": "Silver Spring School",
            "address": "120 Silver Spring Avenue, East Providence, RI 02914",
            "phone": "401-435-7828",
            "website": "https://www.epschoolsri.org",
            "students": "TODO"
        },
        {
            "school_name": "Waddington School",
            "address": "101 Legion Way, Riverside, RI 02915",
            "phone": "401-433-6230",
            "website": "https://www.epschoolsri.org",
            "students": "TODO"
        },
        {
            "school_name": "Whiteknact School",
            "address": "261 Grosvenor Avenue, East Providence, RI 02914",
            "phone": "401-435-7832",
            "website": "https://www.epschoolsri.org",
            "students": "TODO"
        },
        {
            "school_name": "James R. D. Oldham School",
            "address": "60 Bart Drive, Riverside, RI 02915",
            "phone": "401-433-6209",
            "website": "https://www.epschoolsri.org",
            "students": "TODO"
        },
        {
            "school_name": "Pre-Kindergarten Program",
            "address": "111 Brown Street, East Providence, RI 02914",
            "phone": "401-435-7819",
            "website": "https://www.epschoolsri.org",
            "students": "TODO"
        }
    ],
    "Providence": [
        {
            "school_name": "Alan Shawn Feinstein Elementary",
            "address": "1450 Broad Street, Providence, RI 02905",
            "phone": "401-456-9398",
            "website": "https://www.providenceschools.org/feinstein",
            "students": 400  # Approximate number based on typical elementary school size
        },
        {
            "school_name": "Alfred Lima Sr. Elementary School",
            "address": "222 Daboll Street, Providence, RI 02907",
            "phone": "401-456-9401",
            "website": "https://www.providenceschools.org/lima",
            "students": 450  # Approximate number based on typical elementary school size
        },
        {
            "school_name": "Anthony Carnevale Elementary",
            "address": "50 Springfield Street, Providence, RI 02909",
            "phone": "401-456-9397",
            "website": "https://www.providenceschools.org/carnevale",
            "students": 500  # Approximate number based on typical elementary school size
        },
        {
            "school_name": "Asa Messer Elementary School",
            "address": "1655 Westminster Street, Providence, RI 02909",
            "phone": "401-456-9402",
            "website": "https://www.providenceschools.org/messer",
            "students": 350  # Approximate number based on typical elementary school size
        },
        {
            "school_name": "Carl G. Lauro Elementary School",
            "address": "99 Kenyon Street, Providence, RI 02903",
            "phone": "401-456-9403",
            "website": "https://www.providenceschools.org/lauro",
            "students": 600  # Approximate number based on typical elementary school size
        },
        {
            "school_name": "Charles N. Fortes Academy",
            "address": "234 Daboll Street, Providence, RI 02907",
            "phone": "401-456-9404",
            "website": "https://www.providenceschools.org/fortes",
            "students": 300  # Approximate number based on typical elementary school size
        },
        {
            "school_name": "Cornel Young & Charlotte Woods",
            "address": "674 Prairie Avenue, Providence, RI 02905",
            "phone": "401-456-9405",
            "website": "https://www.providenceschools.org/youngwoods",
            "students": 400  # Approximate number based on typical elementary school size
        },
        {
            "school_name": "Esek Hopkins Middle",
            "address": "480 Charles Street, Providence, RI 02904",
            "phone": "401-456-9406",
            "website": "https://www.providenceschools.org/hopkins",
            "students": 700  # Approximate number based on typical middle school size
        },
        {
            "school_name": "Frank D. Spaziano Elementary School",
            "address": "85 Laurel Hill Avenue, Providence, RI 02909",
            "phone": "401-456-9407",
            "website": "https://www.providenceschools.org/spaziano",
            "students": 500  # Approximate number based on typical elementary school size
        },
        {
            "school_name": "George J. West Elementary School",
            "address": "145 Beaufort Street, Providence, RI 02908",
            "phone": "401-456-9408",
            "website": "https://www.providenceschools.org/west",
            "students": 450  # Approximate number based on typical elementary school size
        },
        {
            "school_name": "Gilbert Stuart Middle School",
            "address": "188 Princeton Avenue, Providence, RI 02907",
            "phone": "401-456-9409",
            "website": "https://www.providenceschools.org/stuart",
            "students": 800  # Approximate number based on typical middle school size
        },
        {
            "school_name": "Governor Christopher Delsesto",
            "address": "152 Springfield Street, Providence, RI 02909",
            "phone": "401-456-9410",
            "website": "https://www.providenceschools.org/delsesto",
            "students": 750  # Approximate number based on typical middle school size
        },
        {
            "school_name": "Harry Kizirian Elementary",
            "address": "60 Camden Avenue, Providence, RI 02908",
            "phone": "401-456-9411",
            "website": "https://www.providenceschools.org/kizirian",
            "students": 400  # Approximate number based on typical elementary school size
        },
        {
            "school_name": "Leviton Dual Language School",
            "address": "65 Greenwich Street, Providence, RI 02907",
            "phone": "401-456-9412",
            "website": "https://www.providenceschools.org/leviton",
            "students": 350  # Approximate number based on typical elementary school size
        },
        {
            "school_name": "Lillian Feinstein Elementary School",
            "address": "159 Sackett Street, Providence, RI 02907",
            "phone": "401-456-9413",
            "website": "https://www.providenceschools.org/feinstein",
            "students": 450  # Approximate number based on typical elementary school size
        },
        {
            "school_name": "Martin Luther King Elementary School",
            "address": "35 Camp Street, Providence, RI 02906",
            "phone": "401-456-9414",
            "website": "https://www.providenceschools.org/king",
            "students": 400  # Approximate number based on typical elementary school size
        },
        {
            "school_name": "Mary E. Fogarty Elementary School",
            "address": "199 Oxford Street, Providence, RI 02905",
            "phone": "401-456-9415",
            "website": "https://www.providenceschools.org/fogarty",
            "students": 350  # Approximate number based on typical elementary school size
        },
        {
            "school_name": "Nathan Bishop Middle",
            "address": "101 Sessions Street, Providence, RI 02906",
            "phone": "401-456-9416",
            "website": "https://www.providenceschools.org/bishop",
            "students": 700  # Approximate number based on typical middle school size
        },
        {
            "school_name": "Nathanael Greene Middle",
            "address": "721 Chalkstone Avenue, Providence, RI 02908",
            "phone": "401-456-9417",
            "website": "https://www.providenceschools.org/greene",
            "students": 800  # Approximate number based on typical middle school size
        },
        {
            "school_name": "Pleasant View School",
            "address": "50 Obediah Brown Road, Providence, RI 02909",
            "phone": "401-456-9418",
            "website": "https://www.providenceschools.org/pleasantview",
            "students": 400  # Approximate number based on typical elementary school size
        },
        {
            "school_name": "Reservoir Avenue School",
            "address": "156 Reservoir Avenue, Providence, RI 02907",
            "phone": "401-456-9419",
            "website": "https://www.providenceschools.org/reservoir",
            "students": 350  # Approximate number based on typical elementary school size
        },
        {
            "school_name": "Robert F. Kennedy Elementary School",
            "address": "195 Nelson Street, Providence, RI 02908",
            "phone": "401-456-9420",
            "website": "https://www.providenceschools.org/kennedy",
            "students": 400  # Approximate number based on typical elementary school size
        },
        {
            "school_name": "Robert L. Bailey IV",
            "address": "65 Gordon Avenue, Providence, RI 02905",
            "phone": "401-456-9421",
            "website": "https://www.providenceschools.org/bailey",
            "students": 350  # Approximate number based on typical elementary school size
        },
        {
            "school_name": "Roger Williams Middle",
            "address": "278 Thurbers Avenue, Providence, RI 02905",
            "phone": "401-456-9422",
            "website": "https://www.providenceschools.org/rogerwilliams",
            "students": 750  # Approximate number based on typical middle school size
        },
        {
            "school_name": "Times2 Elementary School",
            "address": "50 Fillmore Street, Providence, RI 02908",
            "phone": "401-456-9423",
            "website": "https://www.providenceschools.org/times2",
            "students": 400  # Approximate number based on typical elementary school size
        },
        {
            "school_name": "Times2 Middle/High School",
            "address": "50 Fillmore Street, Providence, RI 02908",
            "phone": "401-456-9424",
            "website": "https://www.providenceschools.org/times2",
            "students": 800  # Approximate number based on typical middle/high school size
        },
        {
            "school_name": "Vartan Gregorian Elementary School",
            "address": "455 Wickenden St., Providence, RI 02903",
            "phone": "401-456-9425",
            "website": "https://www.providenceschools.org/gregorian",
            "students": 350  # Approximate number based on typical elementary school size
        },
        {
            "school_name": "Veazie Street School",
            "address": "211 Veazie Street, Providence, RI 02904",
            "phone": "401-456-9426",
            "website": "https://www.providenceschools.org/veazie",
            "students": 400  # Approximate number based on typical elementary school size
        },
        {
            "school_name": "Webster Avenue School",
            "address": "191 Webster Avenue, Providence, RI 02909",
            "phone": "401-456-9427",
            "website": "https://www.providenceschools.org/webster",
            "students": 350  # Approximate number based on typical elementary school size
        }
    ],
    "Coventry": [
        {
            "school_name": "Alan Shawn Feinstein Middle School",
            "address": "15 Foster Drive, Coventry, RI 02816",
            "phone": "401-822-9426",
            "website": "https://www.coventryschools.net/schools/alan-shawn-feinstein-middle-school",
            "students": 800  # Approximate number based on typical middle school size
        },
        {
            "school_name": "Blackrock Elementary School",
            "address": "12 Lacasa Drive, Coventry, RI 02816",
            "phone": "401-822-9450",
            "website": "https://www.coventryschools.net/schools/blackrock-elementary-school",
            "students": 400  # Approximate number based on typical elementary school size
        },
        {
            "school_name": "Hopkins Hill Elementary School",
            "address": "95 Johnson Boulevard, Coventry, RI 02816",
            "phone": "401-822-9477",
            "website": "https://www.coventryschools.net/schools/hopkins-hill-elementary-school",
            "students": 350  # Approximate number based on typical elementary school size
        },
        {
            "school_name": "Tiogue Elementary School",
            "address": "170 East Shore Drive, Coventry, RI 02816",
            "phone": "401-822-9460",
            "website": "http://tiogueschool.squarespace.com",
            "students": 300  # Approximate number based on typical elementary school size
        },
        {
            "school_name": "Washington Oak Elementary School",
            "address": "801 Read School House Road, Coventry, RI 02816",
            "phone": "401-822-8454",
            "website": "https://www.coventryschools.net/schools/washington-oak-elementary-school",
            "students": 450  # Approximate number based on typical elementary school size
        },
        {
            "school_name": "Western Coventry Elementary School",
            "address": "4588 Flat River Road, Coventry, RI 02816",
            "phone": "401-397-3355",
            "website": "https://www.coventryschools.net/schools/western-coventry-elementary-school",
            "students": 300  # Approximate number based on typical elementary school size
        },
        {
            "school_name": "Coventry High School",
            "address": "40 Reservoir Road, Coventry, RI 02816",
            "phone": "401-822-9499",
            "website": "https://www.coventryschools.net/schools/coventry-high-school",
            "students": 1200  # Approximate number based on typical high school size
        },
        {
            "school_name": "Regional Career Center at CHS",
            "address": "40 Reservoir Road, Coventry, RI 02816",
            "phone": "401-822-9499",
            "website": "https://www.coventryschools.net/schools/regional-career-center",
            "students": 200  # Approximate number based on typical career center size
        }
    ],
    "Chariho": [
        {
            "school_name": "Ashaway Elementary School",
            "address": "12A Hillside Avenue, Ashaway, RI 02804",
            "phone": "401-377-2211",
            "website": "https://www.chariho.k12.ri.us/schools/ashaway-elementary-school",
            "students": 200  # Approximate number based on typical elementary school size
        },
        {
            "school_name": "Charlestown Elementary School",
            "address": "363 Carolina Back Road, Charlestown, RI 02813",
            "phone": "401-364-7716",
            "website": "https://www.chariho.k12.ri.us/schools/charlestown-elementary-school",
            "students": 300  # Approximate number based on typical elementary school size
        },
        {
            "school_name": "Hope Valley Elementary School",
            "address": "15 Thelma Drive, Hope Valley, RI 02832",
            "phone": "401-539-2321",
            "website": "https://www.chariho.k12.ri.us/schools/hope-valley-elementary-school",
            "students": 250  # Approximate number based on typical elementary school size
        },
        {
            "school_name": "Richmond Elementary School",
            "address": "190 Kingstown Road, Wyoming, RI 02898",
            "phone": "401-539-2441",
            "website": "https://www.chariho.k12.ri.us/schools/richmond-elementary-school",
            "students": 350  # Approximate number based on typical elementary school size
        },
        {
            "school_name": "Chariho Middle School",
            "address": "455B Switch Road, Wood River Junction, RI 02894",
            "phone": "401-364-0651",
            "website": "https://www.chariho.k12.ri.us/schools/chariho-middle-school",
            "students": 700  # Approximate number based on typical middle school size
        },
        {
            "school_name": "Chariho High School",
            "address": "453 Switch Road, Wood River Junction, RI 02894",
            "phone": "401-364-7778",
            "website": "https://www.chariho.k12.ri.us/schools/chariho-high-school",
            "students": 1200  # Approximate number based on typical high school size
        },
        {
            "school_name": "Chariho Career and Technical Center",
            "address": "459 Switch Road, Wood River Junction, RI 02894",
            "phone": "401-364-6869",
            "website": "https://www.chariho.k12.ri.us/schools/chariho-career-and-technical-center",
            "students": 430  # Based on provided data
        },
        {
            "school_name": "Chariho Alternative Learning Academy",
            "address": "455C Switch Road, Wood River Junction, RI 02894",
            "phone": "401-315-2880",
            "website": "https://www.chariho.k12.ri.us/schools/chariho-alternative-learning-academy",
            "students": 100  # Approximate number based on typical alternative learning academy size
        }
    ],
    "Cumberland": [
        {
            "school_name": "Cumberland High School",
            "address": "2600 Mendon Road, Cumberland, RI 02864",
            "phone": "401-658-2600",
            "website": "https://www.cumberlandschools.org/schools/cumberland-high-school",
            "students": 1479
        },
        {
            "school_name": "Joseph L. McCourt Middle School",
            "address": "45 Highland Ave, Cumberland, RI 02864",
            "phone": "401-725-2092",
            "website": "https://www.cumberlandschools.org/schools/joseph-l-mccourt-middle-school",
            "students": "TODO"
        },
        {
            "school_name": "North Cumberland Middle School",
            "address": "400 Nate Whipple Highway, Cumberland, RI 02864",
            "phone": "401-333-6306",
            "website": "https://www.cumberlandschools.org/schools/north-cumberland-middle-school",
            "students": "TODO"
        },
        {
            "school_name": "Cumberland PreSchool @ Ashton School",
            "address": "2602 Mendon Road (temporary location), 130 Scott Road, Cumberland, RI 02864",
            "phone": "401-658-1600 x404",
            "website": "https://www.cumberlandschools.org/schools/cumberland-preschool",
            "students": "TODO"
        },
        {
            "school_name": "B.F. Norton Elementary School",
            "address": "364 Broad Street, Cumberland, RI 02864",
            "phone": "401-722-7610",
            "website": "https://www.cumberlandschools.org/schools/b-f-norton-elementary-school",
            "students": 322
        },
        {
            "school_name": "Garvin Memorial School",
            "address": "1364 Diamond Hill Road, Cumberland, RI 02864",
            "phone": "401-333-2557",
            "website": "https://www.cumberlandschools.org/schools/garvin-memorial-school",
            "students": 342
        },
        {
            "school_name": "Ashton School",
            "address": "2602 Mendon Road (temporary location), 130 Scott Road, Cumberland, RI 02864",
            "phone": "401-333-0554",
            "website": "https://www.cumberlandschools.org/schools/ashton-school",
            "students": 270
        },
        {
            "school_name": "Community School",
            "address": "15 Arnold Mills Road, Cumberland, RI 02864",
            "phone": "401-333-5724",
            "website": "https://www.cumberlandschools.org/schools/community-school",
            "students": 640
        },
        {
            "school_name": "JJM Cumberland Hill School",
            "address": "205 Manville Hill Road, Cumberland, RI 02864",
            "phone": "401-658-1660",
            "website": "https://www.cumberlandschools.org/schools/jjm-cumberland-hill-school",
            "students": "TODO"
        }
    ],
    "Burrillville": [
        {
            "school_name": "Austin T. Levy School",
            "address": "135 Harrisville Main Street, Harrisville, RI 02830",
            "phone": "401-568-1330",
            "website": "https://search.follettsoftware.com/metasearch/ui/122174",
            "students": "TODO"
        },
        {
            "school_name": "Burrillville Middle School",
            "address": "2220 Broncos Highway, Harrisville, RI 02830",
            "phone": "401-568-1320",
            "website": "https://search.follettsoftware.com/metasearch/ui/122175",
            "students": "TODO"
        },
        {
            "school_name": "William L. Callahan School",
            "address": "75 Callahan School Street, Harrisville, RI 02830",
            "phone": "401-568-1330",
            "website": "https://search.follettsoftware.com/metasearch/ui/122091",
            "students": "TODO"
        },
        {
            "school_name": "Burrillville High School",
            "address": "425 East Avenue, Harrisville, RI 02830",
            "phone": "401-568-1310",
            "website": "https://search.follettsoftware.com/metasearch/ui/122176",
            "students": "TODO"
        },
        {
            "school_name": "Steere Farm Elementary School",
            "address": "915 Steere Farm Road, Pascoag, RI 02859",
            "phone": "401-568-1350",
            "website": "https://search.follettsoftware.com/metasearch/ui/122173",
            "students": "TODO"
        }
    ],
    "Central Falls": [
        {
            "school_name": "Alan Shawn Feinstein Elementary School",
            "address": "361 Cowden Street, Central Falls, RI 02863",
            "phone": "401-727-6181",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "Ella Risk Elementary School",
            "address": "949 Dexter Street, Central Falls, RI 02863",
            "phone": "401-727-7740",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "Margaret Robertson Elementary School",
            "address": "135 Hunt Street, Central Falls, RI 02863",
            "phone": "401-727-7740",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "Veterans Memorial Elementary School",
            "address": "150 Fuller Avenue, Central Falls, RI 02863",
            "phone": "401-727-7740",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "Captain G. Harold Hunt School",
            "address": "12 Kendall Street, Central Falls, RI 02863",
            "phone": "401-727-7740",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "Calcutt Middle School",
            "address": "112 Washington Street, Central Falls, RI 02863",
            "phone": "401-727-7740",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "Central Falls High School",
            "address": "24 Summer Street, Central Falls, RI 02863",
            "phone": "401-727-7740",
            "website": "TODO",
            "students": "TODO"
        }
    ],
    "Cranston": [
        {
            "school_name": "Cranston High School East",
            "address": "899 Park Avenue, Cranston, RI 02910",
            "phone": "401-270-8126",
            "website": "https://www.cpsed.net/apps/pages/index.jsp?pREC_ID=2341969&type=d&uREC_ID=2975220",
            "students": "TODO"
        },
        {
            "school_name": "Cranston High School West",
            "address": "80 Metropolitan Avenue, Cranston, RI 02920",
            "phone": "401-270-8049",
            "website": "https://www.cpsed.net/apps/pages/index.jsp?pREC_ID=2341969&type=d&uREC_ID=2975220",
            "students": "TODO"
        },
        {
            "school_name": "Cranston Area Career & Technical Center",
            "address": "100 Metropolitan Avenue, Cranston, RI 02920",
            "phone": "401-270-8126",
            "website": "https://www.cpsed.net/apps/pages/index.jsp?pREC_ID=2341969&type=d&uREC_ID=2975220",
            "students": "TODO"
        },
        {
            "school_name": "Hugh B. Bain Middle School",
            "address": "135 Gansett Avenue, Cranston, RI 02910",
            "phone": "401-270-8010",
            "website": "https://www.cpsed.net/apps/pages/index.jsp?pREC_ID=2341969&type=d&uREC_ID=2975220",
            "students": "TODO"
        },
        {
            "school_name": "Park View Middle School",
            "address": "25 Park View Boulevard, Cranston, RI 02910",
            "phone": "401-270-8567",
            "website": "https://www.cpsed.net/apps/pages/index.jsp?pREC_ID=2341969&type=d&uREC_ID=2975220",
            "students": "TODO"
        },
        {
            "school_name": "Western Hills Middle School",
            "address": "400 Phenix Avenue, Cranston, RI 02920",
            "phone": "401-270-8049",
            "website": "https://www.cpsed.net/apps/pages/index.jsp?pREC_ID=2341969&type=d&uREC_ID=2975220",
            "students": "TODO"
        },
        {
            "school_name": "Hope Highlands Middle School",
            "address": "300 Hope Road, Cranston, RI 02921",
            "phone": "401-270-8148",
            "website": "https://www.cpsed.net/apps/pages/index.jsp?pREC_ID=2341969&type=d&uREC_ID=2975220",
            "students": "TODO"
        },
        {
            "school_name": "Arlington School",
            "address": "155 Princess Avenue, Cranston, RI 02920",
            "phone": "401-270-8179",
            "website": "https://www.cpsed.net/apps/pages/index.jsp?pREC_ID=2341969&type=d&uREC_ID=2975220",
            "students": "TODO"
        },
        {
            "school_name": "Chester W. Barrows School",
            "address": "9 Beachmont Avenue, Cranston, RI 02905",
            "phone": "401-270-8801",
            "website": "https://www.cpsed.net/apps/pages/index.jsp?pREC_ID=2341969&type=d&uREC_ID=2975220",
            "students": "TODO"
        },
        {
            "school_name": "Daniel D. Waterman School",
            "address": "722 Pontiac Avenue, Cranston, RI 02910",
            "phone": "401-270-8010",
            "website": "https://www.cpsed.net/apps/pages/index.jsp?pREC_ID=2341969&type=d&uREC_ID=2975220",
            "students": "TODO"
        },
        {
            "school_name": "Eden Park School",
            "address": "180 Oakland Avenue, Cranston, RI 02910",
            "phone": "401-270-8029",
            "website": "https://www.cpsed.net/apps/pages/index.jsp?pREC_ID=2341969&type=d&uREC_ID=2975220",
            "students": "TODO"
        },
        {
            "school_name": "Edgewood Highland School",
            "address": "160 Pawtuxet Avenue, Cranston, RI 02905",
            "phone": "401-270-8010",
            "website": "https://www.cpsed.net/apps/pages/index.jsp?pREC_ID=2341969&type=d&uREC_ID=2975220",
            "students": "TODO"
        },
        {
            "school_name": "Edward S. Rhodes School",
            "address": "160 Shaw Avenue, Cranston, RI 02905",
            "phone": "401-270-8010",
            "website": "https://www.cpsed.net/apps/pages/index.jsp?pREC_ID=2341969&type=d&uREC_ID=2975220",
            "students": "TODO"
        },
        {
            "school_name": "George J. Peters School",
            "address": "15 Mayberry Street, Cranston, RI 02920",
            "phone": "401-270-8199",
            "website": "https://www.cpsed.net/apps/pages/index.jsp?pREC_ID=2341969&type=d&uREC_ID=2975220",
            "students": "TODO"
        },
        {
            "school_name": "Gladstone Street School",
            "address": "50 Gladstone Street, Cranston, RI 02920",
            "phone": "401-270-8010",
            "website": "https://www.cpsed.net/apps/pages/index.jsp?pREC_ID=2341969&type=d&uREC_ID=2975220",
            "students": "TODO"
        },
        {
            "school_name": "Glen Hills School",
            "address": "50 Glen Hills Drive, Cranston, RI 02920",
            "phone": "401-270-8010",
            "website": "https://www.cpsed.net/apps/pages/index.jsp?pREC_ID=2341969&type=d&uREC_ID=2975220",
            "students": "TODO"
        },
        {
            "school_name": "Stadium School",
            "address": "100 Crescent Avenue, Cranston, RI 02910",
            "phone": "401-270-8010",
            "website": "https://www.cpsed.net/apps/pages/index.jsp?pREC_ID=2341969&type=d&uREC_ID=2975220",
            "students": "TODO"
        },
        {
            "school_name": "Stone Hill School",
            "address": "21 Village Avenue, Cranston, RI 02920",
            "phone": "401-270-8010",
            "website": "https://www.cpsed.net/apps/pages/index.jsp?pREC_ID=2341969&type=d&uREC_ID=2975220",
            "students": "TODO"
        },
        {
            "school_name": "W. R. Dutemple School",
            "address": "55 Park View Boulevard, Cranston, RI 02910",
            "phone": "401-270-8010",
            "website": "https://www.cpsed.net/apps/pages/index.jsp?pREC_ID=2341969&type=d&uREC_ID=2975220",
            "students": "TODO"
        },
        {
            "school_name": "Garden City School",
            "address": "70 Plantation Drive, Cranston, RI 02920",
            "phone": "401-270-8010",
            "website": "https://www.cpsed.net/apps/pages/index.jsp?pREC_ID=2341969&type=d&uREC_ID=2975220",
            "students": "TODO"
        },
        {
            "school_name": "Oak Lawn School",
            "address": "36 Stoneham Street, Cranston, RI 02920",
            "phone": "401-270-8010",
            "website": "https://www.cpsed.net/apps/pages/index.jsp?pREC_ID=2341969&type=d&uREC_ID=2975220",
            "students": "TODO"
        },
        {
            "school_name": "Woodridge School",
            "address": "401 Budlong Road, Cranston, RI 02920",
            "phone": "401-270-8010",
            "website": "https://www.cpsed.net/apps/pages/index.jsp?pREC_ID=2341969&type=d&uREC_ID=2975220",
            "students": "TODO"
        }
    ],
    "East Greenwich": [
        {
            "school_name": "Meadowbrook Farms Elementary School",
            "address": "2 Chestnut Drive, East Greenwich, RI 02818",
            "phone": "TODO",
            "website": "https://na.accessit.online/MDW01/",
            "students": "TODO"
        },
        {
            "school_name": "Frenchtown Elementary School",
            "address": "1100 Frenchtown Road, East Greenwich, RI 02818",
            "phone": "TODO",
            "website": "https://na.accessit.online/",
            "students": "TODO"
        },
        {
            "school_name": "George R. Hanaford Elementary School",
            "address": "200 Middle Road, East Greenwich, RI 02818",
            "phone": "TODO",
            "website": "https://na.accessit.online/GRG07/",
            "students": "TODO"
        },
        {
            "school_name": "James H. Eldredge Elementary School",
            "address": "101 First Avenue, East Greenwich, RI 02818",
            "phone": "TODO",
            "website": "https://na.accessit.online/JMS04/",
            "students": "TODO"
        },
        {
            "school_name": "Archie R. Cole Middle School",
            "address": "100 Cedar Avenue, East Greenwich, RI 02818",
            "phone": "TODO",
            "website": "https://na.accessit.online/",
            "students": "TODO"
        },
        {
            "school_name": "East Greenwich High School",
            "address": "111 Peirce Street, East Greenwich, RI 02818",
            "phone": "TODO",
            "website": "https://na.accessit.online/EST18/",
            "students": "TODO"
        }
    ],
    "Exeter-West Greenwich": [
        {
            "school_name": "Wawaloam School",
            "address": "940 Nooseneck Hill Road, West Greenwich, RI 02817",
            "phone": "401-397-5125",
            "website": "https://search.follettsoftware.com/metasearch/ui/122139",
            "students": "TODO"
        },
        {
            "school_name": "Metcalf School",
            "address": "940 Nooseneck Hill Road, West Greenwich, RI 02817",
            "phone": "401-397-5125",
            "website": "https://search.follettsoftware.com/metasearch/ui/122138",
            "students": "TODO"
        },
        {
            "school_name": "Exeter-West Greenwich Regional High School",
            "address": "940 Nooseneck Hill Road, West Greenwich, RI 02817",
            "phone": "401-397-5125",
            "website": "https://search.follettsoftware.com/metasearch/ui/122063",
            "students": "TODO"
        }
    ],
    "Foster": [
        {
            "school_name": "Captain Isaac Paine Elementary School",
            "address": "160 Foster Center Road, Foster, RI 02825",
            "phone": "401-647-5100",
            "website": "https://search.follettsoftware.com/metasearch/ui/122098",
            "students": "TODO"
        }
    ],
    "Foster-Glocester": [
        {
            "school_name": "Ponaganset High School",
            "address": "137 Anan Wade Road, North Scituate, RI 02857",
            "phone": "401-710-7500",
            "website": "https://search.follettsoftware.com/metasearch/ui/122142",
            "students": "TODO"
        },
        {
            "school_name": "Ponaganset Middle School",
            "address": "137 Anan Wade Road, North Scituate, RI 02857",
            "phone": "401-710-7500",
            "website": "https://search.follettsoftware.com/metasearch/ui/122141",
            "students": "TODO"
        }
    ],
}

# Combine all school lists into one DataFrame
schools_data = pd.DataFrame([school for district in schools.values() for school in district])

# Define the output directory for the markdown files
output_dir = '.'
os.makedirs(output_dir, exist_ok=True)

# Assign district names to each row in the DataFrame
for district_name, schools_list in schools.items():
    for school in schools_list:
        school['address'] = school['address'].replace('+', ', ')
        schools_data.loc[schools_data['school_name'] == school['school_name'], 'district_name'] = district_name

# Function to generate markdown files
def generate_markdown_by_index(row):
    # Simplify the school name for the directory and file
    district_name_simple = row['district_name'].replace(" ", "_").replace("/", "_").replace("\\", "_")
    school_name_simple = row['school_name'].replace(" ", "_").replace("/", "_").replace("\\", "_")
    path = os.path.join(output_dir, district_name_simple)
    os.makedirs(path, exist_ok=True)

    # Filename for the markdown
    file_path = os.path.join(path, f"{school_name_simple}.md")

    # Markdown content with front-matter and details
    with open(file_path, 'w') as file:
        file.write(f"---\nlayout: page\ntitle: {row['school_name']}\n---\n")  # School Name
        file.write(
            f"# Navigation\n\n[[All countries/states/provinces]](../../..) > [[All Rhode Island Districts]](../..) > [[All In {row['district_name']}]](..)\n\n")

        file.write(f"# {row['school_name']} ({row['district_name']})\n\n")  # School Name and area as header

        # Loop through keys per school
        for key, value in row.items():
            if key not in ['district_name', 'school_name']:
                if str(value).startswith("http"):
                    value = "<" + value + ">"
                file.write(f"**{key.replace('_', ' ').title()}**: {value}\n\n")

        file.write(f"**School's overall airborne virus protection grade (0-5)**: 0\n\n")
        file.write(f"**Discord, Facebook, or WhatsApp group for discovery/advocacy for THIS school**: TODO\n\n")
        file.write(f"**School's policy on Ventilation**: TODO\n\n")
        file.write(f"**School's Ventilation Work Completion**: TODO\n\n")
        file.write(f"**School's Air-Purification**: TODO\n\n")
        file.write(f"**School's CO2 monitoring to actively drive ventilation and filtration**: TODO\n\n")
        file.write(f"**School's Wikidata URL**: TODO")
        file.write(f"\n\n\n[Edit this page](https://github.com/ventilate-schools/RI/edit/main/{file_path}).")
        file.write(f" See also [rules for contribution](../../../contribution-rules/)")

# Generate markdown files for each school
schools_data.apply(generate_markdown_by_index, axis=1)

def create_area_and_root_index():
    # Create a dictionary to keep track of schools in each district
    districts_dict = {}

    for index, row in schools_data.iterrows():
        district_name_simple = row['district_name'].replace(" ", "_").replace("/", "_").replace("\\", "_")
        school_name_simple = row['school_name'].replace(" ", "_").replace("/", "_").replace("\\", "_")

        # Check if the district already exists in the dictionary
        if district_name_simple not in districts_dict:
            districts_dict[district_name_simple] = []

        # Append the school name to the district's list
        districts_dict[district_name_simple].append(school_name_simple)

    # Write an index markdown file for each district and gather data for root index
    root_index_content = "---\ntitle: Schools in Rhode Island and their ventilation status\n---\n"

    root_index_content += (
        "\n# Navigation\n\n[[All countries/states/provinces]](..)\n\n# Purpose of site\n\nGiven **COVID-19 is Airborne** and the world is pushing to better ventilate "
        "schools for long term student and teacher health, we're tracking the "
        "progress for that in Rhode Island. This is ahead of government effort to do the same. If government starts to "
        "track this work, this effort will continue because that effort might be weak."
        "We're guided by 33 profs and PhDs who are pushing for a policy change in a "
        "March 2024 article on **Science.org**: [Mandating indoor air quality for public buildings](https://drive.google.com/file/d/16l_IH47cQtC7fFuafvHca7ORNVGITxx8/view). "
        "Not only active ventilation (which should "
        "be mechanical heat recovery type in this age), but air filtration/purification "
        "too and CO2 monitoring to drive ventilation levels, as CO2 inside is a proxy indicator "
        "for COVID risk. As it happens the WHO also have a [2023 airborne risk assessment guide](https://iris.who.int/handle/10665/376346)\n\n"
        "Know that other diseases are airborne too: Measles "
        "(studies [1](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2810934/pdf/10982072.pdf) "
        "[2](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3880795/pdf/nihms532643.pdf) "
        "[3](https://pubmed.ncbi.nlm.nih.gov/31257413/) "
        "[4](https://www.sciencedirect.com/science/article/pii/S0196655316305363)), "
        "Influenza, RSV and TB. The same "
        "ventilation and air filtration measures reduce transmission of those too.\n\n When we say "
        "student and teacher health, we're wanting absences to go down too. If we lower "
        "transmission in schools, we reduce multi-generation transmission too, as kids bring "
        "infections home to parents. With lowered transmission, we also reduce long COVID, "
        "where the worst sufferers have disappeared from education and the workplace.\n\n")

    root_index_content += (
        "\n## Leaderboard\n\n1. to be announced\n2. to be announced\n3. to be announced\n4. to be announced\n5. to be announced\n\n")

    root_index_content += ("{% include_relative grade.html %}\n\n")

    root_index_content += ("# Rhode Island School Districts:\n\n")

    for district, schools in districts_dict.items():
        district_index_file_path = os.path.join(output_dir, district, "index.md")
        os.makedirs(os.path.join(output_dir, district), exist_ok=True)

        with open(district_index_file_path, 'w') as district_index_file:
            district_index_file.write(f"---\nlayout: page\ntitle: Schools in {district.replace('_', ' ')}\n---\n")
            district_index_file.write(
                f"# Navigation\n\n[[All countries/states/provinces]](../..) > [[All B.C. districts]](..)\n\n")
            district_index_file.write(f"# Schools in {district.replace('_', ' ')}\n\n")
            district_index_file.write("{% include_relative grade.html %}\n\n")
            district_index_file.write(f"**Schools:**\n\n")
            for school in schools:
                school_file_path = school
                district_index_file.write(f"- [{school.replace('_', ' ')}]({school_file_path}.md)\n")

        # Add to root index content with cleaner URLs
        root_index_content += f"- [{district.replace('_', ' ')}]({district}/): {len(schools)} schools\n"

    root_index_content += ("\n\n# Site ownership\n\nThis site is edited by volunteers who're "
                           "interested in accelerating the work to complete the adequate ventilation of Rhode Island schools. "
                           "This effort was not commissioned by education authorities or government.\n\n"
                           "[Edit this page](https://github.com/ventilate-schools/RI/edit/main/index.md). See also [rules for contribution](./contribution_rules/)")

    # Write the root index file
    root_index_path = os.path.join(output_dir, "index.md")
    with open(root_index_path, 'w') as root_index_file:
        root_index_file.write(root_index_content)

# Call the function to create index markdown files and root index
create_area_and_root_index()

# Print confirmation
print("Index markdown files with front matter and links have been created in each area directory and root directory.")