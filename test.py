from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights

# result = tavily_search("provide me few best hotels in hyderabad")
# print(result)

result = search_flights("Plan 7 days trip from INDIA to Singapore")
print(result)