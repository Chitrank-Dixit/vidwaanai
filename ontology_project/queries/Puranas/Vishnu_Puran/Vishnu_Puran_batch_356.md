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

### Verse 1 (Vishnu Puran 0.7101)
- **Original**: कमल- योनि भगवान्‌ ब्रक्माजीने उन्हें सम्पूर्ण ओषधि, द्विजजन और नक्षत्रगणके आधिपत्थपर अभिषिक्त कर दिया था
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.7102)
- **Original**: चद्धमाने राजसूय-यज्ञका अनुष्ठान किया
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.7103)
- **Original**: अपने प्रभाव और अति उत्कृष्ट आधिपल्यके अधिकारी होनेसे चद्रमापर राजमद सवार हुआ
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.7104)
- **Original**: तब मदोन्मत्त हो जानेके कारण उसने समस्त देवताओंके गुरु भगवान्‌ बृहस्पतिजीकी भार्या ताराकों हरण कर लिया
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.7105)
- **Original**: तथा बृहस्पतिजीकी प्रेरणासे भगवान्‌ ब्रह्माजीके बहुत कुछ कहने-सुनने और देवर्षियोंके माँगनेपर भी उसे न छोड़ा
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.7106)
- **Original**: बूहस्पतिजीसे द्वेष करनेके कारण शुक्रजी भी चन्द्रमाके सहायक हो गये और अंगिय्से विद्या-ल्त्रभ करनेके कारण अगकान्‌ रुद्रने बृहस्पतिकी सहायता की [क्योंकि बृहस्पतिजी अंगिराके पुष्र हैं]
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.7107)
- **Original**: जिस पक्षमें शुक्रली थे उस ओरसे जम्भ और कुम्प आदि समस्त दैत्य-दानवादिने भी [ सहायता
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.7108)
- **Original**: 5भवत्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.7109)
- **Original**: एवं च तयोरतीवोअसंग्राम- स्तारानिमित्तस्तारकामयो. नामाभूत्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.7110)
- **Original**: ततश्न सप्रस्तशख्नाण्यसुरेषु रुद्रपुरोगमा देवा देवेषु चाशेषदानवा मुप्तुचु:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.7111)
- **Original**: एवं देवासुराहव- जगद्वदह्मांणं॑ झरणं जगाम
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.7112)
- **Original**: ततश्ल॒ भगवानब्जयोनि- रप्युशनस हाद्भरमसुरान्देबांश् निवार्य बृहस्पतये तारामदापयत्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.7113)
- **Original**: ता चान्त:प्रसवा- धार्ष्ट्येनेति
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.7114)
- **Original**: सा च तेनैवमुक्तातिपतिब्रता भर्तृबचनानन्तरं तम्िषीकास्तम्बे. गर्भमुत्ससर्ज
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.7115)
- **Original**: _ स चोत्सृष्टमात्र एवातितेजसा देवानां तेजांस्या- चिक्षेप
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.7116)
- **Original**: बृहस्पतिमिन्दुं च तस्प कुमार- स्थातिचारुतया साभिलाथो दृद्दा देवास्समुत्पन्न- सन्‍्देहास्तारां पप्रच्छु:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.7117)
- **Original**: सत्य कथया- स्माकमिति सुभगे सोमस्याथ वा बृहस्पतेरय॑ पुत्र इति
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.7118)
- **Original**: एवं तैरुक्ता सा तारा हिया किद्निन्नोवाच
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.7119)
- **Original**: । बहुशो5प्यभिहिता यदासौ देवेध्यो नाचच्क्षे ततस्स कुमारस्तां झप्तुमुद्यतः प्राह
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.7120)
- **Original**: दुष्टेउम्ब कस्मान्मम तात॑ नाख्यासि
- **Translation**: 

---

