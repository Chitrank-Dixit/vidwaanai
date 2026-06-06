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

### Verse 1 (Shiv Puran 0.2941)
- **Original**: शिवयो: पूजने सक्ता सा में दिदशत्‌ काद्वितम
- **Translation**: 

---

### Verse 2 (Shiv Puran 0.2942)
- **Original**: महेश्वरके मुखकमलसे प्रकट हुई तथा शिव-पार्वतीके पूजनमें आसक्त रहनेवाली से सरस्वत्तीदेवी मुझे मनोवाओ्छित वस्तु प्रदान करें
- **Translation**: 

---

### Verse 3 (Shiv Puran 0.2943)
- **Original**: विष्णोर्चक्ष:स्थिता लक्ष्मी: ज्िवयो: पूजने रता। जशिलयो। शासनादेव सा में दिशतु काद्ितम्‌
- **Translation**: 

---

### Verse 4 (Shiv Puran 0.2944)
- **Original**: 8जा भगवान्‌ किण्णुके. वक्षःस्थलमें विराजमान रूक्ष्मी देवी, जो सदा जिव और जियाके पूजनमें लगी रहती हैं, उन झिवदप्पतीके आदेशसे ही मेरी अभिल्काषा पूर्ण करें
- **Translation**: 

---

### Verse 5 (Shiv Puran 0.2945)
- **Original**: महागोरी. मह्ादेव्या:.. पादपूजापरायणा । सत्या एस नियोगेंग स्रा मे दिशातु काक्षितम
- **Translation**: 

---

### Verse 6 (Shiv Puran 0.2946)
- **Original**: महादेखी पार्वतीके पादपद्यॉकी पूजापें परायण भहामोटी उन्हींकी आज्ञासे पेरी प्रनचाही वस्तु मुझे दें
- **Translation**: 

---

### Verse 7 (Shiv Puran 0.2947)
- **Original**: ऋषधिकी सिंहमारूठा पार्तत्या: परमा सुता। क्िश्शोर्निदा. महामाया. महामहिषमर्दिनी
- **Translation**: 

---

### Verse 8 (Shiv Puran 0.2948)
- **Original**: निशुप्भश्ुत्भसैहजी मधुपांसासबपिया । सत्कृत्व शासन मातुः सर में दिशत्‌ काब्लितप्‌
- **Translation**: 

---

### Verse 9 (Shiv Puran 0.2949)
- **Original**: क्र जायवीपसंडिता 3530%7##44*5404/ 74 # 74447 +3+0*++%0#44#*%%$2##*4//### 231 कै 3 3$8
- **Translation**: 

---

### Verse 10 (Shiv Puran 0.2950)
- **Original**: 44744$7#आं+++क+ 070 पार्वतीकी सबसे श्रेष्ठ पुत्री सिंहजाहिनी कौहिकी, भगवान्‌ किष्णुकी योगनिद्रा सहापमाया, पहामहिषमर्दिनी, महाल्क्मी तथा भधु और फरलोंके गृदे तथा रसको ग्रेमपूर्वक भोग लूगानेबाली निशुष्प-शुम्पसंहारिणी महासरस्वती माता पार्यतीकी आज़ासे मुझे मनोवान्छित वस्तु प्रदान करें
- **Translation**: 

---

### Verse 11 (Shiv Puran 0.2951)
- **Original**: सुद्रा रुद्रसमप्रज्या: असथाः अधितौजस:
- **Translation**: 

---

### Verse 12 (Shiv Puran 0.2952)
- **Original**: भूतास्याक्ष गठावीर्वा महादेखसमप्रभा:
- **Translation**: 

---

### Verse 13 (Shiv Puran 0.2953)
- **Original**: नित्यगुख्तत गिरुषभा र7र्दन्द्रा निरुषन्नवा:
- **Translation**: 

---

### Verse 14 (Shiv Puran 0.2954)
- **Original**: सौम्या पोरास्तथा मिश्चाक्षात्तरालद्रयात्मिफा: । बिकगाक्ष॒ सुरूपाशध नाजकूपपरास्तथा
- **Translation**: 

---

### Verse 15 (Shiv Puran 0.2955)
- **Original**: सत्कृत्य फिवयोगज् ते मे काथे दिशन्तु सै। रस्त्रदेवके समान तेजस्वी स्खूगणा, कर 789 देव्या: प्रियसश्लीलगों देखीलक्षणल्म्रितः
- **Translation**: 

---

### Verse 16 (Shiv Puran 0.2956)
- **Original**: सहितो रुद्रकल्यामि: दाक्तिमिश्वाप्योकदा:
- **Translation**: 

---

### Verse 17 (Shiv Puran 0.2957)
- **Original**: तृजीयाजरणे झष्मोर्थकत्या निल्ये समार्चित:
- **Translation**: 

---

### Verse 18 (Shiv Puran 0.2958)
- **Original**: वह शिव-पार्यतीकी आज्ञाका सत्कार करके मुझे मड्डरक प्रदान करे
- **Translation**: 

---

### Verse 19 (Shiv Puran 0.2959)
- **Original**: 96-97 ;
- **Translation**: 

---

### Verse 20 (Shiv Puran 0.2960)
- **Original**: दिलाकरों मह्ेशस्थ॒ यूर्शिदीमिसुमण्डलू:
- **Translation**: 

---

