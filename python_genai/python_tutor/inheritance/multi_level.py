class Manager:
    def final_review(self):
        return "Managing team"
    
class Reviewer(Manager):
    def review(self):
        return "Review team meeting"
    
class TeamLead(Reviewer):
    def lead_team(self):
        return "Leading the team"
    
obj = TeamLead()
print(obj.lead_team())        # Output: Leading the team
print(obj.review())          # Output: Review team meeting
print(obj.final_review())    # Output: Managing team