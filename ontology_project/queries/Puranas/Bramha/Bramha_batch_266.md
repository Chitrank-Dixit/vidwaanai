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

### Verse 1 (Bramha 0.5301)
- **Original**: पतियोंसहित ले आओ; तब मैं छोटे रूपमें हो वन्दनीया और सबकी ईश्वरी हैं, जिन्हें ब्रह्मा तथा
- **Translation**: 

---

### Verse 2 (Bramha 0.5302)
- **Original**: जाऊँगी।' “बहुत अच्छा' कहकर समुद्र सप्तर्षियों शिव आदि देवता भी मस्तक झुकाते हैं, उनके
- **Translation**: 

---

### Verse 3 (Bramha 0.5303)
- **Original**: 7 - ; स्वागतमें मुझे कुछ दूर आगेतक जाना चाहिये। नहीं तो मेरे धर्ममें दोष आयेगा। जो अपने घर
- **Translation**: 

---

### Verse 4 (Bramha 0.5304)
- **Original**: आते हुए महाप्ुरुषको लेनेके लिये मोहवश स्वयं
- **Translation**: 

---

### Verse 5 (Bramha 0.5305)
- **Original**: उपस्थित नहीं होता, उस पापीकी रक्षा करनेवाला दोनों लोकोंमें कोई नहीं है।' यों विचारकर समुद्र
- **Translation**: 

---

### Verse 6 (Bramha 0.5306)
- **Original**: .) मूर्तिमान्‌ हो हाथ जोड़े विनीत भावसे गड्जाजीके
- **Translation**: 

---

### Verse 7 (Bramha 0.5307)
- **Original**: 4 तुम्हाशा यह जल, जो आकाश, पाताल और 57 25 203)... इ मर्त्यलोकमें फैला हुआ है, मुझमें आकर मिले--इसके का #
- **Translation**: 

---

### Verse 8 (Bramha 0.5308)
- **Original**: ः लिये मैं कुछ नहीं कहूँगा। मेरे भीतर रत्र, अमृत, हु पर्वत, राक्षम और असुर रहते हैं। इनको तथा हि अन्यान्य भयंकर जलजन्तुओंकों भी मैं धारण #9<8 करता हूँ। मेरे जलमें लक्ष्मोसहित भगवान्‌ विष्णु * महत्वध्यागते कुर्यास्प्रत्युत्थानं न यो मदातू।स धर्मादिपरिभ्रष्टों निस्प॑ तु समाणुयात्‌। (172। 11)
- **Translation**: 

---

### Verse 9 (Bramha 0.5309)
- **Original**: * सामुद्र, ऋषिसत्र आदि तीथोंकी महिमा तथा गौतमी-माहात्यका उपसंहार « 257 और उनकी पत्नियोंकों ले आया। तब गोदावरी
- **Translation**: 

---

### Verse 10 (Bramha 0.5310)
- **Original**: कारण सिद्ध होता है। क्योंकि कर्म करनेसे देवी सात धाराओंमें विभक्त हो गयोँ और उसी
- **Translation**: 

---

### Verse 11 (Bramha 0.5311)
- **Original**: फलकी सिद्धि देखी जाती है और-न करनेसे रूपमें उनका समुद्रसे संगम हुआ। सस्तर्षियोंक
- **Translation**: 

---

### Verse 12 (Bramha 0.5312)
- **Original**: नहीं। अत: फलकी सिद्धि कर्मके ही अधीन है। नामपर वे सप्तगज्ञाके नामसे विख्यात हुईं। वहाँ
- **Translation**: 

---

### Verse 13 (Bramha 0.5313)
- **Original**: कर्म भी दो प्रकारके जानने चाहिये-क्रियमाण भक्तिपूर्वक जो स्रान, दान, श्रवण, पाठ और
- **Translation**: 

---

### Verse 14 (Bramha 0.5314)
- **Original**: और कृत। क्रियमाण कर्मका जो-जो साधन है, स्मरण आदि शुभ कर्म किया जाता है, वह समस्त
- **Translation**: 

---

### Verse 15 (Bramha 0.5315)
- **Original**: बह कर्तव्य बताया गया है। विद्वानू पुरुष कर्म अभीष्ट वस्तुओंको देनेवाला होता है। पापकी
- **Translation**: 

---

### Verse 16 (Bramha 0.5316)
- **Original**: करते हुए जो-जों भावना करता है, उसके हानि, भोग और मोक्षकी प्राप्ति तथा मनकी
- **Translation**: 

---

### Verse 17 (Bramha 0.5317)
- **Original**: अनुरूप ही फलकी सिद्धि होतों है। यदि बिना प्रसन्नताके लिये तीनों लोकोंमें सामुद्रतीर्थसे बढ़कर , भावनाके विधिपूर्वक कर्मका अनुष्ठान करता है तो दूसरा कोई तीर्थ नहीं है। उसे अन्य प्रकारका फल मिलता है। किंतु भावना सामुद्रतीर्थक अतिरिक्त वहाँ ऋषिसत्रतीर्थ भी
- **Translation**: 

---

### Verse 18 (Bramha 0.5318)
- **Original**: करनेपर सम्पूर्ण फल उस भावनाके अनुरूप ही है, जहाँ सातों ऋषि तपस्याके लिये बैठे थे और
- **Translation**: 

---

### Verse 19 (Bramha 0.5319)
- **Original**: होता है; अत: तप, ब्रत, दान, जप और यज्ञ आदि जहाँ भीमेश्वर शिव विराजमान हैं। वहाँका वृत्तान्त
- **Translation**: 

---

### Verse 20 (Bramha 0.5320)
- **Original**: क्रियाएँ कर्मके अनुरूप भाव होनेसे हो अभीष्ट इस प्रकार है। सात ऋषियोंने गढ़्ाकों सात
- **Translation**: 

---

