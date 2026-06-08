import requests

class reporter:
    
    def __init__(self):
        self.repos = []


    def run(self):
        while True:
            username = self.get_input()
            url = "https://api.github.com/users/" + username + "/repos"
            response = requests.get(url)
            self.repos = response.json()
            status = response.status_code
            print(url)
            print(response.status_code)
            
            if status == 200:
                self.display_data(self.repos)
                break
            else:
                print("Invalid Github username")
                continue



    def get_input(self):
        answer = input("Enter Github username: ")
        return answer
    
    def display_data(self,lists):
        for list in lists:
            print(list["name"] + ", " + list["language"] + ", " + str(list["stargazers_count"]))


if __name__ == "__main__":
    Githubrepo = reporter()
    Githubrepo.run()
