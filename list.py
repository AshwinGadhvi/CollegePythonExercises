### Exercises: Level 1

#1. Declare an empty list
empty_List = []
print("Empty List Is : ",empty_List)

#2. Declare a list with more than 5 items
item_List = ["Ashwin","Vishwaraj","Jayraj","Samarth","Siddharth"]
print("\nList With More Than 5 Items Is : ",item_List)

#3. Find the length of your list
print("\nLength Of List Is : ",len(item_List))

#4. Get the first item, the middle item and the last item of the list
print("\nFirst Element : ",item_List[0])
middle_Element= len(item_List)//2
print("\nMiddle Element : ",item_List[middle_Element])
print("\nLast Element : ",item_List[-1])

#5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["ashwin",19,5.9,"Unmarried","Adipur"]
print("\nMixed Data Types List Is : ",mixed_data_types)

#6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies=["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
print("\nit_companies are : ",it_companies)

#7. Print the list using _print()_
print("\nPrinting List Using : ",item_List)

#8. Print the number of companies in the list
print("\nNumber Of IT Companies In List : ",len(it_companies))

#9. Print the first, middle and last company
print("\nFirst Company : ",it_companies[0])
middle_company=len(it_companies)//2
print("\nMiddle Company : ",it_companies[middle_company])
print("\nLast Company : ",it_companies[-1])

#10. Print the list after modifying one of the companies
it_companies[1] = "Yahoo"
print("\nAfter Modifying List It Companies Are : ",it_companies)

#11. Add an IT company to it_companies
it_companies.append("Google")
print("\nAfter Adding IT Companies : ",it_companies)

#12. Insert an IT company in the middle of the companies list
it_companies.insert(middle_company,"Cisco Systems")
print("\nAfter Inserting Middle OF The List Company : ",it_companies)

#13. Change one of the it_companies names to uppercase (IBM excluded!)
print("\nAfter UpperCAsing The Company : ",it_companies[0].upper());

#14. Join the it_companies with a string '#;&nbsp; '
join_it='#;&nbsp;'.join(it_companies)
print("\nAfter Joining It Company : ",join_it)

#15. Check if a certain company exists in the it_companies list.
check_company="Yahoo"
if check_company in it_companies:
    print('\n\n%s is present in the list.' % check_company)
else:
    print('\n\n%s is not present in the list.' % check_company)

#16. Sort the list using sort() method
it_companies.sort()
print("\nAfter Sorting A List : ",it_companies)

#17. Reverse the list in descending order using reverse() method
it_companies.reverse()
print("\nAfter Descending List : ",it_companies)

#18. Slice out the first 3 companies from the list
print("\n Slicing fist three element from list : ",it_companies[:3])

#19. Slice out the last 3 companies from the list
print("\nSlicing Last Three Element From List : ",it_companies[-3:])

#20. Slice out the middle IT company or companies from the list
it_middle=(len(it_companies)//2)
print("\nSlicing Middle Company : ",it_companies[it_middle])

#21. Remove the first IT company from the list
del it_companies[0]
print("\nPrinting List After Removing First It Company : ",it_companies)

#22. Remove the middle IT company or companies from the list
del it_companies[it_middle]
print("\nAfter Removing middle comapny : ",it_companies)

#23. Remove the last IT company from the list
del it_companies[-1]
print("\nAfter Removing Last It Company : ",it_companies)

#24. Remove all IT companies from the list
it_companies.clear()
print("\nAfter Removing All It Company : ",it_companies)

#25. Destroy the IT companies list
del it_companies[0:]
print("\nAfter Destroying It Companies : ",it_companies)

#26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
merge = front_end+back_end
print("\nAfter Merging Two List : ",merge)

#27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack=merge
full_stack.append("Python")
full_stack.append("SQL")
print("\nAfter Appending Values To List : ",full_stack)


### Exercises: Level 2

#1. The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort()
print("\nMinimum Age : ",ages[0])
print("\nMaximum Age : ",ages[-1])

# Add the min age and the max age again to the list
ages.extend([ages[0],ages[-1]])
print("\nList After Adding Min And Max Value Again : ",ages)

# Find the median age (one middle item or two middle items divided by two)
median_age=len(ages)//2
print("\nAfter Finding Median Age : ",ages[median_age])

# Find the average age (sum of all items divided by their number )
find_avg = sum(ages)//len(ages)
print("\nAfter Finding Avg Age in : ",find_avg)

# Find the range of the ages (max minus min)
ages.sort()
range_of_ages = ages[-1] - ages[0]
print("\nAfter Finding Range : ",range_of_ages)

# Compare the value of (min - average) and (max - average), use _abs()_ method
difference_min_avg = abs(ages[0]-find_avg)
difference_max_avg = abs(ages[-1]-find_avg)
print("\nMinimum Average : ",difference_min_avg)
print("\nMaximum Average : ",difference_max_avg)

#1. Find the middle country(ies) in the [countries list]
countries=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
middle_country = len(countries)//2
print("\nMiddle Country Is : ",middle_country)

#2. Divide the countries list into two equal lists if it is even if not one more country for the first half.
first_half=countries[:middle_country]
secong_half=countries[middle_country:]
if len(first_half)<len(secong_half):
    first_half.append("Portugal")
print("\nFirst Half Of Company : ",first_half)
print("\nSecond Half Of Country : ",secong_half)

#3. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
scandic=countries[3:]
print("\nscandic Countries Are : ",scandic)