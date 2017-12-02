# save-webpage.py

import urllib3
import requests
from time import sleep

url = 'https://www.radissonblu.com/reservation/cityRateSearch.do?facilitatorId=CSOSEO&citySearchForm.city=&citySearchForm.country=&rateSearchForm.forcedCitySearch=false&rateSearchForm.homePageSearchType=&rateSearchForm.redemptionSearch=false&rateSearchForm.redemptionCalSearch=false&rateSearchForm.currencyCode=&rateSearchForm.hotelSortFilter=&rateSearchForm.rateSortFilter=%28sort%28availableRates%29%29&rateSearchForm.modifySearch=true&storeHotelSortFilter=true&rateSearchForm.clearFilter=true&rateSearchForm.hotelCodes=KGDZH&rateSearchForm.forcedHotelSearch=true&rateSearchForm.hotelName=Radisson+Hotel%2C+Kaliningrad&rateSearchForm.hotelCode=KGDZH&rateSearchForm.checkinDate=06%2F25%2F2018&rateSearchForm.checkoutDate=06%2F26%2F2018&rateSearchForm.numberRooms=2&rateSearchForm.occupancyForm%5B0%5D.numberAdults=2&rateSearchForm.occupancyForm%5B0%5D.numberChildren=0&rateSearchForm.occupancyForm%5B1%5D.numberAdults=2&rateSearchForm.occupancyForm%5B1%5D.numberChildren=0&rateSearchForm.occupancyForm%5B2%5D.numberAdults=1&rateSearchForm.occupancyForm%5B2%5D.numberChildren=0&rateSearchForm.occupancyForm%5B3%5D.numberAdults=1&rateSearchForm.occupancyForm%5B3%5D.numberChildren=0&rateSearchForm.occupancyForm%5B4%5D.numberAdults=1&rateSearchForm.occupancyForm%5B4%5D.numberChildren=0&rateSearchForm.occupancyForm%5B5%5D.numberAdults=1&rateSearchForm.occupancyForm%5B5%5D.numberChildren=0&rateSearchForm.occupancyForm%5B6%5D.numberAdults=1&rateSearchForm.occupancyForm%5B6%5D.numberChildren=0&rateSearchForm.occupancyForm%5B7%5D.numberAdults=1&rateSearchForm.occupancyForm%5B7%5D.numberChildren=0&rateSearchForm.occupancyForm%5B8%5D.numberAdults=1&rateSearchForm.occupancyForm%5B8%5D.numberChildren=0&rateSearchForm.ecertCodeForNonEligibleRate=&rateSearchForm.rmcCode=&rateSearchForm.ecertCode=&rateSearchForm.corporateAccountID=&rateSearchForm.promotionalCode=&rateSearchForm.travelAgencyId=&rateSortFilter=(sort(availableRates))'

http = urllib3.PoolManager()

while True:
	r = http.request('GET', url)
	if 'Hotel is not available for dates searched' not in str(r.data):
		requests.post("https://api.telegram.org/bot412945024:AAExIRCkJv6CVSBxBKeCkU31F2oVjBC2cM0/sendMessage", data={'chat_id': -271065471, 'text': 'Что-то изменилось на странице бронирования! Срочно надо проверять - https://goo.gl/v9EWQS'})
	sleep(300)