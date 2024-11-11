import pandas as pd
import numpy as np
import random

def generate_random_sentence():
    adjectives = ["", " futuristic", " antique", " old-fashioned", " ordinary", " hideous", " expensive", " elegant", " cheap", " sturdy", " unconventional", " comfy"]
    adj_probabilities = [0.2] + [0.8/(len(adjectives)-1)]*(len(adjectives)-1)
    observations = ["", "-looking", "-feeling"]
    observation_probabilities = [0.7, 0.15, 0.15]
    color_modifiers = ["", " dark", " light", " shiny", " bright"]
    color_modifier_probabilities = [0.5] + [0.5/(len(color_modifiers)-1)]*(len(color_modifiers)-1)
    colors = ["", " red", " green", " blue", " yellow", " white", " black", " orange", " purple", " pink", " brown", " gray", " maroon", " gray"]
    color_probabilities = [0.3] + [0.7/(len(colors)-1)]*(len(colors)-1)
    types = ["", " road", " mountain", " city", " triathlon", " cruiser", " cyclocross", " gravel", " bmx", " racing", " touring"]
    type_probabilities = [0.3, 0.25, 0.2] + [0.25/(len(types)-3)]*(len(types)-3)
    descriptions = ["", " with trispoke wheels", " with a basket", " made for a child", " with thick tires", " with skinny tires", " with spoked wheels", " built for a child", " with skinny tubes", " with thick tubes", " with fenders" " that my grandmother would ride", " that my grandfather would ride", " with a cargo rack"]
    description_probabilities = [0.2] + [0.8/(len(descriptions)-1)]*(len(descriptions)-1)
    a = np.random.choice(adjectives, p=adj_probabilities)
    if a == "":
        o = ""
    else:
        o = np.random.choice(observations, p=observation_probabilities)
    c = np.random.choice(colors, p=color_probabilities)
    if c in ["", " white", " black"]:
        m = ""
    else:
        m = np.random.choice(color_modifiers, p=color_modifier_probabilities)
    t = np.random.choice(types, p=type_probabilities)
    d = np.random.choice(descriptions, p=description_probabilities)
    order_choice = np.random.choice([1, 2], p = [0.2, 0.8])
    if order_choice == 1:
        sentence = m + c + a + o + t + " bike" + d
    else:
        sentence = a + o + m + c + t + " bike" + d
    if sentence[1] in ["a", "e", "i", "o", "u"]:
        sentence = "An" + sentence
    else:
        sentence = "A" + sentence
    sentence = sentence + "."
    return sentence



def describe_color(red, green, blue):
    # Calculate total intensity to create ratios
    total = red + green + blue
    if total == 0:
        return "black"  # If all channels are zero, it's black

    # Calculate ratios for each color component
    red_ratio = red / total
    green_ratio = green / total
    blue_ratio = blue / total

    # Define color based on dominance and combinations of ratios
    if red_ratio > 0.5 and green_ratio < 0.2 and blue_ratio < 0.2:
        return f"{np.random.choice(['vivid', 'fiery', 'intense', 'deep', 'radiant'])} red"
    elif green_ratio > 0.5 and red_ratio < 0.2 and blue_ratio < 0.2:
        return f"{np.random.choice(['bright', 'lush', 'vibrant', 'emerald', 'fresh'])} green"
    elif blue_ratio > 0.5 and red_ratio < 0.2 and green_ratio < 0.2:
        return f"{np.random.choice(['deep', 'cool', 'calm', 'rich', 'bold'])} blue"
    elif red_ratio > 0.4 and blue_ratio > 0.4 and green_ratio < 0.2:
        return f"{np.random.choice(['rich', 'royal', 'deep', 'vibrant', 'mystical'])} purple"
    elif red_ratio > 0.4 and green_ratio > 0.4 and blue_ratio < 0.2:
        return f"{np.random.choice(['vibrant', 'sunny', 'golden', 'bright', 'luminous'])} yellow"
    elif blue_ratio > 0.4 and green_ratio > 0.4 and red_ratio < 0.2:
        return f"{np.random.choice(['striking', 'cool', 'vibrant', 'refreshing', 'crisp'])} cyan"
    elif red_ratio > 0.4 and blue_ratio > 0.2 and green_ratio < 0.2:
        return f"{np.random.choice(['bold', 'striking', 'vivid', 'electric', 'rich'])} magenta"
    elif red_ratio > 0.4 and green_ratio > 0.2 and blue_ratio > 0.2:
        return f"{np.random.choice(['soft', 'bright', 'playful', 'delicate', 'lively'])} pink"
    elif red_ratio > 0.3 and green_ratio > 0.3 and blue_ratio > 0.3:
        return f"{np.random.choice(['neutral', 'pristine', 'elegant', 'bright', 'pure'])} white" if total > 500 else f"{np.random.choice(['balanced', 'sleek', 'modern', 'subtle', 'refined'])} gray"
    else:
        # Fallback to the most dominant color if no strong match
        dominant_color = max((red, 'red'), (green, 'green'), (blue, 'blue'))[1]
        color_descriptions = {
            'red': ["vivid", "fiery", "intense", "deep", "radiant"],
            'green': ["bright", "lush", "vibrant", "emerald", "fresh"],
            'blue': ["deep", "cool", "calm", "rich", "bold"]
        }
        return f"{np.random.choice(color_descriptions[dominant_color])} {dominant_color}"




