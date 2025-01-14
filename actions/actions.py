from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


# mudaraba savings schemes details custom action
class ActionMudarabaSavingsDetails(Action):
    def name(self) -> Text:
        return "action_mudaraba_savings_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Extract the scheme name entity
        scheme_name = tracker.get_slot("scheme_name")
        
        # Scheme details (dummy data; replace with actual details)
        mudaraba_schemes = {
            "Savings": "The Mudaraba Savings Scheme is a profit-sharing scheme offering flexibility and Shariah compliance.",
            "Onkur": "This is for young people, helping them start saving early.Any Bangladeshi school (Class one to Ten) going student can open this account.",
            "Projonmo": "This is a student friendly account. It's suitable for any college/university going student.",
            "Prapti": "It is aimed at long-term financial security for individuals.",
            "Probin": "Probin is for elderly customers, ensuring secure savings for them.",
            "Mehonoty": "Specialized account for people with lower income bracket of the country.",
            "SND": "The SND (Short Notice Deposit) account offers flexible withdrawal options with competitive profit rates.",
            "Smart Account": "The FSIB Smart Account is a savings account that allows unlimited transactions and gives high profit, like a Mudarabah Term Deposit, with profit rates based on different slabs.",
            "FSIB Smart Account": "The FSIB Smart Account is a savings account that allows unlimited transactions and gives high profit, like a Mudarabah Term Deposit, with profit rates based on different slabs."
        }

        # Generate a response dynamically
        if scheme_name in mudaraba_schemes:
            #response = f"Here is information about the {scheme_name} Scheme:\n{mudaraba_schemes[scheme_name]}"
            response = f"{mudaraba_schemes[scheme_name]} Please click the below button for details."
            buttons = [{"title": f"{scheme_name}", "payload": "https://fsibplc.com/mudaraba_savings_account.php"}]
            dispatcher.utter_message(text=response, buttons=buttons)
        else:
            response = "Did you mean any of those?"
            buttons = [{"title": "Savings", "payload": "https://fsibplc.com/mudaraba_savings_account.php"},
                       {"title": "Onkur", "payload": "https://fsibplc.com/mudaraba_savings_account.php"},
                       {"title": "Projonmo", "payload": "https://fsibplc.com/mudaraba_savings_account.php"},
                       {"title": "Prapti", "payload": "https://fsibplc.com/mudaraba_savings_account.php"},
                       {"title": "Probin", "payload": "https://fsibplc.com/mudaraba_savings_account.php"},
                       {"title": "Mehonoty", "payload": "https://fsibplc.com/mudaraba_savings_account.php"},
                       {"title": "SND", "payload": "https://fsibplc.com/mudaraba_savings_account.php"},
                       {"title": "Smart Account", "payload": "https://fsibplc.com/mudaraba_savings_account.php"}]
            dispatcher.utter_message(text=response, buttons=buttons)
        
        return []


#al wadiah account details custom action
class ActionAlWadiahDetails(Action):
    def name(self) -> Text:
        return "action_al_wadiah_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Extract the scheme name entity
        scheme_name = tracker.get_slot("scheme_name")
        
        # Al-Wadiah scheme details (replace with actual details if needed)
        al_wadiah_schemes = {
            "Current Deposit": "The Al-Wadiah Current Deposit Account is a Shariah-compliant account for daily transactions, offering easy access to funds without profit sharing.",
            "Shomman": "The Shomman Scheme is designed for senior citizens, providing a secure and convenient way to manage their savings.",
            "Morjada": "The Morjada Scheme is aimed at professionals and business individuals, ensuring flexible transactions while adhering to Shariah principles."
        }

        # Generate a response dynamically
        if scheme_name in al_wadiah_schemes:
            #response = f"Here is information about the {scheme_name} Scheme:\n{al_wadiah_schemes[scheme_name]}"
            response = f"{al_wadiah_schemes[scheme_name]} Please click the below button for details."
            buttons = [{"title": f"{scheme_name}", "payload": "https://fsibplc.com/al_wadiah_account.php"}]
            dispatcher.utter_message(text=response, buttons=buttons)
        else:
            response = "Which scheme would you like to know more about?"
            buttons = [{"title": "Current Deposit", "payload": "https://fsibplc.com/al_wadiah_account.php"},
                       {"title": "Shomman", "payload": "https://fsibplc.com/al_wadiah_account.php"},
                       {"title": "Morjada", "payload": "https://fsibplc.com/al_wadiah_account.php"}]
            dispatcher.utter_message(text=response, buttons=buttons)
        
        return []
    
    
    
    
