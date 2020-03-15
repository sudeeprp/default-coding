# Data Schema and Access

Today's applications are powered by data,
just like machines are powered by energy.

For example, a cab-booking application would rely on data like your location,
map-information, driver availability, dynamic pricing and payment details.

A relational database models data in terms of entities and relationships.
Here are some examples of entities:

- A `customer` is identified by a `CustomerID`
- A `customer` orders a `ride`
- A `ride` is identifed by an `OrderID`

If you aren't familiar with SQL, you can quickly get a flavor for it
over here: [https://www.w3schools.com/sql/](https://www.w3schools.com/sql/)

## Normalization

Consider the following data:

|CustomerID|CustomerName|...|Pin code|City|Country|
|---|---|---|---|---|---|
|300|Arijit|...|110005|Delhi|India|
|301|John|...|02111|Boston|USA|
|302|Mary|...|02115|Boston|USA|
|303|Sonu|...|560001|Bangalore|India|
|304|Vijay|...|560002|Bangalore|India|
|305|Latha|...|110001|Delhi|India|

Observe that there is some redundancy here.
For example, 'India' will be repeated in every row for all customers in India.
In any case, we can infer both the city and the country from the pin code.

**Normalization** is the process of removing redundancy.
Here is a normalized representation of the above data:

|CustomerID|CustomerName|...|Pin code|
|---|---|---|---|
|300|Arijit|...|110005|
|301|John|...|02111|
|302|Mary|...|02115|
|303|Sonu|...|560001|
|304|Vijay|...|560002|
|305|Latha|...|110001|

|Pin code prefix|City|
|---|---|
|1100|Delhi|
|5600|Bangalore|
|0211|Boston|

|City|Country|
|---|---|
|Delhi|India|
|Bangalore|India
|Boston|USA|

## Denormalization

There are situations where redundancy is actually desirable.
An example is healthcare data. Every medical image needs to be
accompanied by the all the patient's details, for effective diagnosis.

Machine learning algorithms need all the data together to make effective models.

Normalized data can be denormalized using 'join' operations on the data.
Use the [tutorial mentioned](https://www.w3schools.com/sql/sql_join.asp)
to learn about joins.
