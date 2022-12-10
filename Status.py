Teams = {"Barca":"Active", "Chelsea":"inactive", "Manchester":"inactive", "Madrid":"Active"}

for team,status in Teams.copy().items():
    if status == "Active":
        print(team, status , sep=" - ")

  #  else:
  #     print("This teams are inactive.") 