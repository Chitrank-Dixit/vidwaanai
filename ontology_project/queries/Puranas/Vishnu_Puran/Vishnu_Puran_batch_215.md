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

### Verse 1 (Vishnu Puran 0.4281)
- **Original**: 83 यस्‍््वेतद्धवता प्रोक्त सो5हमित्येतदात्मन: । वक्तुं न -शक्यते श्रोतुं तन्ममेच्छा प्रवर्तते
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.4282)
- **Original**: 84 ओविष्णुपुराण
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.4283)
- **Original**: आ0 13 वह एक ही ओतप्रोत है। अतः उसके वृद्धि अथवा क्षय कभी नहीं होते
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.4284)
- **Original**: हे नुप ! जन उसके उपचय (वद्धि), अपचय (क्षय) ही नहीं होते तो तुमने यह ब्बातत किस युक्तिसे कही कि “तू मोटा है ?'
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.4285)
- **Original**: यदि क्रमश: पृथिल्री, पाद, जंभा, काटी, ऊरु और उदरपर स्थित कच्धोंपर रखी हुई यह हिल्रिका मेरे लिये भाररूप हो सकती है तो उसी प्रकार तुम्हारे लिये भी तो हो सकतो है 7 [स्पोकि ये पृथिवों आदि तो जैसे तुमसे पृथक हैं नैसे ही मूझ आत्पासे भा सर्खथा घिन्न हैं]
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.4286)
- **Original**: तथा इस युक्तिसे तो अन्य समस्त जीवोने भी केवल दिबिका हो नहीं, बल्कि सप्पूर्ण पर्वत, ब॒क्ष, गृह और पृथियों आदिका भार उठा रखा है
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.4287)
- **Original**: हे राजन्‌ ! जब प्रकृतिजन्य कारणोंसे पुरुष सर्वथा भिन्न है तो उसव्प्र परिश्रम भी मुझको कैसे हो सकता है ?
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.4288)
- **Original**: और जिस द्ब्यसे यह दिबिका बनी हुई है उसीसे यह आपका, मेरा अथवा और सबक्का झारौर भो बना है; जिसमें क्रि ममत्वक्ता आरोप किया हुआ है
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.4289)
- **Original**: ओआपरादारजी खोले--ऐसा कह जे द्विजवर शिविकाक्रों घारण किये हुए ही मौन हो गये; और राजाने भी तुरुत्त पृथिवीपर उतरकर उनके चरण फ्कड् लिये
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.4290)
- **Original**: राजा ब्ोलला--अहो प्रिजगज ! इस शिक्काकों झोड़कर आप मेरे ऊपर कृपा कीजिये। प्रभो ! कृपया खताइये इस जडलेषको भारण किये आप व्यैन हैं 2
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.4291)
- **Original**: टे विद्वनू ! आप क्यैत हैं ? किस निमित्तसे यहाँ आपका आना हुआ 2? तथा आनेका क्या कारण है ? यह सब आप मुझसे कहिये
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.4292)
- **Original**: मुझे आपके चिपययें सुननेकों बड़ी उल्काठा हो रहो है
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.4293)
- **Original**: ब्राह्मण बोले--हे राजन्‌ ! सुनो, मैं अमुक हूँ--- यह बात कही नहीं जा सकती और तुमने जो मेंर यहाँ आनेज्य कारण पूछा सो आना-जाना आदि सभी क्रियाएँ कर्मफलके उपभोगके लिये ही हुआ करती हैं
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.4294)
- **Original**: सुख-दुःखका भोग हो देह आदिकी प्राप्ति करानेवाल्म है
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.4295)
- **Original**: तथा पर्माधर्मजन्य सुख-दु:खोक्परे भोगनेके लिये हो जाल
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.4296)
- **Original**: डेहादि धारण करता है
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.4297)
- **Original**: हे भूषाल ! समस्त जीखोकी सम्पूर्ण अवस्था ओके कारण ये धर्म और अधर्म ही हैं, फिर तिदेषरूपसे मेरे आगसनक्ता कारण तुम क्‍यों पूछते हो 2
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.4298)
- **Original**: 82 । राजा बोला--अवश्य हो, समस्त कार्याँमें -धर्म और अधर्म ही कारण हैं और कर्मफलके उपभोगके लिये ही एक देहसे दूसरे देहमें जाना होता हैं
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.4299)
- **Original**: किन्तु आपने जो कहा कि “मैं कौन हूँ---यह नहीं बताया -जा
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.4300)
- **Original**: आ- 13 ] योउस्ति सो5हमिति ब्रह्मन्कर्थ बक्तु न शक्यते
- **Translation**: 

---

