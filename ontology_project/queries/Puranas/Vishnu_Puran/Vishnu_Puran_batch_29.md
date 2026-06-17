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

### Verse 1 (Vishnu Puran 0.561)
- **Original**: 16 तासु क्षीणास्वशेषासु वर्द्ममाने च पातके । इलन्द्राभिभवदुःस्त्रार्तास्ता भवन्ति तत: प्रजा:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.562)
- **Original**: 17 तत्तो दुर्गाणि ताक्षक्रुर्धान्य पार्वतमौदकम्‌ । कुत्रिमं च तथा दुर्ग पुरखर्यरकादिकम्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.563)
- **Original**: 18 गृहाणि च यथान्याय॑ तेषु चक्कुः पुरादिषु । झीतातपादिबाधानां प्रशमाय महामते
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.564)
- **Original**: 19 अ्रतीकारमिमं कृत्वा शीतादेस्ता: प्रजा: पुनः । वातॉपाय॑ ततश्षक्रुईस्तसिद्धिं च कर्मजाम्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.565)
- **Original**: 20 ब्रीहयश्ष यवाश्वेव गोधूमाश्ञाणवस्तिला: । प्रियज्भवों ह्रृदाराक्ष कोरदूषा: सतीनकाः
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.566)
- **Original**: 21 माषा मुद्गा मसूराश्ष निष्पावा: सकुलत्थकाः । आदक्यक्रणकाश्षैव द्वाणा: सप्नदह् स्मृताः
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.567)
- **Original**: 22 इत्येता ओषधीनां तु आम्यानां जातयो मुने । चैत्रेय
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.568)
- **Original**: उससे घजामें पुरुषार्थका विधातक तथा अज्ञान और लोभको उत्पन्न करनेव्ात्म्न रागादिरूप अधर्मका बीज उत्पन्न हो जाता है
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.569)
- **Original**: तभीसे उसे बह विष्णुपद- प्राप्ति-रूप स्वाभाविक सिद्धि और रसोल्लास आदि अन्य आए सिद्धियाँ* नहीं मिलती
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.570)
- **Original**: उन समस्त सिर्धियोंके क्षीण हो जाने और पापके बढ़ जानेसे फिर सम्पूर्ण प्रजा इन्द्र, हास और दुःखसे आतुर हो
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.571)
- **Original**: तब उसने मरुभूमि, पर्नत और जल आदिके स्वाभाविक तथा कृत्रिम दुर्ग और पुर तथा - आदि स्थापित किये
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.572)
- **Original**: दे महामते ! उन पुर आदिकोंमें शोत्त और घाम आदि बाधाओंसे बचनेके लिये उसने यथायोग्य घर बनाये
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.573)
- **Original**: इस प्रकार शीतोष्णादिसे बचनेक्ा उपाय करके ठस प्रजाने जोविकाके साधनरूप कृषि तथा: कल्म-क्रौज्ल आदिको रचना को
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.574)
- **Original**: हे मुने ! धान, जौ, गेहूँ , छोटे धान्य, तिल, काँगनी, ज्वार, व्व्रेदो, छोटी मटर, उड़द, पूँग, मसूर, बड़ी मटर, कुलथी, राई, चना और सन--ये सत्रह आम्य ओषधियोंकी जातियाँ हैं। ग्राप्य और बन्य दोनों ओषध्यो यज्ञियाश्रैव आम्यारण्यातुर्दश
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.575)
- **Original**: प्रकारकी मिलाबर कुछ चौदह ओषधियाँ याक्षिक हैं + रसोल्ल्थसादि आष्ट-सिद्धियोका यर्णन स्कत्दपुराणमें इस प्रकार किया है-- स्सस्थ॒ स्वत एवान्तरल्लासः स्पाल्कृते.. युगे। रसोल्छासाह्यिकय सिखिस्तया हन्ति सुर्ध॑ सरः
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.576)
- **Original**: रूपादीज॑ नैरपेश्येण सदा तलुप्ता प्रजास्तथा
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.577)
- **Original**: द्वितोया सिद्धर्दिष्टा. सता : 8 धर्मोत्मक योउस्यासों सा. तृतीयापभिधौयते
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.578)
- **Original**: चतुर्थी. तुल्यता._ तासामायुपः. खुखरूफयों:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.579)
- **Original**: ऐक््रन्यबरल्थाहुल्‍ल्ये विशोका नाम पञ्ञमी
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.580)
- **Original**: परमात्मपरत्वेन तपोध्यानांदिनिरशिता
- **Translation**: 

---

