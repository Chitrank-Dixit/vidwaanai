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

### Verse 1 (Vishnu Puran 0.12501)
- **Original**: 70 अज्नन्दगोचरस्थापि तस्य वै ब्रह्मणो ट्विज । पूजायां भगवच्छब्द: क्रियते ह्युपचारतः
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.12502)
- **Original**: 71 जुद्धे महाविभूत्याख्ये परे त्रह्मणि शब्छते ।
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.12503)
- **Original**: 72 सम्भतेति तथा भर्ता भकारो3र्थद्वयान्वित: । नेता गमप्िता स्रष्टा गकारार्थस्तथा मुने
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.12504)
- **Original**: 73 ऐश्वर्यस्थ समग्रस्य धर्पस्य यशसश्श्रिय: । ज्ञानवैराग्ययोझव षण्णां भग इतीरणा
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.12505)
- **Original**: 74 वसन्ति तत्र भूतानि भूतात्मन्यखिलात्मनि । सच भूतेप्रशेषेषु वकारार्थस्ततो5व्यय:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.12506)
- **Original**: 75 ज्ञान दो प्रकास्का है--ज्ञाख्रजन्य तथा बिवेकज
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.12507)
- **Original**: झब्दब्रह्मका ज्ञान शास्मजन्य है और परबह्मका बोध विवेकज
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.12508)
- **Original**: हे विप्रषें! अज्ञान घोर अन्धक्म्स्के समान है। उसको नष्ट करनेके लिये शास्त्रजन्य* ज्ञान दीपकवत्‌ और विवेकज ज्ञान सूर्यके समान है
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.12509)
- **Original**: है मुनिश्रेष्ठ ! इस विषयमें केदार्थका स्गरणकर मनुजीने जो कुछ कहा है वह बतत्खता हूँ, श्रवण करो
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.12510)
- **Original**: ब्रह्म दो प्रकरका है--शब्दबहा और परवहम
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.12511)
- **Original**: झब्दबह्म (शास्त्रजन्य ज्ञान) में निपुण हो जानेपर जिज्ञासु [ विवेकज ज्ञानके द्वारा] परब्रह्मको प्राप्त कर केता है
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.12512)
- **Original**: अथर्ववेदकी श्रुति है कि विद्या दो प्रकारकी है--परा और अपरा। परासे अक्षर ब्रह्मकी प्राप्ति होतों है और अपरा ऋगादि वेदत्रयीरूपा है
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.12513)
- **Original**: जो अच्यक्त, अजर, अचिन्य, अज, अव्यय, अनिर्देशय, अरूप, पाणि-पादादिशून्य, व्यापक, सर्वगत, तित्य, भूतोंका आदिकारण, स्वयं कारणहीन तथा जिससे सम्पूर्ण व्याप्य और व्यापक प्रकट हुआ है और जिसे पण्डितजन [ जाननेत्रोंसे ] देखते हैं वह परमधाम हो बह्य है मुप्तक्ष्ओंकोी उसीका ध्यान करना चाहिये और वही भगवान्‌ विष्णुका वेदबचनोंसे प्रतिपादित अति सूक्ष्म परमपद है
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.12514)
- **Original**: 66--68
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.12515)
- **Original**: परमात्माका बह स्वरूप ही 'भगवत' शब्दका वाच्य है और भगवत्‌ शब्द ही उस आद्य एवं अक्षय स्वरूपका बाचक है
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.12516)
- **Original**: जिसका ऐसा स्वरूप बतलाया गया है उस परमात्पाके तत्त्वका जिसके द्वारा बरास्तविक ज्ञान होता है वही परमज्ञान (पर विद्या) है । त्रयीमय ज्ञान (कर्मकाण्ड) इससे पृथक्‌ (अपरा विद्या) है
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.12517)
- **Original**: हे द्विज ! यह ऋह्म यद्यपि शब्दका विषय नहीं है तंथापि आदरप्रदर्षनके लिये उसका *भगवत' झब्दसे उपचारत: कथन किया जाता है
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.12518)
- **Original**: है मैत्रेय ! समस्त कारणोंके कारण, महाविभूतिसंज्ञक परतह्मके लिये ही “भगबत्‌' शब्दका प्रयोग हुआ है
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.12519)
- **Original**: इस ('भगवत्‌' झब्द) में भकारके दो अर्थ हैं---पोषण करनेवाल्त और सनका आधार तथा गकारके अर्थ कर्म-फल प्राप्त करनेवाल्त्र, लय करनेबाला और रचयिता हैं
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.12520)
- **Original**: सम्पूर्ण ऐश्वर्य, धर्म, यञ्ञ, श्री, ज्ञान और लैग़ग्य--इन छःका नाम 'भग' है।
- **Translation**: 

---

