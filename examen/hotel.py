from hotelApi import getHotelByName,getReviewsById,getHotelDetailById,getValue

HotelFav = {}
while(True):
    print("1-Search hotel by name")
    print("2-Quality by Id")
    print("3-Import hotels by Id")
    print("4-List hotels")
    print("5-List reviewa by Id")
    print("6-List hotels by value")
    print("7-Exit")
    option = int(input("Select option:"))

    if(option == 7):
        print("BYE! Thanks for using our app.")
        break

    if(option == 1):
        name = input("Hotel name: ")
        resu = getHotelByName(name)
        for hotel in resu:
            print(hotel)
            print("\tName:"+resu[hotel][0])
            print("\tStreet:"+resu[hotel][1])
            print("\tCity:"+resu[hotel][2])
            print("\tProvince:"+resu[hotel][3])

    if(option == 2):
        hotelId = input("Hotel id: ")
        revi = getReviewsById(hotelId)
        print("Reviews: ")
        for rev in range(len(revi)):
            print("\t"+revi[rev])

    if(option == 3):
        hotelId = input("Hotel id: ")
        print("Importing...")
        detail = getHotelDetailById(hotelId)
        HotelFav[hotelId] = detail
        if(hotelId in HotelFav):
            print("Importing succsessful")
            print("You have",len(HotelFav),"favourite hotels")
        else:
            print("Somenthing went wrong")
            print("You have",len(HotelFav),"favourite hotels")

    if(option == 4):
        for hotel in HotelFav:
            print(hotel)
            print("\tName:"+HotelFav[hotel]["name"])
            print("\tStreet:"+HotelFav[hotel]["address"])
            print("\tCity:"+HotelFav[hotel]["city"])
            print("\tProvince:"+HotelFav[hotel]["province"])
            print("\tValue:"+HotelFav[hotel]["value"])
            print("\tReviews:",len(getReviewsById(hotel)))


    if(option == 5):
        hotelId = input("Hotel id: ")
        reviews = getReviewsById(hotelId)
        for review in reviews:
            print(review)
            print("----------------------")

    if(option == 6):
        minValue = input("Minimum value[0-10]: ")
        for hot in HotelFav:
            print(HotelFav[hot]["value"].split("/")[0])
            if(HotelFav[hot]["value"].split("/")[0] >= minValue):
                print(hot)
                print("\tName:"+HotelFav[hot]["name"])
                print("\tStreet:"+HotelFav[hot]["address"])
                print("\tCity:"+HotelFav[hot]["city"])
                print("\tProvince:"+HotelFav[hot]["province"])
                print("\tValue:"+HotelFav[hot]["value"])