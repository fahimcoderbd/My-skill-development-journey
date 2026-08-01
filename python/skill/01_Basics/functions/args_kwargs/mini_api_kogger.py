def log_request(*end_points, **user_info):
    #showing api endpints
    print(f"Endpoints: {end_points}")

    #showing user info and status code
    for key,data in user_info.items():
        print(f"{key} : {data}")

log_request(
    "/login",
    "POST",
    user="fahim",
    status=200
)