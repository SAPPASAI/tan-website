from flask import Flask, render_template,request,redirect,url_for

app = Flask(__name__)

@app.route('/')
def index():
     return render_template('index.html')

@app.route('/about')
def about():
     return render_template('about.html')

@app.route('/founders')
def founders():
     return render_template('founder.html')

@app.route('/trustees')
def trustees():
     return render_template('trusts.html')

@app.route('/previous-leadership')
def previous_leaderships():
     return render_template('previous_leaders.html')

@app.route('/present-leadership')
def present_leaderships():
     return render_template('present_leaders.html')

@app.route('/membership-benefits')
def membership_benefits():
     return render_template('membership_benefits.html')


@app.route("/membership-form", methods=["GET", "POST"])
def membership():
    if request.method == "POST":
        full_name = request.form["full_name"]
        email = request.form["email"]
        phone = request.form["phone"]
        address = request.form.get("address", "")
        gender = request.form.get("gender", "")
        membership_type = request.form.get("membership_type", "")
        message = request.form.get("message", "")

        print(f"New Membership: {full_name}, {email}, {phone}")

        return render_template("membership_form.html", success=True, name=full_name)

    return render_template("membership_form.html", success=False)


@app.route('/members-details')
def members_details():
    # You can replace this list with database query results
    members_list = [
        {"name": "Ravi Kumar", "gender": "Male", "membership_type": "General Member", "message": "Excited to be part of TAN!"},
        {"name": "Sita Devi", "gender": "Female", "membership_type": "Life Member", "message": "Love participating in cultural events."},
        {"name": "Sita Devi", "gender": "Female", "membership_type": "Life Member", "message": "Love participating in cultural events."},
        {"name": "Sita Devi", "gender": "Female", "membership_type": "Life Member", "message": "Love participating in cultural events."},
        {"name": "Sita Devi", "gender": "Female", "membership_type": "Life Member", "message": "Love participating in cultural events."},
        {"name": "Sita Devi", "gender": "Female", "membership_type": "Life Member", "message": "Love participating in cultural events."},
    ]
    return render_template('members_details.html', members=members_list)

@app.route('/sponsors-slider')
def sponsors_slider():
    sponsors_list = [
        {"name": "Company A", "logo": url_for('static', filename='images/sponsors/company-a.png')},
        {"name": "Company B", "logo": url_for('static', filename='images/sponsors/company-b.png')},
        {"name": "Company C", "logo": url_for('static', filename='images/sponsors/company-c.png')}
    ]
    return render_template('sponsors_slider.html', sponsors=sponsors_list)

@app.route('/sponsors-details')
def sponsor_details():
    sponsors = [
        {
            "name": "Company A",
            "description": "Leading provider of tech solutions with over 20 years of experience.",
            "logo": url_for('static', filename='images/sponsors/company-a.png'),
            "website": "https://www.companya.com"
        },
        {
            "name": "Company B",
            "description": "Supporting youth innovation and entrepreneurship.",
            "logo": url_for('static', filename='images/sponsors/company-b.png'),
            "website": "https://www.companyb.org"
        },
        {
            "name": "Company C",
            "description": "Committed to community development and education.",
            "logo": url_for('static', filename='images/sponsors/company-c.png'),
            "website": "https://www.companyc.edu"
        }
    ]
    return render_template('sponsors_details.html', sponsors=sponsors)

@app.route('/gallery-old')
def gallery():
    # Dummy old images
    gallery_images = [
        {"filename": "image1.jpeg", "title": "Community Meetup 2019"},
        {"filename": "image2.jpg", "title": "Annual Tech Fair 2020"},
        {"filename": "image3.png", "title": "Workshop 2021"},
        {"filename": "image4.jpeg", "title": "Health Awareness Camp 2018"},
    ]
    return render_template('gallery_old.html', images=gallery_images)
    
@app.route("/gallery-current")
def gallery_present():
    present_images = [
        {"filename": "image1.jpeg", "title": "Tech Fair 2023"},
        {"filename": "image2.jpg", "title": "Volunteer Day 2024"},
        {"filename": "image3.png", "title": "Annual Meetup 2025"},
        {"filename": "image4.jpeg", "title": "Annual Meetup 2025"},
        # Add more images here
    ]
    return render_template("current_gallery.html", images=present_images)

@app.route("/events")
def events_calendar():
    events = [
        {
            "title": "Tech Talk 2025",
            "start": "2025-06-15"
        },
        {
            "title": "Volunteer Meetup",
            "start": "2025-07-01"
        },
        {
            "title": "Annual Conference",
            "start": "2025-08-21",
            "end": "2025-08-23"
        },
        {
            "title": "festivle",
            "start": "2025-08-23",
            "end": "2025-08-26"
        }
    ]
    return render_template("event.html", events=events)

@app.route('/telugu-calendar')
def telugu_calendar():
    return render_template('telugu_calendar.html')


