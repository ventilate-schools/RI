import os
import pandas as pd

# Burrillville, Central Falls, Chariho, Coventry, Cranston, Cumberland, East Greenwich, Exeter-West Greenwich, Foster, Foster-Glocester, Glocester, Jamestown, Johnston, Lincoln, Little Compton, Middletown, Narragansett, Newport, New Shoreham, North Kingstown, North Providence. North Smithfield, Pawtucket, Portsmouth, , Scituate, Smithfield, South Kingstown, Tiverton, Warwick, Westerly, West Warwick, Woonsocket```
#
# For RI school district Providence ```,  make a python dict of all schools (no placeholders) like so: ```schools = {
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
    ]
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