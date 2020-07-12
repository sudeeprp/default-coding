# Flexible Schema

A schema gives the organization of data. It says what the data means.
In the [previous example](data-schema-access.md),
the 'City' column had the name of the City and not its ID.
That's what is given by a schema, in addition to the table-structure itself.

Often, changes in schema are needed. For example, we may want to
add the Customer's PAN number in response to a Government regulation.

Such changes can require expensive migration - not only in the database,
but also all applications that are using the database.
The addition of a PAN number may only be mandated in India.
Adding it as a column into the table
in the [previous example](data-schema-access.md) will
add it for all rows - even for customers in other countries.

How can we reduce the burden of migration?
Let's try a hierarchical representation of the data:

- A country has cities
- A city has pin codes
- A pin code has customers
- A customer has attributes (incl. PAN)

A common way to express hierarchical data is to use JSON.
Our data could be organized as follows:

```json
{
  "countries": [{
      "name": "India",
      "cities": [{
          "name": "Bangalore",
          "customers": [{
              "name": "Vijay",
              "PAN": "QAYDD3422U",
              "address": "#4, Church Street"
            }
        ]},
        {
          "name": "Delhi",
          "customers": [{
              "name": "Arijit",
              "PAN": "YATBB3423R",
              "address": "#1, Mangal Marg"
            }, {
              "name": "Latha",
              "PAN": "RARAA3455O",
              "address": "#4, Mangal Marg"
          }]
        }]
    }, {
      "name": "USA",
      "cities": [{
          "name": "Boston",
          "customers": [{
              "name": "Mary",
              "address": "#6, Logan lane",
              "SSN": "2381024810498"
          }]
      }]
    }
  ]
}
```

Such records don't have a fixed structure.
Notice that customers in India have a PAN, while those in the US have SSN.

So any change or migration could handle a few records at a time.
We could also update the application per region.
