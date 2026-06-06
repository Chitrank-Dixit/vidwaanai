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

### Verse 1 (Vishnu Puran 0.11281)
- **Original**: तुम सात या आठ दिनतक मेरी प्रतीक्षा करना--ऐसा कहकर वह अपने घस्के भीतर गयी और उस पुरुषको दुँढनेका उपाय करने छगी
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.11282)
- **Original**: श्रीपराशरजी बोले--तदनन्तर [आठ-सात दिन पश्चात्‌ लौटकर] चित्रलेखाने चित्रपटपर मुख्य-मुख्य देवता, दैत्य, गर्धर्व और मनुष्योंके चित्र लिख़कर उषाको दिखलाये
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.11283)
- **Original**: तब उपाने गन्धर्ब, नाग, देवता और दैत्य आदिको छोड़कर केवल मनुष्योपर और उनमें भी विशेषतः अन्धक ओर वृष्णिवंज्ञी यादकोपर ही दृष्टि दी
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.11284)
- **Original**: हे द्विजअ! राम और कृष्णके चित्र देखकर बह सुन्दर भूकुटिवाली छज्जासे जडवत्‌ हो गयो तथा प्रधुन्नक्त्रे देखकर उसने लज्जाबश अपनी दुष्टि हटा ली
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.11285)
- **Original**: तत्पश्चात्‌ प्रदु्नगननय प्रियतम अनिरुद्धजीको देखते ही उस अत्यत्त विलासिनीकी लज्जा मानो कहीं चली गयी
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.11286)
- **Original**: [वह बोल उठी] --'बह यही है, बह यही है ।' उसके इस प्रकार कहनेपर योगगामिनी चित्रलेखाने उस बाणासुरकी कन्यासे कहा---
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.11287)
- **Original**: चित्रलेखा बोली--देवीने प्रसन्न लेकर यह कृष्णका पौत्र ही तेरा पति निश्चित किया है; इसका नाम अनिरुद्ध है और यह अपनी सुन्दरताके लिये प्रसिद्ध है
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.11288)
- **Original**: यदि तुझको यह पति मिल गया तब तो तूने मानो सभी कुछ पा लिया; किन्तु कृष्णकच्रद्ारा सुरक्षित द्वारकापुरीमें पहले अखवेश ही करना कठिन है
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.11289)
- **Original**: तथापि हे सरिति ! किसी उपायसे मैं तेरे पतिको त्थऊँगी ही, तू इस गुप्त रहस्वक्ते किसीसे भी न कहना
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.11290)
- **Original**: मैं ज्ञीघ्र ही आऊँगो, इतनी देर तू मेरे वियोगक्ररे सहन कर । अपनी सस्त्री उषाकों इस प्रकार ययौ द्वारवती चोषां समाश्चास्य तत: सरवीम्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.11291)
- **Original**: ढाढस बैंधाकर चित्रलेखा द्वास्कापुरीक्ों गयी
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.11292)
- **Original**: न इति श्रीविष्णुपुराणे पञ्रमेंऊशे द्वात्रिशो5घ्यायः
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.11293)
- **Original**: च्च्च्त्त्ष् तततता
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.11294)
- **Original**: श्रीविष्णुपुराण [ आ« 33 तैंतीसवाँ अध्याय श्रीकृष्ण और बाणासुरका युद्ध औपराशर उवाच बाणो<पि प्रणिपत्याप्रे मैत्रेयाह त्रलोचनम्‌ । देव बाहुसहल्नेण निर्विण्णोउस्म्याहब॑ बिना
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.11295)
- **Original**: 1 कश्चिन्ममैषां बाहूनां साफल्यजनको रण: । भविष्यति विना युद्ध भाराय मम कि भुजै:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.11296)
- **Original**: 2 श्रीश्फूर उवाच मयूरध्वजभड्टस्ते यदा बाण भविष्यति। पिशिताशिजनानन्दं प्राप्स्यसे त्व॑ तदा रणम्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.11297)
- **Original**: 3 औपराशर उबाच तत: प्रणम्य वरदं शम्भुमभ्यागतो गृहम्‌। सभरम ध्वजमालोक्य हष्टो हर्ष पुनर्ययो
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.11298)
- **Original**: 4 एतस्मिन्नेब काले तु योगविद्याबलेन तम्‌। अनिरुद्धमधथानिन्ये चित्रेखा वराप्सरा:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.11299)
- **Original**: 5 कन्यान्तः:पुरमभ्येत्य रममा्णं सहोषया । विज्ञाय रक्षिणो गत्वा झझंसुर्दैत्यभूपतेः
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.11300)
- **Original**: 6 व्यादिष्ट किद्जराणां तु सैन्य तेन महात्मना । जघान परिघ॑ घोरमादाय परवीरहा
- **Translation**: 

---

