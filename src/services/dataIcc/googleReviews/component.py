class GoogleReviewsComponent:
    def __init__(self) -> None:

        self.base_query = 'https://www.google.co.id/travel/search?q=hotel%20di%20jawa%20timur&ved=0CAAQ5JsGahgKEwiw_J2snYeFAxUAAAAAHQAAAAAQtwE&ap=MAA&qs=SAA'
        self.google_url = 'https://www.google.co.id'
        self.domain = 'www.google.co.id'
        self.path_error_hand = 'src/database/json/google_review_err.json'
        self.path_done = 'src/database/json/google_review_done.json'
        ...