# mudaraba scheme account schemes details custom action
class ActionMudarabaSavingsDetails(Action):
    def name(self) -> Text:
        return "action_mudaraba_scheme_account_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Extract the scheme name entity
        scheme_name = tracker.get_slot("scheme_name")
        
        # Scheme details (dummy data; replace with actual details)
        mudaraba_schemes = {
            "Niramoy": "Save smartly for your family's medical needs and healthcare emergencies.",
            "Agroshor": "Step forward financially with planned savings for your future growth.",
            "Durbar": "An exclusive banking service that gives you special treatment and premium benefits, designed for customers who maintain higher account balances.",
            "Ehsan": "Ehsan, an islamic banking solution for Shariah-compliant savings and growth.",
            "Bondhon": "It is a relationship-focused savings scheme that helps strengthen your financial bonds with your loved ones, perfect for family savings goals.",
            "Ghoroni": "A home-focused banking service that helps you save and plan for housing needs, whether it's buying, building, or renovating your home.",
            "Haj": "A specialized savings scheme designed to help you save money for performing Hajj, making it easier to plan for this important religious journey.",
            "Musafir": "Musafir is a travel-friendly banking service that helps you save for and manage your travel expenses, whether for business or leisure.",
            "Sanchaye Shukh": "Sanchaye Shukh, a happiness savings scheme that helps you save regularly for future happiness and financial peace of mind.",
            "Merchant": "A business-focused banking service designed specifically for merchants and business owners to manage their business finances effectively.",
            "FSIB Care": "A caring banking service that provides special financial support and benefits to meet your various needs.",
            "Cash Waqf": "Cash Waqf is a banking service that lets you contribute to charitable causes while earning rewards in a Shariah-compliant way."
        }

        # Generate a response dynamically
        if scheme_name in mudaraba_schemes:
            #response = f"Here is information about the {scheme_name} Scheme:\n{mudaraba_schemes[scheme_name]}"
            response = f"{mudaraba_schemes[scheme_name]} Please click the below button for details."
            buttons = [{"title": f"{scheme_name}", "payload": "https://fsibplc.com/mudaraba_scheme_account.php"}]
            dispatcher.utter_message(text=response, buttons=buttons)
        else:
            response = "Did you mean any of those?"
            buttons = [{"title": "Niramoy", "payload": "https://fsibplc.com/mudaraba_scheme_account.php"},
                       {"title": "Agroshor", "payload": "https://fsibplc.com/mudaraba_scheme_account.php"},
                       {"title": "Durbar", "payload": "https://fsibplc.com/mudaraba_scheme_account.php"},
                       {"title": "Ehsan", "payload": "https://fsibplc.com/mudaraba_scheme_account.php"},
                       {"title": "Bondhon", "payload": "https://fsibplc.com/mudaraba_scheme_account.php"},
                       {"title": "Ghoroni", "payload": "https://fsibplc.com/mudaraba_scheme_account.php"},
                       {"title": "Haj", "payload": "https://fsibplc.com/mudaraba_scheme_account.php"},
                       {"title": "Musafir", "payload": "https://fsibplc.com/mudaraba_scheme_account.php"},
                       {"title": "Sanchaye Shukh", "payload": "https://fsibplc.com/mudaraba_scheme_account.php"},
                       {"title": "Merchant", "payload": "https://fsibplc.com/mudaraba_scheme_account.php"},
                       {"title": "FSIB Care", "payload": "https://fsibplc.com/mudaraba_scheme_account.php"},
                       {"title": "Cash Waqf", "payload": "https://fsibplc.com/mudaraba_scheme_account.php"}]
            dispatcher.utter_message(text=response, buttons=buttons)
        
        return []

# mudaraba term deposit account scheme details custom action