def generate_bike_name():
    prefixes = [
        "Thunder", "Trail", "Racer", "Falcon", "Speed", "Iron", "Shadow",
        "Lightning", "Peak", "Storm", "Vertex", "Titan", "Bolt", "Sprint",
        "Eagle", "Canyon", "Striker", "Vortex", "Blade", "Hawk", "Summit",
        "Nova", "Maverick", "Stealth", "Meteor", "Echo", "Specter", "Avalanche",
        "Blaze", "Phoenix", "Comet", "Challenger", "Fusion", "Patriot", "Pioneer",
        "Voyager", "Inferno", "Jet", "Rogue", "Cyclone", "Whirlwind", "Zenith",
        "Trek", "Ascend", "Forge", "Thunderbolt", "Flash", "Tempest", "Guardian",
        "Hunter", "Arrow", "Champion", "Mariner", "Navigator", "Titanium", "Forge",
        "Aurora", "Voyage", "Sentinel", "Frontier", "Pulse", "Stormrider", "Vanguard",
        "Raider", "Apex", "Rocket", "Force", "Voyageur", "Outlander", "Hero",
        "Trailblazer", "Adventurer", "Wildcat", "Phantom", "Sonic", "Dominator",
        "Nomad", "Bravo", "Ironclad", "Patron", "Pilot", "Harbinger", "Enigma",
        "Saber", "Nebula", "Prophet", "Conqueror", "Magnum", "Tornado", "Blitz",
        "Shifter", "Impulse", "Scorpion", "Interceptor", "Titanium Viper"
    ]
    
    suffixes = [
        "X", "Pro", "Elite", "Max", "GT", "Ace", "Force", "Sprint", "Wave",
        "Prime", "Ultra", "Turbo", "Carbon", "XR", "One", "Series", "V", "SL",
        "Climb", "CR", "Trail", "Flight", "Rush", "Pulse", "Edge", "Vision",
        "Spirit", "Flow", "Momentum", "Quest", "Surge", "Adventure", "Impact",
        "Hybrid", "Evolution", "Stealth", "Force", "Neo", "Flex", "Enduro",
        "Storm", "Velocity", "Drive", "All-Terrain", "Dynamic", "Fusion", "Terra",
        "Xtreme", "Rider", "Advance", "Supreme", "Commander", "Trailforce",
        "Raptor", "Master", "Invictus", "Champion", "Elite-X", "Infinity", "Voyager",
        "Xpert", "Precision", "Pioneer", "Torque", "Revolution", "Nova", "Excursion",
        "Pursuit", "Altitude", "Shift", "Virtue", "Momentum", "Altitude-X", "Command",
        "Verve", "Impact-X", "Pinnacle", "Rampage", "Circuit", "Ridge", "Axis"
    ]
    
    # Mathematical number patterns for optional endings
    numbers = []
    numbers += [x * 1000 for x in range(1, 10)]  # X000 pattern (1000, 2000, ..., 9000)
    numbers += [x * 100 for x in range(1, 10)]   # X00 pattern (100, 200, ..., 900)
    numbers += [x * 10 for x in range(10, 100)]  # XX0 pattern (100, 110, ..., 990)
    numbers += [x * 100 + 99 for x in range(1, 10)]  # X99 pattern (199, 299, ..., 999)
    
    # Randomly decide whether to add a number (30% chance)
    include_number = np.random.rand() < 0.3
    
    # Construct the bike name
    bike_name = f"{np.random.choice(prefixes)} {np.random.choice(suffixes)}"
    if include_number:
        bike_name += f" {np.random.choice(numbers)}"
    
    return bike_name

