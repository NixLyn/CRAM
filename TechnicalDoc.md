# CRAM
- Customer
- Relations
- A.I.
- Manager


# Overview #

## Usage ##
### FireFlies.ai ###
### TimeDoctor.com ###
### XCLS Sheets ###
### OpenAI ###
### SMTP ###

## FireFlies.ai ##

FireFlies.ai brings you your very own A.I. into the meetings:
- Automated Notes
- Topic Tracking
- Performance Review
- Success Tracking
- Many More tools+integrations

## TimeDoctor ##

Easily manage your companies' productivity:
- Hours tracked
- Productivity percentage
- Work Life Balance tracking


## XLSX Sheets ##

We understand that there are too many apps out there,
that's why we built CRAM to work in the background.


## OPEN_AI ##

Each member of a team is unique and the way they see data is not the same,
that's why we have OpenAI's API summerize and construct each email
to fit the needs of each member's requirements.


## SMTP ##

Our API will collect and process data from all your workflows,
and automatically email the generated reports to the relevant people.



# Technical Overview #

### Hosting ###

Project's main beta test will be deployed to Vercel.

### Base Platform Framework ###

By writing the project in Node/React/NextJS, 
we are able to implement all required background functionality 
as well any frontend requirements ei. Login/Register, Configurations.


## FireFLies.AI ##

``` https://docs.fireflies.ai/ ```

By means of ``` fetch() ``` we are able to collect the transcripts from Fred_AI:

### Node/React/NextJS: ###

```
    fetch('https://api.fireflies.ai/graphql', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer xxxxxxxxxxxxxxxx' //Your authorization token
      },
      body: JSON.stringify({
        query: `
            query {
                transcripts {
                    id
                    title
                    fireflies_users
                    participants
                    date
                    transcript_url
                    duration
                }
            }
        `
      }),
    })
    .then(result => result.json())
    .then(result => console.log(result.data))
    .catch(error => {
      console.error('Error:', error);
    });
```


### Python3 ###

```
class GraphQLClient:
    def __init__(self, url, token):
        self.url = url
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }

    def execute_query(self, query):
        data = json.dumps({"query": query})
        response = requests.post(self.url, headers=self.headers, data=data)
        return response.json()


class RunCRAM:
    def __init__(self):
        self.participants = []
        self.reps_ = []
        self.meets = []
        self.time_sheets = []


    def main(self):
        api_url = "https://api.fireflies.ai/graphql/"
        bearer_token = "d5f23de2-de12-4db6-a806-703be6d78ca1"
        query = "{ transcripts { title date id participants transcript_url duration } }"

        client = GraphQLClient(api_url, bearer_token)
        result = client.execute_query(query)
```


## Time Doctor ##

``` https://timedoctor.redoc.ly/#operation/company ```

With TimeDoctor companies are able to monitor the productivity
of their employees, tracking hours logged in and work done.

### Node/React/NextJS: ###

```
const fetch = require('node-fetch');

const query = new URLSearchParams({
  company: 'string',
  token: 'YOUR_API_KEY_HERE'
}).toString();

const resp = await fetch(
  `https://api2.timedoctor.com/api/1.0/companies?${query}`,
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      noWorkspaces: true,
      name: 'string',
      description: 'string',
      creator: 'string',
      timezone: 'string',
      pricingPlan: 'basic',
      newOwnerId: 'string',
      silentTrackingTimes: {
        days: [1, 2, 3, 4, 5],
        hours: [
          ['8:00', '13:00'],
          ['14:00', '17:00']
        ],
        timezone: 'UTC'
      },
      whoCanAccessScreenshots: 'none'
    })
  }
);

const data = await resp.json();
console.log(data);
```


### Python3 ###

```
import requests

url = "https://api2.timedoctor.com/api/1.0/companies?company=string&token=YOUR_API_KEY_HERE"

query = {
  "company": "string",
  "token": "YOUR_API_KEY_HERE"
}

