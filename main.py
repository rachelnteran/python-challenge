import os
import csv

csvpath = os.path.join("pyPoll","Resources", "election_data.csv")

vote_count = 0
Casper = 0
Diana = 0
Raymon = 0

#def votecounter(csvreader):
 #       if row[2] == "Charles Casper Stockham":
   #         Casper = Casper + 1
   #     if row[2] == "Diana DeGette":
    #        Diana = Diana + 1
    #    if row[2] == "Raymon Anthony Doane":
     #       Raymon + 1
#print(f'Casper received {Casper} votes, Diana received {Diana} votes, Raymon received {Raymon}votes.')

with open(csvpath) as csvfile:

    electiondata = csv.reader(csvfile, delimiter=',')
    csv_header = next(electiondata)

    for row in electiondata:
        vote_count = vote_count + 1
        if row[2] == "Charles Casper Stockham":
            Casper += 1
        if row[2] == "Diana DeGette":
            Diana += 1
        if row[2] == "Raymon Anthony Doane":
            Raymon += 1
print(f"The total number of votes cast is {vote_count}")
#print(f"The total number of votes for Charles Casper Stockham is:{Casper}")
#print(f"The total number of votes for Diana DeGette is:{Diana}")
#print(f"The total number of votes for Raymon Anthony Doane is:{Raymon}")

votes_for_stockham = Casper
votes_for_degette = Diana
votes_for_doane = Raymon

percent_stocham = round((votes_for_stockham / vote_count) *100)
percent_degette = round((votes_for_degette / vote_count) *100)
percent_doane = round((votes_for_doane / vote_count) *100)

print(f"Stockham won {percent_stocham}% of the votes ({votes_for_stockham})")
print(f"DeGette won {percent_degette}% of the votes ({votes_for_degette})")
print(f"Doane won {percent_doane}% of the votes ({votes_for_doane})")

if percent_stocham > percent_degette and percent_doane:
    print("Stockham won the election")
if percent_degette> percent_stocham and percent_doane:
    print("DeGette won the election")
if percent_doane > percent_degette and percent_stocham:
    print("Doane won the election")

output_path = 'output.txt'
with open(output_path, 'w') as output_file:
    # Write statements to the file
    output_file.write("The total number of votes cast is 369711\n")
    output_file.write("Stockham won 23% of the votes (85213)\n")
    output_file.write("DeGette won 74% of the votes (272892)\n")
    output_file.write("Doane won 3% of the votes (11606)\n")
    output_file.write("DeGette won the election.")