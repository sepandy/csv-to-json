# Convert CSV file containing string and their translation to JSON


------------

Exported JSONs will be named after the first row items.
This script will go through all the rows and set first item of each row as key and value of other columns as value per column.

### Example
```
en, de,
Home, Heim,
About, Über,
Contact, Kontakt,
Privacy, Datenschutz,
Terms, Nutzungsbedingungen,
Copyright, Urheberrecht,
All rights reserved, Alle Rechte vorbehalten,
```

### Result

en.json
```json
{
    "Home": "Home",
    "About": "About",
    "Contact": "Contact",
    "Privacy": "Privacy",
    "Terms": "Terms",
    "Copyright": "Copyright",
    "All rights reserved": "All rights reserved"
}
```

de.json
```json
{
    "Home": "Heim",
    "About": "\u00dcber",
    "Contact": "Kontakt",
    "Privacy": "Datenschutz",
    "Terms": "Nutzungsbedingungen",
    "Copyright": "Urheberrecht",
    "All rights reserved": "Alle Rechte vorbehalten"
}
```