payload = {
  "noWorkspaces": True,
  "name": "string",
  "description": "string",
  "creator": "string",
  "timezone": "string",
  "pricingPlan": "basic",
  "newOwnerId": "string",
  "silentTrackingTimes": {
    "days": [
      1,
      2,
      3,
      4,
      5
    ],
    "hours": [
      [
        "8:00",
        "13:00"
      ],
      [
        "14:00",
        "17:00"
      ]
    ],
    "timezone": "UTC"
  },
  "whoCanAccessScreenshots": "none"
}

headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers, params=query)

data = response.json()
print(data)
```



## XL_Sheets ##

Once all the required data has been collected,
we are able to save all the data in their respective 
columns and rows on a set of spreadsheets.

### Node/React/NextJS: ###

```
/* Read & Write  */
import React, { useCallback, useEffect, useState } from "react";
import { read, utils, writeFileXLSX } from 'xlsx';

export default function SheetJSReactAoO() {
  /* the component state is an array of presidents */
  const [pres, setPres] = useState([]);

  /* Fetch and update the state once */
  useEffect(() => { (async() => {
    const f = await (await fetch("https://sheetjs.com/pres.xlsx")).arrayBuffer();
    const wb = read(f); // parse the array buffer
    const ws = wb.Sheets[wb.SheetNames[0]]; // get the first worksheet
    const data = utils.sheet_to_json(ws); // generate objects
    setPres(data); // update state
  })(); }, []);

  /* get state data and export to XLSX */
  const exportFile = useCallback(() => {
    const ws = utils.json_to_sheet(pres);
    const wb = utils.book_new();
    utils.book_append_sheet(wb, ws, "Data");
    writeFileXLSX(wb, "SheetJSReactAoO.xlsx");
  }, [pres]);

  return (<table><thead><th>Name</th><th>Index</th></thead><tbody>
    { /* generate row for each president */
      pres.map(pres => (<tr>
        <td>{pres.Name}</td>
        <td>{pres.Index}</td>
      </tr>))
    }
  </tbody><tfoot><td colSpan={2}>
    <button onClick={exportFile}>Export XLSX</button>
  </td></tfoot></table>);
}
```

### Python3 ###

```
class SaveToXL:

    def save_that(self, result):
        try:
            # Create or load an Excel workbook
            self.workbook = openpyxl.Workbook()
            self.sheet = self.workbook.active

            # Write headers
            self.sheet['A1'] = "Title"
            self.sheet['B1'] = "Date"
            self.sheet['C1'] = "ID"
            self.sheet['D1'] = "People"
            self.sheet['E1'] = "Transcripts"

            # Update XCEL 'MAIN' Sheet
            data_ = result['data']['transcripts']
            print(data_[0])
            for val, dat in enumerate(data_):
                print(f"val: {str(val)} :: data: {str(dat)} " )
                self.sheet[f'A{val+2}']  =  str(dat["title"])
                self.meets.append(str(dat["title"]))
                self.sheet[f'B{val+2}']  =  str(dat["date"])        
                self.sheet[f'C{val+2}']  =  str(dat["id"])
                self.sheet[f'D{val+2}']  =  dat["participants"]
                self.sheet[f'E{val+2}']  =  str(dat["transcript_url"])   
                self.sheet[f'F{val+2}']  =  str(dat["duration"])

            # Save the workbook to a file
            self.workbook.save(f'{datetime.now()}.xlsx')

            print("DATA_SAVED")
        except Exception as e:
            print(e)
            return e

```



## OpenAI ##

### SMTP-By-Role ###

Once a company's list of employees and their roles have been established,
we can implement ``` import openai ``` and structure the data so that emails
are 'role-orientated', meaning every one gets the info they need, no more or less..

### Auto-Report ###

Depending on each company's requirements we are able to auto generate a report,
each day/week/month/etc on the specified data categories, to allow effiencient 
analysis and reviewing.




