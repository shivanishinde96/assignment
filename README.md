# assignment
According to the problem statement,I understood that you are getting emails from agents and you need to parse the data.
I have built this on the windows operating system.
I have worked on the problem statement and parsed the data using index.html file.
As per the assumption,the emails are in HTML format,I have parsed the html file and extracted the required data from the file and formatted it in json.
For parsing html,I have used BeautifulSoup library which is a python library.
Steps that I have done to parse the file:
1.Import the beautifulsoup class from bs4 module.
2.Open the html file and read its contents with the read() method.
3.BeautifulSoup Object is created which is passed to the constructor and the second parameter in the constructor is the parser that I have used,which is html-parser.
4.The data in the index.html file consists of table format,so I looped through the table data.Used find method to find the first matching pattern of table in the given index.html file.
5.Then,looped through the <tr> and <td> tags using find_all method,to find all the tr and td tags.The index.html data has a pattern,under the tr,td tags there was font tag inside which the required data was embedded and to extract the data,I looped through font tag.
6.Inside the font tag,there are tags in which the required data is kept,so using findall and passing a second parameter to it,extracted the useful information.
7.After extracting the information,I have created a output.json file and the mode is in write mode,and dumped all the extracted data into the output.json file.
  
/*Output*/
/*I have used for loops due to which it is printing the data multiple times*/
/*testlead@gmail.com
Test Lead
Test Lead
Test Lead
testlead@gmail.com
testlead@gmail.com
Test Lead
Test Lead
Test Lead
testlead@gmail.com
testlead@gmail.com
testlead@gmail.com
43824 W Sagebrush Trl, Maricopa,
                            AZ 85138
2
3
43824 W Sagebrush Trl, Maricopa,
                            AZ 85138
2
3
43824 W Sagebrush Trl, Maricopa,
                            AZ 85138
2
3
43824 W Sagebrush Trl, Maricopa,
                            AZ 85138
2
3
43824 W Sagebrush Trl, Maricopa,
                            AZ 85138
2
3
43824 W Sagebrush Trl, Maricopa,
                            AZ 85138
2
3*/
