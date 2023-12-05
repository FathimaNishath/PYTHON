current_year=2023
final_year=int(input("Enter the final year:"))
leap_year=[year for year in range(current_year,final_year+1)
if(year%4==0)]
print("Leap year from",current_year,"to",final_year,"are:",leap_year)