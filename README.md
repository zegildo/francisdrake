[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/zegildo/francisdrake/blob/master/License.md) 
[![fork](https://img.shields.io/github/forks/zegildo/francisdrake.svg)](https://github.com/zegildo/francisdrake/network/members)
[![issues](https://img.shields.io/github/issues/zegildo/francisdrake.svg)](https://github.com/zegildo/francisdrake/issues)

# Sir Francis Drake

Catching the professors schedule at UFERSA is an annoying task.
We should to stalk more than 750 personal links, copy and paste
many detail over many semesters. To solve this I developed this web crawler that collect the historical classes schedule for each UFERSA Professor during all his
professor carrer.

## Get Data:

If you are interested only the data:
* [Relational scheme and dump](https://github.com/zegildo/francisdrake/tree/master/sql)
* [CSV files](https://github.com/zegildo/francisdrake/tree/master/output) 

## Execute Code:

If you are interested in execute the code to get all historical classes information:

### Get information about all professors @UFERSA:
```console
foo@bar:~$ sh francis_professors.sh
```
Input:
[departaments](https://github.com/zegildo/francisdrake/blob/master/inputs/departaments): A list of actual and valid departaments in the University.

Output:
[professors_information.csv](https://github.com/zegildo/francisdrake/blob/master/output/professors_information.csv): A dataset with basic information about professors (siape, name, departament, photo, personal link).

### Get historical classes schedule for all professors @UFERSA:
```console
foo@bar:~$ sh francis_schedule.sh
```
Input:
[siapes](https://github.com/zegildo/francisdrake/blob/master/inputs/siapes): a list of siapes (*id professors*).

Output:
[horarios_ufersa.csv](https://github.com/zegildo/francisdrake/blob/master/output/horarios_ufersa.csv): All schedule classes for all professors.

# Important
It is necessary to install the [parallel](https://www.gnu.org/software/parallel/) command to run these **.sh**.


