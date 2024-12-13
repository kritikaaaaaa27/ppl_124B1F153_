def suggest_skincare_products(skin_type, concern):
    # Skincare recommendations database
    recommendations = {
        "dry": {
            "hydration": ["Hyaluronic Acid Serum", "Ceramide Moisturizer", "Hydrating Toner"],
            "anti-aging": ["Peptide Cream", "Retinol Serum", "Nourishing Night Oil"],
            "brightening": ["Vitamin C Serum", "Gentle Exfoliating Toner", "Brightening Cream"]
        },
        "oily": {
            "hydration": ["Lightweight Gel Moisturizer", "Oil-Free Hydrating Serum", "Aloe Vera Gel"],
            "anti-acne": ["Salicylic Acid Cleanser", "Niacinamide Serum", "Clay Mask"],
            "brightening": ["Vitamin C Gel", "Exfoliating Pads", "Brightening Sunscreen"]
        },
        "combination": {
            "hydration": ["Balancing Moisturizer", "Hyaluronic Acid Gel", "Toning Mist"],
            "anti-aging": ["Retinol Cream", "Peptide Serum", "Night Mask"],
            "brightening": ["Vitamin C Cream", "Gentle AHA Exfoliant", "Brightening Serum"]
        },
        "sensitive": {
            "hydration": ["Soothing Cream", "Fragrance-Free Moisturizer", "Calming Toner"],
            "anti-redness": ["Centella Asiatica Serum", "Green Tea Gel", "Chamomile Cream"],
            "brightening": ["Gentle Vitamin C Serum", "Licorice Root Extract", "Brightening Moisturizer"]
        }
    }

    # Check if skin type and concern are valid
    if skin_type in recommendations and concern in recommendations[skin_type]:
        products = recommendations[skin_type][concern]
        return f"For {skin_type} skin with a focus on {concern}, we recommend: {', '.join(products)}."
    else:
        return "Sorry, we don't have recommendations for your input. Please check your skin type and concern."

# User interaction
print("Welcome to the Skincare Product Suggester!")
skin_type = input("Enter your skin type (dry, oily, combination, sensitive): ").lower()
concern = input("Enter your primary skin concern (hydration, anti-aging, brightening, anti-acne, anti-redness): ").lower()

# Get product suggestions
result = suggest_skincare_products(skin_type, concern)
print(result)
makeup_time=input("Do you want steps for flawless makeup:")
if makeup_time=="yes":
    print("Here it is")
    print("[1] Cleanse your Face with a gentle cleanser.",  "[2] Use sunscreen (SPF 30 or higher)",  "[3] Apply a primer moisturizer to smooth skin.",  "[4] Use a BB/CC cream or light foundation and concealer for coverage.",  "[5] Set makeup with a powder ",  "[6] Brush on a natural blush to cheeks.",   "[7]Apply a coat of mascara.",   "[8] Finish with a tinted lip balm or gloss.")  
else:
        print("Ok")