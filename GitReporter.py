import requests

class Reporter:
    
    def __init__(self):
        self.repos = []


    def run(self):
        while True:
            username = self.get_input()
            url = "https://api.github.com/users/" + username + "/repos"
            response = requests.get(url)
            status = response.status_code          
            
            if status == 200:
                self.repos = response.json()
                self.display_data(self.repos)
                break
            else:
                print("Invalid Github username")
                continue

    def get_input(self):
        answer = input("Enter Github username: ")
        return answer
    
    def display_data(self,repos):
        for repo in repos:
            print(f"{repo["name"] or "empty"}, {repo["language"] or "empty"}, {repo["stargazers_count"]} ")


if __name__ == "__main__":
    Githubrepo = Reporter()
    Githubrepo.run()
