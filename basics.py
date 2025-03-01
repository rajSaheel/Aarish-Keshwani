class_size= int(input("How many individuals would you like to save? "))
voters=[]
for i in range(0,class_size,1):
    print("voter",i)
    name= input("What is your name?")
    age= int(input("How old are you? "))
    voter= {"name":name, "age":age}
    voters.append(voter)
for applicant in voters:
    if applicant["age"]>=18:
        print(applicant["name"],"is eligible to vote")
    else:
        print(applicant["name"],"is not eligible to vote")