def generate_wheel_description(df_slice, probabilities):
    # Helper function to determine "a" or "an"
    def get_article(word):
        return "an" if word and word[0].lower() in "aeiou" else "a"
    
    # Wheel adjectives
    wheel_adjectives_1 = ["", "aerodynamic ", "sleek ", "futuristic ", "lightweight ", "precision-engineered ", "optimized "]
    wheel_adjectives_2 = ["", "carbon-fiber ", "race-optimized ", "high-performance "]
    
    # Determine wheel styles
    rim_style_front = max(["spoked", "trispoke", "disc"], key=lambda x: df_slice[f"RIM_STYLE front OHCLASS: {x.upper()}"])
    rim_style_rear = max(["spoked", "trispoke", "disc"], key=lambda x: df_slice[f"RIM_STYLE rear OHCLASS: {x.upper()}"])

    # Probability-based inclusion of spoke descriptor for front wheel if it’s trispoke
    spoke_descriptor_front = ""
    if rim_style_front == "trispoke" and np.random.rand() < probabilities["spoke_count"]:
        num_spokes_front = df_slice["SPOKES composite front"]
        if num_spokes_front == 3:
            spoke_descriptor_front = "tri-spoked "
        elif num_spokes_front == 4:
            spoke_descriptor_front = "quad-spoked "
        elif num_spokes_front == 5:
            spoke_descriptor_front = "penta-spoked "
        elif num_spokes_front == 6:
            spoke_descriptor_front = "hexa-spoked "
        else:
            spoke_descriptor_front = f"{num_spokes_front}-spoked " if num_spokes_front > 0 else ""

    # Construct wheel prefix
    wheel_prefix = str(np.random.choice(wheel_adjectives_1)) + str(np.random.choice(wheel_adjectives_2))
    article = get_article(wheel_prefix)

    # Handle combinations of front and rear wheel styles, omitting spoked-only setups
    if rim_style_front == "spoked" and rim_style_rear == "spoked":
        return None  # No notable feature for default spoked setup

    if rim_style_front == "trispoke" and rim_style_rear == "trispoke":
        return f"{wheel_prefix}{spoke_descriptor_front}composite-spoke wheels"

    elif rim_style_front == "disc" and rim_style_rear == "disc":
        return f"{wheel_prefix}disc wheels"

    elif rim_style_front == "trispoke" and rim_style_rear == "disc":
        return f"{article} {wheel_prefix}{spoke_descriptor_front}composite-spoke front wheel and {article} {wheel_prefix}disc rear wheel"

    elif rim_style_front == "disc" and rim_style_rear == "trispoke":
        return f"{article} {wheel_prefix}disc front wheel and {article} {wheel_prefix}tri-spoked composite-spoke rear wheel"

    elif rim_style_front == "trispoke" and rim_style_rear == "spoked":
        return f"{article} {wheel_prefix}{spoke_descriptor_front}composite-spoke front wheel"

    elif rim_style_front == "disc" and rim_style_rear == "spoked":
        return f"{article} {wheel_prefix}disc front wheel"

    elif rim_style_front == "spoked" and rim_style_rear == "trispoke":
        return f"{article} {wheel_prefix}tri-spoked composite-spoke rear wheel"

    elif rim_style_front == "spoked" and rim_style_rear == "disc":
        return f"{article} {wheel_prefix}disc rear wheel"

    return None


