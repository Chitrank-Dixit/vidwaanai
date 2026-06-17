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

### Verse 1 (Bramha 0.7101)
- **Original**: मड्रल-गान तथा ऋग्वेद आदिके सुमधुर शब्द उन्हें पीटते हैं और वे चिल्लाते हुए यमलोकके
- **Translation**: 

---

### Verse 2 (Bramha 0.7102)
- **Original**: होते रहते हैं। वहाँ महर्षियोंका समुदाय शोभा पथपर अग्रसर होते हैं। पाता है। उस द्वारसे उन्हीं पुण्यात्माओंका प्रवेश इस प्रकार वह मार्ग बड़ा ही दुर्गग और
- **Translation**: 

---

### Verse 3 (Bramha 0.7103)
- **Original**: होता है, जो धर्मज्ञ और सत्यवादी हैं। जिन्होंने अग्निके समान प्रज्वलित है। उसे रौरब (जीवोंको
- **Translation**: 

---

### Verse 4 (Bramha 0.7104)
- **Original**: गर्मीमें दूसरोंको जल पिलाया और सर्दीमें अग्निका रूलानेवाला) कहा गया है। यह नीची-ऊँची
- **Translation**: 

---

### Verse 5 (Bramha 0.7105)
- **Original**: सेवन कराया है, जो थके-माँदे मनुष्योंकी सेवा भूमिसे युक्त होनेके कारण मानवमात्रके लिये
- **Translation**: 

---

### Verse 6 (Bramha 0.7106)
- **Original**: करते और सदा प्रिय बचन बोलते हैं, जो दाता, अगम्य है। तपाये हुए ताँबेकी भाँति उसका वर्ण
- **Translation**: 

---

### Verse 7 (Bramha 0.7107)
- **Original**: शूर और माता-पिताके भक्त हैं तथा जिन्होंने है। वहाँ आगकी चिनगारियाँ और लपटें दिखायी
- **Translation**: 

---

### Verse 8 (Bramha 0.7108)
- **Original**: ब्राह्यणोंकी सेवा और अतिथियोंका पूजन किया देती हैं। बह मार्ग कण्टकॉसे भरा है। शक्ति और
- **Translation**: 

---

### Verse 9 (Bramha 0.7109)
- **Original**: है, वे भी उत्तर्वारसे ही पुरीमें प्रवेश करते हैं। वज़ आदि आयुधोंसे व्याप्त है। ऐसे कष्टप्रद यमपुरीका पश्चिम महाद्वार भाँति-भातिके रत्लोंसे मार्गपर निर्दयी यमदूत जीवको घसीटते हुए ले
- **Translation**: 

---

### Verse 10 (Bramha 0.7110)
- **Original**: विभूषित है। विचित्र-विचित्र मणियोंकी वहाँ जाते हैं और उन्हें सब ग्रकारके अस्त्र-शस्त्रोंसे
- **Translation**: 

---

### Verse 11 (Bramha 0.7111)
- **Original**: सीढ़ियाँ बनी हैं। देवता उस द्वारकी शोभा बढ़ाते मारते रहते हैं। इस तरह यापासक्त अन्यायी
- **Translation**: 

---

### Verse 12 (Bramha 0.7112)
- **Original**: रहते हैं। वहाँ भेरी, मृदज़् और शह्ब आदि मनुष्य विवश होकर मार खाते हुए दुर्धर्ष यमदूतोंके
- **Translation**: 

---

### Verse 13 (Bramha 0.7113)
- **Original**: वाद्योंकी ध्वनि हुआ करती हैं। सिद्धोंके समुदाय द्वारा यमलोकमें ले जाये जाते हैं। यमराजके
- **Translation**: 

---

### Verse 14 (Bramha 0.7114)
- **Original**: सदा हर्षमें भरकर उस द्वारपर मड्भल-गान करते सेवक सभी पापियॉकों उस दुर्गम मार्ममें
- **Translation**: 

---

### Verse 15 (Bramha 0.7115)
- **Original**: हैं। जो मनुष्य भगवान्‌ शिवकी भक्तिमें संलग्न अवहेलनापूर्वक ले जाते हैं। वह अत्यन्त भयंकर
- **Translation**: 

---

### Verse 16 (Bramha 0.7116)
- **Original**: रहते हैं, जो सब तीथोंमें गोते लगा चुके हैं, मार्ग जब समाप्त हो जाता है, तब यमदूत पापी
- **Translation**: 

---

### Verse 17 (Bramha 0.7117)
- **Original**: जिन्होंने पश्चाग्विका सेवन किया है, जो किसी जीवको ताँबे और लोहेकी बनी हुई भयंकर
- **Translation**: 

---

### Verse 18 (Bramha 0.7118)
- **Original**: उत्तम तीर्थस्थानमें अथवा कालिक्कर पर्व॑तपर प्राण- यमपुरीमें प्रवेश कराते हैं।
- **Translation**: 

---

### Verse 19 (Bramha 0.7119)
- **Original**: त्याग करते हैं और जो स्वामी, मित्र अथवा पुरी बहुत है, उसका विस्तार
- **Translation**: 

---

### Verse 20 (Bramha 0.7120)
- **Original**: जगत्‌का कल्याण करनेके लिये एबं गौओंको लाख योजनका है। वह चौकोर बतायी जातो है।। रक्षाके लिये मारे गये हैं, ये शूरवीर और तपस्वी
- **Translation**: 

---

