import requests
import json
import openpyxl
import datetime
from datetime import datetime

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


class Collections:
    def __init__(self):
        self.fireflies = ""
        self.time_doc = ""





class RunCRAM:
    def __init__(self):
        self.participants = []
        self.reps_ = []
        self.meets = []
        self.time_sheets = []


    def collect_time_sheet(self, user_):
        try:
            """
                For each Rep, Collect TimeSheet
            """

            time_sheet = "TODO: write api function with Time-Doctor_API"
            print(f"[saving]:[{user_}]:[{time_sheet}]")
        except Exception as e:
            print(e)
            return e



    def per_user(self, user_, details):
        try:
            """
                For each Rep, Create TimeSheet-MeetsReport
            """
            print(f"[saving]:[{user_}]:[{details}]")

            pass
        except Exception as e:
            print(e)
            return e




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


    def main(self):
        api_url = "https://api.fireflies.ai/graphql/"
        bearer_token = "d5f23de2-de12-4db6-a806-703be6d78ca1"
        query = "{ transcripts { title date id participants transcript_url duration } }"

        client = GraphQLClient(api_url, bearer_token)
        result = client.execute_query(query)
        #print(result)
        #print(result['data'])


        self.save_that(result)



if __name__ == "__main__":
    CRAM = RunCRAM()
    CRAM.main()