@app.route("/temples")
def temples():
    temples_data = [
        {
            "name": "Tirumala Venkateswara Temple",
            "location": "Tirupati, Andhra Pradesh",
            "image_url": "https://www.fabhotels.com/blog/wp-content/uploads/2019/03/Places-to-Visit-in-Tirupati600x400.jpg",
            "description": "One of the most visited and richest temples in the world."
        },
        {
            "name": "Srisailam Mallikarjuna Temple",
            "location": "Srisailam, Andhra Pradesh",
            "image_url": "https://i0.wp.com/oneday.travel/wp-content/uploads/2018/03/one-day-hyderabad-to-srisailam-sightseeing-tour-package-by-car-bhramaramba-mallikarjuna-swamy-temple.jpg?resize=750%2C400&ssl=1",
            "description": "Famous Jyotirlinga shrine located on the banks of River Krishna."
        },
        {
            "name": "Kanaka Durga Temple",
            "location": "Vijayawada, Andhra Pradesh",
            "image_url": "https://kanakadurgamma.org/static/media/IMG-20220413-WA0018@2x.7f356c08.png",
            "description": "Prominent temple of Goddess Durga atop Indrakeeladri hill."
        }
    ]
    return render_template("temples.html", temples=temples_data)

@app.route("/articles")
def articles():
    articles = [
        {
            "title": "Importance of Ugadi Festival",
            "excerpt": "Ugadi marks the beginning of the Telugu New Year and is celebrated with rituals and food...",
            "image_url": "/static/images/gallery/image1.jpeg",
            "tags": ["Festival", "Culture"],
            "link": "/articles/ugadi"
        },
        {
            "title": "Temples in Andhra Pradesh",
            "excerpt": "Andhra Pradesh is home to many famous temples that are spiritual and architectural marvels...",
            "image_url": "/static/images/gallery/image1.jpeg",
            "tags": ["Temples", "Travel"],
            "link": "/articles/temples-ap"
        },
        {
            "title": "Telugu Calendar Explained",
            "excerpt": "The Telugu calendar is a lunisolar calendar with cultural and religious significance...",
            "image_url": "/static/images/gallery/image1.jpeg",
            "tags": ["Calendar", "Culture"],
            "link": "/articles/telugu-calendar"
        }
    ]
    tags = sorted({tag for article in articles for tag in article['tags']})
    return render_template("articles.html", articles=articles, tags=tags)


@app.route("/contact")
def contact_ids():
    contacts = [
        {
            "name": "Sri Ramachandra Rao",
            "designation": "Temple Chairman",
            "phone": "+91 9876543210",
            "email": "ramachandra@example.com",
            "photo": "/static/images/gallery/image3.png",
            "social": {
                "facebook": "https://facebook.com/ramachandra",
                "twitter": "",
                "linkedin": "",
                "instagram": ""
            }
        },
        {
            "name": "Smt. Lakshmi Devi",
            "designation": "Cultural Coordinator",
            "phone": "+91 9123456780",
            "email": "lakshmi@example.com",
            "photo": "/static/images/gallery/image1.jpeg",
            "social": {
                "facebook": "",
                "twitter": "",
                "linkedin": "https://linkedin.com/in/lakshmidevi",
                "instagram": ""
            }
        },
        {
            "name": "Sri Krishna Rao",
            "designation": "Events Manager",
            "phone": "+91 9012345678",
            "email": "krishna@example.com",
            "photo": "/static/images/gallery/image2.jpg",
            "social": {
                "facebook": "",
                "twitter": "https://twitter.com/krishnarao",
                "linkedin": "",
                "instagram": "https://instagram.com/krishnarao"
            }
        }
    ]
    return render_template("contact_id.html", contacts=contacts)


@app.route("/emergency-contacts")
def emergency_contacts():
    emergency_contacts = [
        {
            "name": "Police",
            "description": "For law enforcement or emergencies",
            "phone": "100"
        },
        {
            "name": "Ambulance",
            "description": "For medical emergency assistance",
            "phone": "108"
        },
        {
            "name": "Fire Department",
            "description": "In case of fire or rescue",
            "phone": "101"
        },
        {
            "name": "Disaster Management",
            "description": "Floods, earthquakes, and other disasters",
            "phone": "1078"
        },
        {
            "name": "Women Helpline",
            "description": "Support and assistance for women",
            "phone": "1091"
        },
        {
            "name": "Child Helpline",
            "description": "Help and protection for children",
            "phone": "1098"
        }
    ]
    return render_template("emergency_contact.html", emergency_contacts=emergency_contacts)

@app.route("/jobs")
def all_jobs():
    it_jobs = [
        {"title": "Frontend Developer", "company": "TechCorp", "location": "Hyderabad", "type": "Full-time","apply_link": "https://example.com/apply/frontend"},
        {"title": "Backend Developer", "company": "CodeWorks", "location": "Bangalore", "type": "Remote","apply_link": "https://example.com/apply/frontend"},
    ]
    non_it_jobs = [
        {"title": "HR Executive", "company": "PeopleFirst", "location": "Chennai", "type": "Full-time","apply_link": "https://example.com/apply/frontend"},
        {"title": "Marketing Assistant", "company": "AdZone", "location": "Delhi", "type": "Part-time","apply_link": "https://example.com/apply/frontend"},
    ]
    return render_template("jobs.html", it_jobs=it_jobs, non_it_jobs=non_it_jobs)


# if __name__ == '__main__': 
#      app.run(debug=True)