class topics:
    class health:
        words = ['activity', 'allergy', 'antibiotic', 'appetite', 'appointment', 'back pain', 'blood pressure', 'body mass index (BMI)', 
            'bone health', 'brain health', 'cancer', 'cholesterol', 'chronic disease', 'cold', 'congestion', 'cough', 'dentist', 
            'depression', 'dermatologist', 'diabetes', 'diarrhea', 'diet', 'doctor', 'drugstore', 'earache', 'emergency room', 
            'endocrinologist', 'exercise', 'fever', 'flu', 'food poisoning', 'foot doctor', 'general practitioner (GP)', 'gerontologist', 
            'gynecologist','headache', 'health' ,'heart disease', 'height', 'hepatitis', 'high blood pressure', 'hospital', 'immune system', 'infection', 'injury', 'insulin', 
            'laboratory test', 'lifestyle', 'medication', 'mental health', 'muscle pain', 'nutrition', 'obesity', 'oncologist', 'ophthalmologist', 
            'orthodontist', 'oxygen', 'pain', 'pediatrician', 'pharmacist', 'physical therapist', 'physician', 'pneumonia', 'pregnancy', 'prescription', 
            'prevention', 'psychiatrist', 'psychologist', 'pulmonologist', 'radiologist', 'rheumatologist', 'sleep', 'smoking', 'specialist', 'stress', 
            'surgery', 'symptoms', 'therapist', 'throat pain', 'urinary tract infection (UTI)', 'vaccination', 'vitamin', 'weight loss', 'wellness', 
            "women's health"]
        
        score = 0

        def adding_count_to_score(self,c):
            self.score += c
    
            
    class technology:
        words = [
            "3d", "ai", "bandwidth", "biotechnology", "blockchain", "browser", "chatbot", "cloud", "cloud computing", "code", "coding", "communication",
            "computer", "crypto", "cryptocurrency", "cybersecurity", "database", "device", "digital", "drones", "e-commerce", "e-learning", "electronics",
            "email", "encryption", "engineering", "firmware", "gadget", "gaming", "hosting", "html", "http", "ip address", "it", "linux", "mac OS", "machine",
            "machine learning", "memory", "mobile", "mobile app", "nas", "network", "nanotechnology", "operating", "operating system", "os", "pc", "personal computer",
            "phone", "platform", "privacy", "printer", "programming", "python", "reality", "seo", "server", "smart", "software", "startup", "storage", "stream",
            "system", "tablet", "telecommunications", "ui/ux", "virtual machine", "web", "web development", "wearable"
            ]
                
        score = 0

        def adding_count_to_score(self,c):
            self.score += c

    
    class travelAndTourism:
        words = [
            'accommodation', 'adventure', 'airline', 'arrival', 'attraction', 'backpacking', 'beach', 'biotechnology', 'booking', 'cabin', 'car', 'city', 
            'cruise', 'cultural', 'culture', 'cuisine', 'departure', 'desert', 'destination', 'dining', 'entertainment', 'experience', 'expedition', 'explore', 
            'flight', 'foreign', 'getaway', 'guide', 'heritage', 'hiking', 'historic', 'holiday', 'hospitality', 'itinerary', 'jet', 'journey', 'landmark', 
            'leisure', 'local', 'mountain', 'mountains', 'nature', 'passport', 'package', 'photography', 'pilgrimage', 'recreation', 'reservation', 'reservations', 
            'resort', 'restaurant', 'route', 'safari', 'sailing', 'scenery', 'scenic', 'sightseeing', 'sightseer', 'souvenir', 'suitcase', 'sunset', 'ticket', 
            'tour', 'tourism', 'tourist', 'traveler', 'trip', 'trekking', 'vacation', 'visa', 'voyage', 'wellness', 'wildlife'
            ]

        score = 0

        def adding_count_to_score(self,c):
            self.score += c
    

    class science:
        words = [
            'analyze', 'analysis', 'atoms', 'biological', 'biology', 'chemical', 'chemistry', 'community', 'conclude', 'conclusion', 'control', 'data', 'dependent',
            'discovery', 'ecology', 'elements', 'environment', 'environmental', 'evidence', 'experiment', 'experimentation', 'geology', 'hypothesize', 'hypothesis', 'independent',
            'innovation', 'journal', 'knowledge', 'laboratory', 'measure', 'method', 'methodology', 'molecular', 'molecules', 'observation', 'observe', 'organisms', 'particles',
            'peer', 'physical', 'physics', 'publication', 'reaction', 'research', 'researcher', 'science', 'scientific', 'scientist', 'technology', 'theory', 'variable'
            ]
        
        score = 0

        def adding_count_to_score(self,c):
            self.score += c

    class artAndCulture:
        words = [
        'abstract', 'act', 'antiquity', 'architecture', 'art', 'artist', 'avant-garde', 'baroque', 'brush', 'canvas', 'choreography', 'classical', 'color', 
        'composition', 'contemporary', 'craft', 'craftsman', 'creative', 'creativity', 'cultural', 'culture', 'dance', 'design', 'designer', 'director', 
        'exhibition', 'expression', 'expressionism', 'film', 'folk', 'gallery', 'heritage', 'history', 'impressionism', 'literary', 'literature', 'masterpiece', 
        'modern', 'movie', 'music', 'neoclassical', 'novel', 'palette', 'painting', 'performance', 'poetry', 'pop', 'realism', 'renaissance', 'rococo', 
        'scenic', 'screenplay', 'sculpture', 'symphony', 'theater', 'tradition', 'visual'
        ]
        
        score = 0

        def adding_count_to_score(self,c):
            self.score += c

    class politics:
        words = [
            'administration', 'affairs', 'authority', 'bureaucracy', 'campaign', 'candidate', 'civil', 'congress', 'constitution', 'corruption', 'democracy', 'diplomacy',
            'election', 'foreign', 'government', 'ideology', 'international', 'justice', 'law', 'leadership', 'legislation', 'lobbying', 'minister', 'opposition', 'parliament',
            'party', 'political', 'politician', 'politics', 'power', 'president', 'public', 'relation', 'rights', 'senate', 'voter', 'voting'
        ]
        
        score = 0

        def adding_count_to_score(self,c):
            self.score += c

    class economy:
        words = [
            'agent', 'analysis', 'austerity', 'balance', 'bank', 'banking', 'base', 'bond', 'boom', 'budget', 'bubble', 'business', 'capital',
            'capitalism', 'chain', 'competition', 'consumer', 'cost', 'credit', 'crisis', 'currency', 'cycle', 'debt', 'deficit', 'deflation',
            'demand', 'demand-side', 'development', 'downturn', 'economic', 'economics', 'economist', 'efficiency', 'employment', 'entrepreneur',
            'entrepreneurship', 'equilibrium', 'equity', 'exchange', 'expenditure', 'export', 'fiscal', 'forecast', 'forecasting', 'free',
            'global', 'globalization', 'government', 'growth', 'gross', 'import', 'income', 'indicator', 'inequality', 'industry', 'inflation',
            'inflationary', 'interest', 'investment', 'labor', 'law', 'liquidity', 'loss', 'macroeconomics', 'manipulation', 'market', 'microeconomics',
            'monetary', 'monopoly', 'national', 'opportunity', 'output', 'policy', 'portfolio', 'power', 'price', 'private', 'product', 'profit',
            'protectionism', 'public', 'rate', 'recession', 'reform', 'regulation', 'research', 'revenue', 'sector', 'socialism', 'spending',
            'stimulus', 'stock', 'structure', 'subsidy', 'supply', 'supply-side', 'surplus', 'sustainability', 'system', 'tariff', 'tax', 'taxation',
            'trade', 'unemployment', 'wages', 'well-being'
        ]
        score = 0

        def adding_count_to_score(self,c):
            self.score += c








