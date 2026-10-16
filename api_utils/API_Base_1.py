from playwright.sync_api import Playwright

login_payload = {"userEmail":"gandharvak2759@gmail.com","userPassword":"Rameshwara@123"}
orders_payload = {"orders":[{"country":"India","productOrderedId":"6960ea76c941646b7a8b3dd5"}]}

class API_utils:
    def get_Token(self, playwright: Playwright):
        api_request_context_1 = playwright.request.new_context(base_url="https://rahulshettyacademy.com",ignore_https_errors=True)
        api_response_1=api_request_context_1.post("/api/ecom/auth/login",
                                   data=login_payload)
        assert api_response_1.ok
        api_response_1_body=api_response_1.json()
        print(api_response_1_body)
        return api_response_1_body["token"]


    def create_order(self, playwright: Playwright):
        token = self.get_Token(playwright)
        api_request_context_2 = playwright.request.new_context(base_url="https://rahulshettyacademy.com",ignore_https_errors=True)
        api_response_2 = api_request_context_2.post("/api/ecom/order/create-order",
                                                data=orders_payload,
                                                headers={"Authorization":token,
                                                         "Content-Type":"application/json"})
        print(api_response_2.json())
        response_body = api_response_2.json()
        order_id = response_body["orders"][0]
        return order_id
