# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Vishnu Puran 0.10441)
- **Original**: 74 भ्रामयित्वा शतगुणं दैत्यमल्छममित्रजित्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.10442)
- **Original**: भूमावास्फोटयामास गगने गजजीवितम्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.10443)
- **Original**: 75 भूमावास्फोटितस्तेन चाणूर: शतधाभवत्‌ । रक्तस्नावमहापड्रों चकार च्र तदा भुवम्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.10444)
- **Original**: 76 युयुधे दैत्यमललेन चाणूरेण यथा हरि:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.10445)
- **Original**: 77 सो5प्येन॑ मुष्टिना मूर्ति वक्षस्पाहत्य जानुना । पातयित्वा धरापृष्टे निष्पिषिष गतायुषप्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.10446)
- **Original**: 78 कृष्णास्तोशलक॑ भूयो मल्लराज महाबलम्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.10447)
- **Original**: खापपुष्टिपरहरेण परातवामास॒ भूतले
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.10448)
- **Original**: 79 चाणूरे निहते मल्ले मुप्टिके विनिषातिते। नीते क्षय तोशलके सर्वे मल्‍ला: प्रदुद्दुचु:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.10449)
- **Original**: 80 वबल्गतुस्ततो रख्ढे कृष्णसड्डर्थणावुभौ । समानवयसो गोपान्बलादाकृष्य हर्षितों
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.10450)
- **Original**: 89 पतश्चम अंध् 367 नीचे गिराकर, उहझललकर, घूँसे और वज़के समान कोहनी मारकर, पैरोंसे ठोकर मारकर तथा एक-दूसरेके अंगॉकों रगड़कर लड़ते छगे। उस समय उनमें महान्‌ युद्ध होने लगा
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.10451)
- **Original**: इस प्रकार उस समाजोत्सवके समीप केवछ बल और प्राणशक्तिसे ही सम्पन्न होनेवाला उनका अति भयंकर और दारुण झास्रहीन युद्ध हुआ
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.10452)
- **Original**: चाणूर जैसे-जैसे अगवान्से भिड़ता गया बैसे-ही-वैसे उसकी प्राणदाक्ति थोड़ो-थोड़ी करके अत्यन्त क्लीण होती गयी।
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.10453)
- **Original**: जगन्मय भगवान्‌ कृष्ण भी, भ्रम और कोपके कारण अपने पृष्पमय दिरोभूषणोंमें लगे हुए केशरकों हिल्ानेवाले उस चाणूरसे लीत्प्रपूर्वक लड़ने लगी
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.10454)
- **Original**: उस समय चाणूरके बलक्य क्षय और कृष्णचन्द्रके बल्का ठदय देख कंसने खीझकर तूर्य आदि बाजे बन्द करा दिये
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.10455)
- **Original**: रैगभूमिमें मृदंग और तूर्य आदिके अन्द हो जानेपर आकाझशमें अनेक दिव्य तूर्य एक साथ यजने लगें
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.10456)
- **Original**: और देवगण अत्यन्त हर्षित होकर अल्क्षित- भावसे कहने लगे--''हे गोविन्द ! आपकी जय हो। हे केशव ! आप ज्ञीभ्र ही इस चाणूर दानवकों मार डाल्ड्ये ।'
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.10457)
- **Original**: भगवान्‌ मधुसूदन बहुत देरतक चाणुस्के साथ खेल करते रहे, फिर उसका बध करनेके लिये उच्यत होकर उसे उठाकर घुमाया
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.10458)
- **Original**: झत्रुविजयी श्रीकृष्णच-ड्रने उस दैत्य मल्‍्लको सैकड़ों बार घुमाकर आकाशमें हो निर्जीच हो जानेपर पृथिवीपर पटक दिया
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.10459)
- **Original**: भगवान्‌के द्वार पूथिवीपर गिराये जाते हो चाणूरके दारीस्के सैकड़ों टुकड़े हो गये और उस समय उसने रक्तस्नावसे पृथिवीक्रे अत्यन्त कीचड़मय कर दिया
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.10460)
- **Original**: इधर, जिस प्रकार भगवान्‌ कृष्ण चाणूरसे लछड़ रहे थे उसी प्रकार महाबल्ली बलभद्रजी भी उस समय दैत्य मल्ल मुष्टिकसे भिड़े हुए थे
- **Translation**: 

---