class ActionMudarabaTermDepositDetails(Action):
    def name(self) -> Text:
        return "action_mudaraba_term_deposit_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Extract the scheme name entity
        scheme_name = tracker.get_slot("scheme_name")
        
        # Scheme details (dummy data; replace with actual details)
        mudaraba_term_deposit_schemes = {
            "Mudaraba Term Deposit": "A Shariah-compliant long-term deposit scheme where profits are shared based on a pre-agreed ratio, ensuring ethical and interest-free financial growth.",
            "Mudaraba Monthly Profit Scheme": "A savings plan under Islamic banking principles that offers regular monthly profit payouts derived from Halal investments.",
            "FSIB Murobbi": "A deposit scheme designed for senior citizens, ensuring Shariah-compliant profit distribution and financial security in their later years.",
            "Mahiyasi": "An exclusive savings scheme for women, promoting financial independence and growth through Shariah-based profit-sharing.",
            "FSIB Sanchay": "A disciplined savings plan encouraging ethical and consistent savings, with profits generated from Halal business activities.",
            "Mudaraba Deposit Double Scheme": "A scheme that allows your deposit to double over a fixed period, ensuring all profits are derived from Shariah-compliant investments.",
            "Utshob": "A festive savings plan under Islamic banking principles, offering attractive returns for Halal financial growth.",
            "Mudaraba Smart Deposit Double Scheme": "A smart savings solution that doubles your deposit within a shorter duration, strictly adhering to Halal investment and profit-sharing practices.",
            "Mudaraba Term Deposit Century": "A long-term deposit scheme designed for ethical growth, adhering strictly to Shariah principles over an extended period.",
            "Mudaraba Term Deposit Double Century": "A Halal savings plan that ensures your deposit doubles through Shariah-compliant profit-sharing methods.",
            "MDDS": "A scheme that allows your deposit to double over a fixed period, ensuring all profits are derived from Shariah-compliant investments.",
            "Century": "A long-term deposit scheme designed for ethical growth, adhering strictly to Shariah principles over an extended period.",
            "Double Century": "A Halal savings plan that ensures your deposit doubles through Shariah-compliant profit-sharing methods."
        }

        # Generate a response dynamically
        if scheme_name in mudaraba_term_deposit_schemes:
            # Provide scheme details
            response = f"{mudaraba_term_deposit_schemes[scheme_name]} Please click the below button for details."
            buttons = [{"title": f"{scheme_name}", "payload": "https://fsibplc.com/mudaraba_term_account.php"}]
            dispatcher.utter_message(text=response, buttons=buttons)
        else:
            # Suggest other schemes
            response = "Did you mean any of these schemes?"
            buttons = [
                {"title": "Mudaraba Term Deposit", "payload": "https://fsibplc.com/mudaraba_term_account.php"},
                {"title": "Mudaraba Monthly Profit Scheme", "payload": "https://fsibplc.com/mudaraba_term_account.php"},
                {"title": "FSIB Murobbi", "payload": "https://fsibplc.com/mudaraba_term_account.php"},
                {"title": "Mahiyasi", "payload": "https://fsibplc.com/mudaraba_term_account.php"},
                {"title": "FSIB Sanchay", "payload": "https://fsibplc.com/mudaraba_term_account.php"},
                {"title": "Mudaraba Deposit Double Scheme (MDDS)", "payload": "https://fsibplc.com/mudaraba_term_account.php"},
                {"title": "Utshob", "payload": "https://fsibplc.com/mudaraba_term_account.php"},
                {"title": "Mudaraba Smart Deposit Double Scheme", "payload": "https://fsibplc.com/mudaraba_term_account.php"},
                {"title": "Mudaraba Term Deposit Century", "payload": "https://fsibplc.com/mudaraba_term_account.php"},
                {"title": "Mudaraba Term Deposit Double Century", "payload": "https://fsibplc.com/mudaraba_term_account.php"}
            ]
            dispatcher.utter_message(text=response, buttons=buttons)
        
        return []
    
