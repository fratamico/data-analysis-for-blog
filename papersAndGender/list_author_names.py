#produces a csv of all authors and in the papers.csv file and their genders

import requests, json


#following function is adapted from https://github.com/block8437/gender.py
#it uses the https://genderize.io/ api
def get_gender_genderize(name):
    #>>> print get_gender_genderize("Brian")
    #(u'male', u'1.00', 4456)
    
    req = requests.get("http://api.genderize.io?name[0]=" + name)
    result = json.loads(req.text)


    if result["gender"] is not None:
        retrn = (str(result["gender"]), str(result["probability"]), str(result["count"]))
        #The count represents the number of data entries examined in order to calculate the response.
    else:
        retrn = (u'unknown',u'0.0','0.0')
    return retrn

def get_gender_gender_api(name):
    #>>> print get_gender_gender_api("Brian")
    
    req = requests.get("https://gender-api.com/get?name=" + name + "&key=SmUlyyFdKBSmBGgGUF")
    #lauren.fratamico acct key=BjBbgoAANoQkAYWPNt #1000 left for april
    #laurlaur50 acct key=AjbtNgUByFmbYmEooB #1000 left for april
    #alex acct key=SmUlyyFdKBSmBGgGUF #80 left for april
    result = json.loads(req.text)


    if result["gender"] is not None:
        retrn = (str(result["gender"]), str(result["accuracy"]), str(result["samples"]))
        #The count represents the number of data entries examined in order to calculate the response.
    else:
        retrn = (u'unknown',u'0.0','0.0')
    return retrn


author_set = set()

infile = open("papers.csv", 'r')
lines = infile.readlines()

for line in lines[1:]:
    authors = line.split('","')[3].strip().split("     ")
    
    for author in authors:
        first_name = author.strip().split(" ")[0]

        #when the first name is an initial, replace with middle name
        if "." in first_name or len(first_name) == 1:
            first_name = author.strip().split(" ")[-2]

        #ignore the authors names that are only one character as we won't be able to match those
        if len(first_name) > 1:
            author_set.add(first_name)
print len(author_set)


outfile = open("author_genders.csv", 'a')
#outfile.write("author,genderize_gender,genderize_probability,genderize_count,gender_api_gender,gender_api_probability,gender_api_samples\n")
outfile.write("\n")


for author in sorted(author_set)[4700:]: 
    gender_info_genderize = get_gender_genderize(author)
    gender_info_gender_api = get_gender_gender_api(author)
    try:
        outfile.write(",".join([str(author), gender_info_genderize[0], gender_info_genderize[1], gender_info_genderize[2]]))
        outfile.write(",")
        outfile.write(",".join([gender_info_gender_api[0], gender_info_gender_api[1], gender_info_gender_api[2]]))
    except:
        print author, gender_info_genderize, gender_info_gender_api
    outfile.write("\n")


    