def generate_description(df_slice):
    # Consolidated probabilities for adding each type of feature
    probabilities = {
        "color": 0.9,
        "frame": 0.8,
        "handlebar": 0.8,
        "belt_drive": 0.5,
        "wheels": 0.8,
        "bottle_mounts": 0.8,
        "fenders": 0.7,
        "aerobars": 0.7,  # 40% chance of including aerobars
        "cargo_rack": 0.7,  # 40% chance of including cargo rack
        "spoke_count": 0.0
    }
    
    potential_features = []
    feature_prefixes = ["with", "featuring", "equipped with", "boasting", "designed with", "crafted with"]
    feature_prefixes_2 = ["features", "is equipped with", "boasts", "comes with", "includes", "offers"]

    # Color description generation with 20% probability of being an empty string
    red_rgb = df_slice["FIRST color R_RGB"]
    green_rgb = df_slice["FIRST color G_RGB"]
    blue_rgb = df_slice["FIRST color B_RGB"]
    color_desc = describe_color(red_rgb, green_rgb, blue_rgb) + " "
    if np.random.rand() < 1 - probabilities["color"]:  # Adjust based on probability
        color_desc = ""

    # Fender logic
    front_fender = df_slice["Front Fender include"] >= 0.5
    rear_fender = df_slice["Rear Fender include"] >= 0.5

    if np.random.rand() < probabilities["fenders"]:
        if front_fender and rear_fender:
            potential_features.append("fenders for added protection")
        elif front_fender:
            potential_features.append("a front fender for splatter resistance")
        elif rear_fender:
            potential_features.append("a rear fender for trail comfort")

    # Aerobars logic
    display_aerobars = df_slice["Display AEROBARS"] >= 0.5
    if display_aerobars and np.random.rand() < probabilities["aerobars"]:
        aerobar_descriptions = [
            "a set of aerodynamic bars", 
            "integrated aerobars for optimal performance", 
            "aerobars for time trial efficiency", 
            "racing aerobars for streamlined control",
            "aerobars for triathlon dominance",
            "aerodynamic bars for speed",
        ]
        potential_features.append(np.random.choice(aerobar_descriptions))

    # Cargo rack logic
    display_rack = df_slice["Display RACK"] >= 0.5
    if display_rack and np.random.rand() < probabilities["cargo_rack"]:
        cargo_rack_descriptions = [
            "a cargo rack for extra storage", 
            "a sturdy rear rack for carrying gear", 
            "an integrated cargo rack for commuting", 
            "a versatile rack for added utility"
        ]
        potential_features.append(np.random.choice(cargo_rack_descriptions))

    # Frame material logic with enhanced descriptors
    frame_adjectives = {
        "titanium": ["a lightweight", "an indestructible", "an advanced", "a premium", "a high-end", "a resilient", "a rustproof", "an aerospace-grade", "a sleek"],
        "carbon": ["a high-performance", "an ultra-lightweight", "a cutting-edge", "a race-ready", "a stiff", "a modern", "an aerodynamic", "a competition-grade"],
        "steel": ["a classic", "a strong", "a time-tested", "a durable", "a sturdy", "a retro-inspired", "a resilient", "an enduring"],
        "aluminium": ["a versatile", "a lightweight", "a budget-friendly", "a reliable", "a corrosion-resistant", "a robust", "an affordable", "a sporty"],
        "bamboo": ["an eco-friendly", "a sustainable", "a natural", "a unique", "a shock-absorbing", "a lightweight", "an organic", "a renewable-resource"],
        "other": []  # No adjectives for "other" as we want to exclude it
    }

    # Determine the frame type and add a feature
    if np.random.rand() < probabilities["frame"]:
        frame_type = max(frame_adjectives, key=lambda x: df_slice[f"MATERIAL OHCLASS: {x.upper()}"])
        if frame_type != "other":
            frame_adj = np.random.choice(frame_adjectives[frame_type])
            potential_features.append(f"{frame_adj} {frame_type} frame")

    # Handlebar style logic with expanded descriptors
    handlebar_adjectives = {
        "0": ["classic", "aerodynamic", "road-ready", "versatile", "sleek", "precision-designed", "high-speed", "comfort-optimized"],
        "1": ["rugged", "durable", "off-road", "adventure-ready", "wide", "shock-absorbing", "trail-proven", "versatile"],
        "2": ["aggressive", "urban", "streamlined", "race-oriented", "ergonomic", "city-friendly", "fast-handling", "sleek-profiled"]
    }

    handlebar_names = {
        "0": ["drop handlebars", "road handlebars", "curved bars", "drop bars", "race bars"],
        "1": ["MTB handlebars", "mountain bike bars", "flat bars", "trail bars", "mountain bars"],
        "2": ["bullhorn handlebars", "urban bullhorns", "racing bullhorns", "bullhorns", "track bullhorns"]
    }

    if np.random.rand() < probabilities["handlebar"]:
        handlebar_type = max(["0", "1", "2"], key=lambda x: df_slice[f"Handlebar style OHCLASS: {x.upper()}"])
        handlebar_adj = np.random.choice(handlebar_adjectives[handlebar_type])
        handlebar_name = np.random.choice(handlebar_names[handlebar_type])
        potential_features.append(f"{handlebar_adj} {handlebar_name}")

    # Belt drive logic with more detailed descriptions
    if df_slice["BELTorCHAIN OHCLASS: 0"] > df_slice["BELTorCHAIN OHCLASS: 1"] and np.random.rand() < probabilities["belt_drive"]:
        belt_drive_descriptions = [
            "a belt drive system", 
            "an advanced belt drive setup", 
            "a low-maintenance belt drive", 
            "a smooth and quiet belt drive system", 
            "a modern belt drive configuration", 
            "a hassle-free belt drive system", 
            "a clean and efficient belt drive",
            "a precision-engineered belt drive"
        ]
        potential_features.append(np.random.choice(belt_drive_descriptions))

    # Wheel style logic with expanded descriptors
    potential_wheel_feature = generate_wheel_description(df_slice, probabilities)
    if potential_wheel_feature:
        potential_features.append(potential_wheel_feature)



    # Bottle holder logic with expanded postfix options
    if np.random.rand() < probabilities["bottle_mounts"]:
        seattube_bottle = df_slice["bottle SEATTUBE0 show OHCLASS: False"] < df_slice["bottle SEATTUBE0 show OHCLASS: True"]
        downtube_bottle = df_slice["bottle DOWNTUBE0 show OHCLASS: False"] < df_slice["bottle DOWNTUBE0 show OHCLASS: True"]
        bottle_postfix_options = [
            "", 
            " for quick and easy hydration on the go", 
            " to stay hydrated on your ride", 
            " for easy access to water", 
            " for your convenience", 
            " for easy hydration", 
            " for quick and easy access to water",
            " to keep you refreshed during long rides",
            " to make hydration seamless and simple",
            " designed for effortless water access",
            " so you never miss a sip",
            " for those hot, sunny rides"
        ]
        bottle_postfix = np.random.choice(bottle_postfix_options)

        if seattube_bottle and downtube_bottle:
            potential_features.append(f"dual bottle mounts on the seat tube and down tube{bottle_postfix}")
        elif seattube_bottle:
            potential_features.append(f"a seat tube-mounted bottle holder{bottle_postfix}")
        elif downtube_bottle:
            potential_features.append(f"a down tube-mounted bottle holder{bottle_postfix}")

    fallback_features = [
        "a durable build",
        "precision engineering",
        "an ergonomic design",
        "superior craftsmanship",
        "a sleek and modern finish",
        "a versatile frame",
        "rugged construction",
        "advanced components",
        "high-quality materials",
        "a smooth ride experience",
        "a lightweight profile",
        "a unique aesthetic",
        "stability and comfort",
        "state-of-the-art components",
        "a high-tech build",
        "optimized handling",
        "cutting-edge technology",
        "a user-friendly design",
        "superior balance"
    ]

    if not potential_features:
        potential_features.append(np.random.choice(fallback_features))

    if potential_features:
        random.shuffle(potential_features)

    # Generating the bike description with the collected features
    bike_name = generate_bike_name()
    bike_intro = f"the {color_desc}{bike_name}".strip()

    if len(potential_features) > 2:
        feature_list = ', '.join(potential_features[:-1]) + ', and ' + potential_features[-1]
    elif len(potential_features) == 2:
        feature_list = ' and '.join(potential_features)
    elif potential_features:
        feature_list = potential_features[0]

    prefixing = np.random.choice(feature_prefixes)
    prefixes = np.random.choice(feature_prefixes_2)
    sentence_template = np.random.choice([
        f"{bike_intro} {prefixes} {feature_list}.",
        f"{bike_intro} {prefixes} {feature_list} and is the solution to your cycling needs.",
        f"{bike_intro} {prefixes} {feature_list}, ensuring top-tier performance on every ride.",
        f"{bike_intro} {prefixes} {feature_list} for unmatched cycling performance.",
        f"{prefixing} {feature_list}, {bike_intro} is the ultimate machine for your next ride.",
        f"{prefixing} {feature_list}, {bike_intro} is ready to take on any challenge.",
        f"With {feature_list}, {bike_intro} sets a new standard in cycling.",
        f"Unleash your inner power with {bike_intro}, {prefixing} {feature_list}.",
        f"Get ready for your best ride yet with {bike_intro}, {prefixing} {feature_list}.",
        f"{prefixing} {feature_list}, {bike_intro} promises unparalleled performance.",
        f"Experience excellence with {bike_intro}, {prefixing} {feature_list}.",
        f"Take your rides to the next level with {bike_intro}, {prefixing} {feature_list}.",
        f"{bike_intro}, {prefixing} {feature_list}, is built for those who demand the best.",
        f"Crafted for performance, {bike_intro} {prefixes} {feature_list} to meet your cycling needs.",
        f"Engineered for your adventures, {bike_intro} {prefixes} {feature_list}.",
        f"Redefine your cycling experience with {bike_intro}, {prefixing} {feature_list}.",
        f"Elevate your journey with {bike_intro}, {prefixing} {feature_list}.",
        f"Perfect for enthusiasts, {bike_intro} {prefixes} {feature_list}.",
        f"Reach new heights with {bike_intro} {prefixing} {feature_list}.",
        f"Designed to impress, {bike_intro} {prefixes} {feature_list} for all your adventures.",
        f"Discover the freedom of cycling with {bike_intro} {prefixing} {feature_list}.",
        f"{bike_intro} {prefixes} {feature_list}, perfect for those who demand quality and style.",
        f"{prefixing} {feature_list}, {bike_intro} will redefine your cycling experience.",
        f"Push the limits of your ride with {bike_intro} {prefixing} {feature_list}.",
        f"Transform your rides with {bike_intro}, {prefixing} {feature_list}.",
        f"Built for champions, {bike_intro} {prefixes} {feature_list} for peak performance.",
        f"{bike_intro} {prefixes} {feature_list}, combining innovation and reliability.",
        f"{prefixing} {feature_list}, {bike_intro} delivers unparalleled comfort and control.",
        f"With {feature_list}, {bike_intro} turns every ride into an adventure.",
        f"{bike_intro} {prefixes} {feature_list} to take your cycling further.",
        f"{bike_intro} is made {prefixes} {feature_list} to ensure an unforgettable ride.",
        f"{bike_intro}, {prefixing} {feature_list}, is crafted to exceed your expectations.",
        f"Enjoy every mile with {bike_intro}, {prefixing} {feature_list} for superior handling.",
        f"{prefixing} {feature_list}, {bike_intro} stands out from the competition.",
        f"Explore new trails with {bike_intro}, {prefixing} {feature_list} for unmatched durability.",
        f"{bike_intro} {prefixes} {feature_list}, making each ride smoother and more enjoyable.",
        f"Conquer any road with {bike_intro}, {prefixing} {feature_list} for exceptional performance.",
        f"Embrace the road ahead with {bike_intro}, {prefixing} {feature_list}.",
        f"{prefixing} {feature_list}, {bike_intro} is the perfect companion for your rides.",
        f"Experience the thrill of the ride with {bike_intro}, {prefixing} {feature_list}.",
        f"Built for those who dare, {bike_intro} {prefixes} {feature_list}.",
        f"Feel the power of the road with {bike_intro}, {prefixing} {feature_list}.",
        f"Take on any challenge with {bike_intro}, {prefixing} {feature_list}.",
        f"{bike_intro} {prefixes} {feature_list}, ready to make every ride memorable.",
        f"Push your boundaries with {bike_intro}, {prefixing} {feature_list}.",
        f"{bike_intro} {prefixes} {feature_list} to support your cycling ambitions."
    ])

    # Ensure the first character is capitalized if needed
    if sentence_template[0].islower():
        sentence_template = sentence_template[0].upper() + sentence_template[1:]

    return sentence_template
