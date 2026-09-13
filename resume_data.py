"""
Structured Resume Knowledge Base & Humanized Rule-Based QA Engine for Lohith Sankar S
Grounded strictly in official resume: Lohith_CS(AI)_Resume_.pdf
Provides natural, articulate, professional, and conversational first-person responses.
"""

import re
from typing import Dict, Any, List

PROFILE_DATA: Dict[str, Any] = {
    "personal": {
        "name": "Lohith Sankar S",
        "title": "B.Tech Graduate — Computer Science & Engineering (AI)",
        "headline": "Aspiring AI Engineer | Full-Stack & IoT Developer | GenAI & RAG Specialist",
        "location": "Thiruvananthapuram, Kerala, India",
        "phone": "+91 8547715656",
        "email": "crlohithsankar@gmail.com",
        "linkedin": "https://linkedin.com/in/lohith-sankar-s-676043285",
        "github": "https://github.com/Loh2004",
        "summary": (
            "Aspiring Computer Science Engineer with a strong focus on Artificial Intelligence and practical software development. "
            "Skilled in modern web technologies, object-oriented programming, and IoT hardware interfacing. "
            "Passionate about engineering real-world solutions that combine machine learning models with intuitive user experiences."
        ),
    },
    "education": [
        {
            "degree": "B.Tech — Computer Science & Engineering (Artificial Intelligence)",
            "institution": "Mar Baselios College of Engineering and Technology (Autonomous), Thiruvananthapuram",
            "period": "2022 – 2026",
            "score": "CGPA: 6.58",
            "highlights": "Comprehensive focus on Machine Learning, Deep Learning, Computer Vision, Generative AI, Data Structures, and Embedded IoT systems."
        },
        {
            "degree": "12th Standard (CBSE)",
            "institution": "Dr GR Public School, Neyyattinkara",
            "period": "2022",
            "score": "CGPA: 7.12",
            "highlights": "Science stream with Mathematics and Computer Science."
        },
        {
            "degree": "10th Standard (CBSE)",
            "institution": "Dr GR Public School, Neyyattinkara",
            "period": "2020",
            "score": "CGPA: 8.08",
            "highlights": "Strong foundational performance in STEM subjects."
        }
    ],
    "experience": [
        {
            "role": "Junior Data Analyst Intern",
            "company": "Star City Auto Spare Parts Trading L.L.C",
            "location": "Dubai, UAE (Cross-Office Operations)",
            "period": "Aug 2026 – 1 month",
            "overview": (
                "Built an Automotive Quotation Optimization Engine and an in-house enterprise AI copilot (Athena AI), "
                "conducted business analytics and Excel-based financial reporting across Dubai and Indian branches, "
                "and worked directly with SAP-based order fulfillment workflows."
            ),
            "tech_stack": ["Python", "Streamlit", "Pandas", "NumPy", "ReportLab", "Web Speech API (TTS)", "CSS3 Glassmorphism", "SAP"],
            "contributions": [
                "Engineered Athena AI: An internal corporate copilot featuring speech synthesis (TTS) and a modern glassmorphism UI for instant operational insights.",
                "Automated Quotation Engine: Accelerated sales workflows by turning complex multi-supplier price lookups into one-click PDF quotes via ReportLab.",
                "Cross-Office Analytics: Produced executive Excel-based analytics dashboards comparing sales and inventory turnover across Dubai and Indian offices.",
                "Enterprise Systems: Gained hands-on exposure to SAP-based order flow pipelines and international supplier portals."
            ]
        }
    ],
    "projects": [
        {
            "id": "zenguard",
            "name": "ZenGuard — Real-time AI Stress Detection & Management System",
            "tagline": "Published at ICSAIC-2026 (NICHE) • Selected for MBCET 2026 Tech Exhibition",
            "category": "AI Healthcare / IoT Wearables",
            "stack": ["Arduino", "Python", "Random Forest", "Flutter", "Firebase", "IoT Sensors", "Gemini API"],
            "description": (
                "A wearable IoT health system that monitors physiological vitals in real time "
                "(heart rate, Electrodermal Activity [EDA], body temperature, and motion) to predict psychological "
                "stress levels using Random Forest machine learning, paired with a Flutter app and an empathetic conversational AI companion."
            ),
            "key_features": [
                "Integrated multi-sensor wearable hardware using an Arduino microcontroller.",
                "Trained Scikit-Learn Random Forest classifier for high-accuracy stress categorization.",
                "Real-time telemetry and biometric synchronization via Google Firebase.",
                "Mobile dashboard built with Flutter featuring live stress meters and trend analytics.",
                "AI therapeutic conversational companion powered by Gemini API for on-the-spot calming interventions."
            ],
            "publication": "Published in the proceedings of ICSAIC-2026 (NICHE Conference) and selected for showcase at MBCET 2026 Tech Exhibition."
        },
        {
            "id": "genei",
            "name": "Genei — Autonomous AI Voice Assistant & Cognitive Reasoning Engine",
            "tagline": "Executive Desktop AI Assistant with DeepSeek-R1 & Gemini Dual Cognitive Cores",
            "category": "Generative AI / Autonomous Agents",
            "stack": ["Python", "Streamlit", "DeepSeek-R1 (OpenRouter)", "Google Gemini API", "PyPDF", "Edge Neural TTS", "Windows APIs"],
            "description": (
                "An executive desktop copilot engineered with dual cognitive reasoning models (DeepSeek-R1 and Google Gemini). "
                "Features ChatGPT-style multi-session conversational memory, an automated Document Tutor for multi-page PDF ingestion "
                "and grounded Q&A masterclasses, zero-latency studio neural voice synthesis, and native Windows desktop automation."
            ),
            "key_features": [
                "Dual Cognitive Reasoning Core: Dynamically switches between DeepSeek-R1 and Gemini for deep analysis.",
                "Document Tutor (RAG): Ingests multi-page PDFs, chunks semantic context, and delivers structured study sessions.",
                "Studio Neural Voice: Real-time, zero-latency text-to-speech utilizing Microsoft Edge Neural TTS.",
                "Native Desktop Control: Integrates with Windows APIs for Spotify media control, app launching, and system notifications.",
                "Dynamic Conversation Memory: Multi-session hub with automatic conversation titling."
            ]
        },
        {
            "id": "footlink",
            "name": "FootLink — Football Transfer Market Recommendation System",
            "tagline": "Full-Stack ML Platform for Data-Driven Soccer Club Recruitment",
            "category": "Machine Learning / Sports Analytics",
            "stack": ["Python", "Flask", "Random Forest", "Scikit-Learn", "Pandas", "HTML5", "CSS3"],
            "description": (
                "A full-stack machine learning web platform that analyzes comprehensive player statistical metrics, "
                "performance trajectories, and historical transfer data to predict market valuations and recommend "
                "optimal, budget-conscious player transfers for football club scouts and directors."
            ),
            "key_features": [
                "End-to-end data pipeline cleaning and engineering features across large player datasets.",
                "Accurate market valuation predictions using ensemble Random Forest regressors.",
                "Interactive web portal built with Flask allowing scouts to filter by budget, tactical role, and league.",
                "Data-driven decision matrix assessing the return on investment (ROI) of potential acquisitions."
            ]
        },
        {
            "id": "ecoranger",
            "name": "Autonomous Wildlife Sanctuary Tour Guide Vehicle (EcoRanger)",
            "tagline": "Robotic Tour Guide with Real-Time YOLOv8 Animal Detection & Voice Narration",
            "category": "Robotics / Computer Vision & IoT",
            "stack": ["YOLOv8", "Python", "OpenCV", "Raspberry Pi", "IoT Microcontrollers", "Text-to-Speech (TTS)"],
            "description": (
                "A semi-autonomous robotic guide rover designed for wildlife reserves and ecotourism sanctuaries. "
                "Employs an onboard camera and an optimized YOLOv8 deep learning model running on Raspberry Pi to "
                "detect and classify wildlife in real time, delivering synchronous voice-assisted educational commentary "
                "to visitors."
            ),
            "key_features": [
                "Edge computer vision: YOLOv8 real-time object detection optimized for wildlife species.",
                "Hardware integration: Raspberry Pi interfaced with motor drivers, sensors, and camera module.",
                "Contextual Audio Facts: Automatically triggers relevant ecological facts and safety tips upon identifying animals.",
                "Eco-friendly robotic mobility tailored for natural sanctuary pathways."
            ]
        }
    ],
    "skills": {
        "fundamentals": [
            "Machine Learning", "Deep Learning", "Generative AI (LLMs & RAG)",
            "Computer Vision", "SQL", "Data Structures & Algorithms", "OOP Concepts", "Excel Operations"
        ],
        "languages": ["Python (Primary)", "Java", "C", "SQL", "JavaScript"],
        "web_and_apps": ["Streamlit", "Flask", "FastAPI", "Flutter", "HTML5 / CSS3 (Glassmorphism)", "React"],
        "databases": ["MySQL", "MongoDB", "Firebase"],
        "iot_and_hardware": ["Arduino", "Raspberry Pi", "Physiological Sensors", "IoT Interfacing"],
        "other_technical": ["GUI Development", "2D Animation", "Web Speech API (TTS)", "Edge-TTS", "Prompt Engineering"],
        "soft_skills": ["Teamwork", "Problem-Solving", "Adaptability", "Technical Communication", "Research & Documentation"]
    },
    "additional": {
        "languages_spoken": ["English (Fluent)", "Malayalam (Native)", "Hindi (Conversational)"],
        "interests_and_hobbies": ["Pencil Sketching", "Singing", "Gaming", "Cooking", "AI Researching"],
        "publications": [
            "ICSAIC-2026 (NICHE Conference): Research paper on ZenGuard (Real-time AI Stress Detection & Management System)."
        ],
        "exhibitions": [
            "MBCET 2026 Tech Exhibition: Official showcase of the ZenGuard wearable IoT & AI system."
        ]
    }
}


