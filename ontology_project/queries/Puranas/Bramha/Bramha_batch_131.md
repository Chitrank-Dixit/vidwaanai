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

### Verse 1 (Bramha 0.2601)
- **Original**: मुनि, सिद्ध और योगी भी जिस रमणीय और &&-
- **Translation**: 

---

### Verse 2 (Bramha 0.2602)
- **Original**: रोग-शोकरहित पदको नहीं प्राप्त होते, उसे ही अनुसार कोई उत्तम बर माँगो।' 6] 5 8225 7 ***+%7।
- **Translation**: 

---

### Verse 3 (Bramha 0.2603)
- **Original**: तुम प्राप्त करोगे। सम्पूर्ण लोकोंको लाँधकर मेरे श्रोहरि उनकी भक्तिका विचार करके सम्पूर्ण
- **Translation**: 

---

### Verse 4 (Bramha 0.2604)
- **Original**: लोकमें जाओगे। यहाँ तुमने जो कीर्ति प्राप्त की है, देवताओंके साथ राजाके सामने आये। नील
- **Translation**: 

---

### Verse 5 (Bramha 0.2605)
- **Original**: वह तीनों लोकोंमें फैलेगी और मैं सदा ही यहाँ मेघके समान श्यामवर्ण, कमल-पत्रके समान
- **Translation**: 

---

### Verse 6 (Bramha 0.2606)
- **Original**: निवास करूँगा। इस तीर्थको देवता और दानव बढ़ी-बड़ी आँखें, हाथोंमें देदीप्यमान सुदर्शन,
- **Translation**: 

---

### Verse 7 (Bramha 0.2607)
- **Original**: आदि सब लोग श्वेतगज्जा कहेंगे। जो कुशके बायें हाथमें पाक्जन्य शड्ख तथा अन्य हाथोंमें
- **Translation**: 

---

### Verse 8 (Bramha 0.2608)
- **Original**: अग्रभागसे भी श्वेतगज्ञाका जल अपने ऊपर गदा, शार्ड्रंघनुष और खड्ग-यही उनकी झाँकी ! छिड़केगा, वह स्वर्गलोकमें जायगा। जो यहाँ थी। भगवानने कहा--“राजन्‌! तुम्हारी बुद्धि
- **Translation**: 

---

### Verse 9 (Bramha 0.2609)
- **Original**: स्थापित श्वेतमाधव नामकी ग्रतिमाका दर्शन और बड़ी उत्तम है। तुपमें पापका लेश भी नहीं है।
- **Translation**: 

---

### Verse 10 (Bramha 0.2610)
- **Original**: उसे प्रणाम करेगा, वह देह त्यागकर भगवान्‌का मैं तुमपर बहुत प्रसन्न हूँ। तुम अपनी इच्छाके
- **Translation**: 

---

### Verse 11 (Bramha 0.2611)
- **Original**: स्मरण करते हुए शान्त पदको प्राप्त होगा। 308 #पस्डेसस-2>त मत्स्यमाधवकी महिमा, समुद्रमें मार्जज आदिकी विधि, अष्टाक्षर-मन्त्रकी महत्ता, स्त्रान, तर्पण-विधि तथा भगवान्‌की पूजाका वर्णन ब्रह्माजी कहते हैं-- श्रेतमाधवका दर्शन करके
- **Translation**: 

---

### Verse 12 (Bramha 0.2612)
- **Original**: भगवानके आदि अवतार हैं। पहले पृथ्बीका उनके समीप ही मत्स्यमाधवका दर्शन करे। जो
- **Translation**: 

---

### Verse 13 (Bramha 0.2613)
- **Original**: चिन्तन करके उसपर प्रतिष्ठित हुए भगवान्‌को भगवान्‌ पहले एकार्णवके जलमें मत्स्यरूप धारण , प्रणाम करे। ऐसा करनेसे मनुष्य सब दुःखोंसे करके बेदोंका उद्धार करनेके लिये रसातलमें
- **Translation**: 

---

### Verse 14 (Bramha 0.2614)
- **Original**: मुक्त हो जाता है और उस वैकुण्ठधाममें जाता है, स्थित थे, वे ही मत्स्यमाधव कहलाते हैं। वे
- **Translation**: 

---

### Verse 15 (Bramha 0.2615)
- **Original**: जहाँ साक्षात्‌ भगवान्‌ श्रीहरि विराजमान रहते हैं।
- **Translation**: 

---

### Verse 16 (Bramha 0.2616)
- **Original**: 126 » संक्षिप्त अ्रह्मपुराण * मुनिवरो! इस प्रकार मैंने मत्स्यमाधवके माहात्म्यका
- **Translation**: 

---

### Verse 17 (Bramha 0.2617)
- **Original**: कहते हैं। वहाँ समुद्रके जलसे आकृष्ट सर्वगुणसम्पन्न वर्णन किया। काष्ट है, उसे प्रणाम करके पूजन करनेपर मनुष्य मुनियोने कहा-- भगवन्‌! समुद्रमें जो मार्जन
- **Translation**: 

---

### Verse 18 (Bramha 0.2618)
- **Original**: सम्पूर्ण रोगों तथा पापग्रह आदिकी पीडासे मुक्त और ज्लान-दान आदि किया जाता है, उसका फल
- **Translation**: 

---

### Verse 19 (Bramha 0.2619)
- **Original**: हो जाता है। यतलाइये। स्वर्गद्वारसे समुद्रपर जाकर आचमन करे तथा ब्रह्माजी बोले--मुनिवरों! मार्जनकी विधि
- **Translation**: 

---

### Verse 20 (Bramha 0.2620)
- **Original**: पवित्र भावसे भगवान्‌ नारायणका ध्यान करके सुनो। मार्कण्डेयहदका स््रान पूर्वाह्लकालमें उत्तम
- **Translation**: 

---

