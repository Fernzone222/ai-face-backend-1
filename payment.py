import stripe

stripe.api_key = "sk_test_..."

def create_checkout_session():
    # Placeholder for creating session
    return "cs_test_..."
    
def stripe_webhook(payload):
    # Handle webhook
    pass
