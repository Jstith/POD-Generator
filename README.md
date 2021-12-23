__POD Generator__
================

By: _Jstith_

## Description

This program takes in user input and generates a POD (Plan of the Day) in Markdown format for use on the markdown-rendered sharepoint site for the USCGA PODs. This program will allow cadets to create markdown PODs without needing to understand writing markdown code. This repository also holds the necessary information to format the PODs with markdown by hand if necessary.

#  Distribution

The program is written in python with pysimplegui, but the intended distribution is as a stand-alone windows binary for use on cadet laptops. For this reason, all data and functionality is contained in a single file for simple compiling with pyinstaller.

# Markdown Format

```markdown
# Weekday DD Month YYYY
**CHDO** - [name with two blank spaces after]  
**RCDO** - [name with two blank spaces after]  
**ACDO** - [name with two blank spaces after]  
**Duty Section** - [company with two blank spaces after]  
**Uniform** - Operational Dress Uniforms with Class-Specific Ballcaps and **Parkas**

0600: Reveille

0615: Guardmount

**0620: Morning Formation**

0625: Family Style Breakfast

**0700: Bold (two ** on either side of text) formations and any events special for that day**

**0730: Start events with four digit time and a colon, for example 0600:**

0800-1150: Morning Classes

**1205: Afternoon Formation**

1210: Family Style Lunch

1250-1540: Afternoon Classes

1600-1800: Sports Period

1715-1915: Buffet Dinner

1930: Restricted Cadet Formation

2200: Taps/Restricted Cadet Formation
```
