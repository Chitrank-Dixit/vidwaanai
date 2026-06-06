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

### Verse 1 (Vishnu Puran 0.5301)
- **Original**: 25 सथर्मचारिणोीं प्राष्य गारईस्थ्यं सहितस्तया । समुबलेद्ददात्येतत्सम्यगू् महाफलम्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.5302)
- **Original**: 26 अति मन्द या कौएके समान (कर्णकटु) स्वस्वाली हो तथा पक्ष्मशून्या या गोल नेत्रॉवाली हो उस स्लीसे विवाह न करें
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.5303)
- **Original**: जिसकी जंघाओंपर रोम हों, जिसके गुल्फ (टखने) ऊँचे हों तथा हँसते समय जिसके कपोल्लोमें गड्ढे पड़ते हों उस कन्यासे विवाह न करें
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.5304)
- **Original**: जिसकी कान्ति अत्यन्त उदासीन न हो, नख पाण्डुवर्ण हें, नेत्र त्लछ हो तथा हाथ-पैर कुछ भारी हों, बुद्धिमान्‌ पुछष उस कन्यासे सम्बन्ध न करे
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.5305)
- **Original**: जो अति वामन (नाटी) अथवा अति दीर्घ (लम्बी) हो, जिसकी भूकुटियाँ जुड़ी हुई हो, जिसके दौतोमें अधिक अन्तर हो तथा जो दन्तुर (आगेको दाँत निकले हुए) मुखबाली हो उस खत्रीसे कभी व्रिवाह न करे
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.5306)
- **Original**: हे राजन्‌ ! मातृपक्षसे पाँचवीं पीढीतक और पितृपक्षसे सातवों पीढ़ीतक जिस कन्वाका सम्बन्ध न हो, गृहस्थ पुरुषकों नियमानुसार उसीसे विवाह करना चाहिये
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.5307)
- **Original**: श्राह्म, देव प्राजापत्प, आसुर, गार्र्ष, गक्षस और पैज्ञाच--से आठ प्रकास्के विवाह हैं
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.5308)
- **Original**: इनमेंसे जिस विवांहकों जिस वर्णके लिये महर्षियोंने धर्मानुकूल कहा है उसरीके द्वार दार-परिग्रह करे, अन्य विधियोंकों छोड़ दे
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.5309)
- **Original**: इस प्रकार सहधर्मिणीको प्रा/कर उसके साथ गार्हस्थ्यधर्मका पालन करे, क्योंकि उसका पालन करनेपर बह महान्‌ फल देनेवाल्ा होता है।। 26
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.5310)
- **Original**: इति श्रीविष्णुपुराणे तृतीयेंडशे दशमो5ध्याय:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.5311)
- **Original**: -+-++++- औः च्ज््च््् ग्यारहबाँ अध्याय गृहस्थसम्बन्धी सदाचारका वर्णन सगर उवाच गृहस्थस्य सदाचारं ओतुमिच्छाम्यहं मुने
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.5312)
- **Original**: ल्तेकादस्मात्परस्माध् यमातिप्ठन्न हीयते
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.5313)
- **Original**: 9 ऑर्व उवाच श्रूयतां पृथिवीपाल सदाचारस्य लक्षणम्‌। सदाचारवता पुंसा जितो स्थ्रेकावुभावषि
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.5314)
- **Original**: 2 साथव: क्षीणदोषास्तु सच्छब्दः साधुवाचक: । तेषामाचरणं यत्तु सदाचारस्स उच्चते
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.5315)
- **Original**: 3 सप्तर्षघो5थ मनव:ः प्रजानां पतयस्तथा
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.5316)
- **Original**: सगर बोले--हे म॒ने ! मैं गृहस्थके सदाचारोंका सुनना चाहता हूँ, जिनका आचरण करनेसे यह इहलोक और परल्ओेक दोनों जगह पतित नहीं होता
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.5317)
- **Original**: ओऔर्ब बोले--हे पृथिवीपाल ! तुम सदाचारके लक्षण सुनो। सदाचारी पुरुष इहत्म्रेक और परलोक दोनोहीकोे जीत छेता है
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.5318)
- **Original**: 'सत्‌' शाब्दका अर्थ साधु है और साधु वही है जे। दोषरहित हो । उस साधु पुरुषका जो आचरण होता है उस्तीको सदाचार कहते हैं। 3
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.5319)
- **Original**: है राजन्‌ ! इस सटाचारके वक्तत्र और कर्ता सप्तपिंगण, मनु सदाचारस्प वक्तारः कर्तारश् महीपते
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.5320)
- **Original**: एवं प्रजापति हैं
- **Translation**: 

---

