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

### Verse 1 (Vishnu Puran 0.9861)
- **Original**: यहाँ बैठकर उन्होंने निश्चय ही किसी बड़भागिनीका पुष्पोंसे शुद्ार किया है; अवश्य हो उसने अपने पूर्वजमें सर्वात्मा श्रीविष्णुभगवान्‌की उपासना की होगी
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.9862)
- **Original**: और यह देखो, पुष्पब्धनके सम्मानसे गर्विता होकर उसके मान करनेपर श्रीनन्‍दनन्दन उसे छोड़कर इस मार्गसे चले गये है
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.9863)
- **Original**: अरी सखियो ! देखो, यहाँ कोई नितम्बभारफे कारण मन्दगामिनी गोपी कृष्णचन्द्रके पीछे-पीछे गयी है । जह अपने गतक्तव्य स्थानको तीत्रगतिसे गयी है, इसीसे उसके चरणचिह्नोंके अग्रभाग कुछ नीचे दिखायी देते हैं
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.9864)
- **Original**: यहाँ सह सखी उनके हाथमें अपना पाणिपल्ल्ब देकर चले है इसोसे उसके चरणचिह्ल पणाधीन-से दिखलायी देते हैं
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.9865)
- **Original**: देखो, बहाँसे उस मन्दगासिनीके निराञडा होकर लौटनेके चरणचिह्न दीख रहे हैं, मालूम होता है उस घृर्तनी [ उसकी अन्य आत्तरिक अभिलाषाओंको पूर्ण किये बिना ही ] केवल कर-स्पर्श
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.9866)
- **Original**: इ46 नूनमुक्ता त्वरामीति पुनरेष्यामि तेडन्तिकम्‌ । तेन कृष्णेन येनैषा त्वरिता पदपद्धति:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.9867)
- **Original**: 40 प्रविष्टो गहने कृष्ण: पदमत्र न लक्ष्यते । निवर्तध्व॑ झशाड्ूस्थ नैतहीधितिगोचरे
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.9868)
- **Original**: 41 निवृत्तास्तास्तदा गोप्यो निराशा: कृष्णदर्शने । यमुनातीरमासाद्य. जगुस्तघरितं तथा
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.9869)
- **Original**: 42 ततो ददृशुरायान्त॑ विकासिमुखपद्कुजम्‌। गोप्यस्नैल्लेक्यगोप्तार कृष्णमझ्निप्टवेष्टितम्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.9870)
- **Original**: 43 काचिदालोक्य गोविन्दमायान्तमतिहर्षिता । कृष्ण कृष्णेति कृष्णेति प्राह नान्यदुदी रयत्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.9871)
- **Original**: 4ड कृत्वा ललाटफलकं हरिम्‌ । बिलोक्य नेत्रभूड़ाभ्यां पपौ तन्मुखपद्डजम्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.9872)
- **Original**: 45 काचिदालोक्य गोविन्द निमीलितविलोचना । तस्वैव रूप ध्यायन्ती योगारूढेव सा बभौ
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.9873)
- **Original**: 46 ततः काझ्ित्मियालापैः काम्िदभ्ूभडूवी क्षिते: । निन्येउनुनयमन्यां च करस्पशेन माधव:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.9874)
- **Original**: 47 ताभिः प्रसन्नचित्ताभिगोंपीभिस्सह सादरम्‌। रास रासगोष्ठीभिरुदारचरितों हरि:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.9875)
- **Original**: 48 रासमण्डलबन्धो5पि कृष्णपार्श्रपनुज्झता । गोपीजनेन. नैवाभूदेकस्थानस्थिरात्मना
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.9876)
- **Original**: 49 हस्तेन गृद्य चैकेकां गोपीनां रासमण्डलम्‌ । चकार तत्करस्पर्शनिमीलितदृश॑ हरिः
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.9877)
- **Original**: 750 ततः प्रववृते रासश्चलद्वकयनिस्वन: । अनुयातश्नरत्काव्यगेयगीतिरनुक्रमात्‌_
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.9878)
- **Original**: 51 कृष्णइज्ञरश्चद्भरमसं कौमु्दी कुमुदाकरम्‌। जगौ गोपीजनस्त्वेके कृष्णनाम पुनः पुनः
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.9879)
- **Original**: 52 परिवृत्तिअ्रमेणेका_ चलद्वकयलछापिनीम्‌ । ददौ बाहुलतां स्कन्ये गोपी मधुनिघातिन:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.9880)
- **Original**: 53 अ्रीविष्णुपुराण [ आ« 13 करके उसका अपपान किया है
- **Translation**: 

---

