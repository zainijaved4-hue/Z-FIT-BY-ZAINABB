from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    highlights = [
        {"icon": "🏋️", "title": "State-of-the-Art Equipment", "desc": "200+ premium machines and free weights for every fitness level."},
        {"icon": "🔥", "title": "Expert Trainers", "desc": "Certified coaches who tailor every session to your personal goals."},
        {"icon": "💧", "title": "Recovery Zone", "desc": "Sauna, steam room, and cold plunge to accelerate recovery."},
        {"icon": "📅", "title": "60+ Weekly Classes", "desc": "From HIIT to Yoga — there's always something to keep you moving."},
    ]
    return render_template('home.html', highlights=highlights)

@app.route('/about')
def about():
    team = [
        {"name": "Zainab Javed", "role": "Founder & Head Coach", "bio": "NASM-certified trainer with 10+ years transforming lives through fitness."},
        {"name": "Sara Ahmed", "role": "Nutrition Specialist", "bio": "Registered dietitian crafting personalised meal plans for peak performance."},
        {"name": "Ali Raza", "role": "Strength Coach", "bio": "Former competitive powerlifter bringing elite technique to every session."},
        {"name": "Hira Baig", "role": "Yoga & Mindfulness", "bio": "500-hour certified instructor blending movement with mental wellness."},
    ]
    facilities = [
        "5,000 sq ft Training Floor",
        "Dedicated Cardio Suite",
        "Group Fitness Studio",
        "Private Coaching Rooms",
        "Recovery & Spa Zone",
        "Juice & Nutrition Bar",
        "Secure Locker Rooms",
        "Free Parking",
    ]
    return render_template('about.html', team=team, facilities=facilities)

@app.route('/membership')
def membership():
    plans = [
        {
            "name": "Starter",
            "price": "Rs 4,999",
            "period": "/ month",
            "tag": None,
            "features": [
                "Full gym floor access",
                "2 group classes / week",
                "Locker room access",
                "Fitness assessment",
            ],
            "cta": "Get Started",
        },
        {
            "name": "Elite",
            "price": "Rs 8,999",
            "period": "/ month",
            "tag": "Most Popular",
            "features": [
                "Everything in Starter",
                "Unlimited group classes",
                "1 PT session / month",
                "Nutrition consultation",
                "Recovery zone access",
            ],
            "cta": "Join Elite",
        },
        {
            "name": "VIP",
            "price": "Rs 14,999",
            "period": "/ month",
            "tag": "Best Value",
            "features": [
                "Everything in Elite",
                "4 PT sessions / month",
                "Custom meal plan",
                "Priority class booking",
                "Guest pass (2/month)",
                "Dedicated locker",
            ],
            "cta": "Go VIP",
        },
    ]
    services = [
        {"icon": "🎯", "name": "Personal Training", "desc": "1-on-1 sessions laser-focused on your goals."},
        {"icon": "🥗", "name": "Nutrition Coaching", "desc": "Personalised plans built around your lifestyle."},
        {"icon": "🧘", "name": "Group Classes", "desc": "60+ weekly classes across all disciplines."},
        {"icon": "📊", "name": "Progress Tracking", "desc": "Regular assessments to keep you on target."},
    ]
    return render_template('membership.html', plans=plans, services=services)

if __name__ == '__main__':
    app.run(debug=True)