# foreign currency details scheme custom action
class ActionForeignCurrencyDetails(Action):
    def name(self) -> Text:
        return "action_foreign_currency_account_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Extract the scheme name entity
        scheme_name = tracker.get_slot("scheme_name")
        
        # Foreign Currency schemes details (replace with actual details if needed)
        foreign_currency_schemes = {
            "Private Foreign Currency": "The Private Foreign Currency Scheme enables individuals to open and maintain foreign currency accounts for personal use. Customers can conveniently hold and transact in major currencies such as USD, GBP, EUR, and JPY.",
            "Resident Foreign Currency Deposit": "The Resident Foreign Currency Deposit Scheme enables residents with foreign earnings to save in foreign currencies, ensuring easy access to international funds.",
            "Non-Resident Foreign Currency Deposit": "The Non-Resident Foreign Currency Deposit Scheme offers NRBs the opportunity to save in foreign currencies, with attractive profit-sharing options.",
            "Export Retention Quota": "The Export Retention Quota Scheme is designed for exporters to retain a portion of their export earnings in foreign currency for business operations.",
            "Non-Resident Investor's Taka Account": "The Non-Resident Investor's Taka Account Scheme provides a secure platform for foreign investors to manage their investments in Bangladesh.",
            "PFC": "The Private Foreign Currency Scheme enables individuals to open and maintain foreign currency accounts for personal use. Customers can conveniently hold and transact in major currencies such as USD, GBP, EUR, and JPY.",
            "RFCD": "The Resident Foreign Currency Deposit Scheme enables residents with foreign earnings to save in foreign currencies, ensuring easy access to international funds.",
            "NFCD": "The Non-Resident Foreign Currency Deposit Scheme offers NRBs the opportunity to save in foreign currencies, with attractive profit-sharing options.",
            "ERQ": "The Export Retention Quota Scheme is designed for exporters to retain a portion of their export earnings in foreign currency for business operations.",
            "NITA": "The Non-Resident Investor's Taka Account Scheme provides a secure platform for foreign investors to manage their investments in Bangladesh."
        }

        # Generate a response dynamically
        if scheme_name in foreign_currency_schemes:
            response = f"{foreign_currency_schemes[scheme_name]} Please click the below button for details."
            buttons = [{"title": f"{scheme_name}", "payload": "https://fsibplc.com/foreign_account.php"}]
            dispatcher.utter_message(text=response, buttons=buttons)
        else:
            response = "Which foreign currency account scheme would you like to know more about?"
            buttons = [
                {"title": "Private Foreign Currency", "payload": "https://fsibplc.com/foreign_account.php"},
                {"title": "Resident Foreign Currency Deposit", "payload": "https://fsibplc.com/foreign_account.php"},
                {"title": "Non-Resident Foreign Currency Deposit", "payload": "https://fsibplc.com/foreign_account.php"},
                {"title": "Export Retention Quota", "payload": "https://fsibplc.com/foreign_account.php"},
                {"title": "Non-Resident Investor's Taka Account", "payload": "https://fsibplc.com/foreign_account.php"}
            ]
            dispatcher.utter_message(text=response, buttons=buttons)
        
        return []   
    
    
## service details part of fuad
class ActionDigitalServicesDetails(Action):
    def name(self) -> Text:
        return "action_digital_services"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Extract the service name entity
        service_name = tracker.get_slot("digital_services")
        
        # Digital services details with descriptions and links
        digital_services_details = {
            "FSIB Cloud": {
                "description": "FSIB Cloud is a digital banking solution that allows seamless online banking experiences with advanced features.",
                "link": "https://cloud.fsiblbd.com/FSIBLCLOUD/login?returnUrl=%2F"
            },
            "FirstCash": {
                "description": "FirstCash is a fast and reliable service ensuring secure and hassle-free cash transactions on mobile devices.",
                "link": "https://fsiblbd.com/firstcash/index.php"
            },
            "DCloud": {
                "description": "DCloud is an all-around digital Banking application of FSIB for banked and unbanked persons of Bangladesh promoting Financial Inclusion and Cash-less Society.",
                "link": "https://fsibplc.com/dcloud.php"
            },
            "Freedom": {
                "description": "Freedom is FSIB's online account opening service, making banking more accessible for all.",
                "link": "https://freedom.fsiblbd.com/ekyc"
            },
            "SMS Banking": {
                "description": "SMS Banking allows customers to access account information and transaction updates instantly via SMS.",
                "link": "https://fsibplc.com/smsbanking.php"
            },
            "Corporate Banking": {
                "description": "Corporate Banking is tailored for businesses, offering financial solutions that cater to corporate needs.",
                "link": "https://cloud.fsiblbd.com/Corporate/login?returnUrl=%2F"
            }
        }

        # Generate a response dynamically
        if service_name in digital_services_details:
            service_details = digital_services_details[service_name]
            response = f"{service_details['description']} Please click the below button for details."
            buttons = [{"title": f"{service_name}", "payload": service_details['link']}]
            dispatcher.utter_message(text=response, buttons=buttons)
        else:
            response = "Which service would you like to know about?"
            buttons = [{"title": name, "payload": details['link']} for name, details in digital_services_details.items()]
            dispatcher.utter_message(text=response, buttons=buttons)
        
        return []