print ("  Population Predictor 0.1");
print ("");
print ("  Based On Google's Statistics");
print ("");

ireland_stat = 0.035;
ireland_2016 = 4.726;
year_difference = 0;
result = 0;
cal_year = 2016;

country_input = input("  Choose Country: ");
year_input = input("  Choose Year: ");

if (country_input == "ireland"):
  print ("");
  year_difference = int(year_input) - int(cal_year)
  print ("  In " + str(year_difference) + " years there will be");
  result = ireland_2016 + ireland_stat * year_difference
  print ("  " + str(result) + " million people in Ireland");
  print ("");
elif (country_input == "apocalypse"):
  print ("");
  print ("  In 2020 there will be ");
  print ("  0 people on earth");
else:
  print ("");
  print ("  Unsupported Country!");

print ("");  
print ("  Keep in mind that these results aren't very accurate, accuracy decreases with each year!");
print ("");