def _has_intent(text: str, patterns: List[str]) -> bool:
    """
    Checks whether any pattern matches as whole words / exact phrase boundaries.
    Handles single words and multi-word phrases cleanly using regex word boundaries (\b).
    Prevents false substring matches (e.g. prevents 'about you' from matching 'about your projects').
    """
    text = text.lower()
    for pattern in patterns:
        pattern = pattern.strip().lower()
        if not pattern:
            continue
        words = pattern.split()
        escaped_words = [re.escape(w) for w in words]
        regex_pattern = r"\b" + r"\s+".join(escaped_words) + r"\b"
        if re.search(regex_pattern, text):
            return True
    return False


def get_rule_based_answer(query: str) -> str:
    """
    Returns an articulate, conversational, humanized first-person response
    grounded 100% in Lohith's verified resume and achievements.
    Uses regex word boundaries and a strict intent hierarchy to guarantee
    that project questions return project details, not self-introductions.
    """
    q = query.lower().strip()

    # 1. SPECIFIC PROJECTS & RESEARCH (Highest Priority)
    # 1a. ZenGuard / Stress Detection / Research Paper / ICSAIC
    if _has_intent(q, ["zenguard", "zen guard", "stress", "wearable", "icsaic", "niche", "exhibition", "paper", "research", "publish", "health"]):
        return (
            "### 🛡️ ZenGuard — Real-time AI Stress Detection & Management System\n\n"
            "**ZenGuard** is one of my most meaningful projects. Our research was accepted and published in the proceedings of "
            "the **ICSAIC-2026 (NICHE)** conference and selected for demonstration at the **MBCET 2026 Tech Exhibition**.\n\n"
            "**The Problem:** Chronic psychological stress is often recognized too late. We wanted to design a non-invasive, proactive "
            "wearable that could continuously monitor body signals and alert users before stress escalates.\n\n"
            "**How We Built It:**\n"
            "1. **IoT Hardware Interfacing:** We integrated biometric sensors (heart rate, Electrodermal Activity [EDA], body temperature, and motion) using an Arduino microcontroller.\n"
            "2. **Machine Learning Model:** Sensor streams are processed by an optimized Scikit-Learn **Random Forest classifier** that categorizes physiological stress levels with high reliability.\n"
            "3. **Cloud Telemetry & Mobile App:** Data is synced to **Google Firebase** in real time, rendering live vitals and stress trends on a custom **Flutter** mobile app.\n"
            "4. **AI Companion:** When elevated stress is detected, the app activates an empathetic therapeutic chatbot powered by the **Gemini API** to guide the user through breathing exercises and calming techniques.\n\n"
            "🛠️ **Tech Stack:** `Arduino` • `Python` • `Random Forest` • `Flutter` • `Firebase` • `IoT Sensors` • `Gemini API`"
        )

    # 1b. Star City Auto / Athena AI / Dubai Internship
    if _has_intent(q, ["star city", "athena", "athena ai", "internship", "dubai", "quotation", "sap", "excel", "experience", "work experience", "job"]):
        return (
            "### 🏢 Junior Data Analyst Intern — Star City Auto Spare Parts Trading L.L.C\n"
            "**📍 Dubai, UAE | 🗓️ Aug 2026 (1 Month)**\n\n"
            "During my internship with Star City Auto, I contributed to sales automation and operational business intelligence:\n\n"
            "• **Athena AI Enterprise Copilot:** I designed and built an in-house AI assistant named *Athena AI* using Python, Streamlit, and modern CSS3 glassmorphism. It integrated the Web Speech API (TTS) so team members could interact via voice and receive instant operational insights.\n"
            "• **Automotive Quotation Optimization Engine:** In the spare parts industry, comparing prices across international suppliers can take hours. I created a custom pricing optimization tool in Streamlit that automated calculation matrices and generated clean, client-ready quotation PDFs using ReportLab.\n"
            "• **Cross-Office Financial & Inventory Analytics:** Conducted comprehensive Excel-based business reporting, tracking order flow, stock turnover, and profitability across the company's offices in Dubai and India.\n"
            "• **SAP Order Flow Exposure:** Gained hands-on operational exposure to SAP-based order fulfillment workflows and supplier portals.\n\n"
            "🛠️ **Tech Stack:** `Python` • `Streamlit` • `Pandas` • `NumPy` • `ReportLab` • `Web Speech API (TTS)` • `CSS3 Glassmorphism` • `SAP`"
        )

    # 1c. Genei / Autonomous Voice Assistant / DeepSeek
    if _has_intent(q, ["genei", "jarvis", "assistant", "voice", "voice assistant", "deepseek", "cognitive", "document tutor", "desktop automation", "spotify"]):
        return (
            "### ⚡ Genei — Autonomous AI Voice Assistant & Cognitive Reasoning Engine\n\n"
            "**Genei** is an advanced desktop executive copilot that I engineered to combine deep cognitive reasoning with native desktop productivity.\n\n"
            "**Key Capabilities:**\n"
            "• **Dual Reasoning Cores:** Connects with both **DeepSeek-R1** (via OpenRouter) and **Google Gemini** to deliver structured, thoughtful problem-solving.\n"
            "• **Document Tutor (RAG):** Features an automated document ingestion pipeline using PyPDF. You can upload multi-page textbooks or research papers, and Genei chunks the content to run grounded, interactive study masterclasses with quiz questions.\n"
            "• **Zero-Latency Neural Voice:** Utilizes Microsoft **Edge Neural TTS** to provide studio-quality, lifelike voice responses with virtually zero audio lag.\n"
            "• **Windows Desktop Automation:** Directly interfaces with Windows APIs to execute system commands, control Spotify media playback, launch applications, and schedule Action Center toast notifications.\n"
            "• **Dynamic Memory Hub:** ChatGPT-style multi-session conversational history with automatic topic-based session titling.\n\n"
            "🛠️ **Tech Stack:** `Python` • `Streamlit` • `DeepSeek-R1` • `Gemini API` • `PyPDF` • `Edge Neural TTS` • `Windows APIs`"
        )

    # 1d. FootLink / Football Transfer Market
    if _has_intent(q, ["footlink", "foot link", "football", "soccer", "transfer", "market", "player", "player valuation"]):
        return (
            "### ⚽ FootLink — Football Transfer Market Recommendation System\n\n"
            "**FootLink** is a full-stack machine learning web application I developed to bring data science to football recruitment and player valuations.\n\n"
            "**How It Works:**\n"
            "• **Data Pipeline:** Extracted and cleaned comprehensive soccer player performance datasets, covering minutes played, passing accuracy, defensive actions, injury history, and historical transfer fees.\n"
            "• **Predictive Valuation:** Implemented Scikit-Learn **Random Forest regression models** to accurately forecast market value and identify undervalued players in the market.\n"
            "• **Scouting Web Portal:** Deployed a responsive web platform using **Flask** and clean HTML/CSS where club scouts can filter targets by budget constraints, tactical position, and league.\n\n"
            "🛠️ **Tech Stack:** `Python` • `Flask` • `Random Forest` • `Scikit-learn` • `Pandas` • `HTML5/CSS3`"
        )

    # 1e. EcoRanger / Wildlife Guide Vehicle / YOLOv8 / Robotics
    if _has_intent(q, ["ecoranger", "eco ranger", "wildlife", "sanctuary", "tour guide", "vehicle", "rover", "yolo", "yolov8", "raspberry", "animal"]):
        return (
            "### 🚙 Autonomous Wildlife Sanctuary Tour Guide Vehicle (EcoRanger)\n\n"
            "**EcoRanger** is a semi-autonomous robotic guide rover engineered for ecotourism reserves and wildlife parks.\n\n"
            "**Key Innovations:**\n"
            "• **Edge Computer Vision:** Features an onboard camera running a custom-trained **YOLOv8** object detection model directly on a **Raspberry Pi**, identifying animals in real time as the rover moves.\n"
            "• **Automated Voice Narration:** When a species is detected, the vehicle dynamically triggers an automated text-to-speech engine delivering educational ecological facts and safety tips to visitors.\n"
            "• **Hardware Control:** Raspberry Pi interfaces with motor drivers, distance sensors for collision prevention, and power management modules.\n\n"
            "🛠️ **Tech Stack:** `YOLOv8` • `Python` • `OpenCV` • `Raspberry Pi` • `IoT Sensors` • `Text-to-Speech (TTS)`"
        )

    # 2. GENERAL PROJECTS OVERVIEW (Checked BEFORE general self-introduction!)
    if _has_intent(q, ["project", "projects", "portfolio", "built", "build", "worked on", "creations", "applications"]):
        return (
            "### 🚀 Featured Engineering Projects\n\n"
            "I have engineered several impactful, end-to-end projects spanning Artificial Intelligence, IoT hardware, and full-stack software:\n\n"
            "1. **🛡️ ZenGuard — Real-time AI Stress Detection & Management System**\n"
            "   • Biometric wearable IoT system integrating Arduino sensors with a Scikit-Learn **Random Forest classifier**, real-time **Firebase** telemetry, and a **Flutter** companion app with Gemini API therapeutic support.\n"
            "   • **Published in ICSAIC-2026** (NICHE Conference) and showcased at the **MBCET 2026 Tech Exhibition**!\n\n"
            "2. **🏢 Athena AI — Enterprise Copilot & Quotation Optimization**\n"
            "   • Built during my internship at **Star City Auto Spare Parts Trading L.L.C** (Dubai) using Python, Streamlit, Web Speech API (TTS), and automated pricing matrices generating PDF quotes with ReportLab.\n\n"
            "3. **⚡ Genei — Autonomous AI Voice Assistant & Cognitive Reasoning Engine**\n"
            "   • Dual reasoning cores (**DeepSeek-R1** & **Google Gemini**), interactive Document Tutor (RAG) with PyPDF, ultra-low-latency Microsoft **Edge Neural TTS**, and native Windows desktop automation.\n\n"
            "4. **⚽ FootLink — Football Transfer Market Recommendation System**\n"
            "   • Full-stack ML platform forecasting soccer player market valuations using Scikit-Learn Random Forest regression and a responsive Flask scouting portal.\n\n"
            "5. **🚙 EcoRanger — Autonomous Wildlife Sanctuary Tour Guide Rover**\n"
            "   • Semi-autonomous rover running custom-trained **YOLOv8** edge computer vision on a **Raspberry Pi** with dynamic automated voice narration for sanctuary visitors.\n\n"
            "💡 *Tip: You can switch to the **'🚀 Featured Projects'** section in the navigation dropdown to see complete architectural breakdowns, or ask me for details on any specific project!*"
        )

    # 3. TECHNICAL SKILLS & TOOLS
    if _has_intent(q, ["skill", "skills", "stack", "tech", "languages", "programming languages", "programming", "framework", "frameworks", "database", "databases", "tools", "iot", "ml", "ai", "technologies", "tech stack"]):
        return (
            "### 💻 My Technical Toolbelt\n\n"
            "Here is how my technical skills break down:\n\n"
            "• **🧠 AI & Machine Learning:** Machine Learning, Deep Learning, Generative AI (LLMs & RAG), Computer Vision (YOLOv8, OpenCV), Scikit-Learn, PyTorch basics, Data Structures & Algorithms.\n"
            "• **⚡ Programming Languages:** Python (primary), Java, C, SQL, JavaScript.\n"
            "• **🌐 Web, App & UI Frameworks:** Streamlit, Flask, FastAPI, Flutter, HTML5, CSS3 (Glassmorphism), React basics.\n"
            "• **🔌 Hardware & IoT:** Arduino Microcontrollers, Raspberry Pi, Sensor Interfacing (Heart rate, EDA, Temperature), Telemetry.\n"
            "• **🗄️ Databases & Storage:** MySQL, MongoDB, Firebase.\n"
            "• **🛠️ Tools & Business Analytics:** Excel Operations, SAP Order Flow exposure, ReportLab, Web Speech API, Edge-TTS, Prompt Engineering.\n"
            "• **🤝 Soft Skills:** Problem Solving, Teamwork, Technical Writing & Research, Fast Adaptability."
        )

    # 4. EDUCATION & ACADEMICS
    if _has_intent(q, ["education", "college", "degree", "university", "mbcet", "school", "cgpa", "btech", "b.tech", "study", "studied", "academics", "marks", "grades", "graduate"]):
        return (
            "### 🎓 Academic Background\n\n"
            "• **B.Tech in Computer Science & Engineering (Artificial Intelligence)**\n"
            "  * *Mar Baselios College of Engineering and Technology (Autonomous), Thiruvananthapuram* (2022 – 2026)\n"
            "  * **CGPA: 6.58**\n"
            "  * Key coursework: Artificial Intelligence, Machine Learning, Deep Neural Networks, Computer Vision, Operating Systems, Database Management Systems, and IoT Architectures.\n\n"
            "• **12th Standard (CBSE) — 2022**\n"
            "  * *Dr GR Public School, Neyyattinkara* | **CGPA: 7.12**\n"
            "  * Science & Computer Science stream.\n\n"
            "• **10th Standard (CBSE) — 2020**\n"
            "  * *Dr GR Public School, Neyyattinkara* | **CGPA: 8.08**"
        )

    # 5. RESUME & CV DOWNLOAD
    if _has_intent(q, ["resume", "cv", "download", "pdf", "file", "document"]):
        return (
            "### 📄 Official Resume\n\n"
            "You can easily access and review my complete official resume:\n\n"
            "• Use the **'Download Official Resume'** button on the left sidebar to download `Lohith_Sankar_S_Resume.pdf`.\n"
            "• Or select **'📄 Resume Document'** from the sidebar dropdown menu to inspect the full embedded document right here in your browser!"
        )

    # 6. CONTACT & SOCIAL PROFILES
    if _has_intent(q, ["contact", "email", "phone", "reach", "call", "message", "github", "linkedin", "hire", "talk", "touch", "location", "connect"]):
        return (
            "### 📫 Let's Connect!\n\n"
            "I'm always open to discussing exciting AI engineering roles, software development opportunities, or collaborative research. "
            "Here is how you can reach me directly:\n\n"
            "• **📧 Email:** [crlohithsankar@gmail.com](mailto:crlohithsankar@gmail.com)\n"
            "• **📱 Phone:** +91 8547715656\n"
            "• **💼 LinkedIn:** [linkedin.com/in/lohith-sankar-s](https://linkedin.com/in/lohith-sankar-s-676043285)\n"
            "• **🐙 GitHub:** [github.com/Loh2004](https://github.com/Loh2004)\n"
            "• **📍 Location:** Thiruvananthapuram, Kerala, India\n\n"
            "Feel free to drop me an email or connect on LinkedIn!"
        )

    # 7. HOBBIES & PERSONAL INTERESTS
    if _has_intent(q, ["hobby", "hobbies", "interest", "interests", "sketch", "sketching", "sing", "singing", "cook", "cooking", "gaming", "game", "languages known", "free time"]):
        return (
            "### 🎨 Beyond Coding\n\n"
            "Outside software development and AI research, here is a bit about my personal passions:\n\n"
            "• **Pencil Sketching:** I love creating detailed pencil drawings and portraits.\n"
            "• **Singing & Music:** Enjoy singing and exploring diverse musical genres.\n"
            "• **Gaming:** Playing strategic and story-driven video games.\n"
            "• **Cooking:** Experimenting with cooking and trying new culinary recipes.\n"
            "• **Languages Spoken:** Fluent in English, native speaker of Malayalam, and conversational in Hindi."
        )

    # 8. SELF INTRODUCTION / BIO / BACKGROUND
    if _has_intent(q, ["who is lohith", "who are you", "about yourself", "tell me about yourself", "introduce yourself", "about you", "bio", "summary", "background", "who are u"]):
        return (
            "I'm **Lohith Sankar S**, an aspiring Computer Science Engineer with a dedicated focus on "
            "**Artificial Intelligence**, **Generative AI & RAG**, and **full-stack software development**.\n\n"
            "🎓 I completed my B.Tech in CSE (Artificial Intelligence) at **Mar Baselios College of Engineering and Technology** "
            "in Thiruvananthapuram (2022–2026).\n\n"
            "💡 What drives me is building practical, end-to-end technology that solves real-world challenges. "
            "Rather than focusing solely on theoretical models, I love connecting algorithms to real interfaces and hardware—whether "
            "that means training a Random Forest classifier on wearable physiological sensors (**ZenGuard**), "
            "engineering enterprise copilot tools with speech synthesis (**Athena AI**), building autonomous robotic guides with edge computer vision (**EcoRanger**), "
            "or developing desktop voice assistants powered by reasoning LLMs (**Genei**).\n\n"
            "When I'm not coding or researching, you'll often find me pencil sketching, singing, gaming, or trying out new cooking recipes!"
        )

    # 9. GREETINGS & PLEASANTRIES
    if _has_intent(q, ["hi", "hello", "hey", "good morning", "good afternoon", "good evening", "greetings", "sup", "wassup", "howdy"]):
        return (
            "Hi there! Welcome to my portfolio! 👋\n\n"
            "I'm **Lohith Sankar S**, a Computer Science graduate specializing in **Artificial Intelligence** "
            "from Mar Baselios College of Engineering and Technology (MBCET) in Thiruvananthapuram.\n\n"
            "Feel free to ask me anything about:\n"
            "• My published research project **ZenGuard** (ICSAIC-2026)\n"
            "• My work at **Star City Auto** in Dubai developing the **Athena AI** copilot\n"
            "• My autonomous desktop assistant **Genei**\n"
            "• My **FootLink** or **EcoRanger** projects\n"
            "• My complete **technical skill set**, education, or how to get in touch!\n\n"
            "What would you like to explore first?"
        )

    # 10. FALLBACK FOR UNHANDLED QUESTIONS
    return (
        "Thank you for asking! 😊\n\n"
        "As Lohith's dedicated portfolio assistant, I'm specifically programmed to provide accurate, grounded answers "
        "about his professional experience, technical projects, and academic background.\n\n"
        "Here are some great topics you can ask me about:\n"
        "• *'Tell me about ZenGuard and your published research'* \n"
        "• *'What did you build during your internship at Star City Auto?'* \n"
        "• *'How does Genei AI assistant work?'* \n"
        "• *'What are your core programming languages and frameworks?'* \n"
        "• *'Where did you study?'* \n"
        "• *'How can I contact you?'*\n\n"
        "Feel free to select one of the suggested questions from the dropdown or type a question about any of these areas!"
    )
