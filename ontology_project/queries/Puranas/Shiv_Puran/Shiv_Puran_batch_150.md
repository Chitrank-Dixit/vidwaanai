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

### Verse 1 (Shiv Puran 0.2981)
- **Original**: ###### ###ऊ#%ऊ#%# # # # हम! 'ऋ। 4207 70+ 034 न 7 + + 0 7 #॑. ##777477 70/47/4077 # 4 '###& छिवकी आज्ञाके अधीन हो मुझे मक़ल ज्रदान करें
- **Translation**: 

---

### Verse 2 (Shiv Puran 0.2982)
- **Original**: 113--117 5
- **Translation**: 

---

### Verse 3 (Shiv Puran 0.2983)
- **Original**: चत्वास्थ तथा वेदा: सरेतिदासपुरणका:
- **Translation**: 

---

### Verse 4 (Shiv Puran 0.2984)
- **Original**: धर्मझास्णणि जिल्लाभिवैंदिकोधि: समन्विता:
- **Translation**: 

---

### Verse 5 (Shiv Puran 0.2985)
- **Original**: झिजप्रकृतिपादकाः
- **Translation**: 

---

### Verse 6 (Shiv Puran 0.2986)
- **Original**: , । ही
- **Translation**: 

---

### Verse 7 (Shiv Puran 0.2987)
- **Original**: ह। ः 4
- **Translation**: 

---

### Verse 8 (Shiv Puran 0.2988)
- **Original**: अहाणो5पि विरश्छेता जनक्रस्तस्थ तत्सुतः
- **Translation**: 

---

### Verse 9 (Shiv Puran 0.2989)
- **Original**: / 'जनकस्ततयक्रापि. विश्णोरषि_ नियासक्र: । खोघकश तथोर्नितापनुफकरः: प्रफुतरररा। अप्खस्पान्तीहिर्च्त'॑ रद्रो. सोकदय्याग्िप: । शिवप्रियः दिप्वासक्त: शिवपादार्थने रतः
- **Translation**: 

---

### Verse 10 (Shiv Puran 0.2990)
- **Original**: सृष्टि है। सृष्टि, पालन और संहार करनेके कारण इनका कर्म असाधारण माना जाता है । ये ब्रह्माजीके भी मस्तकका छेदन करनेबाले हैं। ब्रह्माजीके पिता और पुत्र भी हैं । इसी तरह किष्णुके भी जनक और पुत्र हैं तथा उन्हें नियन्तणपें रखनेवाले हैं। ये उन दोनों -- ्रह्म और किष्णुको ज्ञान देनेवाले तथा नित्य उनपर अतुग्रह रखनेवाले हैं। थे अभु अद्याण्डके भीतर और बाहर भी व्याप्त हैं तथा इहस्करक और परत्ठोक--दोनों स्लेकोंके अधिपति रूद्ध हैं। थे विधके प्रिय, शिवमें ही आसक्त तथा झिवके ही बरणारक्न्दोंकी अर्चनामें तत्पर हैं, अत: शिवकी आज्ञाकों सामने रखते हुए मेरा मजल करें
- **Translation**: 

---

### Verse 11 (Shiv Puran 0.2991)
- **Original**: 118--123 5
- **Translation**: 

---

### Verse 12 (Shiv Puran 0.2992)
- **Original**: तस्प खद्मय पड़ड्ानि तिद्रेश्रानी तथाएकम्‌
- **Translation**: 

---

### Verse 13 (Shiv Puran 0.2993)
- **Original**: च्त्वारो मुर्तिभिदाल द्िसपूर्या: शियार्थफा: । शिवस्थाज्ों पुरस्कृल्य मज़ाक प्रदिशन्तु में
- **Translation**: 

---

### Verse 14 (Shiv Puran 0.2994)
- **Original**: 1₹प्ता भगवान्‌ झंकरके स्वरूप भूत ईंशानादि ब्रह्म, हृदयादि छ: अज्भ, आठ विशेश्वर, दिव आदि चार मूर्तिभेद--शिव, भव, हर और मृड--थे सब-के-सब दिवके पूजक हैं। ये स्तेग जशिवकी आज्ञाकों झिरोधार्य करके मुझे मदर प्रदान करें
- **Translation**: 

---

### Verse 15 (Shiv Puran 0.2995)
- **Original**: 124-12575
- **Translation**: 

---

### Verse 16 (Shiv Puran 0.2996)
- **Original**: अथ चिष्णुमहिद्वास्य शिवस्पैज परा तनु:
- **Translation**: 

---

### Verse 17 (Shiv Puran 0.2997)
- **Original**: देक्षिणाज्ञभतेगापि स्पर्धमानः स्ववस्धुवा
- **Translation**: 

---

### Verse 18 (Shiv Puran 0.2998)
- **Original**: आद्येन अह्यणा साक्षात्सृष्ट: सख्रज्ा च तस्प तु। अच्छस्वासग्रीटिर्वती. विष्णुस्केक्ड्रयाधिप: #129
- **Translation**: 

---

### Verse 19 (Shiv Puran 0.2999)
- **Original**: 4 असुरान्तकरक्षत्री इक्रस्यापि तथानुजः । प्रादुर्भूतेक्ष दशा. भृगुशापच्कत्सदिह
- **Translation**: 

---

### Verse 20 (Shiv Puran 0.3000)
- **Original**: भूभारनिप्रहार्धथीय. स्वेल्टयालातरत्‌. क्षितौ
- **Translation**: 

---

